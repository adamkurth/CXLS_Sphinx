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

`file:///home/labuser/Development/adam/vscode/CXLS_Sphinx/docs/build/html/index.html`

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

```bash {"id":"01HH2XHY84BNQN13BZC8FFJE8A"}
conda deactivate
```

### 7. From here...

From here, we need to make `.rst` files in the following fashion. Say we need another page (`another_page.rst`) to link to out main `index.rst` from running `sphinx-quickstart`.

``` bash
touch another_page.rst
```

After creating this file, we need to go into out main `index.rst` and create a table of contents tree (toctree) like this. 

``` sphinx
toctree::
   :maxdepth: 2
   :caption: Contents:

   another_page
```

What this will do is link the newly made file, and make this accessible to the user of the website. 

- To make this toctree accessible only in the main side pannel of `index.rst` we need to use the `hidden` option.

``` sphinx
toctree::
   :maxdepth: 2
   :caption: Contents:
   :hidden:
   
   another_page
```

Now we can proceed with adapting `another_page.rst` using sphinx syntax to build our page.

