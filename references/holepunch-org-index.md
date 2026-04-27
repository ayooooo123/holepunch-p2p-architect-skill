# Holepunch Organization Repository Index

Generated at: 2026-04-27
Source organization: `holepunchto`

## Scope

- Public repositories returned by GitHub search for `user:holepunchto`.
- GitHub returned **593** public repositories at refresh time.
- Repositories are regrouped by inferred use case for faster scanning.

## Use-case taxonomy

### 1) Bare runtime & platform
Core runtime, workers, shells, and process primitives for Bare.

- `bare` — Small and modular JavaScript runtime for desktop and mobile.
- `bare-runtime` — Prebuilt Bare binaries for macOS, iOS, Linux, Android, and Windows.
- `bare-kit` — Bare for native application development.
- `bare-native` — Native application development framework for Bare.
- `bare-worker` — Higher-level worker threads for JavaScript.
- `bare-vm` — Isolated JavaScript contexts for Bare.
- `bare-channel` — Inter-thread messaging for JavaScript.
- `bare-process` — Node.js-compatible process control for Bare.
- `bare-subprocess` — Native process spawning for JavaScript.
- `bare-daemon` — Create and manage daemon processes in JavaScript.
- `bare-open` — Cross-platform application launcher for Bare.
- `bare-realm` — Realm support for Bare.
- `bare-os` — Operating system utilities for Bare.
- `bare-runtime-bare` — bare binary that bootstraps the platform.
- `bare-runtime-updater` — Listens for OTA Bare updates.
- `bare-runtime-bootstrap` — Bootstrap helper for the Bare runtime.

### 2) Bare builtins & standard-library shims
Compatibility modules, core APIs, and common runtime helpers for Bare.

- `b4a` — Bridging the gap between buffers and typed arrays.
- `bare-buffer` — Native buffers for JavaScript.
- `bare-events` — Event emitters for JavaScript.
- `bare-console` — WHATWG debugging console for JavaScript.
- `bare-fs` — Native file system operations for Bare.
- `bare-net` — TCP and IPC servers and clients for JavaScript.
- `bare-tcp` — Native TCP sockets for JavaScript.
- `bare-dgram` — Native UDP for JavaScript.
- `bare-tls` — Transport Layer Security (TLS) streams for JavaScript.
- `bare-http1` — HTTP/1 library for JavaScript.
- `bare-fetch` — WHATWG Fetch implementation for Bare.
- `bare-ws` — WebSocket library for JavaScript.
- `bare-url` — WHATWG URL implementation for JavaScript.
- `bare-path` — Path manipulation library for JavaScript.
- `bare-encoding` — WHATWG text encoding interfaces for JavaScript.
- `bare-inspector` — V8 inspector support for Bare.
- `bare-utils` — Node.js-compatible utility functions for Bare.
- `events-universal` — Universal wrapper for the Node.js events module.
- `require-addon` — Import native addons across JavaScript runtimes.
- `require-asset` — Import assets across JavaScript runtimes.

### 3) Pear runtime, shell, and lifecycle
Pear runtime plumbing, application lifecycle, CLI flows, and documentation.

