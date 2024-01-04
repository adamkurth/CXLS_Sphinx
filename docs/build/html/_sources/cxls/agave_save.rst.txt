AGAVE Access
============

This document provides useful references and step-by-step guidelines for accessing and utilizing the AGAVE supercomputer.

Useful References
-----------------

Here are some useful references for information on AGAVE:

- `AGAVE RC Documentation <https://asurc.atlassian.net/wiki/spaces/RC/pages/46268520/Agave+Supercomputer>`_
- `AGAVE Nodes Information <https://asurc.atlassian.net/wiki/spaces/RC/pages/45875228/Compute+Nodes>`_
- `AGAVE SSH <https://asurc.atlassian.net/wiki/spaces/RC/pages/45318147/Connecting+with+SSHr>`_
- `AGAVE Interactive Session <https://asurc.atlassian.net/wiki/spaces/RC/pages/1643839520/Starting+an+Interactive+Session>`_
- `AGAVE Tutorials <https://asurc.atlassian.net/wiki/spaces/RC/pages/46334137/Tutorials>`_
- `General RC Documentation <https://cores.research.asu.edu/research-computing/getting-started>`_

Prerequisites
-------------

Before accessing AGAVE, ensure the following prerequisites are met:

1. **VPN Connection**:
   - Run `Cisco Secure Client` and login to the ASU network.
   - Under the connect field, enter `sslvpn.asu.edu`.
   - Click connect, and enter your ASURITE credentials, including the Duo Mobile Code for dual-factor authentication.

AGAVE Login Steps
-----------------

Using SSH to access AGAVE supercomputer:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **SSH Login**:
   - Run the following command to log in:
   
   .. code-block:: bash
       
      $ ssh -Y ASURITE@agave.asu.edu
   
   - Replace `ASURITE` with your ASURITE username.
   - Enter your ASURITE password, ensuring `Cisco Secure Client` is running.

2. **Interactive Node**:
   - Once logged in, switch from the login node:
   
   .. code-block:: bash
       
      $ interactive

3. **Activate Conda Environment**:
   - Activate your conda environment:
   
   .. code-block:: bash
       
      $ source /home/ASURITE/anaconda3/bin/activate

Using Web Browser to access AGAVE Virtual Desktop:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Open AGAVE Portal**:
   - Click here to open the AGAVE Web Portal: `AGAVE Web Portal <https://asurc.atlassian.net/wiki/spaces/RC/overview>`_.
   - Navigate to `Agave Web Portal` link on the ASU Research Computing website.

   .. image:: images/agave_web_portal.jpg
      :alt: AGAVE Web Portal
      :width: 500px
      :height: 400px
      :align: center

2. **Start Interactive Session**:
   - Click `Get started with the Agave Web Portal` and navigate to `My Interactive Sessions`.
   - Select `Agave Virtual Desktop` under `Interactive Apps`.
   - Fill out the fields `Partition`, `QOS`, `Cores`, `Session Wall Time`, and click `Launch`.
   - Once resources are ready, click the `Launch Agave Virtual Desktop` button.

Loading Modules
---------------

1. **Check Available Modules**:
   - Run the following to list all available modules:
   
   .. code-block:: bash
       
      $ module -l avail

2. **Load Modules**:
   - Load a specific module:
   
   .. code-block:: bash
       
      $ module load module_name/version_number

3. **View Loaded Modules**:
   - Check currently loaded modules:
   
   .. code-block:: bash
       
      $ module list

4. **Unload Modules**:
   - Unload a specific module:
   
   .. code-block:: bash
       
      $ module unload module_name/version_number
   - Unload all modules:
   
   .. code-block:: bash
       
      $ module purge

Partitions at AGAVE
-------------------

Before submitting jobs, understand the partitions available:

1. **Check Partition Status**:
   - For a specific partition:
   
   .. code-block:: bash
       
      $ sinfo -p partition_name
   - For all partitions:
   
   .. code-block:: bash
       
      $ sinfo -a

2. **Monitor Jobs**:
   - Watch a specific job:
   
   .. code-block:: bash
       
      $ squeue -j job_id
   - Watch all your jobs:
   
   .. code-block:: bash
       
      $ watch 'squeue -u ASURITE'

Running `pattern_sim` through CrystFEL
--------------------------------------

Ensure you're logged into AGAVE and have loaded the `crystfel` module.

**Access and Execution**:

- Access the script at `/home/ASURITE/Development/run_pattern_sim.sh`.
- Run `pattern_sim` through CrystFEL using `run_pattern_sim.sh`.

**Arguments**:

- `RUN`: Run name (e.g., `sim_run1`).
- `GEOM_FILE`: Path to the geometry file.
- `PDB_FILE`: Path to the PDB file.
- `INTENSITY_FILE`: Path to the intensity file.
- `TASKS`: Number of tasks.
- `PARTITION`: Partition name.
- `QOS`: Quality of service.
- `TIME`: Time limit.
- `TAG`: Job tag.

**Run the Script**:

.. code-block:: bash

   $ ./run_pattern_sim.sh RUN GEOM_FILE PDB_FILE INTENSITY_FILE TASKS PARTITION QOS TIME TAG

Indexing Images `indexamajig` through CrystFEL
----------------------------------------------

Ensure you're logged into AGAVE and have loaded the `crystfel` module.

**Preparation**:

1. Verify `.h5` files from `pattern_sim`.
2. Create a list of images to index:
   
   .. code-block:: bash
       
      $ ls /path/to/h5/files/*.h5 > my_images.list

3. Load necessary modules (`ccp4` and `crystfel`).

**Indexing**:

- Index images using `indexamajig`:
  
  .. code-block:: bash
       
     $ indexamajig -i my_images.list -o output.stream -g geom_file.geom --additional-options

Refer to `SLURM Scripts <slurm_script>` for more information on submitting jobs.

.. note::
   Adjust arguments as necessary and refer to CrystFEL documentation for detailed usage.
