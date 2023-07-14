# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.1/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.7] - 2023-07-14

### Fixed

- Process after `git flow finish` :
  - Push **develop** branch's commits
  - \+ Instructions to execute ONLY on *hotfixes* and *releases*
  - Push **master** branch's commits
  - Rebase the **master** branch to the **develop** branch
  - Push **master** branch's commits
  - Push tags

## [0.1.6] - 2023-07-14

### Fixed

- Process after `git flow finish` :
  - Push **develop** branch's commits
  - Push **master** branch's commits
  - Rebase the **master** branch to the **develop** branch
  - Push **master** branch's commits
  - Push tags

## [0.1.5] - 2023-07-14

### Added

- Process after `git flow finish` :
  - Push commits on **develop** branch and **master** branch
  - Rebase the **master** branch to the **develop** branch

### Fixed

- PATCH body of a PR instead of merging it on `git flow finish`

## [0.1.4] - 2023-07-14

### Changed

- PATCH body of a PR instead of merging it on `git flow finish`

## [0.1.3] - 2023-06-18

### Added

- Many changes (to be define on later notice)