- `pear` — combined Peer-to-Peer (P2P) Runtime, Development & Deployment tool.
- `pear-runtime` — Embeddable Runtime library for Pear with P2P OTA updates, Bare workers and storage APIs.
- `pear-desktop` — `pear://runtime`.
- `pear-electron` — Pear User-Interface Library for Electron.
- `pear-terminal` — Pear Terminal User Interface library.
- `pear-cli` — 🍐
- `pear-cmd` — Pear command parser & definitions.
- `pear-api` — Pear API Base & Integration Module.
- `pear-interface` — global.Pear API jsdoc type interface.
- `pear-info` — View Pear project information by link.
- `pear-link` — Pear url parser.
- `pear-bridge` — Local HTTP Bridge for Pear Desktop Applications.
- `pear-build` — Build appling for a Pear application.
- `pear-bundle` — Generate a bare-bundle from a Pear application entrypoint.
- `pear-pack` — Bundle and prebuild generation for Pear.
- `pear-stage` — Synchronize from-disk to app drive peer-to-peer.
- `pear-seed` — Seed or reseed a Pear project by link.
- `pear-dump` — Synchronize files from link to dir peer-to-peer or from-disk.
- `pear-shake` — Get the dependency tree of a Pear application bundle from a drive and its entrypoints.
- `pear-init` — Create initial Pear project files.
- `pear-prefetcher` — Platform prefetch runner.
- `pear-installer` — Used by Application Installers for Pear Applications.
- `pear-distributable-bootstrap` — Pear Application Distributable Bootstrapper.
- `pear-ipc` — IPC for Pear.
- `pear-ipc-client` — Helper to create a Pear IPC client.
- `pear-message` — Send object messages between a Pear application's processes/threads, pattern matching them with pear-messages.
- `pear-messages` — Receive object messages from a Pear application's processes/threads using object pattern-matching.
- `pear-opstream` — Pear operations stream base class.
- `pear-opwait` — Pear operation stream promise wrapper.
- `pear-state` — Pear state.
- `pear-rti` — Pear Core Runtime Information.
- `pear-constants` — Pear constants.
- `pear-errors` — Pear Core Error Types.
- `pear-release` — Set application production release version length.
- `pear-prerelease` — Prerelease helper.
- `pear-wakeups` — Pear platform and application update notifications.
- `pear-updates` — Pear platform and application update notifications.
- `pear-force-update` — Pear force update.
- `pear-restart` — Restart Pear application or platform.
- `pear-reset` — Reset an application to initial state.
- `pear-drop` — Drop data, including application reset.
- `pear-gracedown` — Pear graceful closer.
- `pear-crasher` — Pear uncaught crash handler.
- `pear-tryboot` — Pear sidecar tryboot for pear-ipc connect function.
- `pear-changelog` — Changelog parser and differ.
- `pear-md` — markdown rendering utility for pear.
- `pear-prefs` — Pear Preferences.
- `pear-user-dirs` — Get the path of user-specific directories.
- `pear-aliases` — `pear://<alias>` list.
- `pear-docs` — documentation hub.
- `pear-templates` — Templates for Pear.
- `pear-workshop` — 🍐
- `speedrun` — speedrun demo for pear react app with watch reload and production update flows.
- `hello-pear-electron` — Integrating Pear into a hello world electron desktop app.
- `pear-radio` — Pear Music Streamer.
- `pear-radio-backend` — Pear radio backend.
- `pear-ci` — Stateless stage for pear-runtime apps.
- `pear-ci-example` — how to stage on ci relatively safely.
- `pear-ci-multisig` — Specialized subset of pear multisig CLI for CI pipelines.
- `pear-multisig-link` — Deterministic multisig link per multisig inputs.

### 4) Hypercore data, storage, and drive tooling
Distributed logs, file systems, corestores, and drive-oriented workflows.

- `hypercore` — Hypercore is a secure, distributed append-only log.
- `hyperbee` — An append-only B-tree running on a Hypercore.
- `hyperdrive` — Hyperdrive is a secure, real time distributed file system.
- `hyperdrive-next` — Hyperdrive is a secure, real-time distributed file system.
- `hyperdb` — P2P first database.
- `corestore` — A simple corestore that wraps a random-access-storage module.
- `autobase` — Autobase lets you write concise multiwriter data structures with Hypercore.
- `autopass` — Multiwriter password and note sharing module.
- `hyperblobs` — A blob store for Hypercore.
- `hyperconf` — Always available, remotely updateable config.
- `hyper-multisig` — multisig hypercore and hyperdrive.
- `hypercore-storage` — RocksDB storage driver for Hypercore.
- `hypercore-sign` — Sign and verify Hypercores.
- `hypercore-proof-queue` — Store a bunch of Hypercore proofs to a file and consume them later.
- `hypercore-stats` — Stats for Hypercores, with Prometheus support.
- `core-coupler` — Couple the peers of cores.
- `key-collection` — Hyperdb-based collection of 32-byte keys.
- `multi-profile-store` — Manage multiple corestores easily in a multi profile setup.
- `drive-resolve` — Asynchronous require resolution in Hyperdrive.
- `watch-drive` — Watch a Hyperdrive or a Localdrive and get the diff.
- `serve-drive` — HTTP drive server for entries delivery.
- `localdrive` — File system API that is similar to Hyperdrive.
- `mirror-drive` — Mirror two drives.
- `drives` — CLI to download, seed, and mirror a Hyperdrive or Localdrive.
- `simple-seeder` — Dead simple seeder with zero bugs.
- `seedbee` — Bee for seeds.

