RCSB Search API Scripts
=======================

The RCSB Search API Scripts provide a convenient way to interact with the RCSB Search API, allowing users to search and download PDB files based on specific criteria.

Official Documentation
----------------------

For more information about the RCSB Search API, visit the official documentation: `RCSB Search API <https://github.com/rcsb/py-rcsbsearchapi.git>`_.

Installation and Setup
----------------------

1. **Install RCSB Search API**:

    Install the RCSB Search API using pip:

    .. code-block:: bash

        pip install rcsbsearchapi

2. **Clone the Repository**:

    Clone the PDB RCSB API Scripts repository to your local machine:

    .. code-block:: bash

        git clone https://github.com/adamkurth/pdb_rcsb_api_scripts.git

    Repository Link: `PDB RCSB API Repo <https://github.com/adamkurth/pdb_rcsb_api_scripts.git>`_

Accessing PDB IDs using `scrape.py`
-----------------------------------

The `scrape.py` script, located in the root directory of the `pdb_rcsb_api_scripts` repository, is used to retrieve PDB IDs from the RCSB Search API.

**Usage**:

Run the script with the desired symmetry and limit:

.. code-block:: bash

    python scrape.py -h symmetry --limit limit

**Arguments**:

- **symmetry**: Symmetry of the protein (e.g., `-h monoclinic`).
- **limit**: Number of PDB IDs to retrieve (e.g., `--limit 100`).

**Script Overview**:

The script utilizes several classes and functions from the `rcsbsearchapi` package to perform queries and handle results:

