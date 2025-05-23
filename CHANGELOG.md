# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.1/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.1] - 2025-05-04

### Changed

- Retrieving the git repository name from it's remote config (it was from folder name)

## [0.3.0] - 2025-04-21

### Added

- Gitflow options feature
  - `use-latest` : automate the creation of the latest tag on new tags (hotfixes and releases)

### Fixed

- Creation of "latest" tag

## [0.2.2] - 2025-04-20

### Changed

- Bold text for input

### Fixed

- Using old (undefined) variable

## [0.2.1] - 2025-04-20

### Added

- A README file

### Changed

- Properly formatted code
- Colorize hooks output

## [0.2.0] - 2024-04-27

### Added

- Utils library

### Changed

- Ability to handle multiple owners

## [0.1.7] - 2023-07-14

### Fixed

- Process after `git flow finish` :
  - Push **develop** branch's commits
  - \+ Instructions to execute ONLY on _hotfixes_ and _releases_
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