### 5) Networking, DHT, RPC, and transport
Peer discovery, swarms, multiplexing, protocol bridges, and transport layers.

- `hyperdht` — The DHT powering Hyperswarm.
- `hyperswarm` — A distributed networking stack for connecting peers.
- `hyperswarm-secret-stream` — Secret stream backed by Noise and libsodium's secretstream.
- `hyperswarm-dht-relay` — Relaying the Hyperswarm DHT over other transport protocols to bring decentralized networking to everyone.
- `hyperswarm-testnet` — Small module to help you spin up a local Hyperswarm testnet.
- `hyperswarm-stats` — Stats for Hyperswarm and the connections it swarms, with Prometheus support.
- `hyperdht-stats` — HyperDHT stats, with Prometheus support.
- `instrumented-dht-node` — A DHT node exposing Prometheus metrics.
- `dht-rpc` — Make RPC calls over a Kademlia based DHT.
- `rpc` — RPC over the Hyperswarm DHT.
- `protomux` — Multiplex multiple message oriented protocols over a stream.
- `protomux-rpc` — RPC over Protomux channels.
- `protomux-rpc-client` — Connect to protomux-rpc servers.
- `protomux-rpc-client-pool` — Reliably connect to one of a pool of protomux-rpc servers.
- `protomux-wakeup` — Wakeup protocol over protomux.
- `jsonrpc-mux` — Mux JSON-RPC 2.0.
- `hrpc` — Append only API definition and code generation.
- `bare-rpc` — https://github.com/holepunchto/librpc ABI compatible RPC for Bare.
- `bare-rpc-swift` — https://github.com/holepunchto/librpc ABI compatible RPC for Swift.
- `bare-net` — TCP and IPC servers and clients for JavaScript.
- `bare-tcp` — Native TCP sockets for JavaScript.
- `bare-dgram` — Native UDP for JavaScript.
- `bare-tls` — Transport Layer Security (TLS) streams for JavaScript.
- `bare-http-parser` — Streaming HTTP request and response parser for Bare.
- `bare-ws` — WebSocket library for JavaScript.
- `bare-dns` — Domain name resolution for JavaScript.
- `http-forward-host` — Simple stream proxy that sniffs the HTTP host or x-forwarded-for header and allows you to to forward the stream based on that.
- `netpaste` — Copy and paste over the DHT.
- `repl-swarm` — Attach to a node repl using Hyperswarm.
- `mininet` — Spin up and interact with virtual networks using Mininet and Node.js.
- `hypermininet` — Mininet, the easy way.
- `git-remote-punch-transport` — Git remote helper for Hyperswarm transport.

### 6) Blind networking & Keet-specific flows
Blind peer discovery, pairing, relays, and Keet application identity flows.

- `blind-peer` — Peer that is blind.
- `blind-peer-cli` — CLI for running a blind peer.
- `blind-peer-encodings` — Blind Peer encodings.
- `blind-peer-muxer` — Protomux channel muxer for blind peers.
- `blind-peering` — Peer side mirror manager.
- `blind-peering-cli` — CLI for blind-peering.
- `blind-relay` — Blind relay for UDX over Protomux channels.
- `blind-relay-service` — CLI for running blind relays.
- `blind-pairing` — Blind pairing using HyperDHT.
- `blind-pairing-core` — Core module for managing for Keet pairing requests.
- `blind-encryption-sodium` — Implemention of encryption encoding for Autobase blind encryption using sodium easy box.
- `keypear` — keychain that derives deterministic Ed25519 keypairs and attestations.
- `keet-identity-key` — Hierarchical deterministic key pairs for use in Keet identity system.
- `keet-appling` — Keet application shell for macOS, Linux, and Windows.
- `keet-appling-next` — Keet application shell.
- `keet-prefs` — Keet Preferences.
- `keet-mobile-releases` — Keet mobile releases.
- `pear-multisig-link` — Deterministic multisig link per multisig inputs.

### 7) Native libraries and bindings
Reusable C/C++/Swift/Go/Rust building blocks, ABI layers, and native wrappers.

