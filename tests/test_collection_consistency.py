"""Regression test: split-brain ChromaDB collection bug + stopword dedup.

The search/read path must resolve the SAME ChromaDB collection that the config
declares (previously it hardcoded "brain_drawers"). The shared stop-word set
must preserve the union of the original per-module sets.
"""

import chromadb

from ailawfirm_singapore import config as _config_mod
from ailawfirm_singapore import searcher
from ailawfirm_singapore.stopwords import STOPWORDS


def _collection_name():
    """Resolve the config-declared collection name (config class name varies per edition)."""
    for name in dir(_config_mod):
        obj = getattr(_config_mod, name)
        if isinstance(obj, type) and name.endswith("Config"):
            try:
                inst = obj()
            except Exception:
                continue
            if getattr(inst, "collection_name", None):
                return inst.collection_name
    raise RuntimeError("no *Config class exposing collection_name found in config module")


def test_read_path_uses_config_not_hardcoded_name():
    """Config is the single source of truth; the read path does not hardcode the old name."""
    import inspect

    assert _collection_name(), "config must declare a collection name"
    assert '"brain_drawers"' not in inspect.getsource(searcher), (
        "searcher still hardcodes the old 'brain_drawers' collection"
    )


def test_drawer_written_by_config_collection_is_findable_by_search(tmp_path):
    """Functional round-trip: write to the config collection, search must find it."""
    palace = str(tmp_path / "palace")
    write_name = _collection_name()  # canonical config-declared collection

    client = chromadb.PersistentClient(path=palace)
    col = client.get_or_create_collection(write_name)
    try:
        col.add(
            documents=["The data protection regulator reviewed the consent notice on Tuesday."],
            ids=["d1"],
            metadatas=[{"wing": "test", "room": "test", "source_file": "t.md"}],
        )
        out = searcher.search_memories("When was the consent notice reviewed?", palace_path=palace)
    except Exception as exc:  # embedding backend unavailable offline
        import pytest

        pytest.skip(f"embedding backend unavailable in this env: {exc}")

    assert "error" not in out, out
    assert out["results"], (
        "drawer written to the config collection is not findable by search (split-brain bug)"
    )


def test_common_stopwords_preserved_in_shared_set():
    """Guard the dedup: words present in the original sets must survive the union."""
    for word in ("the", "and", "like", "very", "also", "only", "no", "every"):
        assert word in STOPWORDS, f"stopword {word!r} was lost in the shared-set merge"
