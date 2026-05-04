# Holepunch Organization Repository Index

Generated at: 2026-05-04  
Source organization: `holepunchto`  
Public repositories discovered by GitHub search: **597**

## Scope

- Grouped by inferred primary use case from repo name, description, topics, and language.
- Repos are listed once under their most likely home.
- Archived repos remain included when they are part of the public inventory.

## Delta since previous refresh

- Newly surfaced repos in this refresh include `libhc`, `libkv`, `libflattree`, `sentry-bare`, `liblexkey`, `rocksdb-blobs`, `bare-readline`, `bare-signals`, `bare-env`, `bare-boot`, `bare-atomics`, `bare-abort`, `bare-gif`, `bare-union-bundle`, `bare-xdiff`, `cross-worker`, `msix-manager`, `bare-tpl`, `compact-encoding-golang`, and `bare-rpc-golang`, plus several newer packaging/runtime helpers.
- The taxonomy below keeps the previous grouping style so the index stays easy to scan, but the repo counts and top-level inventory were refreshed to the latest public search results.

## 1) Bare runtime & platform

Core runtime, process primitives, worker model, and platform abstractions.

- Runtime / process core: `bare`, `bare-runtime`, `bare-kit`, `bare-native`, `bare-worker`, `bare-vm`, `bare-channel`, `bare-process`, `bare-subprocess`, `bare-daemon`, `bare-sidecar`, `bare-open`, `bare-os`, `bare-thread`, `bare-realm`, `bare-inspector`, `bare-inspector-gc`, `bare-performance`, `bare-hrtime`, `bare-walk-handles`, `bare-storage`, `bare-node-runtime`, `bare-node`, `bare-async-hooks`, `bare-queue-microtask`, `bare-stdio`, `bare-run`, `bare-repl`.
- Standard-library style shims: `b4a`, `bare-buffer`, `bare-events`, `bare-console`, `bare-fs`, `bare-net`, `bare-tcp`, `bare-dgram`, `bare-tls`, `bare-http1`, `bare-http-parser`, `bare-https`, `bare-fetch`, `bare-ws`, `bare-url`, `bare-path`, `bare-querystring`, `bare-mime`, `bare-encoding`, `bare-intl`, `bare-string-decoder`, `bare-punycode`, `bare-form-data`, `bare-abort-controller`, `bare-structured-clone`, `bare-diagnostics-channel`, `bare-type`, `bare-utils`, `bare-semver`, `bare-format`, `bare-ansi-escapes`, `bare-assert`, `bare-inspect`, `bare-stream`, `bare-crypto`.
- Runtime helpers and module tooling: `events-universal`, `require-addon`, `require-asset`, `which-runtime`, `bare-node-fetch`, `bare-module`, `bare-module-lexer`, `bare-module-resolve`, `bare-module-traverse`, `bare-addon-resolve`, `bare-link`, `gip-transport`.
- Native platform integrations: `bare-bluetooth-apple`, `bare-bluetooth-android`, `bare-web-kit`, `bare-web-kit-gtk`, `bare-ui-kit`, `bare-win-ui`, `bare-gtk`, `bare-sdl`, `bare-bmp`, `bare-png`, `bare-jpeg`, `bare-heif`, `bare-webp`, `bare-svg`, `bare-ico`, `bare-tiff`, `bare-exif`, `bare-image-resample`, `bare-ffmpeg`, `bare-md4c`, `bare-zlib`, `bare-media`, `bare-delta`, `bare-posix`, `bare-ndk`, `bare-lief`, `bare-zmq`.
- Bare utilities and runtime diagnostics: `bare-file-logger`, `bare-system-logger`, `bare-logger`, `bare-debug-log`, `bare-compat-napi`, `bare-v8`, `bare-v8-to-istanbul`, `bare-addon`, `bare-addon-rust`, `bare-addon-java`, `bare-addon-jstl`, `bare-rust`, `thread-stats`.
- Runtime-adjacent UI and cross-runtime support: `react-native-bare-kit`, `react-native-b4a`, `expo-bare-kit`, `expo-file-stream`, `sveltekit-adapter-bare`, `bare-app-kit`, `bare-crypto`.