- `libjs` — Simple and ABI stable C bindings to V8 built on libuv.
- `libqjs` — ABI compatible replacement for `libjs` built on QuickJS.
- `libjsc` — ABI compatible replacement for `libjs` built on JavaScriptCore.
- `libjerry` — ABI compatible replacement for `libjs` built on JerryScript.
- `libmqjs` — ABI compatible replacement for `libjs` built on Micro QuickJS.
- `libnapi` — Node-API compatibility layer for `libjs`.
- `libjsi` — React Native JavaScript Interface implemented on top of `libjs`.
- `libjstl` — C++ template library for `libjs`.
- `libjnitl` — C++ template library for the Java Native Interface (JNI).
- `libpear` — Native utilities for Pear applications.
- `libappling` — Low-level plumbing for Pear application shells.
- `libpearsync` — Simple message passing between a libuv thread and something else.
- `libdynload` — Utilities for loading of versioned dynamic libraries.
- `libmem` — General purpose memory allocator for C built on mimalloc.
- `liblog` — Simple logging library.
- `libdaemon` — Simple daemon spawning and management.
- `librlimit` — Small library for managing process-wide resource limits.
- `libjson` — Small and memory efficient library for working with JSON in C.
- `libpath` — Low-level filesystem path manipulation library.
- `libutf` — Small library for working with Unicode in C.
- `liburl` — WHATWG URL parser in C.
- `libbase64` — Encoder and decoder for base64 in C.
- `libhex` — Encoder and decoder for hex in C.
- `libz32` — Encoder and decoder for z-base-32 in C.
- `libcrc` — Cross-platform implementation of CRC32 with hardware acceleration.
- `libprng` — Pseudorandom number generators for C based on https://prng.di.unimi.it.
- `libquickbit` — The fastest bit in the West; a library for working with bit fields.
- `libsimdle` — Simple and portable SIMD instructions for 128 bit vectors, inspired by the WASM SIMD specification.
- `libbitarray` — Compact and SIMD accelerated bit array data structure in C.
- `libcompact` — Compact encoding schemes for C with the same ABI as `compact-encoding`.
- `libintrusive` — Allocation-free intrusive data structures for C.
- `libparseline` — Parse streaming lines in C.
- `libtls` — Minimal TLS library for C, based on BoringSSL.
- `librabin` — Rabin fingerprinting for C based on rabin-cdc.
- `librpc` — Low-level RPC codec implemented in C for wide language support.
- `librocksdb` — Asynchronous C bindings to RocksDB with support for batch operations.
- `libfs` — A simple but extensive file system library built on libuv.
- `libfx` — Low-level, cross-platform GUI library for native desktop and mobile.
- `libtt` — Virtual console extensions built on libuv.
- `quickbit-native` — JavaScript bindings for `libquickbit`.
- `bitarray-native` — JavaScript bindings for `libbitarray`.
- `simdle-native` — JavaScript bindings for `libsimdle`.
- `crc-native` — JavaScript bindings for `libcrc`.
- `rabin-native` — JavaScript bindings for `librabin`.
- `sqlite3-native` — Asynchronous SQLite3 bindings for JavaScript with VFS support.
- `rocksdb-native` — JavaScript bindings for `librocksdb`.
- `udx-native` — udx is reliable, multiplexed, and congestion-controlled streams over udp.
- `fx-native` — JavaScript bindings for `libfx`.
- `tt-native` — JavaScript bindings for `libtt`.
- `bare-compat-napi` — Bare compatibility headers for Node-API.
- `bare-v8` — V8 utilities for Bare.
- `bare-v8-to-istanbul` — coverage support for Bare V8 output.
- `bare-addon-rust` — Template repository for creating Bare native addons using `bare-rust`.
- `bare-addon-java` — Template repository for creating Bare native addons using Java via `libjnitl`.
- `bare-addon-jstl` — Template repository for creating Bare native addons using C++ via `libjstl`.
- `bare-addon-resolve` — Low-level addon resolution algorithm for Bare.
- `bare-bluetooth-apple` — CoreBluetooth bindings for Bare.
- `bare-bluetooth-android` — Android Bluetooth bindings for Bare.
- `bare-web-kit` — WebKit bindings for Bare.
- `bare-web-kit-gtk` — WebKitGTK bindings for Bare.
- `bare-ui-kit` — UIKit bindings and runtime for Bare.
- `bare-win-ui` — WinUI bindings and runtime for Bare.
- `bare-gtk` — GTK bindings and runtime for Bare.
- `bare-sdl` — SDL bindings for Bare.
- `bare-bmp` — Native BMP codec for Bare.
- `bare-png` — PNG support for Bare.
- `bare-jpeg` — JPEG support for Bare.
- `bare-heif` — HEIF support for Bare.
- `bare-webp` — WebP support for Bare.
- `bare-svg` — SVG support for Bare.
- `bare-ico` — ICO support for Bare.
- `bare-tiff` — TIFF support for Bare.
- `bare-exif` — EXIF support for Bare.
- `bare-image-resample` — Image resampling support for Bare.
- `bare-ffmpeg` — Low-level FFmpeg bindings for Bare.
- `bare-md4c` — Fast markdown push parser.
- `bare-zlib` — Stream-based zlib bindings for JavaScript.
- `bare-media` — A set of media APIs for Bare.
- `bare-mime` — MIME type parsing for Bare.
- `bare-punycode` — Punycode support for Bare.
- `bare-delta` — Binary patch handling for Bare.
- `bare-walk-handles` — Walk the event loop handles of the Bare process.
- `thread-stats` — Get resource usage for individual threads in the current process.

