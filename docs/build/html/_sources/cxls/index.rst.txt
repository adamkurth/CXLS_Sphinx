.. CXLS Sphinx documentation master file, created by
   sphinx-quickstart on Wed Nov 22 10:24:38 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

CXLS Documentation Home Page
============================


Introduction
------------

By adapting the uses of Reborn repository (https://gitlab.com/kirianlab/reborn), we have created a new repository for CXLS. 

This repository is tailored to the uses at CXLS and gathering and analyzing crystallography data. 

The documentation for Reborn can be found here: https://kirianlab.gitlab.io/reborn/.

This documentation is still under construction and will be updated regularly.

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   overview
   agave
   globus
   sol
   slurm_script
   cxls_eiger_4m
   rcsb_search_api
   projects

.. _installation: 

Installation
------------

Please refer to the `README.md` file in the repository for installation and setup instructions, available here: available here: `README <https://github.com/adamkurth/CXLS_Sphinx/blob/main/README.md>`_.
.. _reborn:

Documentation for Reborn
-------------------------
The GitLab repository for reborn can be found here: https://gitlab.com/kirianlab/reborn.

The documentation for reborn can be found here: https://kirianlab.gitlab.io/reborn/.


.. _dcu:

Troubleshooting DCU Notes
-------------------------

Software:
---------

- Verify that all instructions on :doc:`README.md` have been followed, available here: `README <https://github.com/adamkurth/CXLS_Sphinx/blob/main/README.md>`_.
- Verify that the DCU is connected to the network (either via ethernet or wifi)


Hardware:
---------

- Verify that the chiller is running and set to 22°C
- Verify that the dry air is flowing (just enough that you can feel it on your lip should be plenty)
- Verify that the blue LED on the power brick is lit
- Verify that the detector's POWER switch is depressed
- Verify that the DCU is powered on and booted, and that the iDRAC LED or display panel do not show any errors
   