# Changelog
All notable changes to this project should be documented in this file.

The format of this file is based on [Keep a Changelog][kac], and this project
uses [Semantic Versioning][sv].

## [Unreleased][new]

## [0.2.0][0.2.0] — 2021-09-13

### Added
- Dependencies on [deepen][deep], [h5py][h5py], [numpy][numpy], and
    [Pillow][pil].
- Classify the uploaded image using a pre-trained, neural network.
- Utility script to train a model from default data.

### Changed
- New upper bound on the required Python version to satisfy a constraint for the
    current stable version of numpy.

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

[deep]: https://github.com/petejh/deepen/
[gfm]: https://github.github.com/gfm/
[h5py]: https://www.h5py.org/
[kac]: https://keepachangelog.com/en/1.0.0/
[numpy]: https://numpy.org/
[pil]: https://python-pillow.org/
[sv]: https://semver.org

[new]: https://github.com/petejh/meimei/compare/HEAD..v0.2.0
[0.2.0]: https://github.com/petejh/meimei/releases/tag/v0.2.0
[0.1.0]: https://github.com/petejh/meimei/releases/tag/v0.1.0
[0.0.0]: https://github.com/petejh/meimei/releases/tag/v0.0.0
