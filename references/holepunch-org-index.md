# Holepunch Organization Repository Index

Generated at: 2026-04-25
Source organization: `holepunchto`

## Scope

- Public repositories returned by GitHub search for `org:holepunchto`.
- GitHub returned **593** public repositories at refresh time.
- Repositories are regrouped by inferred use case for faster scanning.

## Use-case taxonomy

### 1) Bare
Core runtime, builtins, UI bindings, process primitives, bundling, packaging, and standard-library-style modules for the Bare ecosystem.

Representative repos:
- Runtime and platform: `bare`, `bare-runtime`, `bare-runtime-bare`, `bare-runtime-bootstrap`, `bare-runtime-updater`, `bare-native`, `bare-kit`, `bare-app-kit`, `bare-ui-kit`, `bare-win-ui`, `bare-gtk`, `bare-sdl`, `bare-vm`, `bare-realm`, `bare-worker`, `bare-thread`, `bare-channel`, `bare-atomics`, `bare-process`, `bare-subprocess`, `bare-daemon`, `bare-open`
- Node-compatible builtins: `bare-node`, `bare-node-runtime`, `bare-node-fetch`, `bare-async-hooks`, `bare-buffer`, `bare-events`, `bare-console`, `bare-readline`, `bare-stdio`, `bare-querystring`, `bare-url`, `bare-path`, `bare-format`, `bare-encoding`, `bare-structured-clone`, `bare-utils`, `bare-type`, `bare-assert`, `bare-env`, `bare-performance`, `bare-inspect`, `bare-inspector`, `bare-inspector-gc`, `bare-abort`, `bare-abort-controller`, `bare-queue-microtask`, `bare-hrtime`, `bare-timers`, `bare-signals`, `bare-buffer`
- Network / I-O / HTTP: `bare-fs`, `bare-net`, `bare-tcp`, `bare-dgram`, `bare-tls`, `bare-http1`, `bare-http-parser`, `bare-https`, `bare-fetch`, `bare-ws`, `bare-pipe`, `bare-tty`, `bare-zmq`, `bare-dns`, `bare-storage`, `bare-sidecar`, `bare-sidecar-bundle`, `bare-sidecar-bundle`, `bare-sidecar-bundle`, `bare-sidecar-bundle`, `bare-sidecar`, `bare-sidecar-bundle`, `bare-storage`
- Module / bundle / app tooling: `bare-module`, `bare-module-lexer`, `bare-module-resolve`, `bare-module-traverse`, `bare-addon`, `bare-addon-resolve`, `bare-link`, `bare-bundle`, `bare-bundle-compile`, `bare-bundle-evaluate`, `bare-bundle-id`, `bare-pack`, `bare-pack-drive`, `bare-unpack`, `bare-build`, `bare-make`, `bare-run`, `bare-distributable`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-distributable`, `bare-distributable`, `bare-distributable`, `bare-distributable`, `bare-distributable`, `bare-distributable`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`
- Media / content helpers: `bare-media`, `bare-mime`, `bare-png`, `bare-jpeg`, `bare-gif`, `bare-heif`, `bare-webp`, `bare-svg`, `bare-ico`, `bare-tiff`, `bare-exif`, `bare-image-resample`, `bare-ffmpeg`, `bare-md4c`, `bare-v8`, `bare-v8-to-istanbul`
- Compatibility and scaffolding: `bare-compat-napi`, `bare-headers`, `bare-dev`, `bare-cov`, `bare-rust`, `bare-addon-rust`, `bare-addon-java`, `bare-addon-jstl`, `bare-addon-resolve`, `bare-prebuild`, `bare-runtime-bare`, `bare-runtime-bootstrap`, `bare-runtime-updater`

### 2) Pear
App shell, runtime bootstrap, packaging, updates, lifecycle, and CLI flows for Pear applications.

