# Build and Deploy Playbook

Use this playbook when the task is to generate a complete app that should be runnable, testable, and packageable.

Last reviewed: Wednesday, April 8, 2026.

## Standard script contract
Every generated app should try to provide these scripts in package.json:
- `dev`
- `test`
- `build`
- `package`
- `release`
- `lint` if there is linting
- `start` if the app has a single production entrypoint

If a target platform needs custom scripts, keep the same script names and swap only the implementation.

## Desktop playbook
Use when the app ships as a Pear desktop app.

Recommended flow:
1. Install dependencies.
2. Start the local dev shell.
3. Run unit tests against shared core logic.
4. Package the app.
5. Verify update / restart behavior if the app uses it.

Suggested script mapping:
- `dev`: start the Pear desktop app shell
- `test`: run shared-core tests and adapter smoke tests
- `build`: bundle or prepare desktop assets
- `package`: produce distributable desktop artifact
- `release`: perform final validation and release tagging

## Terminal playbook
Use when the app should be validated quickly from the command line.

Recommended flow:
1. Install dependencies.
2. Run the terminal entrypoint.
3. Run shared-core tests.
4. Confirm peer discovery / replication behavior.
5. Package if the app produces a distributable CLI or bundle.

Suggested script mapping:
- `dev`: run the terminal entrypoint in watch or interactive mode
- `test`: run core and protocol tests
- `build`: prepare the terminal bundle
- `package`: emit the runnable terminal artifact
- `release`: publish or tag the terminal build

## Mobile / BareKit playbook
Use when the app targets iOS or Android via Bare/BareKit.

Recommended flow:
1. Install dependencies.
2. Ensure native bridge or worklet bootstrapping works.
3. Run platform-adapter tests where possible.
4. Verify lifecycle/resume behavior.
5. Package the native build.

Suggested script mapping:
- `dev`: run the Bare/BareKit entrypoint or simulator/dev build
- `test`: run shared-core tests and adapter-level smoke checks
- `build`: prepare native bundles / runtime assets
- `package`: produce native package artifacts
- `release`: finalize the mobile release path

## Suggested command checklist for generated repos
- `npm install` or `pnpm install`
- `npm test`
- `npm run dev`
- `npm run build`
- `npm run package`
- `npm run release`

If a repository uses different tooling, the generated app must still present the equivalent commands with the same meaning.

## Build and deploy requirements
- Keep the app runnable before packaging.
- Keep packaging separate from development startup.
- Use tests that can run without a full UI session when possible.
- Include at least one command that proves the app starts successfully.
- Include at least one command that proves the app can be packaged or prepared for deployment.

## Release checklist
- Version is set
- Scripts run successfully
- Tests pass
- Entry point exists for each target platform
- Config files exist for each target platform
- Update behavior is documented if the app ships with updates