### 8) Build, CI, packaging, and release automation
Cross-platform build helpers, packaging recipes, release tooling, and repo operations.

- `actions` — Shared GitHub actions.
- `canary-runner` — Run all tests of a list of repositories.
- `slack-build-status` — GitHub Actions for posting and updating build status messages in Slack.
- `oidc-publishing` — OIDC publishing tools for GitHub and npm.
- `oidc-publishing-sandbox` — Sandbox for testing OIDC publishing.
- `prettier-config-holepunch` — The Prettier shared configuration used by Holepunch.
- `bare-prebuild` — Tool for recursively prebuilding installed native addons from source.
- `prebuild-containers` — Containers for prebuilding native Node.js modules.
- `chromium-prebuilds` — Build definitions for making prebuilds of Chromium modules.
- `musl-toolchains` — Prebuilt musl cross-compilation toolchains.
- `ninja-runtime` — Prebuilt Ninja binaries for macOS, Linux, and Windows.
- `cmake-bare` — Bare utilities for CMake.
- `cmake-drive` — Drive utilities for CMake.
- `cmake-pear` — Pear utilities for CMake.
- `cmake-runtime` — Prebuilt CMake binaries for macOS, Linux, and Windows.
- `cmake-toolchains` — Clang-based CMake toolchain definitions for easy cross compilation.
- `cmake-vcpkg` — Opinionated vcpkg integration for CMake.
- `cmake-android` — Android utilities for CMake.
- `cmake-ios` — iOS utilities for CMake.
- `cmake-java` — Java utilities for CMake.
- `cmake-macos` — macOS utilities for CMake.
- `cmake-meson` — Meson bridge for CMake.
- `cmake-msix` — MSIX packaging utilities for CMake.
- `cmake-napi` — Node-API utilities for CMake.
- `cmake-npm` — npm utilities for CMake.
- `cmake-windows` — Windows utilities for CMake.
- `cmake-zig` — Zig bridge for CMake.
- `cmake-harden` — Compiler options hardening for CMake based on the OpenSSF guidelines.
- `cmake-cargo` — Cargo bridge for CMake.
- `cmake-gn` — Bridging CMake and GN.
- `cmake-fetch` — Minimal package manager for CMake based on FetchContent.
- `cmake-ports` — Simple build recipe manager for CMake based on ExternalProject.
- `cmake-app-image` — AppImage packaging utilities for CMake.
- `bare-make` — Opinionated build system generator based on CMake.
- `bare-build` — Application builder for Bare.
- `bare-bundle` — Application bundle format for JavaScript.
- `bare-bundle-compile` — Compile a bundle of CommonJS modules to a single module.
- `bare-bundle-evaluate` — Evaluate a bundle of CommonJS modules across JavaScript runtimes.
- `bare-bundle-id` — Construct a unique ID for a bundle.
- `bare-pack` — Bundle packing for Bare.
- `bare-pack-drive` — Pack drives to Bare bundles.
- `bare-unpack` — Bundle unpacking for Bare.
- `bare-sidecar-bundle` — Bare bundler optimised for sidecars to be used in pear-runtime.
- `bare-distributable` — Template repository for creating custom Bare distributables.
- `bare-app-image` — AppImage packaging tools for Bare.
- `bare-apk` — APK packaging tools for Bare.
- `bundlebee` — Bundles powered by Bees.
- `bundlebee-cli` — Manage, push, sign and seed your Bundles with Bees!
- `make-pear-app` — Action for making Pear apps.
- `electron-runtime` — Build the runtime app.
- `pear-ci` — Stateless stage for pear-runtime apps.
- `pear-ci-example` — how to stage on ci relatively safely.
- `pear-ci-multisig` — Specialized subset of pear multisig CLI for CI pipelines.