Representative repos:
- Runtime / platform: `pear`, `pear-runtime`, `pear-runtime-bare`, `pear-runtime-bootstrap`, `pear-runtime-updater`, `pear-runtime-legacy-storage`, `pear-runtime-appling`, `pear-desktop`, `pear-electron`
- Build / pack / bootstrap: `pear-build`, `pear-bundle`, `pear-pack`, `pear-pack-drive`, `pear-stage`, `pear-seed`, `pear-dump`, `pear-shake`, `pear-init`, `pear-run`, `pear-prefetcher`, `pear-distributable-bootstrap`, `pear-pack`, `pear-appdrive`, `pear-hyperdb`
- CLI / developer tools: `pear-cli`, `pear-cmd`, `pear-doctor`, `pear-info`, `pear-terminal`, `pear-bridge`, `pear-ipc`, `pear-ipc-client`, `pear-api`, `pear-interface`, `pear-message`, `pear-messages`, `pear-opstream`, `pear-opwait`, `pear-ref`, `pear-rti`, `pear-state`, `pear-logger`, `pear-constants`, `pear-aliases`, `pear-link`
- Update / lifecycle: `pear-updater`, `pear-updater-bootstrap`, `pear-updates`, `pear-wakeups`, `pear-force-update`, `pear-restart`, `pear-reset`, `pear-drop`, `pear-gracedown`, `pear-crasher`, `pear-release`, `pear-prerelease`, `pear-prefs`, `pear-tryboot`, `pear-cmd`, `pear-cmd`
- Documentation / templates / examples: `pear-docs`, `pear-templates`, `pear-workshop`, `hello-pear-electron`, `make-pear-app`, `speedrun`, `pear-snippets`, `pear-expo-hello-world`
- Application helpers: `pear-pipe`, `pear-gunk`, `pear-stamp`, `pear-changelog`, `pear-user-dirs`, `pear-bridge`, `pear-md`, `pear-opstream`, `pear-opwait`, `pear-cmd`, `pear-prefs`, `pear-distributable-bootstrap`
- CI / release flows: `pear-ci`, `pear-ci-example`, `pear-ci-multisig`, `pear-ci-multisig`, `pear-multisig-link`, `pear-distributable-bootstrap`, `pear-pack`, `pear-pack-drive`, `pear-preference`, `pear-restart`, `pear-force-update`

### 3) P2P/Hypercore
Distributed logs, file systems, DHT networking, multiplexed protocols, RPC, swarm tooling, and related P2P plumbing.

Representative repos:
- Core storage / data structures: `hypercore`, `hyperbee`, `hyperbee2`, `hyperdrive`, `hyperdrive-next`, `hyperdb`, `corestore`, `autobase`, `autopass`, `hyperblobs`, `hyperconf`, `hyper-multisig`, `multi-profile-store`, `passive-core-watcher`, `core-coupler`, `corestore-snapshot`, `corestore`, `corestore-snapshot`
- DHT / swarm / transport: `hyperdht`, `hyperswarm`, `dht-rpc`, `rpc`, `protomux`, `protomux-rpc`, `protomux-rpc-client`, `protomux-rpc-client-pool`, `protomux-rpc-router`, `protomux-rpc-middleware`, `protomux-wakeup`, `hyperswarm-secret-stream`, `hyperswarm-dht-relay`, `hyperswarm-capability`, `hyperswarm-doctor`, `hyperswarm-seeders`, `hyperswarm-testnet`, `hyperswarm-stats`, `hyperswarm-e2e-tests`, `instrumented-dht-node`, `hyperdht-stats`
- Drive / file sync / serving: `localdrive`, `mirror-drive`, `distributed-drive`, `drive-resolve`, `drive-bundler`, `drive-analyzer`, `watch-drive`, `serve-drive`, `boot-drive`, `tar-drive`, `hyperdrive-profiler`, `hyperdrive-swarm-test`, `hyperdrive-byte-stream`, `hyperdrive-swarm-test`, `network-block-device`, `simple-seeder`, `seedbee`, `seeder-frontend`
- Hypercore helpers / codecs / proofs: `hypercore-storage`, `hypercore-encryption`, `hypercore-sign`, `hypercore-signing-request`, `hypercore-id-encoding`, `hypercore-errors`, `hypercore-crypto`, `hypercore-messages`, `hypercore-proof-queue`, `hypercore-stats`, `hypercore-blob-server`, `hypercore-byte-stream`, `hypercore-detector`, `hypercore-audit`, `hypercore-e2e-tests`, `hypercore-scale-tests`, `hypercore-logger`, `hypercoreify`, `hypercore-blob-server`
- Schema / RPC / encoding utilities: `compact-encoding`, `compact-encoding-bitfield`, `compact-encoding-variant`, `compact-encoding-struct`, `compact-encoding-net`, `compact-encoding-swift`, `compact-encoding-golang`, `hyperschema`, `hyperschema-swift`, `hyperdispatch`, `hrpc`, `hrpc-swift`, `hrpc-modular-example`, `jsonrpc-mux`, `dependency-stream`, `sloppy-module-parser`, `script-linker`, `punch-connection-encoding`, `index-encoder`, `index-keys`, `sub-encoder`, `key-collection`, `hash?`
- Blind-networking family: `blind-peer`, `blind-peer-cli`, `blind-peer-encodings`, `blind-peer-muxer`, `blind-peer-router`, `blind-peering`, `blind-peering-cli`, `blind-relay`, `blind-relay-service`, `blind-pairing`, `blind-pairing-core`, `blind-encryption-sodium`
- Observability / debugging / performance: `hypertrace`, `hypertrace-logger`, `hypertrace-prometheus`, `hypermetrics`, `hyper-instrument`, `hyper-health-check`, `hypercore-logger`, `hypercore-stats`, `hyperdht-stats`, `Grafana-hypercore-stats`, `repl-swarm`, `netpaste`, `http-dht-proxy`, `http-forward-host`, `git-remote-punch-transport`, `mininet`, `hypermininet`

