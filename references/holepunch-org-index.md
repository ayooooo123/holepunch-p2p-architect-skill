# Holepunch Organization Repository Index

Generated at: 2026-04-24
Source organization: `holepunchto`

## Scope

- Public repositories currently returned by GitHub search for `org:holepunchto`.
- GitHub returned **591** public repositories at refresh time.
- Repositories are regrouped by inferred use case for faster scanning.

## Use-case taxonomy

### 1) Bare
Core runtime, builtins, UI bindings, process primitives, and standard-library-style modules.

Representative repos:
- `bare`, `bare-runtime`, `bare-kit`, `bare-native`, `bare-app-kit`
- `bare-node`, `bare-node-runtime`, `bare-node-fetch`
- `bare-fs`, `bare-net`, `bare-tcp`, `bare-dgram`, `bare-tls`, `bare-http1`, `bare-http-parser`, `bare-https`, `bare-fetch`
- `bare-buffer`, `bare-stream`, `bare-events`, `bare-console`, `bare-readline`, `bare-stdio`, `bare-process`, `bare-thread`, `bare-worker`, `bare-channel`, `bare-atomics`
- `bare-url`, `bare-path`, `bare-querystring`, `bare-encoding`, `bare-structured-clone`, `bare-utils`, `bare-assert`, `bare-env`
- `bare-vm`, `bare-realm`, `bare-performance`, `bare-inspector`, `bare-inspector-gc`, `bare-abort`, `bare-abort-controller`
- `bare-module`, `bare-module-lexer`, `bare-module-resolve`, `bare-module-traverse`, `bare-link`, `bare-addon`, `bare-addon-resolve`
- `bare-bundle`, `bare-bundle-compile`, `bare-bundle-evaluate`, `bare-bundle-id`, `bare-pack`, `bare-unpack`, `bare-sidecar`, `bare-build`, `bare-make`, `bare-run`, `bare-distributable`, `bare-open`
- `bare-apk`, `bare-app-image`, `bare-boot`, `bare-storage`, `bare-headers`, `bare-dev`, `bare-cov`

### 2) Pear
App shell, runtime bootstrap, updates, packing, CLI flows, and app lifecycle tools.

Representative repos:
- `pear`, `pear-runtime`, `pear-runtime-bare`, `pear-runtime-bootstrap`, `pear-runtime-updater`, `pear-runtime-legacy-storage`
- `pear-build`, `pear-bundle`, `pear-pack`, `pear-stage`, `pear-seed`, `pear-run`, `pear-init`, `pear-info`
- `pear-desktop`, `pear-electron`, `pear-terminal`, `pear-cli`, `pear-cmd`, `pear-docs`, `pear-templates`
- `pear-ipc`, `pear-ipc-client`, `pear-api`, `pear-interface`, `pear-message`, `pear-messages`, `pear-opstream`, `pear-opwait`, `pear-ref`, `pear-rti`, `pear-state`
- `pear-updater`, `pear-updater-bootstrap`, `pear-updates`, `pear-wakeups`, `pear-force-update`, `pear-restart`, `pear-reset`, `pear-drop`, `pear-gracedown`, `pear-crasher`
- `pear-aliases`, `pear-link`, `pear-prefetcher`, `pear-prerelease`, `pear-release`, `pear-stamp`, `pear-shake`, `pear-hyperdb`, `pear-appdrive`, `pear-dump`, `pear-radio`, `pear-radio-backend`
- `pear-appling`, `_pear-build`, `pear-ci`, `pear-ci-example`, `pear-ci-multisig`, `pear-multisig-link`
- `hello-pear-electron`, `sveltekit-adapter-bare`, `make-pear-app`, `pear-workshop`, `pear-snippets`, `speedrun`

### 3) P2P/Hypercore
Distributed logs, file systems, DHT networking, multiplexed protocols, RPC, and swarm tooling.

Representative repos:
- `hypercore`, `hyperdrive`, `hyperbee`, `hyperbee2`, `hyperblobs`, `corestore`, `autobase`, `hyperdb`, `hyperconf`
- `hyperdht`, `hyperswarm`, `dht-rpc`, `rpc`, `protomux`, `protomux-rpc`, `protomux-rpc-client`, `protomux-rpc-client-pool`, `protomux-rpc-router`, `protomux-rpc-middleware`, `protomux-wakeup`
- `libudx`, `udx-native`, `bare-dgram`, `bare-tcp`, `bare-https`, `bare-tls`, `bare-ws`
- `hypercore-storage`, `hypercore-encryption`, `hypercore-sign`, `hypercore-signing-request`, `hypercore-id-encoding`, `hypercore-errors`, `hypercore-crypto`, `hypercore-messages`, `hypercore-proof-queue`, `hypercore-stats`, `hypercore-blob-server`, `hypercore-byte-stream`, `hypercore-detector`, `hypercore-audit`, `hypercore-e2e-tests`, `hypercore-scale-tests`
- `hyperdrive-next`, `hyperdrive-profiler`, `hyperdrive-swarm-test`, `mirror-drive`, `localdrive`, `tar-drive`, `serve-drive`, `drive-resolve`, `drive-bundler`, `drive-analyzer`, `watch-drive`, `boot-drive`, `distributed-drive`
- `rabin-stream`, `rabin-native`, `rocksdb-native`, `rocksdb-blobs`, `multi-profile-store`, `passive-core-watcher`, `core-coupler`, `index-encoder`, `index-keys`, `sub-encoder`, `key-collection`
- `seedbee`, `simple-seeder`, `hyperswarm-seeders`, `hyperswarm-testnet`, `hyperswarm-doctor`, `hyperswarm-stats`, `hyperswarm-secret-stream`, `hyperswarm-dht-relay`, `hyperbeam`, `repl-swarm`, `netpaste`, `http-dht-proxy`, `http-forward-host`, `git-remote-punch-transport`, `mininet`, `hypermininet`, `hyperdht-stats`, `instrumented-dht-node`, `Grafana-hypercore-stats`, `hyper-health-check`
- Blind-networking family: `blind-peer`, `blind-peer-cli`, `blind-peer-encodings`, `blind-peer-muxer`, `blind-peer-router`, `blind-peering`, `blind-peering-cli`, `blind-relay`, `blind-relay-service`, `blind-pairing`, `blind-pairing-core`, `blind-encryption-sodium`

