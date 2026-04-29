# Holepunch Organization Repository Index

Generated at: 2026-04-29
Source organization: `holepunchto`

## Scope

- Public repositories returned by GitHub search for `user:holepunchto`.
- GitHub returned **593** public repositories at refresh time.
- This is a taxonomy-first index: repositories are grouped by inferred primary use case, with representative repos listed under each group.
- Private repositories are not included in GitHub search results.

## Use-case taxonomy

### 1) Bare runtime & platform
Core runtime, workers, shells, and process primitives.

- `bare` — Small and modular JavaScript runtime for desktop and mobile.
- `bare-runtime` — Prebuilt Bare binaries for macOS, iOS, Linux, Android, and Windows.
- `bare-kit` — Bare for native application development.
- `bare-native` — Native application development framework for Bare.
- `bare-worker` — Higher-level worker threads for JavaScript.
- `bare-vm` — Isolated JavaScript contexts for Bare.
- `bare-channel` — Inter-thread messaging for JavaScript.
- `bare-process`, `bare-subprocess`, `bare-daemon`, `bare-sidecar`, `bare-open`, `bare-os`, `bare-thread`, `bare-realm`, `bare-inspector`, `bare-inspector-gc`, `bare-performance`, `bare-hrtime`, `bare-walk-handles`, `bare-storage`, `bare-node-runtime`, `bare-node`, `bare-async-hooks`, `bare-queue-microtask`, `bare-stdio`.

### 2) Bare builtins, shims, and compatibility layers
Compatibility modules and standard-library style helpers for Bare and adjacent runtimes.

- `b4a` — Bridging the gap between buffers and typed arrays.
- `bare-buffer`, `bare-events`, `bare-console`, `bare-fs`, `bare-net`, `bare-tcp`, `bare-dgram`, `bare-tls`, `bare-http1`, `bare-http-parser`, `bare-https`, `bare-fetch`, `bare-ws`.
- `bare-url`, `bare-path`, `bare-querystring`, `bare-mime`, `bare-encoding`, `bare-intl`, `bare-string-decoder`, `bare-punycode`, `bare-form-data`, `bare-abort-controller`, `bare-structured-clone`, `bare-diagnostics-channel`, `bare-type`, `bare-utils`, `bare-semver`.
- `events-universal`, `require-addon`, `require-asset`, `which-runtime`, `bare-node-fetch`.

### 3) Pear runtime, lifecycle, and CLI flows
Pear runtime plumbing, application lifecycle, command-line flows, and docs.

- `pear` — Combined Peer-to-Peer runtime, development, and deployment tool.
- `pear-runtime`, `pear-desktop`, `pear-electron`, `pear-terminal`, `pear-cli`, `pear-cmd`, `pear-api`, `pear-interface`, `pear-info`, `pear-link`, `pear-bridge`.
- `pear-build`, `pear-bundle`, `pear-pack`, `pear-stage`, `pear-seed`, `pear-dump`, `pear-shake`, `pear-init`, `pear-prefetcher`, `pear-installer`, `pear-distributable-bootstrap`.
- `pear-ipc`, `pear-ipc-client`, `pear-message`, `pear-messages`, `pear-opstream`, `pear-opwait`, `pear-state`, `pear-rti`, `pear-constants`, `pear-errors`, `pear-release`, `pear-prerelease`.
- `pear-wakeups`, `pear-updates`, `pear-force-update`, `pear-restart`, `pear-reset`, `pear-drop`, `pear-gracedown`, `pear-crasher`, `pear-tryboot`, `pear-changelog`, `pear-md`, `pear-prefs`, `pear-user-dirs`, `pear-aliases`.
- `pear-docs`, `pear-templates`, `pear-workshop`, `pear-radio`, `pear-radio-backend`, `pear-ci`, `pear-ci-example`, `pear-ci-multisig`, `pear-runtime-updater`, `pear-runtime-bootstrap`, `pear-runtime-bare`, `pear-runtime-legacy-storage`, `pear-logger`, `pear-gunk`, `pear-appling`, `pear-pipe`, `pear-hyperdb`.

