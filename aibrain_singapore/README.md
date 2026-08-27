# aibrain_singapore/ — core package

The Python package that powers **AI Brain — Singapore**.

For the product overview, install guide, and the authoritative agent / MCP-tool list, see the repository [README.md](../README.md). This file documents the internal package layout for contributors.

## Layout

This package follows the standard AI Brain — Singapore shape: a CLI entry point, a configuration loader, a set of specialist agents under `agents/`, an MCP server exposing the tools described in the top-level README, and a forked memory/retrieval layer.

Run `ls aibrain_singapore/` for the authoritative, current module set — the package is the source of truth, not this file.

## Credit

The memory / retrieval architecture is forked from MemPalace (MIT) and credited in the top-level README.
