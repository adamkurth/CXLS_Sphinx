---
runme:
  id: 01HGH1C5W5NH560Z1NN3HFF4VF
  version: v2.0
---

## CXLS Sphinx Repository

This repository is the documentation for CXLS using Sphinx GitPages. This is under construction currently and will be updated regularly.

Changed so that when pushing to either the `main`, or `progress` branch, `.github/workflows/sphinx_deploy.yml` file is automatically triggered to update the website available at:

[Click here to access the documentation](https://adamkurth.github.io/CXLS_Sphinx/docs/build/html/)

For testing and development the html file, after running `make html` is available here:

`file:///Users/adamkurth/Documents/vscode/CXFEL_Image_Analysis/CXFEL/CXLS_Sphinx/docs/build/html/index.html`

and for work station:

`file:///home/labuser/Development/adam/vscode/CXLS_Sphinx/docs/build/html/home.html`

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

- Using conda, we need to install Sphinx with:

<<<<<<< HEAD

```bash {"id":"01HH2XHY84BNQN13BZC2XTX3H8"}
=======
```bash {"id":"01HHYX7DZ9MAG3H6JA2XD73NNX"}
>>>>>>> a6d8cca373bc52ec476f1bbf4ec006d15be863d6
conda install sphinx
```

- Also, install useful other packages such as `sphinx_rtd_theme` and `recommonmark`.

<<<<<<< HEAD

```bash {"id":"01HH2XHY84BNQN13BZC4K0MZJG"}
=======
```bash {"id":"01HHYX7DZ9MAG3H6JA2XR8Z4PD"}
>>>>>>> a6d8cca373bc52ec476f1bbf4ec006d15be863d6
conda install sphinx_rtd_theme recommonmark sphinxawesome_theme
```

### 5. Verify Installation

- Verify installation and create initial sphinx build for documentation with:

<<<<<<< HEAD

```bash {"id":"01HH2XHY84BNQN13BZC4XNGXS9"}
=======
```bash {"id":"01HHYX7DZ9MAG3H6JA2Z37Y1WG"}
>>>>>>> a6d8cca373bc52ec476f1bbf4ec006d15be863d6
sphinx-quickstart
```

### 6. Deactivate Enviornment

- When done working with the enviornment, deactivate using:

<<<<<<< HEAD

```bash {"id":"01HH2XHY84BNQN13BZC8FFJE8A"}
=======
```bash {"id":"01HHYX7DZ9MAG3H6JA2ZGDR0ZD"}
>>>>>>> a6d8cca373bc52ec476f1bbf4ec006d15be863d6
conda deactivate
```

