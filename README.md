<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/sticker.png">
    <img src="assets/sticker.png" alt="PennyLane Agent Experiments" width="160"/>
  </picture>
</p>

<h1 align="center">📓 PennyLane Agent Experiments</h1>

<p align="center">
  <a href="https://github.com/NullLabTests/pennylane-agent-experiments/actions/workflows/ci-smoke.yml">
    <img src="https://github.com/NullLabTests/pennylane-agent-experiments/actions/workflows/ci-smoke.yml/badge.svg?style=flat-square&logo=githubactions" alt="CI">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square&logo=opensourceinitiative" alt="License">
  </a>
  <a href="https://pennylane.ai">
    <img src="https://img.shields.io/badge/PennyLane-0.45.0-blueviolet?style=flat-square&logo=quantum" alt="PennyLane">
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python" alt="Python 3.12">
  </a>
  <a href="https://github.com/NullLabTests/pennylane-agent-hypotheses">
    <img src="https://img.shields.io/badge/Hypotheses-Definition-00D4AA?style=flat-square" alt="Hypotheses">
  </a>
  <a href="https://github.com/NullLabTests/pennylane-demos">
    <img src="https://img.shields.io/badge/Demos-Implementation-7C3AED?style=flat-square" alt="Demos">
  </a>
  <a href="https://github.com/NullLabTests/pennylane-agent-experments/pulse">
    <img src="https://img.shields.io/github/commit-activity/w/NullLabTests/pennylane-agent-experiments?style=flat-square" alt="Activity">
  </a>
</p>

<p align="center">
  <b>Runnable Jupyter notebooks</b> for agent-generated hypotheses about quantum machine learning with <a href="https://pennylane.ai">PennyLane</a>.<br/>
  Each experiment is packaged as a 📓 notebook, ⚙️ config, and ✅ smoke test — validated in CI.
</p>

<br/>

---

## 🎯 Overview

This repository provides **executable experiments** that implement the hypotheses defined in the <a href="https://github.com/NullLabTests/pennylane-agent-hypotheses"><img src="https://img.shields.io/badge/Hypotheses-north%20star-00D4AA?style=flat-square"></a> project. Each experiment is self-contained and designed for reproducibility.

<br/>

### 🔗 Ecosystem

```mermaid
graph TB
    subgraph Define["📋 Define"]
        H[("🧪 agent-hypotheses")]
    end
    subgraph Implement["⚙️ Implement"]
        D[("🐍 pennylane-demos")]
    end
    subgraph Execute["▶️ Execute"]
        E[("📓 agent-experiments<br/><b>← this repo</b>)")]
        subgraph Components[" "]
            NB[("📓 Notebooks")]
            YM[("⚙️ YAML Configs")]
            ST[("✅ Smoke Tests")]
        end
    end
    H -->|"defines"| D
    D -->|"packaged as"| E
    E --- Components
    ST -->|"validated by"| CI[("🤖 CI Pipeline")]
    style H fill:#1a1a2e,stroke:#00d4aa,stroke-width:2,color:#ccc
    style D fill:#1a1a2e,stroke:#7C3AED,stroke-width:2,color:#ccc
    style E fill:#1a1a2e,stroke:#10B981,stroke-width:3,color:#fff
    style NB fill:#1e293b,stroke:#64748b,color:#ccc
    style YM fill:#1e293b,stroke:#64748b,color:#ccc
    style ST fill:#1e293b,stroke:#64748b,color:#ccc
    style CI fill:#1e293b,stroke:#F59E0B,color:#ccc
```

<br/>

---

## 🧪 Experiments

<p align="center">