### 4) Hypercore data, storage, and drive tooling
Distributed logs, file systems, corestores, and drive-oriented workflows.

- `hypercore`, `hyperbee`, `hyperbee2`, `hyperdrive`, `hyperdrive-next`, `hyperdb`, `corestore`, `corestore-snapshot`, `hyperblobs`, `hyperconf`.
- `hypercore-storage`, `hypercore-sign`, `hypercore-signing-request`, `hypercore-crypto`, `hypercore-encryption`, `hypercore-errors`, `hypercore-id-encoding`, `hypercore-proof-queue`, `hypercore-byte-stream`, `hypercore-blob-server`, `hypercore-audit`, `hypercore-logger`, `hypercore-stats`, `hypercore-detector`, `hypercore-e2e-tests`, `hypercore-scale-tests`.
- `hyperdrive-profiler`, `hyperdrive-swarm-test`, `drive-resolve`, `watch-drive`, `serve-drive`, `localdrive`, `mirror-drive`, `drives`, `drive-bundler`, `distributed-drive`, `network-block-device`, `simple-seeder`, `seedbee`, `localwatch`, `throwaway-local-cache`.
- `rocksdb-blobs`, `rocksdb-native`, `sqlite3-native`, `key-collection`, `multi-profile-store`, `passive-core-watcher`, `index-encoder`, `index-keys`, `emoji-index`.

### 5) Networking, DHT, RPC, and transport
Peer discovery, swarms, multiplexing, protocol bridges, and transport layers.

- `hyperdht`, `hyperswarm`, `hyperswarm-secret-stream`, `hyperswarm-dht-relay`, `hyperswarm-testnet`, `hyperswarm-stats`, `hyperdht-stats`, `hyperswarm-capability`, `hyperswarm-seeders`, `hyperswarm-doctor`, `hyperswarm-e2e-tests`.
- `dht-rpc`, `rpc`, `protomux`, `protomux-rpc`, `protomux-rpc-client`, `protomux-rpc-client-pool`, `protomux-rpc-router`, `protomux-rpc-middleware`, `protomux-wakeup`, `jsonrpc-mux`, `hrpc`, `hrpc-swift`, `hrpc-modular-example`, `bare-rpc`, `bare-rpc-swift`, `bare-rpc-golang`, `bare-zmq`, `bot-rpc`, `hp-rpc-cli`.
- `bare-net`, `bare-tcp`, `bare-dgram`, `bare-tls`, `bare-ws`, `bare-http1`, `bare-http-parser`, `bare-https`, `bare-dns`, `http-forward-host`, `http-dht-proxy`, `netpaste`, `repl-swarm`, `hyperssh`, `hyperbeam`, `git-remote-punch-transport`, `autobase-discovery`, `autobase-discovery-cli`, `gip-remote`, `gip-transport`, `punch-connection-encoding`, `pattern-router`, `ptnm`, `iambus`, `raw-text-display-parser`.

### 6) Blind networking and Keet-specific flows
Blind peer discovery, pairing, relays, and Keet identity flows.

- `blind-peer`, `blind-peer-cli`, `blind-peer-encodings`, `blind-peer-muxer`, `blind-peer-router`, `blind-peering`, `blind-peering-cli`, `blind-relay`, `blind-relay-service`, `blind-pairing`, `blind-pairing-core`, `blind-encryption-sodium`.
- `keypear`, `keet-identity-key`, `keet-appling`, `keet-appling-next`, `keet-prefs`, `keet-mobile-releases`, `pear-multisig-link`.

### 7) Native libraries, ABI layers, and bindings
Reusable C/C++/Swift/Go/Rust building blocks, ABI layers, and native wrappers.

