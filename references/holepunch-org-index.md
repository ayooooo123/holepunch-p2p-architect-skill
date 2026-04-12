# Holepunch Organization Repository Index

Generated at: 2026-04-12

Source organization: `holepunchto`

## Scope

- This is a **filtered, high-signal regrouping** of the public repositories in the `holepunchto` GitHub organization.
- It is **not an exhaustive dump** of all 587 public repositories.
- The list prioritizes repositories that are most significant, active, starred, or representative of each use case so the index stays readable and useful for regrouping.
- Each entry includes the repository name, description, and primary language.

## Bare (Runtime/Dev/Tooling)

- **bare** — Small and modular JavaScript runtime for desktop and mobile. *(C)*
- **bare-runtime** — Prebuilt Bare binaries for macOS, iOS, Linux, Android, and Windows. *(JavaScript)*
- **bare-kit** — Bare for native application development. *(C)*
- **bare-native** — Native application development framework for Bare. *(JavaScript)*
- **bare-build** — Application builder for Bare. *(JavaScript)*
- **bare-pack** — Bundle packing for Bare. *(JavaScript)*
- **bare-run** — Cross-platform script runner for Bare. *(JavaScript)*
- **bare-node** — Compatibility modules for Node.js builtins in Bare. *(JavaScript)*
- **bare-node-runtime** — Compatibility layer for Node.js builtins and globals in Bare. *(JavaScript)*
- **bare-process** — Node.js-compatible process control for Bare. *(JavaScript)*
- **bare-worker** — Higher-level worker threads for JavaScript. *(JavaScript)*
- **bare-prebuild** — Tool for recursively prebuilding installed native addons from source. *(JavaScript)*
- **bare-distributable** — Template repository for creating custom Bare distributables. *(C)*
- **bare-bundle** — Application bundle format for JavaScript, inspired by `asar`. *(JavaScript)*
- **bare-module** — Module support for JavaScript. *(JavaScript)*
- **bare-repl** — Read-Evaluate-Print-Loop environment for JavaScript. *(JavaScript)*
- **bare-inspector** — V8 inspector support for Bare. *(JavaScript)*
- **bare-console** — WHATWG debugging console for JavaScript. *(JavaScript)*
- **bare-assert** — Assertion library for JavaScript. *(JavaScript)*
- **bare-utils** — Node.js-compatible utility functions for Bare. *(JavaScript)*

## P2P (Hypercore, Hyperswarm, Dht, Corelibs)

- **hypercore** — Hypercore is a secure, distributed append-only log. *(JavaScript)*
- **hyperdrive** — Hyperdrive is a secure, real time distributed file system. *(JavaScript)*
- **hyperbee** — An append-only B-tree running on a Hypercore. *(JavaScript)*
- **hyperdb** — P2P first database. *(JavaScript)*
- **hyperdht** — The DHT powering Hyperswarm. *(JavaScript)*
- **hyperswarm** — A distributed networking stack for connecting peers. *(JavaScript)*
- **autobase** — Autobase lets you write concise multiwriter data structures with Hypercore. *(JavaScript)*
- **corestore** — A simple corestore that wraps a random-access-storage module. *(JavaScript)*
- **hyperblobs** — A blob store for Hypercore. *(JavaScript)*
- **hypercore-crypto** — The crypto primitives used in hypercore, extracted into a separate module. *(JavaScript)*
- **hypercore-storage** — RocksDB storage driver for Hypercore. *(JavaScript)*
- **hypercore-sign** — Sign and verify Hypercores. *(JavaScript)*
- **hypercore-signing-request** — Generate shareable signing requests for Hypercore. *(JavaScript)*
- **hypercore-id-encoding** — Convert Hypercore keys to/from z-base32 or hex. *(JavaScript)*
- **hypercore-stats** — Stats for Hypercores, with Prometheus support. *(JavaScript)*
- **hyperswarm-secret-stream** — Secret stream backed by Noise and libsodium's secretstream. *(JavaScript)*
- **hyperswarm-doctor** — Debugging tool for the swarm. *(JavaScript)*
- **hyperswarm-testnet** — Small module to help you spin up a local Hyperswarm testnet. *(JavaScript)*
- **hyperswarm-stats** — Stats for Hyperswarm and the connections it swarms, with Prometheus support. *(JavaScript)*
- **hyperswarm-seeders** — A seeders only swarm. *(JavaScript)*
- **hyperswarm-dht-relay** — Relaying the Hyperswarm DHT over other transport protocols to bring decentralized networking to everyone. *(JavaScript)*
- **hyperbeam** — A 1-1 end-to-end encrypted internet pipe powered by Hyperswarm. *(JavaScript)*
- **hyperssh** — Run SSH over hyperswarm! *(JavaScript)*
- **dht-rpc** — Make RPC calls over a Kademlia based DHT. *(JavaScript)*
- **core-coupler** — Couple the peers of cores. *(JavaScript)*
- **corestore-snapshot** — Make a corestore snapshot for ci. *(JavaScript)*
- **key-collection** — Hyperdb-based collection of 32-byte keys. *(JavaScript)*