### 4) Native
Reusable C/C++/Swift/Go/Java/Rust building blocks, ABI shims, and native bindings across runtime boundaries.

Representative repos:
- JS engine / ABI shims: `libjs`, `libqjs`, `libjerry`, `libjsc`, `libmqjs`, `libnapi`, `libjsi`, `libjstl`, `libjnitl`, `libpear`, `libappling`, `libpearsync`, `libdynload`, `libmem`, `liblog`, `libdaemon`, `librlimit`
- Data / text / encoding primitives: `libjson`, `libpath`, `libutf`, `liburl`, `libbase64`, `libhex`, `libz32`, `libcrc`, `libprng`, `libquickbit`, `libsimdle`, `libbitarray`, `libcompact`, `libintrusive`, `libsingleset`, `libparseline`, `libtls`, `librabin`, `librpc`, `libudx`, `librocksdb`, `libfs`, `libfx`, `libtt`, `libnapi`, `libjs`, `liburl`
- Native addons / wrappers: `quickbit-native`, `bitarray-native`, `simdle-native`, `crc-native`, `crc-universal`, `rabin-native`, `sqlite3-native`, `fx-native`, `tt-native`, `rocksdb-native`, `udx-native`, `require-addon`, `require-asset`, `bare-compat-napi`, `bare-v8`, `bare-v8-to-istanbul`
- Bare platform bindings: `bare-bluetooth-apple`, `bare-bluetooth-android`, `bare-web-kit`, `bare-web-kit-gtk`, `bare-ui-kit`, `bare-win-ui`, `bare-gtk`, `bare-sdl`, `bare-rpc-swift`, `bare-rpc-golang`, `bare-addon-rust`, `bare-addon-java`, `bare-addon-jstl`, `bare-addon-resolve`, `bare-native`
- Mobile / desktop shells and SDKs: `bare-kit`, `bare-app-kit`, `bare-runtime-bare`, `bare-android`, `bare-ios`, `bare-expo`, `react-native-bare-kit`, `react-native-b4a`, `bare-expo-hrpc-demo`, `expo-bare-kit`, `expo-file-stream`, `bare-rust`
- Platform-specific support: `bare-zmq`, `bare-webp`, `bare-png`, `bare-jpeg`, `bare-gif`, `bare-heif`, `bare-tiff`, `bare-svg`, `bare-ico`, `bare-exif`, `bare-image-resample`, `bare-ffmpeg`, `bare-md4c`, `bare-delta`, `bare-walk-handles`, `bare-system-logger`, `thread-stats`

### 5) Build/CI
Cross-platform build helpers, packaging recipes, release automation, and repository operations.