## 2) Pear runtime, application lifecycle, and CLI flows

Pear runtime plumbing, lifecycle control, IPC, updates, and release tooling.

- Core Pear runtime / CLI: `pear`, `pear-runtime`, `pear-runtime-bare`, `pear-runtime-bootstrap`, `pear-runtime-updater`, `pear-runtime-legacy-storage`, `pear-desktop`, `pear-electron`, `pear-cli`, `pear-cmd`, `pear-api`, `pear-interface`, `pear-info`, `pear-link`, `pear-terminal`.
- App lifecycle and packaging: `pear-build`, `pear-bundle`, `pear-pack`, `pear-stage`, `pear-seed`, `pear-init`, `pear-installer`, `pear-distributable-bootstrap`, `pear-prefetcher`, `pear-updater`, `pear-updater-bootstrap`, `pear-force-update`, `pear-restart`, `pear-reset`, `pear-drop`, `pear-gracedown`, `pear-crasher`, `pear-tryboot`, `pear-release`, `pear-prerelease`, `pear-changelog`, `pear-md`, `pear-prefs`, `pear-user-dirs`, `pear-aliases`, `pear-wakeups`, `pear-updates`, `pear-runtime-updater`.
- IPC, messaging, and process coordination: `pear-ipc`, `pear-ipc-client`, `pear-message`, `pear-messages`, `pear-opstream`, `pear-opwait`, `pear-state`, `pear-rti`, `pear-constants`, `pear-errors`, `pear-gunk`, `pear-logger`, `pear-appling`, `pear-pipe`, `pear-hyperdb`, `pear-appdrive`, `pear-hyperdb`.
- Documentation, templates, and ecosystem apps: `pear-docs`, `pear-templates`, `pear-workshop`, `pear-radio`, `pear-radio-backend`, `pear-ci`, `pear-ci-example`, `pear-ci-multisig`, `hello-pear-electron`, `pearpass-example`, `autopass-mobile-example`, `speedrun`.
- Legacy / archived Pear utilities: `pear-runtime-appling`, `pear-stdio`, `pear-doctor`, `pear-bridge`, `pear-hotmods`, `pear-run`, `pear-shake`.

## 3) Hypercore, storage, drives, and data plane

Distributed logs, databases, corestores, drive tools, and storage-oriented workflows.

- Core data structures: `hypercore`, `hyperbee`, `hyperbee2`, `hyperdb`, `hyperdrive`, `hyperdrive-next`, `autobase`, `corestore`, `hyperblobs`, `hyperconf`, `core-coupler`, `hyper-multisig`, `hyper-multisig-cli`.
- Storage, drivers, and persistence: `hypercore-storage`, `hypercore-crypto`, `hypercore-encryption`, `hypercore-errors`, `hypercore-id-encoding`, `hypercore-proof-queue`, `hypercore-byte-stream`, `hypercore-blob-server`, `hypercore-audit`, `hypercore-detector`, `hypercore-messages`, `hypercore-sign`, `hypercore-signing-request`, `hypercore-logger`, `hypercore-stats`, `hypercore-scale-tests`, `hypercore-e2e-tests`, `hyperdrive-profiler`, `hyperdrive-swarm-test`, `hyperdb-workshop`, `hyperdb-autobase-workshop`, `hyperdb-benchmarking`, `rocksdb-blobs`.
- Drive tools and file sync: `localdrive`, `mirror-drive`, `serve-drive`, `watch-drive`, `drives`, `drive-resolve`, `drive-bundler`, `distributed-drive`, `network-block-device`, `simple-seeder`, `seedbee`, `localwatch`, `throwaway-local-cache`, `corestore-snapshot`, `passive-core-watcher`, `multi-profile-store`, `key-collection`, `index-encoder`, `index-keys`, `emoji-index`.
- Hypercore-related apps and experiments: `autobase-example`, `autobase-test-helpers`, `autobase-light-writer`, `autobase-discovery`, `autobase-discovery-cli`, `hypercore-byte-stream`, `hypercore-storage`, `hypercore-logger`, `hypercore-stats`, `hypercore-e2e-tests`, `hypercore-scale-tests`, `hypercore-signing-request`, `hypercore-blob-server`, `drive-analyzer`.

