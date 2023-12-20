.. _agave-access:

Agave Access
============

To access the supercomputer using Agave, follow these steps:

Prerequisites
-------------
1. Make sure to run `Cisco Secure Client` and login to ASU network before running the following commands.

2. Under the connect field, make sure `sslvpn.asu.edu` is entered.

3. Click connect, and enter your ASURITE credentials;
   
    - ASURITE username and password, and Duo Mobile Code for dual-factor authentication.

4. Click connect, and when connected, follow the next steps to access AGAVE supercomputer.

Login Steps
------------

1. Once logged in, make sure and get off of the login node by running the following command:

    .. code-block:: bash

        $ interactive

2. Now to activate conda environment, run the following command:
    
    - replace `username` with your ASURITE username.
    
    .. code-block:: bash

        $ source /home/username/anaconda3/bin/activate

Loading Modules
----------------
1. To check which modules are available, run the following command:

    .. code-block:: bash

        $ module -l avail

    Note this is not a particularly fast command, and will take some time.

2. To load modules, run the following command:
    
        .. code-block:: bash
    
            $ module load module_name/version_number
    
        Replace `module_name` with the name of the module you want to load.

        For example, to load the `crystfel` module verion `0.9.0`, run the following command:

        .. code-block:: bash

            $ module load crystfel/0.9.0

3. To view the currently loaded modules, run the following command:

    .. code-block:: bash

        $ module list

4. To unload a module, run the following command:
    
        .. code-block:: bash
    
            $ module unload module_name/version_number
    
        Replace `module_name` with the name of the module you want to unload.

        For example, to unload the `crystfel` module verion `0.9.0`, run the following command:

        .. code-block:: bash

            $ module unload crystfel/0.9.0

5. To unload all modules, run the following command:

    .. code-block:: bash

        $ module purge

Submitting Jobs
---------------

Before submitting jobs, here is the information about how to find the partition to run your jobs:

- To check the status of a particular partition, run the following command:

.. code-block:: bash

    $ sinfo

- To check the status of all partitions, run the following command:

.. code-block:: bash

    $ sinfo -a

- To check the status of a particular partition, run the following command:

.. code-block:: bash

    $ sinfo -p partition_name

Replace `partition_name` with the name of the partition you want to check.

- To change the output to only partitions, run the following command:

.. code-block:: bash

    $ sinfo -h --format="%P"

Equivalently, you can run the following command:

.. code-block:: bash

    $ sinfo -o "%P"

- To check the status of all partitions, run the following command:

.. code-block:: bash

    $ sinfo -a

- To watch a job, run the following command:

.. coe-block:: bash

    $ squeue -j job_id
 
Or to watch all jobs make sure to replace `username`, run the following command:

.. code-block:: bash

    $ watch 'squeue -u username'

Running `pattern_sim` through CrystFEL
--------------------------------------

ACCESS PATTERN_SIM FILE FOR USERS????

- How to run `pattern_sim` through CrystFEL through custom script: 

    Using the script called `run_pattern_sim.sh`, you can run `pattern_sim` through CrystFEL. The script is located in the following directory: `/home/username/Development/run_pattern_sim.sh`.

    Here are the arguments for the script:

    - `RUN=$1`: is the run name, for example `sim_run1`.

    - `GEOM_FILE=$2`: is the path to the geometry file, for CXFEL this will correspond to the Eiger4M .geom file (`Eiger4M.geom`). Make sure this file is in the same directory as the `run_pattern_sim` script.

    - `PDB_FILE=$3`: is the path to the pdb file, for example `1vds.pdb`. Make sure this file is in the same directory as the `run_pattern_sim` script.

    - `INTENSITY_FILE=$4`: is the path to the intensity file, for example `1vds.pdb.hkl`. Make sure this file is in the same directory as the `run_pattern_sim` script.

    - `TASKS=$5`: is the number of tasks to run, for example `10`.

    - `PARTITION=$6`: is the partition to run the job on, for example `gpu`.

    - `QOS=$7`: is the quality of service, for example `wildfire`.

    - `TIME=$8`: is the time limit for the job, for example `4`.

    - `TAG=$9`: is the tag for the job, for example `sim_run1`.

    To adjust the pattern_sim arguments to CrystFEL, please edit the `run_pattern_sim.sh` script, please add comment.

- All together, the command to run the script is as follows:

    .. code-block:: bash

        $ ./run_pattern_sim.sh RUN GEOM_FILE PDB_FILE INTENSITY_FILE TASKS PARTITION QOS TIME TAG

    Replace `RUN`, `GEOM_FILE`, `PDB_FILE`, `INTENSITY_FILE`, `TASKS`, `PARTITION`, `QOS`, `TIME`, and `TAG` with the appropriate values.

    .. code-block:: bash

        $ ./run_pattern_sim.sh sim_run1 Eiger4M.geom 1vds.pdb 1vds.pdb.hkl 10 gpu wildfire 4 sim_run1


Indexing Images through CrystFEL
--------------------------------

1. Check the outputted `.h5` files from `pattern_sim` to make sure they are correct.

2. Run the following to create a list of images to index:

    .. code-block:: bash

        $ ls /home/amkurth/Development/pattern_simulations/9_18_23_high_intensity/*.h5 > high_intensity.list

3. Ensure that the pipe operator worked as desired by running the following command:

    .. code-block:: bash

        $ less high_intensity.list

4. Load CCP4 and CrystFEL modules by running the following commands:

    .. code-block:: bash

        $ module load ccp4/7.0.077
        $ module load crystfel/0.9.0

5. Finally, index the list of images by running the following command:

    .. code-block:: bash

        $ indexamajig -i low_intensity.list -o index_test_low/test_low.stream -g Eiger4M.geom --peaks=peakfinder8 --threshold=200 --min-snr=8.0 --min-pix-count=1 --min-peaks=8 --min-res=50 --int-rad=2,4,6 --indexing=mosflm  --pdb=1vds.pdb --multi --check-peaks 

    - Adjust arguments as desired. For more information on the arguments, refer to the CrystFEL documentation at https://www.desy.de/~twhite/crystfel/manual.html#indexamajig.

6. Check the outputted `.stream` file in the workind directory, to make sure it is correct.