.. code-block:: python

    from rcsbsearchapi import AttributeQuery, STRUCTURE_ATTRIBUTE_SEARCH_SERVICE
    import argparse
    from rcsbsearchapi.search import TextQuery, AttributeQuery, SequenceQuery, SeqMotifQuery, StructSimilarityQuery, Attr
    from rcsbsearchapi import rcsb_attributes as attrs
    from rcsbsearchapi.const import STRUCTURE_ATTRIBUTE_SEARCH_SERVICE
    import argparse
    # From rcsbsearchapi 
    # comment and add as needed, for reference check the quickstart.ipynb in rcsbsearchapi repo 

    def get_pdb_ids(space_group, str_type, limit=50):
        # By default, service is set to "text" for structural attribute search
        q1 = AttributeQuery("symmetry.cell_setting", "exact_match", str_type, STRUCTURE_ATTRIBUTE_SEARCH_SERVICE)
        q2 = AttributeQuery("symmetry.space_group_name_H_M", "exact_match", space_group, STRUCTURE_ATTRIBUTE_SEARCH_SERVICE)
        query = q2  # combining queries use & | operators
        pdb_ids = list(query())
        pdb_lim = truncate(pdb_ids, limit)
        print(f"From search: {space_group} \n", pdb_lim)
        return pdb_lim

    def truncate(pdb_ids, limit):
        if len(pdb_ids) > limit:
            pdb_ids = pdb_ids[:limit]
        return pdb_ids


    def interactive_script():
        parser = argparse.ArgumentParser(description='Download PDB files based on symmetry and space group.')
        parser.add_argument('symmetry_shape', type=str, help='Crystal symmetry to list space groups for')
        parser.add_argument('--limit', type=int, default=50, help='Limit number of PDB files to download (default: 50)')
        
        args, _ = parser.parse_known_args()
        
        symmetry_shape = args.symmetry_shape
        symmetry_shape = symmetry_shape.lower()
        limit = args.limit
            
        space_groups = {
            # Additional space groups from International Tables for Crystallography (ITC)
            "cubic": ["P 2 3", "F 2 3", "I 2 3", "P 21 3", "I 21 3", "P 4 3 2", "P 42 3 2", "F 4 3 2", "F 41 3 2", "I 4 3 2", "P 43 3 2", "P 41 3 2", "I 41 3 2", "P 42 3 2", "I 42 3 2", "F 43 3 2", "F 41 3 2", "I 43 3 2", "P 4 3 3", "F 4 3 3", "I 4 3 3", "P 41 3 3", "I 41 3 3", "P 42 3 3", "I 42 3 3", "P 43 3 3", "I 43 3 3"],
            "tetragonal": ["P 4 2 2", "P 42 2 2", "P 4 21 2", "P 41 2 2", "P 41 21 2", "P 42 21 2", "I 4 2 2", "I 41 2 2", "P 4 2 3", "P 42 2 3", "F 4 2 3", "F 41 2 3", "I 4 2 3", "P 43 2 3", "P 41 2 3", "I 41 2 3", "P 42 2 3", "I 42 2 3", "F 43 2 3", "F 41 2 3", "I 43 2 3"],
            "orthorhombic": ["P 2 2 2", "P 2 2 21", "P 2 21 2", "P 21 2 2", "P 21 2 21", "P 21 21 2", "P 21 21 21", "C 2 2 21", "C 2 2 2", "F 2 2 2", "I 2 2 2", "P 2 2 2 1", "P 2 2 21 1", "P 2 21 2 1", "P 21 2 2 1", "P 21 2 21 1", "P 21 21 2 1", "P 21 21 21 1", "C 2 2 21 1", "C 2 2 2 1", "F 2 2 2 1", "I 2 2 2 1"],
            "hexagonal": ["P 3", "P 31", "P 32", "P 3 1 2", "P 3 2 1", "R 3", "R 3 2", "P -3", "P 3*", "P 31*", "P 32*", "R 3*", "R 3 2*", "P -3*", "R -3", "R -3 2", "P 3 1 21", "P 3 21 1", "P 31 1 2", "P 31 2 1", "P 32 1 2", "P 32 2 1", "P 6", "P 61", "P 65", "P 62", "P 64", "P 63", "P 6 1 22", "P 6 5 22", "P 6 2 22", "P 6 4 22", "P 6 3 22", "P 6 1 2 1", "P 6 5 2 1", "P 6 2 2 1", "P 6 4 2 1", "P 6 3 2 1"],
            "trigonal": ["P 3", "P 31", "P 32", "P 3 1 2", "P 3 2 1", "R 3", "R 3 2", "P -3", "P 3*", "P 31*", "P 32*", "R 3*", "R 3 2*", "P -3*", "R -3", "R -3 2", "P 3 1 21", "P 3 21 1", "P 31 1 2", "P 31 2 1", "P 32 1 2", "P 32 2 1", "P 3 1 2 1", "P 3 2 1 1", "R 3 2 1", "P 3 1 21 1", "P 3 21 1 1", "P 31 1 2 1", "P 31 2 1 1", "P 32 1 2 1", "P 32 2 1 1", "P 3 1 2 1 1", "P 3 2 1 1 1", "R 3 2 1 1"],
            "monoclinic": ["P 2 1", "P 21", "C 2 2", "P 2 2 21", "P 2 21 2", "P 21 2 2", "P 21 21 2", "P 21 21 21", "C 2 2 21", "C 2 2 2", "I 2 2 2", "P 2 2 2 1", "P 2 2 21 1", "P 2 21 2 1", "P 21 2 2 1", "P 21 2 21 1", "P 21 21 2 1", "P 21 21 21 1", "C 2 2 21 1", "C 2 2 2 1", "I 2 2 2 1"],
            "triclinic": ["P 1", "P -1", "P 1 1 2", "P 1 1 21", "P 1 21 1", "P 21 1 1", "P 1 21 21", "P 21 1 21", "P 21 21 1", "P 1 1 2 1", "P 1 1 21 1", "P 1 21 1 1", "P 21 1 1 1", "P 1 21 21 1", "P 21 1 21 1", "P 21 21 1 1", "P 1 1 2 1 1", "P 1 1 21 1 1", "P 1 21 1 1 1", "P 21 1 1 1 1", "P 1 21 21 1 1", "P 21 1 21 1 1", "P 21 21 1 1 1"],
        }
        
        # Check if the symmetry_shape is valid and list possible space groups
        if symmetry_shape in space_groups:
            print(f"Select a space group for symmetry shape '{symmetry_shape}':")
            for idx, sg in enumerate(space_groups[symmetry_shape], 1):
                print(f"{idx}. {sg}")
            
            # Prompt the user to select a space group
            sg_choice = int(input("Enter the number of your chosen space group: "))
            if 1 <= sg_choice <= len(space_groups[symmetry_shape]):
                selected_space_group = space_groups[symmetry_shape][sg_choice - 1]
                print(f"You have selected space group '{selected_space_group}'.")
                print(f"Retrieving up to {limit} PDB IDs for space group '{selected_space_group}'...")
                
                # Retrieve and print PDB IDs for the selected space group
                ids = get_pdb_ids(selected_space_group, symmetry_shape, limit)
            else:
                print("Invalid choice. Please run the script again and select a valid number.")
        else:
            print(f"Invalid symmetry shape '{symmetry_shape}'. Please run the script again with a valid symmetry shape.")

    if __name__ == "__main__":
        interactive_script()

