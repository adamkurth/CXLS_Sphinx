RCSB Search API Scripts
=======================

From the official [RCSB Search API](https://search.rcsb.org/#search-api) documentation: `https://github.com/rcsb/py-rcsbsearchapi.git` 

Some quick access to PDB data using the RCSB Search API.

In order to use this script, you need to install the RCSB Search API using `pip`. You can do this by running the following command in your terminal:

.. code-block:: bash

    pip install rcsbsearchapi

Then, you need to clone this repository to your local machine. You can do this by running the following command in your terminal:

.. code-block:: bash

    git clone https://github.com/adamkurth/pdb_rcsb_api_scripts.git

Access PDB IDs
--------------

This is an overview of how to use the script called `scrape.py` that will allow you to access PDB IDs from the RCSB Search API.

- `scrape.py` script is located in the root directory of `pdb_rcsb_api_scripts` repository.

To retrieve PDB IDs, you need to run the following command in your terminal:

    .. code-block:: bash

        python scrape.py -h symmetry --limit limit

    - After running this command, you will see a list of PDB IDs in your terminal. If this PDB symmetry has entries in the RCSB PDB, you will see a list of PDB IDs in your terminal. Otherwise this will show an empty list.

Arguments: 

- `symmetry` argument is the symmetry of the protein you are looking for, `-h monoclinic`.

- `limit` argument is the number of PDB IDs you want to retrieve, for example `--limit 100`.

- You can also use `--help` argument to see the help message.

    This is a quick easy way to access PDB IDs from the RCSB Search API for other programs and scripts.

Downloading PDB Files
---------------------

This is an overview of how to use the script called `download_pdb_files.py` that will allow you to download PDB files from the RCSB Search API.

- `download_pdb_files.py` script is located in the root directory of `pdb_rcsb_api_scripts` repository.

- This script will create a new directory called `pdb_files` in the root directory of `pdb_rcsb_api_scripts` repository, as well as store the PDB files in that directory.

To download PDB files, (much like the `scrape.py` usage) you need to run the following command in your terminal:

    .. code-block:: bash

        python download_pdb_files.py -h symmetry --limit limit


    - After running this command, (like `scrape.py`) you will see a list of PDB IDs in your terminal. If this PDB symmetry has entries in the RCSB PDB, you will see a list of PDB IDs in your terminal. Otherwise this will show an empty list.

    - This script will create a directory named `pdb_files` in the root directory of the `pdb_rcsb_api_scripts` repository. To organize the structure within the newly created directory, for example, `P2221`, the structure will be `pdb_rcsb_api_scripts/P2221/data/ids`. The `ids` directory will contain the PDB files.

Arguments: 

- `symmetry` argument is the symmetry of the protein you are looking for, `-h monoclinic`.

- `limit` argument is the number of PDB IDs you want to retrieve, for example `--limit 100`.

- You can also use `--help` argument to see the help message.


    This is a quick easy way to access PDB IDs and download the files locally from the RCSB PDB for other programs and scripts.

