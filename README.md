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
    <img src="https://img.shields.io/badge/Python-3.12-blue.svg?style=flat-square&logo=python" alt="Python 3.12">
  </a>
  <a href="https://github.com/NullLabTests/pennylane-agent-hypotheses">
    <img src="https://img.shields.io/badge/Hypotheses-Definition-00D4AA?style=flat-square" alt="Hypotheses">
  </a>
  <a href="https://github.com/NullLabTests/pennylane-demos">
    <img src="https://img.shields.io/badge/Demos-Implementation-7C3AED?style=flat-square" alt="Demos">
  </a>
  <a href="https://github.com/NullLabTests/pennylane-agent-experiments/pulse">
    <img src="https://img.shields.io/github/commit-activity/w/NullLabTests/pennylane-agent-experiments?style=flat-square&logo=git" alt="Activity">
  </a>
  <a href="https://github.com/NullLabTests/pennylane-agent-experiments/issues">
    <img src="https://img.shields.io/badge/Contributions-Welcome-orange?style=flat-square&logo=contributorcovenant" alt="Contributions">
  </a>
</p>

<p align="center">
  <b>Runnable Jupyter notebooks</b> for agent-generated hypotheses about quantum machine learning with <a href="https://pennylane.ai">PennyLane</a>.<br/>
  Each experiment: <b>📓 notebook</b> + <b>⚙️ config</b> + <b>✅ smoke test</b> — validated in <b>🤖 CI</b>.
</p>

<br/>

<p align="center">
  <img src="assets/experiment_lifecycle.svg" alt="Experiment Lifecycle Diagram" width="95%">
</p>
<p align="center"><sub>Complete experiment lifecycle: Create (notebook + config + test) → Validate (CI smoke tests) → Execute (run notebook) → Analyze (results JSON). All 5 experiments (H1–H5) are complete and ready to run.</sub></p>

<br/>

---

## 🎯 Overview

This repository provides **executable experiments** that bring the hypotheses from <a href="https://github.com/NullLabTests/pennylane-agent-hypotheses"><img src="https://img.shields.io/badge/agent--hypotheses-00D4AA?style=flat-square"></a> to life. Each experiment is:

- **Self-contained** — install deps and run
- **Reproducible** — YAML configs capture every hyperparameter
- **Tested** — smoke tests run in CI on every commit
- **Extensible** — add a new hypothesis in 3 files

<br/>

---

## 🔗 Ecosystem Architecture

```mermaid
graph TB
    classDef def fill:#1a1a2e,stroke:#00d4aa,stroke-width:2,color:#ccc
    classDef impl fill:#1a1a2e,stroke:#7C3AED,stroke-width:2,color:#ccc
    classDef exec fill:#1a1a2e,stroke:#10B981,stroke-width:3,color:#fff
    classDef up fill:#333,stroke:#666,stroke-width:1,color:#999

    subgraph Research["📋 Research Layer"]
        H[("🧪 agent-hypotheses")]
        J["📄 hypotheses.json"]
    end
    subgraph Engineering["⚙️ Engineering Layer"]
        D[("🐍 pennylane-demos")]
        S["📁 experiments/H1-H5.py"]
    end
    subgraph Execution["▶️ Execution Layer <b>← You Are Here</b>"]
        direction TB
        E[("📓 agent-experiments")]
        N[("📓 Jupyter Notebooks")]
        C[("⚙️ YAML Configs")]
        T[("✅ Smoke Tests")]
        CI[("🤖 GitHub Actions")]
    end
    subgraph Output["📊 Output Layer"]
        R[("📈 results/<id>/")]
        P[("🖼️ Training Plots")]
        M[("📊 Metric JSON")]
    end

    J -.-> H
    H -->|"defines"| D
    D -->|"implements"| S
    S -->|"packaged as"| E
    E --> N
    E --> C
    E --> T
    T --> CI
    N -->|"generates"| R
    R --> P
    R --> M
    M -->|"validates"| H
    D -.->|"forked"| U["🔬 PennyLaneAI/demos"]

    class H def
    class D,impl,S def
    class E,exec,N,C,T,CI exec
    class U up
    class R,P,M exec
```

<br/>

---

## 🧪 Experiment Catalog

### All 5 Experiments — Quick Reference

<p align="center">

| ID | Hypothesis | Notebook | Config | Smoke Test | CI Status |
|:--:|-----------|:--------:|:------:|:----------:|:---------:|
| **H1** | Local cost functions to mitigate barren plateaus | [![NB](https://img.shields.io/badge/-Notebook-10B981?style=flat-square)](demos/experiments/hypothesis_H1.ipynb) | [![YAML](https://img.shields.io/badge/-Config-64748B?style=flat-square)](experiments/H1.yaml) | [![Test](https://img.shields.io/badge/-Smoke-EF4444?style=flat-square)](tests/test_H1_smoke.py) | [![CI](https://img.shields.io/badge/CI-passing-success?style=flat-square)](https://github.com/NullLabTests/pennylane-agent-experiments/actions) |
| **H2** | Data re-uploading classifier vs standard feature map | [![NB](https://img.shields.io/badge/-Notebook-10B981?style=flat-square)](demos/experiments/hypothesis_H2.ipynb) | [![YAML](https://img.shields.io/badge/-Config-64748B?style=flat-square)](experiments/H2.yaml) | [![Test](https://img.shields.io/badge/-Smoke-EF4444?style=flat-square)](tests/test_H2_smoke.py) | [![CI](https://img.shields.io/badge/CI-passing-success?style=flat-square)](https://github.com/NullLabTests/pennylane-agent-experiments/actions) |
| **H3** | Post-variational strategies on non-convex landscapes | [![NB](https://img.shields.io/badge/-Notebook-10B981?style=flat-square)](demos/experiments/hypothesis_H3.ipynb) | [![YAML](https://img.shields.io/badge/-Config-64748B?style=flat-square)](experiments/H3.yaml) | [![Test](https://img.shields.io/badge/-Smoke-EF4444?style=flat-square)](tests/test_H3_smoke.py) | [![CI](https://img.shields.io/badge/CI-unknown-lightgrey?style=flat-square)](https://github.com/NullLabTests/pennylane-agent-experiments/actions) |
| **H4** | PDE-constrained loss functions suppress gradient vanishing | [![NB](https://img.shields.io/badge/-Notebook-10B981?style=flat-square)](demos/experiments/hypothesis_H4.ipynb) | [![YAML](https://img.shields.io/badge/-Config-64748B?style=flat-square)](experiments/H4.yaml) | [![Test](https://img.shields.io/badge/-Smoke-EF4444?style=flat-square)](tests/test_H4_smoke.py) | [![CI](https://img.shields.io/badge/CI-unknown-lightgrey?style=flat-square)](https://github.com/NullLabTests/pennylane-agent-experiments/actions) |
| **H5** | Data-reuploading with trainable scaling on small benchmarks | [![NB](https://img.shields.io/badge/-Notebook-10B981?style=flat-square)](demos/experiments/hypothesis_H5.ipynb) | [![YAML](https://img.shields.io/badge/-Config-64748B?style=flat-square)](experiments/H5.yaml) | [![Test](https://img.shields.io/badge/-Smoke-EF4444?style=flat-square)](tests/test_H5_smoke.py) | [![CI](https://img.shields.io/badge/CI-unknown-lightgrey?style=flat-square)](https://github.com/NullLabTests/pennylane-agent-experiments/actions) |

</p>

### Detailed Specifications

| ID | Device | Qubits | Epochs | Batch | LR | Optimizer | Est. Runtime |
|:--:|:------:|:------:|:------:|:-----:|:--:|:---------:|:-----------:|
| H1 | `lightning.qubit` | 4 | 50 | 20 | 0.05 | GradientDescent | 30s |
| H2 | `lightning.qubit` | 4 | 60 | 24 | 0.05 | GradientDescent | 45s |
| H3 | `default.qubit` | 4 | 30 | — | 0.10 | Manual SGD | 60s |
| H4 | `default.qubit` | 2–6 | 80 | — | 0.01 | Parameter-shift | 120s |
| H5 | `lightning.qubit` | 1 | 8 | — | 0.50 | Adam | 90s |

### Hypothesis-to-Metric Mapping

```mermaid
flowchart LR
    classDef h1 fill:#8B5CF6,color:#fff
    classDef h2 fill:#3B82F6,color:#fff
    classDef h3 fill:#EF4444,color:#fff
    classDef h4 fill:#F59E0B,color:#fff
    classDef h5 fill:#10B981,color:#fff

    H1["H1<br/>NAS HQNN"] --> M1["📊 Pareto Hypervolume"]
    H2["H2<br/>Dissipation"] --> M2["📉 Gradient Variance"]
    H3["H3<br/>Post-Variational"] --> M3["🎯 Accuracy vs MLP"]
    H4["H4<br/>PDE-Constrained"] --> M4["📉 Decay Exponent"]
    H5["H5<br/>Data-Reuploading"] --> M5["📊 Accuracy Gap"]

    class H1 h1
    class H2 h2
    class H3 h3
    class H4 h4
    class H5 h5
    class M1,M2,M3,M4,M5 h2
```

<br/>

---

## 🚀 Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/NullLabTests/pennylane-agent-experiments.git
cd pennylane-agent-experiments

# Core dependencies
pip install pennylane pennylane-lightning

# For all experiments
pip install matplotlib jupyter scikit-learn
```

### 2. Run a Notebook

```bash
# Launch Jupyter
jupyter notebook demos/experiments/hypothesis_H1.ipynb
```

### 3. Run Smoke Tests

```bash
# Run all smoke tests
pip install pytest
pytest tests/ -q -v --tb=short

# Or run individually
python tests/test_H1_smoke.py
python tests/test_H5_smoke.py
```

<br/>

---

## ✅ CI/CD Pipeline

```mermaid
graph LR
    classDef event fill:#1e293b,stroke:#64748b,color:#ccc
    classDef step fill:#1a1a2e,stroke:#7C3AED,stroke-width:2,color:#fff
    classDef passS fill:#14532d,stroke:#22c55e,color:#fff
    classDef failS fill:#7f1d1d,stroke:#ef4444,color:#fff

    PUSH(["📤 Push / PR"]) --> CHECKOUT["📥 Checkout repo"]
    CHECKOUT --> SETUP["🐍 Setup Python 3.12"]
    SETUP --> INSTALL["📦 pip install pennylane<br/>pennylane-lightning<br/>matplotlib"]
    INSTALL --> SMOKE["🧪 pytest tests/ -q"]
    SMOKE --> PASS(["✅ All Smoke Tests Pass"])
    SMOKE --> FAIL(["❌ Smoke Tests Fail"])

    class PUSH event
    class CHECKOUT,SETUP,INSTALL,SMOKE step
    class PASS passS
    class FAIL failS
```

**Workflow file:** [`.github/workflows/ci-smoke.yml`](.github/workflows/ci-smoke.yml)

| Trigger | Action |
|---------|--------|
| `push` (any branch) | Run all 5 smoke tests |
| `pull_request` | Run all 5 smoke tests |

Current status: <a href="https://github.com/NullLabTests/pennylane-agent-experiments/actions/workflows/ci-smoke.yml"><img src="https://github.com/NullLabTests/pennylane-agent-experiments/actions/workflows/ci-smoke.yml/badge.svg?style=flat-square" alt="CI"></a>

<br/>

---

## 📁 Repository Map

```
📦 pennylane-agent-experiments
│
├── 📁 demos/
│   └── 📁 experiments/              # 📓 Jupyter notebooks
│       ├── hypothesis_H1.ipynb      #   Local cost vs global cost
│       ├── hypothesis_H2.ipynb      #   Data re-uploading vs standard
│       ├── hypothesis_H3.ipynb      #   Post-variational strategies
│       ├── hypothesis_H4.ipynb      #   PDE-constrained loss
│       └── hypothesis_H5.ipynb      #   Trainable data reuploading
│
├── 📁 experiments/                   # ⚙️ YAML configuration files
│   ├── H1.yaml                      #   Hyperparameters for H1
│   ├── H2.yaml                      #   Hyperparameters for H2
│   ├── H3.yaml                      #   Hyperparameters for H3
│   ├── H4.yaml                      #   Hyperparameters for H4
│   └── H5.yaml                      #   Hyperparameters for H5
│
├── 📁 tests/                         # ✅ Smoke tests (CI-validated)
│   ├── test_H1_smoke.py
│   ├── test_H2_smoke.py
│   ├── test_H3_smoke.py
│   ├── test_H4_smoke.py
│   └── test_H5_smoke.py
│
├── 📁 assets/                       # 🖼️ Visual assets
│   ├── sticker.png
│   └── sticker.svg
│
├── 📁 results/                      # 📊 Generated data (gitignored)
│   └── .gitkeep
│
├── 📁 .github/workflows/            # 🤖 CI pipeline
│   └── ci-smoke.yml
│
├── 📄 README.md                     # ℹ️ This file
├── 📄 LICENSE                       # ⚖️ MIT
└── 📄 .gitignore                    # 🙈 Ignored files
```

<br/>

---

## 📊 Results Format

Each notebook saves results to `results/<id>/`:

```
results/H1/
├── run_20260601_120000.json     # 📊 Metrics (JSON)
│   {
│     "global": {"final_acc": 0.85, "losses": [...]},
│     "local":  {"final_acc": 0.92, "losses": [...]}
│   }
├── run_20260601_120000.json     # Multiple runs preserved
└── plot.png                     # 🖼️ Training convergence plot
```

| Field | Type | Description |
|-------|------|-------------|
| `final_acc` | `float` | Test-set accuracy after training |
| `losses` | `list[float]` | Per-epoch training loss |
| `label` | `str` | Strategy identifier |
| `params` | `list[float]` | Final trained parameters |

<br/>

---

## 🔧 How to Add a New Hypothesis

Adding H6 is straightforward — 3 files:

```mermaid
flowchart LR
    A["📓 demos/experiments/<br/>hypothesis_H6.ipynb"] --> B["⚙️ experiments/<br/>H6.yaml"]
    B --> C["✅ tests/<br/>test_H6_smoke.py"]
    C --> D["📄 README.md<br/>(add to table)"]
    style A fill:#8B5CF6,color:#fff
    style B fill:#3B82F6,color:#fff
    style C fill:#10B981,color:#fff
    style D fill:#F59E0B,color:#fff
```

1. **Notebook** — Copy `hypothesis_H1.ipynb` as template, update cell content
2. **Config** — Copy `H1.yaml`, update hyperparameters
3. **Smoke test** — Copy `test_H1_smoke.py`, verify circuit executes
4. **README** — Add row to experiment table

<br/>

---

## 🛠️ Dependency Matrix

| Package | Version | Used By |
|---------|:-------:|---------|
| `pennylane` | ≥0.38 | All experiments (core) |
| `pennylane-lightning` | ≥0.38 | H1, H2, H5 (fast simulator) |
| `matplotlib` | ≥3.5 | H2, H4 (plotting) |
| `jupyter` | ≥1.0 | All notebooks |
| `scikit-learn` | ≥1.3 | H1, H3, H5 (datasets, MLP) |
| `torch` | ≥2.0 | H1 (TorchLayer) |
| `pytest` | ≥7.0 | Smoke tests |

<br/>

---

## 📄 License

**MIT** — see [LICENSE](LICENSE) for details.

---

<p align="center">
  <sub>Part of the <a href="https://github.com/NullLabTests">NullLabTests</a> agent-driven research ecosystem.</sub>
  <br/>
  <sub>
    <img src="https://img.shields.io/badge/-hypotheses-00D4AA?style=flat-square">
    <img src="https://img.shields.io/badge/-demos-7C3AED?style=flat-square">
    <img src="https://img.shields.io/badge/-experiments-10B981?style=flat-square">
  </sub>
</p>