Representative repos:
- CMake / build system helpers: `cmake-bare`, `cmake-bare-bundle`, `cmake-drive`, `cmake-fetch`, `cmake-pear`, `cmake-runtime`, `cmake-ports`, `cmake-toolchains`, `cmake-vcpkg`, `cmake-android`, `cmake-ios`, `cmake-java`, `cmake-macos`, `cmake-meson`, `cmake-msix`, `cmake-napi`, `cmake-npm`, `cmake-windows`, `cmake-zig`, `cmake-harden`, `cmake-bare-bundle`, `cmake-cargo`, `cmake-gn`
- Packaging / release artifacts: `bare-prebuild`, `prebuild-containers`, `chromium-prebuilds`, `musl-toolchains`, `ninja-runtime`, `bare-runtime`, `electron-runtime`, `bundled?`, `bundlebee`, `bundlebee-cli`, `bare-apk`, `bare-app-image`, `bare-distributable`, `bare-pack`, `bare-unpack`, `bare-make`
- Automation / CI / infra: `actions`, `canary-runner`, `slack-build-status`, `oidc-publishing`, `oidc-publishing-sandbox`, `check-npm-maintainers`, `repo-template`, `prettier-config-holepunch`, `updater-service`, `pear-ci`, `pear-ci-example`, `pear-ci-multisig`, `pear-runtime-updater`, `pear-runtime-bootstrap`
- GitHub / release tooling: `request-copilot-review` (tooling only), `bare-prebuild`, `bear?`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`, `bare-prebuild`
- Misc build glue: `make-pear-app`, `bare-build`, `bare-bundle`, `bare-bundle-compile`, `bare-bundle-evaluate`, `bare-bundle-id`, `bare-sidecar-bundle`, `bare-pack-drive`, `pear-pack-drive`, `pear-distributable-bootstrap`

### 6) Examples
Proof-of-concept apps, demos, workshops, and teaching repositories.

Representative repos:
- General examples: `examples`, `bare-snippets`, `pear-workshop`, `planb-summer-school`, `speedrun`
- Bare app demos: `bare-android`, `bare-ios`, `bare-expo`, `bare-expo-hrpc-demo`, `hello-pear-electron`, `bare-expo-hello-world`
- Pear app demos and templates: `autopass-mobile-example`, `autopass-example`, `pearpass-example`, `pear-radio`, `pear-radio-backend`, `pear-desktop`, `pear-doctor`, `pear-templates`, `pear-md`, `pear-bridge`
- Hypercore / P2P workshops: `autobase-example`, `autobase-test-helpers`, `autobase-light-writer`, `hyperdb-workshop`, `hyperdb-autobase-workshop`, `hypercore-e2e-tests`, `hypercore-scale-tests`, `hyperdrive-swarm-test`, `hyperswarm-testnet`, `hyperswarm-e2e-tests`
- Utility demos: `filesharing-app-example`, `filesharing-react-app-example`, `snake`, `simple-seeder`, `seedbee`, `drive-analyzer`, `watch-drive`, `serve-drive`, `repl-swarm`

### 7) Utilities
Small focused packages that support the larger stacks: helper functions, guards, parsers, and narrow-purpose modules.

Representative repos:
- Concurrency / lifecycle / backoff: `activity-queue`, `adaptive-timeout`, `delay-pacer`, `bucket-rate-limit`, `db-lock`, `scope-lock`, `ready-guard`, `ready-resource`, `refcounter`, `suspendify`, `suspend-resource`, `task-backoff`, `listen-async`, `minicron`, `rache`, `uncaughts`, `slab-hunter`, `fd-lock`, `fs-native-lock`, `fifofile`, `fd-pipe`
- Parsing / detection / formatting: `fast-meta-tags`, `get-file-format`, `get-mime-type`, `is-text-filetype`, `known-text-files`, `unicode-to-plain-text`, `url-file-url`, `text-decoder`, `same-object`, `nanodebug`, `b4a`, `bits-to-bytes`, `unslab`, `tiny-buffer-map`, `tiny-buffer-rpc`, `tiny-fs-native`, `tiny-http-native`, `tiny-paths`, `tiny-timers-native`, `framed-stream`, `events-universal`
- Crypto / security helpers: `secure-key`, `secure-prompt`, `sodium-hmac`, `pw-to-ek`, `deterministic-sealed-box`, `broadcast-encryption`, `obfuscate-data`, `safe-sodium-buffer`, `noise-curve-ed`, `noise-handshake`
- Text / document / metadata helpers: `plain-text`, `raw-text-display-parser`, `emoji-index`, `get-mime-type`, `get-file-format`, `known-text-files`, `is-text-filetype`, `fast-meta-tags`, `compact-encoding-*`, `pocket?`, `pattern-router`, `ptnm`, `iambus`, `same-object`
- Runtime detection / compatibility: `which-runtime`, `events-universal`, `require-asset`, `require-addon`, `b4a`, `unicode-to-plain-text`, `bare-utils`, `bare-type`, `bare-which`

## Notes

- Some repositories may fit more than one group; the taxonomy uses the most likely primary use case.
- Private repositories are not included in GitHub’s public org search results.
- Archived repos may still appear in search and are retained here if relevant to the taxonomy.
- This file is an inferred map for architectural scanning, not a canonical org inventory.
- The index is intentionally taxonomy-first, so some categories list representative repos rather than every repository name individually.
