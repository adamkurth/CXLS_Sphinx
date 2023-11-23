---
runme:
  id: 01HFWNATD09N5FAN2MDKRTZZE2
  version: v2.0
---

## CXLS Sphinx Repository

This repository relies on the use of a virtual environment called .venv. This is included in the root directory of this repository, and should be properly installed before adjusting the sphinx documentation.

Instead please install this virtual enviornment.

1. install `virtualenv` package using:
    ```bash
    pip install virtualenv
    ```

2. Go to project directory in terminal, where the virtual environment will be made. 

3. Create virtual environment, naming it what you like. 
    ```bash
    virtualenv env
    ```

4. Activate this 
   
- for Mac & Linux
    ```bash 
    source env/bin/activate
    ```
- for Windows
    ```
    .\env\Scripts\activate
    ```

5. Now install needed packages such as 
    ```bash 
    pip install numpy
    ```
6. Check the installed packages by using
    ```bash 
    pip freeze
    ```
7. Finally when done, 
   ```bash
   deactivate
   ```

file:///Users/adamkurth/Documents/vscode/CXFEL_Image_Analysis/CXFEL/CXLS_Sphinx/docs/build/html/index.html