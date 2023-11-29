.. CXLS Sphinx documentation master file, created by
   sphinx-quickstart on Wed Nov 22 10:24:38 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to CXLS GitPages documentation!
=======================================
Through use of reborn repository, we have created a new documentation for CXLS. This documentation is based on Sphinx and ReadTheDocs. The documentation is still under construction and will be updated regularly.
*For use of CXLS Eiger 4M Detector* please refer to the  :doc:`documentation for CXLS Eiger 4M Detector`.

Contents:
---------
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   background_subtraction.rst
   stream_background_subtraction.rst
   overwrite_background_subtraction.rst
   overwrite.rst

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _introduction:

Introduction
============

CXLS is a python package for data analysis of X-ray scattering data. Specially tailored for uses at CXLS, repository . It is based on the python package reborn, tailored to the uses at CXLS. The documentation for reborn can be found here: https://kirianlab.gitlab.io/reborn/.

.. _installation: 

Installation
------------
The installation of CXLS is very simple. You can install it by using pip.
```
pip install cxls
```
If you want to install it in a virtual environment, you can do the following:
.. code-block:: console
    (.venv) $ pip install cxls

.. _usage:

Usage
-----
CXLS is a python package for data analysis of X-ray crystallography experimental data. 

.. _cxls:

Documentation for CXLS
----------------------



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

.. py:function:: ``cxls_eiger4m.read_eiger4m_data(filename, data_type='image')``

   Read Eiger 4M data from a file. The data can be either image or series of images. The data is returned as a numpy array.

   :param filename: The name of the file to be read.
   :type filename: str
   :param data_type: The type of data to be read. The default is 'image'. The other option is 'series'.
   :type data_type: str
   :return: The data read from the file.
   :rtype: numpy.ndarray

.. _development:
