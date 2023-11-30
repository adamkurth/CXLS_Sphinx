.. CXLS Sphinx documentation master file, created by
   sphinx-quickstart on Wed Nov 22 10:24:38 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to CXLS GitPages documentation!
=======================================


Introduction
------------

By adapting the uses of Reborn repository (https://gitlab.com/kirianlab/reborn), we have created a new repository for CXLS. 
This repository is tailored to the uses at CXLS and gathering and analyzing crystallography data. 
The documentation for Reborn can be found here: https://kirianlab.gitlab.io/reborn/.

This documentation is still under construction and will be updated regularly.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   background_subtraction
   stream_background_subtraction
   overwrite_background_subtraction

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _installation: 

Installation
------------

Example use of code block: 

The installation of CXLS is very simple. You can install it by using pip.

```
pip install cxls
```
If you want to install it in a virtual environment, you can do the following:
.. code-block:: console
    (.venv) $ pip install cxls


.. _reborn:

Documentation for Reborn
-------------------------
The GitLab repository for reborn can be found here: https://gitlab.com/kirianlab/reborn.
The documentation for reborn can be found here: https://kirianlab.gitlab.io/reborn/.


.. _cxls_eiger4m:

Documentation for CXLS Eiger 4M Detector
-----------------------------------------

.. _testing:

Testing Functionalities in Sphinx
---------------------------------

Refer to :doc::`Water Background Subtraction (Overwrite)` for more information.


.. py:function:: ``cxls_eiger4m.read_eiger4m_data(filename, data_type='image')``

   Read Eiger 4M data from a file. The data can be either image or series of images. The data is returned as a numpy array.

   :param filename: The name of the file to be read.
   :type filename: str
   :param data_type: The type of data to be read. The default is 'image'. The other option is 'series'.
   :type data_type: str
   :return: The data read from the file.
   :rtype: numpy.ndarray
