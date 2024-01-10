Submitting SLURM Jobs
======================

This page will provide a brief overview of how to submit jobs using SLURM on the AGAVE supercomputer cluster. 

*Added sections will be added to address SOL supercomputer*

Before running any scripts, make sure you are logged into the ASU network using the `Cisco Secure Client` VPN. From there, you can SSH into the supercomputer using your ASURITE credentials.

*For more information and helpful RC documentaion please refer to.* :doc:`AGAVE <agave>`


AGAVE indexamajig Script
-------------------------

The script is designed to submit jobs to a SLURM workload manager with specific parameters for indexing crystallography data. It creates and submits a job script based on user-provided parameters.

Parameters
----------

- **NAME ($1)**: Input file name or pattern.
- **RUN ($2)**: Base name for the run, used to generate filenames.
- **GEOM ($3)**: Geometry file for the indexing process.
- **STREAMDIR ($4)**: Directory to save the output stream.
- **TASKS ($5)**: Number of tasks to request from SLURM.
- **PARTITION ($6)**: The partition to submit the job to.
- **QOS ($7)**: Quality of Service parameter for the job.
- **HOURS ($8)**: Maximum time for the job (in hours).
- **TAG ($9)**: A tag to append to the run name for identification.

Script Description
------------------

The script performs the following steps:

1. **Prepare Filenames**: Based on the run name and tag, it prepares filenames for the SLURM script, output, and error logs.

2. **SLURM Script Creation**: It creates a new SLURM script file with the necessary SBATCH directives including time, tasks, job name, output, and error file locations.

3. **Command Construction**: It constructs the `indexamajig` command with the provided parameters and some default values for peak finding and indexing.

4. **Job Submission**: Finally, the script submits the job to the SLURM scheduler with the specified partition, QOS, and time limit.

Usage
-----
1. Make sure that the `crystfel` module is loaded on the cluster. This can be done by running the following command:

    .. code-block:: bash

        $ module load crystfel/version
    
    - Replace `version` with the version of `crystfel` you want to use.

    .. code-block:: bash

        $ module load crystfel/0.9.0

2. First navigate to the directory where the script is located.

    .. code-block:: bash

        $ cd ~/Development

3. To use this script, provide the necessary parameters:

    .. code-block:: bash

        ./index-turbo-slurm.sh [NAME] [RUN] [GEOM] [STREAMDIR] [TASKS] [PARTITION] [QOS] [HOURS] [TAG]

    Replace the bracketed items with your actual parameters. Ensure that the script has execute permissions before running.

    .. note:: 
        This script assumes you have a working SLURM environment and the necessary permissions to submit jobs. Adjust the `#SBATCH` options as per your cluster's configuration.

    .. warning:: 
        This script is designed to run on the ASU supercomputer cluster. It may not work on other clusters without modification.

- This provides automated indexing of crystallography data using the `indexamajig` program. It is designed to be used with the `index-turbo-slurm.sh` script.


AGAVE pattern_sim Script
------------------------

The `run_pattern_sim.sh` script is designed to facilitate the submission of simulation jobs to a SLURM workload manager. This script focuses on using `pattern_sim` from CrystFEL, running simulations for pattern generation with specific geometry and crystal parameters.

Usage
-----

Execute the script with the following parameters:

.. code-block:: bash

    ./run_pattern_sim.sh [RUN] [GEOM_FILE] [PDB_FILE] [STREAMDIR] [INTENSITY_FILE] [TASKS] [PARTITION] [QOS] [HOURS] [TAG]

Replace the bracketed items with your actual parameters.

Parameters
----------

- **RUN ($1)**: Base name for the run, used to generate filenames.
- **GEOM_FILE ($2)**: Geometry file for the simulation.
- **PDB_FILE ($3)**: PDB file describing the crystal structure.
- **INTENSITY_FILE ($4)**: File containing intensity information.
- **TASKS ($6)**: Number of tasks to request from SLURM.
- **PARTITION ($6)**: The partition to submit the job to.
- **QOS ($7)**: Quality of Service parameter for the job.
- **HOURS ($8)**: Maximum time for the job (in hours).
- **TAG ($9)**: A tag to append to the run name for identification.

Script Description
------------------

The script performs the following steps:

1. **Prepare Filenames**: Constructs filenames based on the provided run name and tag.

2. **SLURM Script Creation**: Generates a SLURM script with specified SBATCH directives including time, tasks, job name, output, and error file locations.

3. **Command Construction**: Constructs the `pattern_sim` command with provided parameters and additional options for simulation specifics.

4. **Job Submission**: Submits the constructed job to the SLURM scheduler with specified partition, QOS, and time limit.

Key Components
--------------

SLURM Directives
~~~~~~~~~~~~~~~~~

.. code-block:: bash

    #SBATCH --time=0-60:00     # Job Time
    #SBATCH --ntasks=$TASKS    # Number of tasks
    #SBATCH --chdir   $PWD     # Change to current directory
    #SBATCH --job-name  $RUN   # Job Name
    #SBATCH --output    $RUN.out # Output
    #SBATCH --error    $RUN.err  # Error

Command Construction
~~~~~~~~~~~~~~~~~~~~

The script constructs a command to execute `pattern_sim` with various parameters like geometry file, PDB file, intensity file, and other simulation specifics.

.. code-block:: bash

    command="pattern_sim -g $GEOM_FILE -p $PDB_FILE --number=1000 -o $RUN"
    command="$command --intensities=$INTENSITY_FILE --no-noise --really-random --no-fringes"
    
Simulation Options
~~~~~~~~~~~~~~~~~~

Different flags and options can be appended to tailor the simulation, such as `--no-noise`, `--really-random`, and `--no-fringes`.

.. note::
   Modify the script to include or exclude extra options based on the specific needs of your simulation.

.. warning:: 
   Ensure that all the provided files and parameters are correct and accessible before running the script to avoid errors during job submission.

To execute the script, ensure it's correctly set up in your environment with the necessary permissions and SLURM is configured properly. Replace the placeholders with your specific parameters to tailor the simulation to your needs.