## 4) Networking, DHT, RPC, and transport

Peer discovery, swarming, multiplexing, and transport layers.

- DHT and swarm stack: `hyperdht`, `hyperswarm`, `hyperswarm-secret-stream`, `hyperswarm-dht-relay`, `hyperswarm-testnet`, `hyperswarm-doctor`, `hyperswarm-seeders`, `hyperswarm-stats`, `hyperdht-stats`, `hyperswarm-capability`, `hyperswarm-e2e-tests`, `hyperbeam`, `hypermininet`, `instrumented-dht-node`.
- RPC and protocol muxing: `dht-rpc`, `rpc`, `protomux`, `protomux-rpc`, `protomux-rpc-client`, `protomux-rpc-client-pool`, `protomux-rpc-router`, `protomux-rpc-middleware`, `protomux-wakeup`, `jsonrpc-mux`, `hrpc`, `hrpc-swift`, `hrpc-modular-example`, `bare-rpc`, `bare-rpc-swift`, `bare-rpc-golang`, `bot-rpc`, `hp-rpc-cli`.
- Transports and network helpers: `bare-net`, `bare-tcp`, `bare-dgram`, `bare-tls`, `bare-ws`, `bare-http1`, `bare-http-parser`, `bare-https`, `bare-dns`, `http-forward-host`, `http-dht-proxy`, `netpaste`, `repl-swarm`, `hyperssh`, `git-remote-punch-transport`, `gip-remote`, `gip-transport`, `punch-connection-encoding`, `pattern-router`, `ptnm`, `iambus`, `raw-text-display-parser`, `listen-async`, `framed-stream`, `tiny-buffer-rpc`, `tiny-http-native`, `tiny-fs-native`, `tiny-paths`, `tiny-timers-native`.
- Network control, scheduling, and coordination: `adaptive-timeout`, `bucket-rate-limit`, `delay-pacer`, `task-backoff`, `db-lock`, `scope-lock`, `fd-lock`, `fs-native-lock`, `fifofile`, `fd-pipe`, `activity-queue`.

## 5) Blind networking, Keet, and identity flows

Blind peer discovery, pairing, relays, and Keet-specific application flows.

- Blind peer stack: `blind-peer`, `blind-peer-cli`, `blind-peer-encodings`, `blind-peer-muxer`, `blind-peer-router`, `blind-peering`, `blind-peering-cli`, `blind-relay`, `blind-relay-service`, `blind-pairing`, `blind-pairing-core`, `blind-encryption-sodium`.
- Identity and key management: `keypear`, `keet-identity-key`, `secure-key`, `pw-to-ek`, `sodium-hmac`, `deterministic-sealed-box`, `broadcast-encryption`, `obfuscate-data`.
- Keet application tooling and shells: `keet-appling`, `keet-appling-next`, `keet-prefs`, `keet-mobile-releases`, `pear-multisig-link`.

## 6) Native libraries, ABI layers, and bindings

Reusable C/C++/Swift/Go/Rust building blocks, ABI compatibility layers, and generated bindings.

- Core native libraries: `libjs`, `libqjs`, `libjsc`, `libjerry`, `libmqjs`, `libnapi`, `libjsi`, `libjstl`, `libjnitl`, `libpear`, `libappling`, `libpearsync`, `libdynload`, `libmem`, `liblog`, `libdaemon`, `librlimit`, `libjson`, `libpath`, `libutf`, `liburl`, `libbase64`, `libhex`, `libz32`, `libcrc`, `libprng`, `libquickbit`, `libsimdle`, `libbitarray`, `libcompact`, `libintrusive`, `libparseline`, `libtls`, `librabin`, `librpc`, `librocksdb`, `libfs`, `libfx`, `libtt`, `libudx`, `libsingleset`, `libflattree`, `libhc`, `libkv`, `liblexkey`.
- Universal / compatibility wrappers: `quickbit-universal`, `crc-universal`, `bitarray-universal`, `simdle-universal`, `sodium-universal`, `events-universal`, `require-addon`, `require-asset`, `which-runtime`, `bare-node-fetch`, `bare-node-runtime`.
- JavaScript/C/C++ bindings: `quickbit-native`, `bitarray-native`, `simdle-native`, `crc-native`, `rabin-native`, `sqlite3-native`, `rocksdb-native`, `udx-native`, `fx-native`, `tt-native`, `appling-native`, `libjsi`.
- Cross-language bindings and codegen: `compact-encoding-swift`, `compact-encoding-golang`, `bare-rpc-golang`, `hrpc-swift`, `hyperschema-swift`, `compact-encoding-net`, `hyperdht-address`.
- Encoding and schema libraries: `compact-encoding`, `compact-encoding-struct`, `compact-encoding-bitfield`, `compact-encoding-variant`, `compact-encoding-net`, `libcompact`, `punch-connection-encoding`, `bare-ffmpeg-encodings`.
- Native utilities for app shells / UI / packaging: `bare-kit-swift`, `react-native-bare-kit`, `bare-app-kit`, `bare-ui-kit`, `bare-win-ui`, `bare-gtk`, `bare-web-kit`, `bare-web-kit-gtk`, `bare-sdl`, `bare-ndk`, `bare-rust`.

