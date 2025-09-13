<!-- markdownlint-disable MD024 -->

# Changelog

## 0.1.0 - 2024-08-18

### New

* Core functionality
* CLI: click
* Test: pytest + tox
* Example configs

## 0.1.1 - 2024-08-21

### New

* Nix + Home Manager Support
* Coverage + Code Quality
* Module entry

### Changes

* Optional Dependency: ruff
* Dynamic elements in readme

## 0.2.0 - 2024-09-14

### New

* Include ruff errors/warning at the bottom

### Changes

* Uses json output format instead of concise

### Fixes

* Compatibility issues with older ruff versions #4

## 0.2.1 - 2025-09-13

### New

* pre-commit typos

### Changes

* Click targets are now Path objects
* Change `shell.nix` to use `devenv.nix`

### Fixes

* Removed coverage reporter in local tox tests
