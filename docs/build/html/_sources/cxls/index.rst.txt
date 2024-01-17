CXLS Documentation Home Page
============================

.. raw:: html

    <div class="custom-buttons">
        <a href="index.html" class="button">Access CXLS Docs</a>
        <a href="../cxfel/index.html" class="button">Access CXFEL Docs</a>
    </div>


Introduction
------------

For the uses of CXLS, we have adapted the existing Reborn repository. `Here <https://gitlab.com/kirianlab/reborn>`_ is the hyperlink for this repo. Specifically, this repository is tailored to the uses at CXLS and gathering and analyzing crystallography data. 

Click here to view the documentation for Reborn: `Reborn Documentation <https://kirianlab.gitlab.io/reborn/>`_.

This documentation is still under construction and will be updated regularly.

.. toctree::
   :maxdepth: 5
   :hidden:
   :caption: CXLS Contents:

   index_test
   accelerator/accelerator
   accelerator/overview
   endstations/endstations
   endstations/area_detector
   endstations/cxls_eiger_4m
   sample_delivery/sample_delivery
   data_analysis/data_analysis
   data_analysis/access/agave
   data_analysis/access/sol
   data_analysis/access/globus
   data_analysis/slurm_script
   data_analysis/external_software
   data_analysis/custom_software/custom_software
   data_analysis/custom_software/rcsb_search_api
   data_analysis/online_analysis
   data_analysis/offline_analysis
   data_analysis/projects
   data_analysis/projects/background_subtraction
   data_analysis/projects/stream_background_subtraction
   data_analysis/projects/overwrite_background_subtraction


.. _cxls_installation: 

Installation
------------

Please refer to the `README.md` file in the repository for installation and setup instructions, available here: available here: `README <https://github.com/adamkurth/CXLS_Sphinx/blob/main/README.md>`_.

.. _reborn:

Documentation for Reborn
-------------------------
The GitLab repository for reborn can be found here: `Reborn Repository <https://gitlab.com/kirianlab/reborn>`_.

The documentation for reborn can be found here: `Reborn Documentation <https://kirianlab.gitlab.io/reborn/>`_.


.. _dcu:

Troubleshooting DCU Notes
-------------------------

Software:
---------

- Verify that all instructions on `README.md` have been followed, available here: `README <https://github.com/adamkurth/CXLS_Sphinx/blob/main/README.md>`_.

- Verify that the DCU is connected to the network (either via ethernet or wifi)


Hardware:
---------

- Verify that the chiller is running and set to 22°C
- Verify that the dry air is flowing (just enough that you can feel it on your lip should be plenty)
- Verify that the blue LED on the power brick is lit
- Verify that the detector's POWER switch is depressed
- Verify that the DCU is powered on and booted, and that the iDRAC LED or display panel do not show any errors
   