### 9) Examples, workshops, and demos
Proof-of-concept apps, teaching repos, and end-to-end examples.

- `examples` — Examples of basic flows for modules in the Holepunch ecosystem.
- `bare-snippets` — Examples of how Bare makes running Javascript everywhere easy.
- `pear-workshop` — 🍐
- `planb-summer-school` — the workshop stuff.
- `autobase-example` — Just a runnable E2E autobase example.
- `autobase-test-helpers` — Helpers when writing tests for an Autobased application.
- `autobase-light-writer` — Detached autobase writer that is just a single core with no causal info.
- `hyperdb-workshop` — Workshop explaining basic hyperdb usage.
- `hyperdb-autobase-workshop` — Using hyperdb with autobase for multiple writers.
- `hyperdb-benchmarking` — Benchmarking HyperDB on Rocks.
- `filesharing-app-example` — file-sharing app example.
- `filesharing-react-app-example` — React file-sharing app example.
- `hello-pear-electron` — Integrating Pear into a hello world electron desktop app.
- `pear-radio` — Pear Music Streamer.
- `pear-radio-backend` — Pear radio backend.
- `pearpass-example` — Pear password-sharing example.
- `autopass-mobile-example` — Mobile example for Autopass.
- `bare-android` — Example of embedding Bare in an Android application using `bare-kit`.
- `bare-ios` — Example of embedding Bare in an iOS application using `bare-kit`.
- `bare-expo` — Example of embedding Bare in an Expo application using `react-native-bare-kit`.
- `bare-expo-hrpc-demo` — Bare Expo HRPC demo.
- `expo-bare-kit` — `bare-kit` for Expo.
- `expo-file-stream` — Stream file to Readable with no temp files.
- `hyperclip-ios` — Hyperclip iOS app.
- `hyperclip-android` — Hyperclip Android app.
- `hyperclip-desktop` — Pear desktop app to go with Hyperclip iOS and Android.
- `snake` — Multiplayer P2P Snake Game on Pear.
- `cellery` — Experimental rendering for all platforms.
- `cellery-html` — Cellery HTML demo.
- `drives` — CLI to download, seed, and mirror a Hyperdrive or Localdrive.
- `drive-analyzer` — Static analysis of a Pear app bundle.
- `watch-drive` — Watch a Hyperdrive or a Localdrive and get the diff.
- `serve-drive` — HTTP drive server for entries delivery.
- `simple-seeder` — Dead simple seeder with zero bugs.
- `seedbee` — Bee for seeds.
- `repl-swarm` — Attach to a node repl using Hyperswarm.
- `lunte` — Lunte demo.

### 10) Utilities, observability, and security helpers
Small focused packages for scheduling, parsing, crypto, debugging, and metrics.