- Core native layers: `libjs`, `libqjs`, `libjsc`, `libjerry`, `libmqjs`, `libnapi`, `libjsi`, `libjstl`, `libjnitl`, `libpear`, `libappling`, `libpearsync`, `libdynload`, `libmem`, `liblog`, `libdaemon`, `librlimit`, `libjson`, `libpath`, `libutf`, `liburl`, `libbase64`, `libhex`, `libz32`, `libcrc`, `libprng`, `libquickbit`, `libsimdle`, `libbitarray`, `libcompact`, `libintrusive`, `libparseline`, `libtls`, `librabin`, `librpc`, `librocksdb`, `libfs`, `libfx`, `libtt`, `libudx`, `libsingleset`.
- JavaScript/C API bindings: `quickbit-native`, `bitarray-native`, `simdle-native`, `crc-native`, `rabin-native`, `sqlite3-native`, `rocksdb-native`, `udx-native`, `fx-native`, `tt-native`, `appling-native`, `libjsi`.
- Bare platform / native add-ons: `bare-compat-napi`, `bare-v8`, `bare-v8-to-istanbul`, `bare-addon`, `bare-addon-rust`, `bare-addon-java`, `bare-addon-jstl`, `bare-addon-resolve`, `bare-bluetooth-apple`, `bare-bluetooth-android`, `bare-web-kit`, `bare-web-kit-gtk`, `bare-ui-kit`, `bare-win-ui`, `bare-gtk`, `bare-sdl`, `bare-bmp`, `bare-png`, `bare-jpeg`, `bare-heif`, `bare-webp`, `bare-svg`, `bare-ico`, `bare-tiff`, `bare-exif`, `bare-image-resample`, `bare-ffmpeg`, `bare-md4c`, `bare-zlib`, `bare-media`, `bare-mime`, `bare-punycode`, `bare-delta`, `bare-posix`, `bare-ndk`, `bare-lief`, `bare-zmq`, `bare-node-fetch`, `bare-file-logger`, `bare-system-logger`, `bare-performance`, `bare-logger`, `bare-debug-log`.

### 8) Build, packaging, and release automation
Cross-platform build helpers, packaging recipes, and release tooling.

- Shared tooling: `actions`, `canary-runner`, `slack-build-status`, `oidc-publishing`, `oidc-publishing-sandbox`, `prettier-config-holepunch`, `repo-template`.
- Native build helpers: `bare-prebuild`, `prebuild-containers`, `chromium-prebuilds`, `musl-toolchains`, `ninja-runtime`.
- CMake and bridge modules: `cmake-bare`, `cmake-bare-bundle`, `cmake-drive`, `cmake-pear`, `cmake-runtime`, `cmake-toolchains`, `cmake-vcpkg`, `cmake-android`, `cmake-ios`, `cmake-java`, `cmake-macos`, `cmake-meson`, `cmake-msix`, `cmake-napi`, `cmake-npm`, `cmake-windows`, `cmake-zig`, `cmake-harden`, `cmake-cargo`, `cmake-gn`, `cmake-fetch`, `cmake-ports`, `cmake-app-image`.
- Bundle and distributable tooling: `bare-make`, `bare-build`, `bare-bundle`, `bare-bundle-compile`, `bare-bundle-evaluate`, `bare-bundle-id`, `bare-pack`, `bare-pack-drive`, `bare-unpack`, `bare-sidecar-bundle`, `bare-app-image`, `bare-apk`, `bare-distributable`, `bundlebee`, `bundlebee-cli`, `make-pear-app`, `electron-runtime`, `electron-forge-maker-snap`, `electron-forge-maker-flatpak`, `node-bare-bundle`, `extract-bare-bundle`, `drive-bundler`, `rebuild-git`, `bare-rust`.

### 9) Examples, workshops, and demos
Proof-of-concept apps, teaching repos, and end-to-end examples.

