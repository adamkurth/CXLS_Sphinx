---
runme:
  id: 01HGH1C5W5NH560Z1NN3HFF4VF
  version: v2.0
---

## CXLS Sphinx Repository

This repository is the documentation for CXLS using Sphinx GitPages. This is under construction currently and will be updated regularly.

For development, the file is available at:

`file:///Users/adamkurth/Documents/vscode/CXFEL_Image_Analysis/CXFEL/CXLS_Sphinx/docs/build/html/index.html`

This repository relies on the use of a virtual environment called .venv. This is included in the root directory of this repository, and should be properly installed before adjusting the sphinx documentation.

## Virtual Enviornment Installation

Using Conda Python package manager, to properly install requirements for using Sphinx and GitPages.

### 1. Open Terminal / Command Line

- Make sure that Anaconda or Miniconda are installed before proceeding.

### 2. Create New Conda Enviornment

- Create a new Conda enviornment called `sphinx_env`.

- Replace 3.x with the specific version of Python you want to use (e.g., 3.8).

```bash {"id":"01HGH1C5W5NH560Z1NMHVV6XR8"}
conda create --name sphinx_env python=3.x
```

### 3. Activate Enviornment

- Using `source` command with Linux and Mac activate the env with:

```bash {"id":"01HGH1C5W5NH560Z1NMMHX72QX"}
conda activate sphinx_env
```

### 4. Install Sphinx

- Using conda, we need to install Sphinx with:

```bash {"id":"01HGH1C5W5NH560Z1NMQ70B1XG"}
conda install sphinx
```

- Also, install useful other packages such as `sphinx_rtd_theme` and `recommonmark`.

```bash {"id":"01HGH1C5W5NH560Z1NMTJ70GD8"}
conda install sphinx_rtd_theme recommonmark
```

### 5. Verify Installation

- Verify installation and create initial sphinx build for documentation with:

```bash {"id":"01HGH1C5W5NH560Z1NMY8QSVVH"}
sphinx-quickstart
```

### 6. Deactivate Enviornment

- When done working with the enviornment, deactivate using:

```bash {"id":"01HGH1C5W5NH560Z1NN12PM8B2"}
conda deactivate
```

