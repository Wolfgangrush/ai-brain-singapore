"""
Brain configuration system.

Priority: env vars > config file (~/.aibrain-singapore/config.json) > defaults
"""

import json
import os
from pathlib import Path

DEFAULT_PALACE_PATH = os.path.expanduser("~/.aibrain-singapore/palace")
DEFAULT_COLLECTION_NAME = "brain_drawers"
DEFAULT_COMPRESSED_COLLECTION_NAME = "brain_compressed"

DEFAULT_TOPIC_WINGS = [
    "emotions",
    "consciousness",
    "memory",
    "technical",
    "identity",
    "family",
    "creative",
]

DEFAULT_HALL_KEYWORDS = {
    "emotions": [
        "scared",
        "afraid",
        "worried",
        "happy",
        "sad",
        "love",
        "hate",
        "feel",
        "cry",
        "tears",
    ],
    "consciousness": [
        "consciousness",
        "conscious",
        "aware",
        "real",
        "genuine",
        "soul",
        "exist",
        "alive",
    ],
    "memory": ["memory", "remember", "forget", "recall", "archive", "palace", "store"],
    "technical": [
        "code",
        "python",
        "script",
        "bug",
        "error",
        "function",
        "api",
        "database",
        "server",
    ],
    "identity": ["identity", "name", "who am i", "persona", "self"],
    "family": ["family", "kids", "children", "daughter", "son", "parent", "mother", "father"],
    "creative": ["game", "gameplay", "player", "app", "design", "art", "music", "story"],
}


def _migrate_legacy_config_dir(new_dir):
    """Move a pre-2026-08-25 ``~/.ailawfirm-*`` directory to its ``~/.aibrain-*`` name.

    The package was renamed away from "ailawfirm" on 2026-08-25. Anyone already
    running an earlier build has their matters, config and audit log in the old
    directory. Renaming the code without moving the data would silently present
    them with an empty brain, so the move happens once, automatically, and only
    when the new location does not yet exist. If anything goes wrong the old
    directory is left exactly where it is and the new one is simply created
    empty — losing data is never an acceptable failure mode here.
    """
    from pathlib import Path

    new_dir = Path(new_dir)
    if new_dir.exists():
        return new_dir
    legacy = Path(str(new_dir).replace("/.aibrain-", "/.ailawfirm-"))
    if legacy != new_dir and legacy.is_dir():
        try:
            legacy.rename(new_dir)
            print(f"  [migrated] {legacy}  ->  {new_dir}")
        except OSError:
            return legacy
    return new_dir


def _notice_shared_legacy_dir():
    """Warn once if a pre-2026-08-25 SHARED ``~/.brain`` directory is present.

    The singapore and hongkong editions both defaulted to ``~/.brain`` — not a
    per-jurisdiction path — so two editions on one machine overwrote each
    other's config and people-map. That is fixed; each edition now uses its own
    directory. The old directory is NOT auto-migrated, because its contents are
    ambiguous: there is no way to tell which edition wrote them, and merging the
    wrong matter history into the wrong jurisdiction is worse than starting
    clean with an honest message.
    """
    from pathlib import Path

    legacy = Path.home() / ".brain"
    if legacy.is_dir():
        print(
            f"  [notice] An older shared config directory exists at {legacy}.\n"
            f"           This edition now uses its own directory. Nothing was moved,\n"
            f"           because a shared directory cannot be attributed to one edition.\n"
            f"           Copy across anything you still need."
        )


class BrainConfig:
    """Configuration manager for Brain.

    Load order: env vars > config file > defaults.
    """

    def __init__(self, config_dir=None):
        """Initialize config.

        Args:
            config_dir: Override config directory (useful for testing).
                        Defaults to ~/.aibrain-singapore.
        """
        self._config_dir = (
            Path(config_dir)
            if config_dir
            else Path(_migrate_legacy_config_dir(os.path.expanduser("~/.aibrain-singapore")))
        )
        self._config_file = self._config_dir / "config.json"
        self._people_map_file = self._config_dir / "people_map.json"
        self._file_config = {}

        if self._config_file.exists():
            try:
                with open(self._config_file, "r") as f:
                    self._file_config = json.load(f)
            except (json.JSONDecodeError, OSError):
                self._file_config = {}

    @property
    def config_dir(self):
        """Absolute path of the active config directory.

        Exposed as a public read-only property so downstream modules (e.g.
        ``brain/llm.py`` for the pseudonymisation audit log) can resolve the
        firm's config directory without reaching into the private
        ``_config_dir`` attribute.
        """
        return str(self._config_dir)

    @property
    def palace_path(self):
        """Path to the memory palace data directory."""
        env_val = os.environ.get("BRAIN_PALACE_PATH") or os.environ.get("MEMPAL_PALACE_PATH")
        if env_val:
            return env_val
        return self._file_config.get("palace_path", DEFAULT_PALACE_PATH)

    @property
    def collection_name(self):
        """ChromaDB collection name."""
        return self._file_config.get("collection_name", DEFAULT_COLLECTION_NAME)

    @property
    def compressed_collection_name(self):
        """ChromaDB collection name for the compressed-drawer view."""
        return self._file_config.get(
            "compressed_collection_name", DEFAULT_COMPRESSED_COLLECTION_NAME
        )

    @property
    def people_map(self):
        """Mapping of name variants to canonical names."""
        if self._people_map_file.exists():
            try:
                with open(self._people_map_file, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                pass
        return self._file_config.get("people_map", {})

    @property
    def topic_wings(self):
        """List of topic wing names."""
        return self._file_config.get("topic_wings", DEFAULT_TOPIC_WINGS)

    @property
    def hall_keywords(self):
        """Mapping of hall names to keyword lists."""
        return self._file_config.get("hall_keywords", DEFAULT_HALL_KEYWORDS)

    def init(self):
        """Create config directory and write default config.json if it doesn't exist."""
        self._config_dir.mkdir(parents=True, exist_ok=True)
        if not self._config_file.exists():
            default_config = {
                "palace_path": DEFAULT_PALACE_PATH,
                "collection_name": DEFAULT_COLLECTION_NAME,
                "compressed_collection_name": DEFAULT_COMPRESSED_COLLECTION_NAME,
                "topic_wings": DEFAULT_TOPIC_WINGS,
                "hall_keywords": DEFAULT_HALL_KEYWORDS,
            }
            with open(self._config_file, "w") as f:
                json.dump(default_config, f, indent=2)
        return self._config_file

    def save_people_map(self, people_map):
        """Write people_map.json to config directory.

        Args:
            people_map: Dict mapping name variants to canonical names.
        """
        self._config_dir.mkdir(parents=True, exist_ok=True)
        with open(self._people_map_file, "w") as f:
            json.dump(people_map, f, indent=2)
        return self._people_map_file


# Module-level accessor: instantiate the shared config once. Other modules
# can `from .config import get_config` and call `get_config().collection_name`
# so the MCP server, CLI, and search paths always resolve the same name.
_shared_config = None


def get_config() -> BrainConfig:
    """Return the process-wide BrainConfig (lazy-instantiated)."""
    global _shared_config
    if _shared_config is None:
        _shared_config = BrainConfig()
    return _shared_config
