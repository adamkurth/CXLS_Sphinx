Quick Start Guide for Data Analysis at CXLS
============================================

Here we intend to provide a quick guide for using the CXLS data analysis tools. This will cover activating reborn (our data analysis package), setting up the data stream using ZMQ, and then using the data analysis tools for both online and offline analysis.

Getting Started
----------------

.. administation details/labuser problem
To get started at the Data Analysis station at CXLS, you will need to log in to the computer `cxls-data-analysis` using your ASURITE credentials ( RESOLVE labuser ). 

.. activating reborn
Once you have logged in, you will need to activate the `reborn` environment. To do this, you will need to open a terminal and type the following commands:


.. code-block:: bash

    $ source activate reborn


Same thing can be done using `conda` command:


.. code-block:: bash

    $ conda activate reborn


This will activate the `reborn` environment, which contains all of the packages that you will need to do your data analysis.


Setting up the Data Stream
--------------------------

.. zmq stream


Accessing the Data
------------------

.. accessing data
To access the offline data, please refer to the `Access <access>`_ section of the documentation.

This will guide you through the steps involved in using AGAVE, SOL, and Globus.
