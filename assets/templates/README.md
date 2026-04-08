# Canonical Templates

These templates are the starting point for one-shot app generation.

## Shared first, then platform adapters
- `shared-core.md` for the domain layer and protocol model
- `desktop.md` for Pear desktop apps
- `terminal.md` for Pear terminal apps
- `mobile.md` for Bare / BareKit mobile apps

## How to use
1. Pick the template that matches the requested app type.
2. Copy the file tree into the generated repo.
3. Keep business logic in the shared core.
4. Put runtime, UI, and packaging differences into adapters and configs.
5. Add the commands from `references/build-deploy.md`.