## 7) Build, packaging, release, and CI automation

Cross-platform build helpers, packaging recipes, and release infrastructure.

- Shared org tooling: `actions`, `canary-runner`, `slack-build-status`, `oidc-publishing`, `oidc-publishing-sandbox`, `prettier-config-holepunch`, `repo-template`, `check-npm-maintainers`.
- Native build helpers: `bare-prebuild`, `prebuild-containers`, `chromium-prebuilds`, `musl-toolchains`, `ninja-runtime`, `bare-headers`, `bare-build`, `bare-make`, `bare-pack`, `bare-pack-drive`, `bare-unpack`, `bare-bundle`, `bare-bundle-compile`, `bare-bundle-evaluate`, `bare-bundle-id`, `bare-sidecar-bundle`, `bare-distributable`, `bare-app-image`, `bare-apk`, `bare-link`.
- CMake and build-system bridges: `cmake-bare`, `cmake-bare-bundle`, `cmake-drive`, `cmake-pear`, `cmake-runtime`, `cmake-toolchains`, `cmake-vcpkg`, `cmake-android`, `cmake-ios`, `cmake-java`, `cmake-macos`, `cmake-meson`, `cmake-msix`, `cmake-napi`, `cmake-npm`, `cmake-windows`, `cmake-zig`, `cmake-harden`, `cmake-cargo`, `cmake-gn`, `cmake-fetch`, `cmake-ports`, `cmake-app-image`, `msix-manager`.
- Packaging and distributable workflows: `bundlebee`, `bundlebee-cli`, `make-pear-app`, `node-bare-bundle`, `extract-bare-bundle`, `drive-bundler`, `rebuild-git`, `electron-runtime`, `electron-forge-maker-snap`, `electron-forge-maker-flatpak`, `pear-runtime-bootstrap`, `pear-runtime-updater`, `pear-distributable-bootstrap`, `pear-installer`, `pear-prefetcher`, `bare-union-bundle`.
- Repo / release plumbing and legacy build repos: `bare-sidecar`, `bare-sidecar-bundle`, `bare-dev`, `make-pear-app`, `_pear-build`, `pear-electron`, `pear-runtime-appling`, `pear-shake`.

## 8) Examples, workshops, demos, and apps

Runnable examples, teaching repos, and application-level references.

- General examples and workshops: `examples`, `bare-snippets`, `pear-workshop`, `planb-summer-school`, `autobase-example`, `autobase-test-helpers`, `autobase-light-writer`, `hyperdb-workshop`, `hyperdb-autobase-workshop`, `hyperdb-benchmarking`.
- App demos and reference apps: `filesharing-app-example`, `filesharing-react-app-example`, `hello-pear-electron`, `pear-radio`, `pear-radio-backend`, `pearpass-example`, `autopass-mobile-example`, `bare-android`, `bare-ios`, `bare-expo`, `bare-expo-hrpc-demo`, `expo-bare-kit`, `expo-file-stream`, `hyperclip-ios`, `hyperclip-android`, `hyperclip-desktop`, `snake`, `cellery`, `cellery-html`, `sveltekit-adapter-bare`, `lunte`, `speedrun`.
- Runtime / platform demos: `bare-runtime`, `bare-kit`, `bare-native`, `bare-run`, `bare-repl`, `bare-node`, `bare-node-runtime`, `bare-sidecar`, `bare-open`, `bare-storage`.
- Pear demos and app flows: `pear-ci`, `pear-ci-example`, `pear-ci-multisig`, `pear-docs`, `pear-templates`, `pear-prefs`, `pear-user-dirs`, `pear-messages`, `pear-message`, `pear-hyperdb`, `pear-appdrive`.