### 4) Native
Reusable C/C++/Swift/Go/Java/Rust building blocks and ABI shims.

Representative repos:
- `libjs`, `libqjs`, `libjerry`, `libjsc`, `libmqjs`, `libnapi`, `libjsi`, `libjstl`, `libjnitl`
- `librocksdb`, `libudx`, `librpc`, `liblog`, `libfs`, `libfx`, `libtt`, `libjson`, `libpath`, `libutf`, `liburl`, `libmem`, `libprng`, `libsingleset`, `libintrusive`, `librlimit`, `libdaemon`, `libdynload`, `libparseline`, `libtls`, `libcrc`, `libbase64`, `libhex`, `libz32`, `libquickbit`, `libsimdle`, `libbitarray`, `libcompact`, `libpearsync`
- Native wrappers: `quickbit-native`, `bitarray-native`, `simdle-native`, `crc-native`, `crc-universal`, `rabin-native`, `sqlite3-native`, `fx-native`, `tt-native`, `libjsi`, `require-addon`, `require-asset`, `bare-compat-napi`
- Mobile / desktop bindings: `bare-bluetooth-apple`, `bare-bluetooth-android`, `bare-web-kit-gtk`, `bare-ui-kit`, `bare-win-ui`, `bare-gtk`, `bare-sdl`, `bare-rpc-swift`, `compact-encoding-swift`, `hrpc-swift`, `hyperschema-swift`

### 5) Build/CI
Cross-platform build helpers, packaging recipes, release automation, and repository ops.

Representative repos:
- `cmake-bare`, `cmake-bare-bundle`, `cmake-drive`, `cmake-fetch`, `cmake-pear`, `cmake-runtime`, `cmake-ports`, `cmake-toolchains`, `cmake-vcpkg`, `cmake-android`, `cmake-ios`, `cmake-java`, `cmake-macos`, `cmake-meson`, `cmake-msix`, `cmake-napi`, `cmake-npm`, `cmake-windows`, `cmake-zig`, `cmake-harden`
- `bare-prebuild`, `prebuild-containers`, `chromium-prebuilds`, `musl-toolchains`, `ninja-runtime`
- `bundlebee`, `bundlebee-cli`, `bare-prebuild`, `bare-runtime`, `electron-runtime`, `pear-runtime-appling`
- `actions`, `canary-runner`, `slack-build-status`, `oidc-publishing`, `oidc-publishing-sandbox`, `check-npm-maintainers`, `repo-template`, `prettier-config-holepunch`

### 6) Examples
Proof-of-concept apps and teaching repos.

Representative repos:
- `examples`, `pear-workshop`, `planb-summer-school`
- `bare-android`, `bare-ios`, `bare-expo`, `bare-expo-hrpc-demo`, `hello-pear-electron`, `speedrun`
- `autobase-example`, `autobase-test-helpers`, `autobase-light-writer`, `hyperdb-workshop`, `hyperdb-autobase-workshop`, `pearpass-example`, `filesharing-app-example`, `filesharing-react-app-example`, `pear-radio`, `snake`

### 7) Utilities
Small focused packages that support the larger stacks.

Representative repos:
- `activity-queue`, `adaptive-timeout`, `delay-pacer`, `bucket-rate-limit`, `db-lock`, `scope-lock`, `ready-guard`, `ready-resource`, `refcounter`, `suspendify`, `suspend-resource`, `task-backoff`, `time-decoder`/`text-decoder`, `same-object`, `nanodebug`, `uncaughts`, `slab-hunter`, `fd-lock`, `fs-native-lock`, `fifofile`, `listen-async`, `minicron`, `rache`
- `fast-meta-tags`, `get-file-format`, `get-mime-type`, `is-text-filetype`, `known-text-files`, `unicode-to-plain-text`, `url-file-url`, `wasm-tools`, `which-runtime`, `rache`
- `b4a`, `bits-to-bytes`, `unslab`, `tiny-buffer-map`, `tiny-buffer-rpc`, `tiny-fs-native`, `tiny-http-native`, `tiny-paths`, `tiny-timers-native`, `framed-stream`, `fd-pipe`, `emoji-index`

## Notes

- Some repositories may fit more than one group; the taxonomy uses the most likely primary use case.
- Private repositories are not included in GitHub’s public org search results.
- Archived repos may still appear in search and are retained here if relevant to the taxonomy.
- This file is an inferred map for architectural scanning, not a canonical org inventory.
