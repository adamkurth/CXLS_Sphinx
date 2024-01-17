Data Analysis
==============

.. Simple CXLS/CXFEL buttons.
.. raw:: html

    <div class="custom-buttons">
        <a href="../index.html" class="button">Access CXLS Docs</a>
        <a href="../../cxfel/index.html" class="button">Access CXFEL Docs</a>
    </div>

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   quick_start
   access
   access/agave
   access/sol
   access/globus
   slurm_script
   external_software
   custom_software/custom_software
   custom_software/rcsb_search_api
   online_analysis
   offline_analysis
   projects
   projects/background_subtraction
   projects/stream_background_subtraction
   projects/overwrite_background_subtraction
   


Introduction
------------

Here is the *comprehensive* homepage for the CXLS/CXFEL data analysis. This page will describe the data analysis workflow for CXLS and CXFEL.

If you are looking for a quick start guide, please see the `Quick Start Guide <quick_start>`_.

Fundamentally, the workflow is divided into two parts: online and offline analysis. Online analysis is performed during the experiment, while offline analysis is performed after the experiment. 
The online analysis is performed on the fly, and the results are used to make decisions about the experiment. The offline analysis is performed after the experiment, and the results are used to publish the data.

Because of the size of the data being transferred, we have to seperate this into two parts.

1. *Online Analysis:* During the experiment, we will stream the data directly to the data analysis station for quick viewing. By this workflow, quick changes can be made to obtain the desired images. 

    This process will be further described here: `Online Analysis <online_analysis>`_ 

2. *Offline Analysis:*  After the experiment, this data is then stored by ASU Research Computing. The experiment data will be stored here for further processing.

    This process will be further described here: `Offline Analysis <offline_analysis>`_


.. note:: The data analysis station is a Linux machine. 