| ID | Hypothesis | Notebook | Config | Smoke Test |
|:-:|-----------|:--------:|:------:|:----------:|
| **H1** | Local cost functions to mitigate barren plateaus | [![NB](https://img.shields.io/badge/-Notebook-10B981?style=flat-square)](demos/experiments/hypothesis_H1.ipynb) | [![YAML](https://img.shields.io/badge/-Config-64748B?style=flat-square)](experiments/H1.yaml) | [![Test](https://img.shields.io/badge/-Smoke-EF4444?style=flat-square)](tests/test_H1_smoke.py) |
| **H2** | Data re-uploading classifier vs standard feature map | [![NB](https://img.shields.io/badge/-Notebook-10B981?style=flat-square)](demos/experiments/hypothesis_H2.ipynb) | [![YAML](https://img.shields.io/badge/-Config-64748B?style=flat-square)](experiments/H2.yaml) | [![Test](https://img.shields.io/badge/-Smoke-EF4444?style=flat-square)](tests/test_H2_smoke.py) |
| **H3** | Post-Variational Strategies on Non-Convex Landscapes | [![NB](https://img.shields.io/badge/-Notebook-10B981?style=flat-square)](demos/experiments/hypothesis_H3.ipynb) | [![YAML](https://img.shields.io/badge/-Config-64748B?style=flat-square)](experiments/H3.yaml) | [![Test](https://img.shields.io/badge/-Smoke-EF4444?style=flat-square)](tests/test_H3_smoke.py) |
| **H4** | PDE-Constrained Loss Functions Suppress Gradient Vanishing | [![NB](https://img.shields.io/badge/-Notebook-10B981?style=flat-square)](demos/experiments/hypothesis_H4.ipynb) | [![YAML](https://img.shields.io/badge/-Config-64748B?style=flat-square)](experiments/H4.yaml) | [![Test](https://img.shields.io/badge/-Smoke-EF4444?style=flat-square)](tests/test_H4_smoke.py) |
| **H5** | Data-Reuploading with Trainable Scaling on Small Benchmarks | [![NB](https://img.shields.io/badge/-Notebook-10B981?style=flat-square)](demos/experiments/hypothesis_H5.ipynb) | [![YAML](https://img.shields.io/badge/-Config-64748B?style=flat-square)](experiments/H5.yaml) | [![Test](https://img.shields.io/badge/-Smoke-EF4444?style=flat-square)](tests/test_H5_smoke.py) |

</p>

### 📊 Experiment Details

| ID | Device | Qubits | Epochs | Est. Runtime | Key Metric |
|:--:|:------:|:------:|:------:|:------------:|:----------:|
| H1 | `lightning.qubit` | 4 | 50 | 30s | Test accuracy |
| H2 | `lightning.qubit` | 4 | 60 | 45s | Test accuracy |
| H3 | `default.qubit` | 4 | 30 | 60s | Accuracy vs MLP |
| H4 | `default.qubit` | 6 | 80 | 120s | Gradient variance |
| H5 | `lightning.qubit` | 1 | 8 | 90s | Accuracy gap to MLP |

<br/>

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/NullLabTests/pennylane-agent-experiments.git
cd pennylane-agent-experiments

# Install dependencies
pip install pennylane pennylane-lightning matplotlib jupyter scikit-learn

# Launch a specific experiment
jupyter notebook demos/experiments/hypothesis_H1.ipynb
```

<br/>

## ✅ Run Smoke Tests

```bash
# Individual tests
python tests/test_H1_smoke.py
python tests/test_H2_smoke.py

# Or all at once with pytest
pip install pytest
pytest tests/ -q -v --tb=short
```

> Smoke tests run automatically via [GitHub Actions](.github/workflows/ci-smoke.yml) on every push and PR.

<br/>

---

## 📁 Repository Structure

```
📦 pennylane-agent-experiments
├── 📁 demos/
│   └── 📁 experiments/        # 📓 Jupyter notebooks (one per hypothesis)
│       ├── hypothesis_H1.ipynb
│       ├── hypothesis_H2.ipynb
│       ├── hypothesis_H3.ipynb
│       ├── hypothesis_H4.ipynb
│       └── hypothesis_H5.ipynb
├── 📁 experiments/             # ⚙️ YAML configuration files
│   ├── H1.yaml  ─── H5.yaml
├── 📁 tests/                   # ✅ Smoke tests (validated in CI)
│   ├── test_H1_smoke.py ─── test_H5_smoke.py
├── 📁 assets/                  # 🖼️ Visual assets
│   ├── sticker.png
│   └── sticker.svg
├── 📁 results/                 # 📊 Training curves & metrics (gitignored)
├── 📁 .github/workflows/       # 🤖 CI pipeline
│   └── ci-smoke.yml
├── 📄 README.md
├── 📄 LICENSE                  # MIT
└── 📄 .gitignore
```

<br/>

---

## 📊 Results

Per-experiment training curves and metrics are saved to `results/<id>/`:

```
results/
├── H1/
│   ├── run_20260601_120000.json   # Timestamped metrics
│   └── plot.png                   # Training convergence plot
├── H2/
│   ├── run_20260601_120000.json
│   └── plot.png
└── ...
```

> This directory is **gitignored** — generated locally when notebooks are run.

<br/>

---

## 🤖 CI Pipeline

```mermaid
graph LR
    PUSH(["📤 Push / PR"]) --> CHECKOUT["📥 Checkout"]
    CHECKOUT --> SETUP["🐍 Setup Python 3.12"]
    SETUP --> INSTALL["📦 Install deps"]
    INSTALL --> SMOKE["🧪 Run Smoke Tests"]
    SMOKE --> PASS(["✅ All Pass"])
    SMOKE --> FAIL(["❌ Fail"])
    style PASS fill:#14532d,stroke:#22c55e,color:#fff
    style FAIL fill:#7f1d1d,stroke:#ef4444,color:#fff
```

Current status: <a href="https://github.com/NullLabTests/pennylane-agent-experiments/actions/workflows/ci-smoke.yml"><img src="https://github.com/NullLabTests/pennylane-agent-experiments/actions/workflows/ci-smoke.yml/badge.svg?style=flat-square" alt="CI"></a>

<br/>

---

## 📄 License

**MIT** — see [LICENSE](LICENSE) for details.