- `activity-queue` — Easily track activity and when that activity flushes.
- `adaptive-timeout` — Weighted moving average cache with fallbacks.
- `delay-pacer` — High precision delay based pacer.
- `bucket-rate-limit` — A lightweight, bucket-based rate limiter for JavaScript that controls request frequency with minimal overhead.
- `db-lock` — Simple concurrent lock for DB patterns.
- `scope-lock` — Some concurrency semantics around entering scopes.
- `ready-guard` — Simple signal to do composite resource lifecycles.
- `ready-resource` — Modern single resource management.
- `refcounter` — Simple refcounter.
- `suspendify` — Suspend/resume state machine with linger support.
- `suspend-resource` — Ready resource with suspend/resume.
- `task-backoff` — Small module to do smart delays in tight loops to maintain a certain event loop delay.
- `listen-async` — Easily listen on a http/net server async.
- `minicron` — Simple utility for scheduling functions at fixed intervals.
- `uncaughts` — Cleanly register uncaughtException and unhandledRejection handlers.
- `slab-hunter` — Hunt for Buffer slabs indicative of a memory leak.
- `fd-lock` — Stateful file descriptor locks for JavaScript.
- `fs-native-lock` — Cross platform lock file.
- `fifofile` — Userland FIFO file.
- `fd-pipe` — Enviornment based file descriptor Pipe (bare/node).
- `fast-meta-tags` — Get the meta tags and title from an url.
- `get-file-format` — Detect the format of a file by looking at its magic number.
- `get-mime-type` — simple extension to mimetype.
- `is-text-filetype` — Determines whether a file specifier is plain text using heuristics based on extensions, common filenames, and dotfiles.
- `known-text-files` — Combined list of plain text file extensions, common extensionless files and dotfiles.
- `unicode-to-plain-text` — Convert fancy Unicode text to plain ASCII with smart language preservation.
- `url-file-url` — Small module that converts from URLs to filenames to URLs.
- `text-decoder` — Streaming text decoder that preserves multibyte Unicode characters.
- `same-object` — Determine if two objects are deeply equal.
- `nanodebug` — A tiny, zero overhead debugging utility.
- `bits-to-bytes` — Functions for doing bit manipulation of typed arrays.
- `unslab` — Unslab some slab'ed buffers.
- `tiny-buffer-map` — A very simple Map for Buffers and Uint8Arrays.
- `tiny-buffer-rpc` — Lightweight binary bi-directional RPC.
- `tiny-fs-native` — Native fs for Javascript.
- `tiny-http-native` — Tiny HTTP library made purely on libuv and napi.
- `tiny-paths` — path for platforms without path.
- `tiny-timers-native` — Native timers for Javascript.
- `framed-stream` — Read/write stream messages prefixed 8, 16, 24 or 32 bit length.
- `events-universal` — Universal wrapper for the Node.js events module.
- `sodium-hmac` — HMAC utility.
- `pw-to-ek` — Derive a secure encryption key from a password using the sodium's scrypt implementation.
- `deterministic-sealed-box` — Deterministically create sealed boxes.
- `broadcast-encryption` — Distribute encryption keys to a dynamic set of receivers.
- `obfuscate-data` — Reversibly obfuscate data with a secret key.
- `noise-curve-ed` — Ed25519 elliptic curve operations for `noise-handshake`.
- `noise-handshake` — Simple noise handshake, supporting generic handshake patterns.
- `secure-key` — Password protected ed25519 key pairs.
- `secure-prompt` — Securely prompt stdio using secure buffers.
- `brittle` — Brittle TAP test framework.
- `brittle-snapshot` — Traditional snapshots for brittle.
- `bare-tap` — Minimal TAP library for Bare.
- `test-suspend` — Utilities for testing process suspension.
- `hypertrace` — Add tracing and insights to classes in modules.
- `hypertrace-prometheus` — Add support for Prometheus/Grafana to hypertrace.
- `hypermetrics` — Prometheus metrics for Holepunch modules.
- `hyper-instrument` — Instrument services within the hypercore ecosystem.
- `hyper-health-check` — Check the health of hypercores and export as prometheus metrics.
- `hyperdht-stats` — HyperDHT stats, with Prometheus support.
- `hypercore-stats` — Stats for Hypercores, with Prometheus support.
- `Grafana-hypercore-stats` — Grafana dashboard for Hypercore, Hyperswarm, Hyperdht and UDX stats exported over Prometheus.
- `prom-client` — Prometheus client for node.js.
- `safe-sodium-buffer` — Safe sodium buffer helpers.
- `check-npm-maintainers` — Maintainership validation helper.
- `repo-template` — Repository template.

## Notes

- Some repositories may fit more than one group; the taxonomy uses the most likely primary use case.
- Private repositories are not included in GitHub’s public org search results.
- Archived repos may still appear in search and are retained here if relevant to the taxonomy.
- This file is an inferred map for architectural scanning, not a canonical org inventory.
- The index is intentionally taxonomy-first, so some categories list representative repos rather than every repository name individually.
