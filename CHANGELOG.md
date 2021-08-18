# Changelog
All notable changes to this project should be documented in this file.

The format of this file is based on [Keep a Changelog][kac], and this project
uses [Semantic Versioning][sv].

## [Unreleased][new]

## [0.1.0][0.1.0] — 2021-08-18

### Added
- Provide a form on the home page to submit an image file to classify.
- Accept a POST request containing an image file to analyze on '/'.
- Validate any image format found in `detect_image()` against a compile-time
    configured list, `IMAGE_FORMATS`, of acceptable filetypes.
- Add 'Configuring...', 'Testing...', and 'Running the Server' sections to
    README.

## [0.0.0][0.0.0] — 2021-04-12

### Added
- Create the project. A web app interfacing an AI that can spot cats.

---
_This file is composed with [GitHub Flavored Markdown][gfm]._

[gfm]: https://github.github.com/gfm/
[kac]: https://keepachangelog.com/en/1.0.0/
[sv]: https://semver.org

[new]: https://github.com/petejh/meimei/compare/HEAD..v0.1.0
[0.1.0]: https://github.com/petejh/meimei/releases/tag/v0.1.0
[0.0.0]: https://github.com/petejh/meimei/releases/tag/v0.0.0