- `examples`, `bare-snippets`, `pear-workshop`, `planb-summer-school`, `autobase-example`, `autobase-test-helpers`, `autobase-light-writer`, `hyperdb-workshop`, `hyperdb-autobase-workshop`, `hyperdb-benchmarking`.
- `filesharing-app-example`, `filesharing-react-app-example`, `hello-pear-electron`, `pear-radio`, `pear-radio-backend`, `pearpass-example`, `autopass-mobile-example`, `bare-android`, `bare-ios`, `bare-expo`, `bare-expo-hrpc-demo`, `expo-bare-kit`, `expo-file-stream`, `hyperclip-ios`, `hyperclip-android`, `hyperclip-desktop`, `snake`, `cellery`, `cellery-html`, `drive-analyzer`, `sveltekit-adapter-bare`, `lunte`, `speedrun`.

### 10) Utilities, observability, security, and dev tools
Small focused packages for scheduling, parsing, crypto, debugging, and metrics.

- Coordination and lifecycle: `activity-queue`, `adaptive-timeout`, `delay-pacer`, `bucket-rate-limit`, `db-lock`, `scope-lock`, `ready-guard`, `ready-resource`, `refcounter`, `suspendify`, `suspend-resource`, `task-backoff`, `listen-async`, `minicron`, `uncaughts`, `fd-lock`, `fs-native-lock`, `fifofile`, `fd-pipe`.
- Parsing and conversion helpers: `fast-meta-tags`, `get-file-format`, `get-mime-type`, `is-text-filetype`, `known-text-files`, `unicode-to-plain-text`, `url-file-url`, `text-decoder`, `same-object`, `nanodebug`, `bits-to-bytes`, `unslab`, `tiny-buffer-map`, `tiny-buffer-rpc`, `tiny-fs-native`, `tiny-http-native`, `tiny-paths`, `tiny-timers-native`, `framed-stream`, `events-universal`.
- Crypto and verification: `sodium-hmac`, `pw-to-ek`, `deterministic-sealed-box`, `broadcast-encryption`, `obfuscate-data`, `noise-curve-ed`, `noise-handshake`, `secure-key`, `secure-prompt`, `safe-sodium-buffer`.
- Test, tracing, and metrics: `brittle`, `brittle-snapshot`, `bare-tap`, `test-suspend`, `hypertrace`, `hypertrace-prometheus`, `hypermetrics`, `hyper-instrument`, `hyper-health-check`, `hypercore-logger`, `hypercore-stats`, `hyperdht-stats`, `Grafana-hypercore-stats`, `prom-client`, `check-npm-maintainers`, `device-file`.

## Recent additions surfaced in this refresh

These repos are good indicators of the latest org activity and were added or became prominent in the most recent search pass.

- Runtime / compatibility: `bare-https`, `bare-stream`, `bare-node-runtime`, `bare-sidecar`, `bare-os`, `bare-thread`, `bare-storage`, `bare-form-data`, `bare-intl`, `bare-querystring`, `bare-punycode`, `bare-async-hooks`.
- Networking / RPC: `bare-rpc-swift`, `bare-rpc-golang`, `bare-zmq`, `gip-remote`, `gip-transport`, `http-dht-proxy`, `hyperbeam`, `hyperssh`, `protomux-rpc-router`, `protomux-rpc-middleware`.
- Build / CI / packaging: `electron-forge-maker-snap`, `electron-forge-maker-flatpak`, `slack-build-status`.
- Examples / developer experience: `sveltekit-adapter-bare`, `bare-expo-hrpc-demo`, `bare-snippets`, `drive-analyzer`.

## Notes

- Some repositories fit more than one group; the taxonomy uses the most likely primary use case.
- Archived repos may still appear in GitHub search and are retained where relevant.
- This file is an inferred map for architectural scanning, not a canonical org inventory.
- The index is intentionally taxonomy-first, so the repo lists are representative rather than exhaustive.