## Networking/Protocols (Udp, Tcp, Muxers, QUIC)

- **protomux** — Multiplex multiple message oriented protocols over a stream. *(JavaScript)*
- **protomux-rpc** — RPC over Protomux channels. *(JavaScript)*
- **protomux-rpc-client** — Connect to protmux-rpc servers. *(JavaScript)*
- **protomux-rpc-client-pool** — Reliably connect to one of a pool of protomux-rpc servers. *(JavaScript)*
- **protomux-wakeup** — Wakeup protocol over protomux. *(JavaScript)*
- **protomux-rpc-middleware** — No description set. *(JavaScript)*
- **protomux-rpc-router** — No description set. *(JavaScript)*
- **rpc** — RPC over the Hyperswarm DHT. *(JavaScript)*
- **tiny-buffer-rpc** — Lightweight binary bi-directional RPC. *(JavaScript)*
- **libudx** — udx is reliable, multiplexed, and congestion-controlled streams over udp. *(C)*
- **udx-native** — udx is reliable, multiplexed, and congestion-controlled streams over udp. *(JavaScript)*
- **bare-dgram** — Native UDP for JavaScript. *(JavaScript)*
- **bare-tcp** — Native TCP sockets for JavaScript. *(JavaScript)*
- **bare-net** — TCP and IPC servers and clients for JavaScript. *(JavaScript)*
- **bare-http1** — HTTP/1 library for JavaScript. *(JavaScript)*
- **bare-https** — HTTPS library for JavaScript. *(JavaScript)*
- **bare-ws** — WebSocket library for JavaScript. *(JavaScript)*
- **bare-tls** — Transport Layer Security (TLS) streams for JavaScript. *(JavaScript)*
- **bare-ipc** — Lightweight pipe-based IPC for Bare. *(JavaScript)*
- **bare-dns** — Domain name resolution for JavaScript. *(C)*
- **network-block-device** — Network block device server for JavaScript. *(JavaScript)*
- **http-forward-host** — Simple stream proxy that sniffs the HTTP host or x-forwarded-for header and allows you to forward the stream based on that. *(JavaScript)*
- **framed-stream** — Read/write stream messages prefixed 8, 16, 24 or 32 bit length. *(JavaScript)*
- **blind-relay** — Blind relay for UDX over Protomux channels. *(JavaScript)*
- **blind-peer-muxer** — Protomux channel muxer for blind peers. *(JavaScript)*
- **blind-pairing** — Blind pairing using HyperDHT. *(JavaScript)*
- **blind-pairing-core** — Core module for managing for Keet pairing requests. *(JavaScript)*
- **blind-peering** — Peer side mirror manager. *(JavaScript)*

## Pear/Keet/Desktop Apps (Pear, Keet, Desktop runtime)

