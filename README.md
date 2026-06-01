<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/sticker.png">
    <img src="assets/sticker.png" alt="PennyLane Agent Experiments" width="180"/>
  </picture>
</p>

<h1 align="center">PennyLane Agent Experiments</h1>

<p align="center">
  <a href="https://github.com/NullLabTests/pennylane-agent-experiments/actions/workflows/ci-smoke.yml">
    <img src="https://github.com/NullLabTests/pennylane-agent-experiments/actions/workflows/ci-smoke.yml/badge.svg?style=flat-square" alt="CI — Smoke Tests">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License: MIT">
  </a>
  <a href="https://pennylane.ai">
    <img src="https://img.shields.io/badge/PennyLane-0.45.0-blueviolet?style=flat-square" alt="PennyLane">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.12-blue?style=flat-square" alt="Python 3.12">
  </a>
  <a href="https://github.com/NullLabTests/pennylane-agent-hypotheses">
    <img src="https://img.shields.io/badge/Hypotheses-north%20star-00D4AA?style=flat-square" alt="View Hypotheses">
  </a>
  <a href="https://github.com/NullLabTests/pennylane-demos">
    <img src="https://img.shields.io/badge/Demos-implementations-8B5CF6?style=flat-square" alt="Demos Implementations">
  </a>
</p>

<p align="center">
  <b>Runnable Jupyter notebooks</b> for agent-generated hypotheses about quantum machine learning with <a href="https://pennylane.ai">PennyLane</a>.
</p>

---

## Overview

This repository provides executable experiments — each packaged as a Jupyter notebook, YAML config, and smoke test — that implement the hypotheses defined in the [pennylane-agent-hypotheses](https://github.com/NullLabTests/pennylane-agent-hypotheses) project.

### Project Ecosystem

| Repository | Role |
|-----------|------|
| [pennylane-agent-hypotheses](https://github.com/NullLabTests/pennylane-agent-hypotheses) | Research hypotheses, evaluation metrics, references |
| [pennylane-demos](https://github.com/NullLabTests/pennylane-demos) | Python implementations (fork of PennyLaneAI/demos) |
| **pennylane-agent-experiments** (this repo) | Runnable notebooks, configs, CI smoke tests |

---

## Experiments

| ID | Hypothesis | Notebook | Config | Smoke Test |
|----|-----------|----------|--------|------------|
| H1 | Local cost functions to mitigate barren plateaus | [`demos/experiments/hypothesis_H1.ipynb`](demos/experiments/hypothesis_H1.ipynb) | [`experiments/H1.yaml`](experiments/H1.yaml) | [`tests/test_H1_smoke.py`](tests/test_H1_smoke.py) |
| H2 | Data re-uploading classifier vs standard feature map | [`demos/experiments/hypothesis_H2.ipynb`](demos/experiments/hypothesis_H2.ipynb) | [`experiments/H2.yaml`](experiments/H2.yaml) | [`tests/test_H2_smoke.py`](tests/test_H2_smoke.py) |
| H3 | Post-Variational Strategies on Non-Convex Landscapes | [`demos/experiments/hypothesis_H3.ipynb`](demos/experiments/hypothesis_H3.ipynb) | [`experiments/H3.yaml`](experiments/H3.yaml) | [`tests/test_H3_smoke.py`](tests/test_H3_smoke.py) |
| H4 | PDE-Constrained Loss Functions Suppress Gradient Vanishing | [`demos/experiments/hypothesis_H4.ipynb`](demos/experiments/hypothesis_H4.ipynb) | [`experiments/H4.yaml`](experiments/H4.yaml) | [`tests/test_H4_smoke.py`](tests/test_H4_smoke.py) |
| H5 | Data-Reuploading with Trainable Scaling on Small Benchmarks | [`demos/experiments/hypothesis_H5.ipynb`](demos/experiments/hypothesis_H5.ipynb) | [`experiments/H5.yaml`](experiments/H5.yaml) | [`tests/test_H5_smoke.py`](tests/test_H5_smoke.py) |

---

## Quick Start

```bash
# Install dependencies
pip install pennylane pennylane-lightning matplotlib jupyter

# Launch a specific experiment
jupyter notebook demos/experiments/hypothesis_H1.ipynb
```

## Run Smoke Tests

```bash
# Individual tests
python tests/test_H1_smoke.py
python tests/test_H2_smoke.py

# Or all at once
pip install pytest
pytest tests/ -q -v
```

---

## Repository Structure

```
├── demos/
│   └── experiments/       # Jupyter notebooks (one per hypothesis)
├── experiments/            # YAML configuration files
│   ├── H1.yaml
│   └── H2.yaml
├── tests/                  # Smoke tests (validated in CI)
│   ├── test_H1_smoke.py
│   └── test_H2_smoke.py
├── assets/                 # Visual assets
│   └── sticker.png
├── results/                # Training curves & metrics (gitignored)
├── .github/workflows/      # CI pipeline
├── README.md
└── LICENSE
```

---

## Results

Per-experiment training curves and metrics are saved to `results/<id>/`. This directory is gitignored; generated locally when notebooks are run.

---

## License

MIT — see [LICENSE](LICENSE) for details.
