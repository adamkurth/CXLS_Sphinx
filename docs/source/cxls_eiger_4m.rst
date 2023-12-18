Dectris-Eiger4M
===============

This page contains documentaion for the operation of the Dectris Eiger4M detector. It includes steps for activating the zmq listener, initializing and arming the detector, troubleshooting, and additional resources for handling images and using AGAVE.

Setup and Operation
===================

Accessing the Dectris Menu
--------------------------

- Open `http://10.139.1.5` in any browser to access the Dectris menu options for the detector.
- Data images will be stored at `http://10.139.1.5/data/`.
- Use `setup.sh` to download these images onto your computer (details provided later in this document).

Activate zmq Listener
---------------------

0. If not done already, please clone the reborn repository `https://gitlab.com/kirianlab/reborn.git`.

Steps
-----
1. Switch to develop branch:

    .. code-block:: bash

        $ git checkout develop

2. Navigate to the correct directory:

    .. code-block:: bash

        $ cd /home/labuser/Projects/Dectris/reborn/developer/rkirian/projects/cxls/dectris/fromzach/DEigerStream

3. Activate `reborn` enviornment:

    .. code-block:: bash

        $ source activate reborn

    - Note that this will activate the `reborn` conda enviornment.
      
4. Run `DEigerStream.py`: This will start the zmq listener, and display menu options for the detector.

    .. code-block:: bash

        $ python DEigerStream.py -i 10.139.1.5 -f junk.log

    - Usually best to isolate this window in a separate terminal window.

    - The `-i` flag specifies the IP address of the detector.

    - The `-f` flag specifies the name of the log file.   
    
    - If desired, to exit the zmq listener, press `Ctrl+C`.


Initializing and Arming
-----------------------

Next, initialize and arm the detector. This will allow you to control the detector using the zmq listener.

1. Source `setup.sh` to use simplified commands like initialize, arm, disarm, etc.:
    
    .. code-block:: bash

        $ source setup.sh
        $ initialize

2. Set parameters and enable desired outputs using functions from `setup.sh`:

    .. code-block:: bash

        $ set_nimages num
        $ set_frame_time num
        $ set_count_time num
        $ set_nimages_per_file num
        $ enable_monitor
        $ enable_stream
        $ enable_filewriter

    - `set_nimages` sets the number of images to be taken.
    - `set_frame_time` sets the frame time.
    - `set_count_time` sets the count time.
    - `set_nimages_per_file` sets the number of images per file.
    - `enable_monitor` enables the monitor output.
    - `enable_stream` enables the stream output.
    - `enable_filewriter` enables the filewriter output.

3. Control the detector:
  .. code-block:: bash
      $ arm
      $ disarm
      $ trigger

Downloading and Overwrite Images
--------------------------------

1. Navigate to the desired directory to store images:
    .. code-block:: bash

        $ cd /home/labuser/Projects/Dectris/test/temp_data

    - Note that this will download all images listed on `http://10.139.1.5/data/`.

2. Source `setup.sh` and call the download function to start downloading images from `http://10.139.1.5/data/`:
    
    .. code-block:: bash

        $ source setup.sh
        $ download_images_from_IP

Viewing HDF5 Images Through Reborn
----------------------------------

1. Navigate to the recent downloaded images directory:

  .. code-block:: bash
      
      $ cd /home/labuser/Projects/Dectris/test/temp_data
  
2. Export the Python path:
  
    .. code-block:: bash

      $ export PYTHONPATH=/home/labuser/Projects/Dectris/reborn/developer/rkirian/projects/cxls/dectris/fromzach/DEigerStream:$PYTHONPATH

3. Run `test_h5_reading.py` or any other Python file:
    python test_h5_reading.py

Troubleshooting
---------------

- If encountering module errors, check the modules available in reborn:
  conda list

- If a module is not installed, install using:
  conda install <modulename>

Using AGAVE
-----------

Steps
-----

1. On startup in AGAVE, get off the interactive node for computationally intensive tasks:
    interactive

2. Activate conda enviornment
    source /home/<username>/anaconda3/bin/activate

3. Manage modules in AGAVE:
    - Check available modules:
      module -l avail

    - Load a module:
      module load <module load>/<version number>

    - Check loaded modules:
      module list

    - Unload all modules
      module purge

Working with Slurm in AGAVE
---------------------------

- Find partitions:
  sinfo

- Select output of only partition names:
  sinfo -h --format="%P"

- Get detailed information of a specific partition:
  sinfo -p <partition_name>

- Watch tasks:
  watch 'squeue -u <username>'

Additional Notes
----------------

- Ensure you are following the specific protocols and safety measures associated with operating the Eiger4M detector.
- this README is general guide, specific steps may vary.