- **pear** — Combined Peer-to-Peer (P2P) Runtime, Development & Deployment tool. *(JavaScript)*
- **pear-runtime** — Embeddable Runtime library for Pear with P2P OTA updates, Bare workers and storage APIs. *(JavaScript)*
- **pear-runtime-bare** — Bare binary that bootstraps the platform. *(C)*
- **pear-runtime-updater** — Listens for OTA Pear App updates. *(JavaScript)*
- **pear-desktop** — `pear://runtime`. *(JavaScript)*
- **pear-cli** — 🍐. *(JavaScript)*
- **pear-build** — Build appling for a Pear application. *(JavaScript)*
- **pear-pack** — Bundle and prebuild generation for Pear. *(JavaScript)*
- **pear-bundle** — Generate a bare-bundle from a Pear application entrypoint. *(JavaScript)*
- **pear-run** — Run Pear app from app p2p with `pear://` link. *(JavaScript)*
- **pear-stage** — Synchronize from-disk to app drive peer-to-peer. *(JavaScript)*
- **pear-seed** — Seed or reseed a Pear project by link. *(JavaScript)*
- **pear-dump** — Synchronize files from link to dir peer-to-peer or from-disk. *(JavaScript)*
- **pear-api** — Pear API Base & Integration Module. *(JavaScript)*
- **pear-ipc** — IPC for Pear. *(JavaScript)*
- **pear-message** — Send object messages between a Pear application's processes/threads, pattern matching them with pear-messages. *(JavaScript)*
- **pear-messages** — Receive object messages from a Pear application's processes/threads using object pattern-matching. *(JavaScript)*
- **pear-terminal** — Pear Terminal User Interface library. *(JavaScript)*
- **pear-electron** — Pear User-Interface Library for Electron. *(JavaScript)*
- **keet-appling** — Keet application shell for macOS, Linux, and Windows. *(CMake)*
- **keet-appling-next** — Keet application shell. *(JavaScript)*
- **keet-identity-key** — Hierarchical deterministic key pairs for use in Keet identity system. *(JavaScript)*
- **keet-prefs** — Keet Preferences. *(JavaScript)*
- **pear-updater** — Pear Updater. *(JavaScript)*

## Native Libs/Build (C/C++, CMake, Build tools)

- **libjs** — Simple and ABI stable C bindings to V8 built on libuv. *(C)*
- **libqjs** — ABI compatible replacement for `libjs` built on QuickJS. *(C)*
- **libjsc** — ABI compatible replacement for `libjs` built on JavaScriptCore. *(C)*
- **libjerry** — ABI compatible replacement for `libjs` built on JerryScript. *(C)*
- **libmqjs** — ABI compatible replacement for `libjs` built on Micro QuickJS. *(C)*
- **libnapi** — Node-API compatibility layer for `libjs`. *(C)*
- **libjstl** — C++ template library for `libjs`. *(C++)*
- **libjnitl** — C++ template library for the Java Native Interface (JNI). *(C++)*
- **libjsi** — React Native JavaScript Interface (JSI) implemented on top of `libjs`. *(C++)*
- **libfx** — Low-level, cross-platform GUI library for native desktop and mobile. *(C)*
- **libappling** — Low-level plumbing for Pear application shells. *(C)*
- **libpear** — Native utilities for Pear applications. *(C)*
- **libudx** — udx is reliable, multiplexed, and congestion-controlled streams over udp. *(C)*
- **librocksdb** — Asynchronous C bindings to RocksDB with support for batch operations. *(C++)*
- **libfs** — A simple but extensive file system library built on libuv. *(C)*
- **liburl** — WHATWG URL parser in C. *(C)*
- **libhex** — Encoder and decoder for hex in C. *(C)*
- **libz32** — Encoder and decoder for z-base-32 in C. *(C)*
- **libbase64** — Encoder and decoder for base64 in C. *(C)*
- **libcompact** — Compact encoding schemes for C with the same ABI as `compact-encoding`. *(C)*
- **libpath** — Low-level filesystem path manipulation library. *(C)*
- **libprng** — Pseudorandom number generators for C based on https://prng.di.unimi.it. *(C)*
- **libbitarray** — Compact and SIMD accelerated bit array data structure in C. *(C)*
- **libcrc** — Cross-platform implementation of CRC32 with hardware acceleration. *(C)*
- **libtls** — Minimal TLS library for C, based on BoringSSL. *(C)*
- **liblog** — Simple logging library with a unified interface to os_log, syslog, Logcat, and TraceLogging. *(C++)*
- **libmem** — General purpose memory allocator for C built on `mimalloc`. *(C)*
- **libutf** — Small library for working with Unicode in C. *(C)*
- **librlimit** — Small library for managing process-wide resource limits. *(C)*
- **libdaemon** — Simple daemon spawning and management. *(C)*
- **libtt** — Virtual console extensions built on libuv. *(C)*
- **libpearsync** — Simple message passing between a libuv thread and something else. *(C)*
- **librpc** — Low-level RPC codec implemented in C for wide language support. *(C)*
- **libsimdle** — Simple and portable SIMD instructions for 128 bit vectors, inspired by the WASM SIMD specification. *(C)*
- **libquickbit** — The fastest bit in the West; a library for working with bit fields, accelerated using SIMD on supported hardware. *(C)*
- **librabin** — Rabin fingerprinting for C based on `fd0/rabin-cdc`. *(C)*
- **libjson** — Small and memory efficient library for working with JSON in C. *(C)*
- **libsingleset** — Header only fast set implementation for objects that are only in a single set. *(C)*
- **libintrusive** — Allocation-free intrusive data structures for C. *(C)*
- **libparseline** — Parse streaming lines in C. *(C)*
- **cmake-bare** — Bare utilities for CMake. *(CMake)*
- **cmake-pear** — Pear utilities for CMake. *(CMake)*
- **cmake-runtime** — Prebuilt CMake binaries for macOS, Linux, and Windows. *(JavaScript)*
- **cmake-toolchains** — Clang-based CMake toolchain definitions for easy cross compilation. *(CMake)*
- **cmake-fetch** — Minimal package manager for CMake based on FetchContent. *(CMake)*
- **cmake-vcpkg** — Opinionated vcpkg integration for CMake. *(CMake)*
- **prebuild-containers** — Containers for prebuilding native Node.js modules. *(Dockerfile)*
- **musl-toolchains** — Prebuilt musl cross-compilation toolchains. *(Not specified)*
- **chromium-prebuilds** — Build definitions for making prebuilds of Chromium modules. *(Python)*