**Functions**:

- **get_pdb_ids()**: Retrieves PDB IDs based on space group and structure type.
- **truncate()**: Limits the number of PDB IDs to the specified limit.
- **interactive_script()**: Provides an interactive command-line interface for the user.

Downloading PDB Files using `download_pdb_files.py`
---------------------------------------------------

The `download_pdb_files.py` script allows users to download PDB files based on specified criteria.

**Usage**:

Run the script with the desired symmetry and limit:

.. code-block:: bash

    python download_pdb_files.py -h symmetry --limit limit

**Script Overview**:

This script creates a directory named `pdb_files` in the root directory of the `pdb_rcsb_api_scripts` repository and organizes downloaded PDB files.

.. code-block:: python

    import requests
    import os
    import argparse
    from scrape import get_pdb_ids  # Import the function from scrape.py

    class ProteinDownloader:
        """Class to download PDB files for specified proteins."""
        
        def __init__(self, base_dir=None):
            """Initialize ProteinDownloader class."""
            self.base_dir = base_dir or os.getcwd()

        def is_url_accessible(self, url):
            """Check if a URL is accessible."""
            response = requests.head(url)
            return response.status_code == 200

        def download_files(self, protein_ids, space_group):
            """Download PDB files for specified proteins, organized by space group."""
            formatted_space_group = space_group.replace(" ", "")  # remove spaces
            target_dir = os.path.join(self.base_dir, f"{formatted_space_group}/data/ids")
            os.makedirs(target_dir, exist_ok=True)  # Create directory structure
            
            PDB_URL_TEMPLATE = "https://files.rcsb.org/download/{}.pdb"
            
            for protein_id in protein_ids:
                print(f"Processing Protein: {protein_id}, Space Group: {formatted_space_group}")
                pdb_url = PDB_URL_TEMPLATE.format(protein_id)
                
                if self.is_url_accessible(pdb_url):
                    response = requests.get(pdb_url)
                    with open(os.path.join(target_dir, f"{protein_id}.pdb"), 'wb') as file:
                        file.write(response.content)
                else:
                    print(f"URL not accessible for Protein ID: {protein_id}")
                    
    def main():
        parser = argparse.ArgumentParser(description='Download PDB files based on space group and symmetry.')
        parser.add_argument('symmetry_shape', type=str, help='Crystal symmetry to list space groups for')
        parser.add_argument('--limit', type=int, default=50, help='Limit number of PDB files to download')
        parser.add_argument('--base_dir', type=str, default=os.getcwd(), help='Base directory to save PDB files to')    
        args = parser.parse_args()
        
        space_groups = {
            # Additional space groups from International Tables for Crystallography (ITC)
            "cubic": ["P 2 3", "F 2 3", "I 2 3", "P 21 3", "I 21 3", "P 4 3 2", "P 42 3 2", "F 4 3 2", "F 41 3 2", "I 4 3 2", "P 43 3 2", "P 41 3 2", "I 41 3 2", "P 42 3 2", "I 42 3 2", "F 43 3 2", "F 41 3 2", "I 43 3 2", "P 4 3 3", "F 4 3 3", "I 4 3 3", "P 41 3 3", "I 41 3 3", "P 42 3 3", "I 42 3 3", "P 43 3 3", "I 43 3 3"],
            "tetragonal": ["P 4 2 2", "P 42 2 2", "P 4 21 2", "P 41 2 2", "P 41 21 2", "P 42 21 2", "I 4 2 2", "I 41 2 2", "P 4 2 3", "P 42 2 3", "F 4 2 3", "F 41 2 3", "I 4 2 3", "P 43 2 3", "P 41 2 3", "I 41 2 3", "P 42 2 3", "I 42 2 3", "F 43 2 3", "F 41 2 3", "I 43 2 3"],
            "orthorhombic": ["P 2 2 2", "P 2 2 21", "P 2 21 2", "P 21 2 2", "P 21 2 21", "P 21 21 2", "P 21 21 21", "C 2 2 21", "C 2 2 2", "F 2 2 2", "I 2 2 2", "P 2 2 2 1", "P 2 2 21 1", "P 2 21 2 1", "P 21 2 2 1", "P 21 2 21 1", "P 21 21 2 1", "P 21 21 21 1", "C 2 2 21 1", "C 2 2 2 1", "F 2 2 2 1", "I 2 2 2 1"],
            "hexagonal": ["P 3", "P 31", "P 32", "P 3 1 2", "P 3 2 1", "R 3", "R 3 2", "P -3", "P 3*", "P 31*", "P 32*", "R 3*", "R 3 2*", "P -3*", "R -3", "R -3 2", "P 3 1 21", "P 3 21 1", "P 31 1 2", "P 31 2 1", "P 32 1 2", "P 32 2 1", "P 6", "P 61", "P 65", "P 62", "P 64", "P 63", "P 6 1 22", "P 6 5 22", "P 6 2 22", "P 6 4 22", "P 6 3 22", "P 6 1 2 1", "P 6 5 2 1", "P 6 2 2 1", "P 6 4 2 1", "P 6 3 2 1"],
            "trigonal": ["P 3", "P 31", "P 32", "P 3 1 2", "P 3 2 1", "R 3", "R 3 2", "P -3", "P 3*", "P 31*", "P 32*", "R 3*", "R 3 2*", "P -3*", "R -3", "R -3 2", "P 3 1 21", "P 3 21 1", "P 31 1 2", "P 31 2 1", "P 32 1 2", "P 32 2 1", "P 3 1 2 1", "P 3 2 1 1", "R 3 2 1", "P 3 1 21 1", "P 3 21 1 1", "P 31 1 2 1", "P 31 2 1 1", "P 32 1 2 1", "P 32 2 1 1", "P 3 1 2 1 1", "P 3 2 1 1 1", "R 3 2 1 1"],
            "monoclinic": ["P 2 1", "P 21", "C 2 2", "P 2 2 21", "P 2 21 2", "P 21 2 2", "P 21 21 2", "P 21 21 21", "C 2 2 21", "C 2 2 2", "I 2 2 2", "P 2 2 2 1", "P 2 2 21 1", "P 2 21 2 1", "P 21 2 2 1", "P 21 2 21 1", "P 21 21 2 1", "P 21 21 21 1", "C 2 2 21 1", "C 2 2 2 1", "I 2 2 2 1"],
            "triclinic": ["P 1", "P -1", "P 1 1 2", "P 1 1 21", "P 1 21 1", "P 21 1 1", "P 1 21 21", "P 21 1 21", "P 21 21 1", "P 1 1 2 1", "P 1 1 21 1", "P 1 21 1 1", "P 21 1 1 1", "P 1 21 21 1", "P 21 1 21 1", "P 21 21 1 1", "P 1 1 2 1 1", "P 1 1 21 1 1", "P 1 21 1 1 1", "P 21 1 1 1 1", "P 1 21 21 1 1", "P 21 1 21 1 1", "P 21 21 1 1 1"],
        } 
        
        if args.symmetry_shape in space_groups:
            print(f"Select a space group for symmetry shape '{args.symmetry_shape}':")
            for idx, sg in enumerate(space_groups[args.symmetry_shape], 1):
                print(f"{idx}. {sg}")
            
            sg_choice = int(input("Enter the number of your chosen space group: "))
            if 1 <= sg_choice <= len(space_groups[args.symmetry_shape]):
                selected_space_group = space_groups[args.symmetry_shape][sg_choice - 1]
                print(f"You have selected space group '{selected_space_group}'.")
                print(f"Retrieving up to {args.limit} PDB IDs for space group '{selected_space_group}'...")
                
                pdb_ids = get_pdb_ids(selected_space_group, args.symmetry_shape, args.limit)
                
                downloader = ProteinDownloader(args.base_dir)
                downloader.download_files(pdb_ids, selected_space_group)
            else:
                print("Invalid choice. Please run the script again and select a valid number.")
        else:
            print(f"Invalid symmetry shape '{args.symmetry_shape}'. Available options are: {', '.join(space_groups.keys())}")

    if __name__ == "__main__":
        main()

**Functions**:

- **ProteinDownloader**: A class to manage the download and organization of PDB files.
- **is_url_accessible()**: Checks if the PDB file URL is accessible.
- **download_files()**: Downloads and organizes PDB files into the specified directory.

**How to Use**:

1. Run the script with the desired symmetry and limit.
2. PDB files will be downloaded and organized in the `pdb_files` directory under the specified space group.

**Space Groups**:

The script includes a comprehensive list of space groups for various crystal symmetries. Users can select the desired space group to narrow down their search.

**Conclusion**:

These scripts offer a user-friendly way to access and download PDB files from the RCSB PDB database, streamlining the process for researchers and developers working in the field of structural biology and crystallography.