## 9) Utilities, observability, security, and dev tools

Small focused packages for scheduling, parsing, crypto, debugging, metrics, and operational tooling.

- Coordination, lifecycle, and state: `activity-queue`, `adaptive-timeout`, `bucket-rate-limit`, `delay-pacer`, `task-backoff`, `db-lock`, `scope-lock`, `ready-guard`, `ready-resource`, `refcounter`, `suspendify`, `suspend-resource`, `minicron`, `listen-async`, `uncaughts`, `fd-lock`, `fs-native-lock`, `fifofile`, `fd-pipe`, `cross-worker`, `bare-readline`, `bare-signals`, `bare-env`, `bare-boot`, `bare-atomics`, `bare-abort`, `bare-gif`, `bare-xdiff`, `bare-tpl`.
- Parsing, formatting, and conversions: `fast-meta-tags`, `get-file-format`, `get-mime-type`, `is-text-filetype`, `known-text-files`, `unicode-to-plain-text`, `text-decoder`, `url-file-url`, `same-object`, `nanodebug`, `bits-to-bytes`, `unslab`, `tiny-buffer-map`, `tiny-paths`, `tiny-timers-native`, `framed-stream`, `bare-inspect`, `bare-structured-clone`.
- Crypto, identity, and data protection: `sodium-hmac`, `pw-to-ek`, `deterministic-sealed-box`, `broadcast-encryption`, `obfuscate-data`, `noise-curve-ed`, `noise-handshake`, `secure-key`, `secure-prompt`, `safe-sodium-buffer`, `bip39-mnemonic`.
- Observability and metrics: `hypertrace`, `hypertrace-logger`, `hypertrace-prometheus`, `hypermetrics`, `hyper-instrument`, `hyper-health-check`, `hypercore-logger`, `hypercore-stats`, `hyperdht-stats`, `Grafana-hypercore-stats`, `prom-client`, `slab-hunter`, `device-file`, `sentry-bare`.
- Testing and developer experience: `brittle`, `brittle-snapshot`, `bare-tap`, `test-suspend`, `check-npm-maintainers`, `bare-cov`, `bare-v8-to-istanbul`, `globbie`, `semifies`, `same-object`.
- Miscellaneous helpers: `fast-meta-tags`, `get-mime-type`, `known-text-files`, `is-text-filetype`, `raw-text-display-parser`, `simple-lnd`, `jsonrpc-mux`.

## 10) Org infrastructure and misc

- Org / repository scaffolding: `.github`, `repo-template`, `prettier-config-holepunch`, `actions`.
- Packaging / maintenance one-offs: `slack-build-status`, `canary-runner`, `oidc-publishing`, `oidc-publishing-sandbox`, `check-npm-maintainers`, `bare-union-bundle`.
- Miscellaneous or cross-cutting repositories: `bundlebee`, `bundlebee-cli`, `device-file`, `globbie`, `hisect`, `lunte`, `rache`, `rebuild-git`, `uncaughts`, `nanodebug`, `minicron`, `same-object`, `semifies`, `rocksdb-blobs`.

## Notes

- Some repositories fit more than one group; the taxonomy uses the most likely primary use case.
- The index is intentionally taxonomy-first, so repo lists are compact and name-oriented rather than fully annotated.
- This file is an inferred map for architectural scanning, not a canonical org inventory.
- Refreshes should keep the total repo count and category placement aligned with the latest GitHub search results.
- Latest refresh surfaced `libhc`, `libkv`, `libflattree` and other recently added runtime/build helpers; if you need a stricter canonical inventory, regenerate from a full repo export rather than search snapshots.