## Examples/Documentation/Tests (Demos, Guides, Test suites)

- **examples** — Examples of basic flows for modules in the Holepunch ecosystem. *(JavaScript)*
- **bare-snippets** — Examples of how Bare makes running Javascript everywhere easy. *(JavaScript)*
- **bare-ios** — Example of embedding Bare in an iOS application using `bare-kit`. *(Swift)*
- **bare-android** — Example of embedding Bare in an Android application using `bare-kit`. *(Kotlin)*
- **bare-expo** — Example of embedding Bare in an Expo application using `react-native-bare-kit`. *(TypeScript)*
- **hello-pear-electron** — Integrating Pear into a hello world electron desktop app. *(JavaScript)*
- **filesharing-app-example** — No description set. *(JavaScript)*
- **filesharing-react-app-example** — No description set. *(JavaScript)*
- **pear-workshop** — 🍐. *(JavaScript)*
- **pear-docs** — No description set. *(Language not specified)*
- **pear-templates** — Templates for Pear - `pear init pear://templates/<name>`. *(JavaScript)*
- **hyperdb-workshop** — Workshop explaining basic hyperdb usage. *(JavaScript)*
- **hyperdb-autobase-workshop** — Using hyperdb with autobase for multiple writers. *(JavaScript)*
- **hypercore-e2e-tests** — End-to-end tests for Hypercore replication. *(JavaScript)*
- **hyperswarm-e2e-tests** — Hyperdht end-to-end tests. *(JavaScript)*
- **hypercore-scale-tests** — No description set. *(JavaScript)*
- **hyperdrive-swarm-test** — No description set. *(JavaScript)*
- **brittle** — Brittle TAP test framework. *(JavaScript)*
- **brittle-snapshot** — Traditional snapshots for brittle. *(JavaScript)*
- **canary-runner** — Run all tests of a list of repositories. *(JavaScript)*
- **test-suspend** — Utilities for testing process suspension. *(JavaScript)*
- **planb-summer-school** — the workshop stuff. *(JavaScript)*
- **speedrun** — speedrun demo for pear react app with watch reload and production update flows. *(JavaScript)*
- **snake** — Multiplayer P2P Snake Game on Pear. *(JavaScript)*
- **pear-ci-example** — how to stage on ci relatively safely. *(JavaScript)*
- **pear-ci-multisig** — Specialized subset of pear multisig CLI for CI pipelines. *(JavaScript)*
- **bare-expo-hrpc-demo** — No description set. *(JavaScript)*

## Archived public repos

These are public repos in `holepunchto` that are archived and were not included in the main grouped index above.

- **prom-client** — Prometheus client for node.js. *(Language not specified)*
- **bare-dev** — Development tooling for Bare. *(JavaScript)*
- **pear-expo-hello-world** — No description set. *(C++)*
- **pear-stdio** — Pear STDIO. *(JavaScript)*
- **barely-node** — Bare distribution aiming to be mostly Node.js compatible. *(CMake)*
