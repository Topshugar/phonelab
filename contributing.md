# Contributing to PhoneLab

First off, thanks for considering contributing! 🎉 PhoneLab needs you.

### How Can I Contribute?

We track everything on our [Project Board](https://github.com/Topshugar/phonelab/projects) and [Issues](https://github.com/Topshugar/phonelab/issues).

**Good First Issues:** Look for issues labeled `good first issue` - perfect for first-time contributors.

[[Good First Issue](https://img.shields.io/github/issues/Topshugar/phonelab/good%20first%20issue?label=Good%20First%20Issues)](https://github.com/Topshugar/phonelab/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

### Our Roadmap - Pick One & Own It

This is our priority list. Click to contribute:

| Version | Feature | Status | Contribute |
| --- | --- | --- | --- |
| **v0.2** | Screen Recorder + HTML Report | 🔴 TODO | [Claim this task](https://github.com/Topshugar/phonelab/issues/new?title=v0.2%20Screen%20Recorder) |
| **v0.3** | Record Mode - Record taps to JSON | 🔴 TODO | [Claim this task](https://github.com/Topshugar/phonelab/issues/new?title=v0.3%20Record%20Mode) |
| **v0.4** | Multi-phone Parallel Testing | 🔴 TODO | [Claim this task](https://github.com/Topshugar/phonelab/issues/new?title=v0.4%20Multi-phone) |
| **v0.5** | iOS Support | 🔴 TODO | [Claim this task](https://github.com/Topshugar/phonelab/issues/new?title=v0.5%20iOS) |
| **v1.0** | Web Dashboard | 🔴 TODO | [Claim this task](https://github.com/Topshugar/phonelab/issues/new?title=v1.0%20Web%20Dashboard) |

### Quick Start for Contributors

```bash
# 1. Fork and clone
git clone https://github.com/YOUR_USERNAME/phonelab.git
cd phonelab

# 2. Create branch
git checkout -b feature/my-feature

# 3. Install dev dependencies
pip install -r requirements.txt

# 4. Make your changes to python_controller/farm.py

# 5. Test
python python_controller/farm.py --test flows/login_flow.json

# 6. Push and PR
git push origin feature/my-feature
Then open a Pull Request on GitHub.

### Code Style
- Keep it simple - this is for beginners
- Use Python 3.10+
- Comment your code
- Test on a real phone if possible

### Questions?
Open an https://github.com/Topshugar/phonelab/issues/new or start a https://github.com/Topshugar/phonelab/discussions.

We will respond within 24 hours.

Push it:
```bash
git add CONTRIBUTING.md
git commit -m "docs: add contributing guide"
git push
