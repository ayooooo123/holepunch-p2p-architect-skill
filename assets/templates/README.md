# Canonical Templates

These templates are the starting point for one-shot app generation.

## Default rule
Start with `bare-worker.md` unless the request clearly requires a different shell or target. All platform templates assume a worker-first architecture and keep business logic out of the shell.

## Shared first, then platform adapters
- `bare-worker.md` for the default worker-first app shape
- `shared-core.md` for the domain layer and protocol model
- `desktop.md` for Pear desktop shell apps
- `terminal.md` for Pear terminal shell apps
- `mobile.md` for Bare / BareKit mobile shell apps

## How to use
1. Pick the template that matches the requested app type.
2. Copy the file tree into the generated repo.
3. Keep business logic in the shared core and the worker host.
4. Put runtime, UI, and packaging differences into adapters and config.
5. Add the commands from `references/build-deploy.md`.

## Template notes
- The worker host should own transport setup, persistence orchestration, and replication lifecycle.
- Shells should be thin and should only boot the worker host, surface UI, or expose CLI commands.
- If a template seems to depend on `pear run`, rewrite it to use the pear-runtime library or an equivalent bootstrap layer instead.
