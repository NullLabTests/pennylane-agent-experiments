# PennyLane Agent Experiments

[![CI — Smoke Tests](https://github.com/NullLabTests/pennylane-agent-experiments/actions/workflows/ci-smoke.yml/badge.svg)](https://github.com/NullLabTests/pennylane-agent-experiments/actions/workflows/ci-smoke.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PennyLane](https://img.shields.io/badge/PennyLane-0.45.0-blueviolet)](https://pennylane.ai)
[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://python.org)

Runnable experiments for agent-generated hypotheses about quantum machine learning with PennyLane.

## Experiments

| ID | Hypothesis | Notebook | Config |
|----|-----------|----------|--------|
| H1 | Local cost functions to mitigate barren plateaus | [`demos/experiments/hypothesis_H1.ipynb`](demos/experiments/hypothesis_H1.ipynb) | [`experiments/H1.yaml`](experiments/H1.yaml) |
| H2 | Data re-uploading classifier vs standard feature map | [`demos/experiments/hypothesis_H2.ipynb`](demos/experiments/hypothesis_H2.ipynb) | [`experiments/H2.yaml`](experiments/H2.yaml) |

## Quick Start

```bash
pip install pennylane pennylane-lightning matplotlib
jupyter notebook demos/experiments/hypothesis_H1.ipynb
```

## Run Smoke Tests

```bash
pip install pennylane pennylane-lightning
python tests/test_H1_smoke.py
python tests/test_H2_smoke.py
# or
pip install pytest
pytest tests/ -q -v
```

## Results

Per-experiment training curves and metrics are saved to `results/<id>/`.

## License

MIT — see [LICENSE](LICENSE).

## Topics

`quantum` `qml` `pennylane` `experiments` `agents`
