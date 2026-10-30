# Contributing to PhoneLab

First off, thanks for considering contributing! 🎉 PhoneLab needs you.

## How Can I Contribute?

We track everything on our Project Board and Issues.

**Good First Issues:** Look for issues labeled `good first issue` - perfect for first-time contributors.

👉 [Good First Issue](https://github.com/Topshugar/phonelab/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

### Our Roadmap - Pick One & Own It
This is our priority list. Click to contribute:

| Version | Feature | Status | Contribute |
| :--- | :--- | :--- | :--- |
| v0.2 | Screen Recorder + HTML Report | 🔴 TODO | [Claim this task](https://github.com/Topshugar/phonelab/issues) |
| v0.3 | Record Mode - Record taps to JSON | 🔴 TODO | [Claim this task](https://github.com/Topshugar/phonelab/issues) |
| v0.4 | Multi-phone Parallel Testing | 🔴 TODO | [Claim this task](https://github.com/Topshugar/phonelab/issues) |
| v0.5 | iOS Support | 🔴 TODO | [Claim this task](https://github.com/Topshugar/phonelab/issues) |
| v1.0 | Web Dashboard | 🔴 TODO | [Claim this task](https://github.com/Topshugar/phonelab/issues) |

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