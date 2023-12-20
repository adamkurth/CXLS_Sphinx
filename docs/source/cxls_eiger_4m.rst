Operation of the Dectris Eiger4M Detector
==========================================

This page contains documentaion for the operation of the Dectris Eiger4M detector. It includes steps for activating the zmq listener, initializing and arming the detector, troubleshooting, and additional resources for handling images and using AGAVE.

Accessing the Dectris Menu
--------------------------

- Open `http://10.139.1.5` in any browser to access the Dectris menu options for the detector.
- Data images will be stored at `http://10.139.1.5/data/`.
- Use `setup.sh` to download these images onto your computer (details provided later in this document).

Steps to Activate zmq Listener
------------------------------

1. Clone the reborn repository:

    .. code-block:: bash

        $ git clone https://gitlab.com/kirianlab/reborn.git

2. Switch to develop branch:

    .. code-block:: bash

        $ git checkout develop

3. Navigate to the correct directory:

    .. code-block:: bash

        $ cd /home/labuser/Projects/Dectris/reborn/developer/rkirian/projects/cxls/dectris/fromzach/DEigerStream

4. Activate `reborn` enviornment:

    .. code-block:: bash

        $ source activate reborn

    - Note that this will activate the `reborn` conda enviornment.
      
5. Run `DEigerStream.py`: This will start the zmq listener, and display menu options for the detector.

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
    
    - Note that this will initialize the detector, and return `true`.

2. Set parameters and enable desired outputs using functions from `setup.sh`:

    - Choose from the options below:

    .. code-block:: bash

        $ enable_monitor
        $ enable_stream
        $ enable_filewriter

    .. code-block:: bash
      
        $ nimages num
        $ frame_time num
        $ count_time num
        $ nimages_per_file num

    - `nimages` sets the number of images collected in a series.
    - `frame_time` sets the frame time (time between readouts or inverse of collection rate).
    - `count_time` sets the exposure time.
    - `nimages_per_file` sets the number of images per file.
    - `enable_monitor` enables the monitor output.
    - `enable_stream` enables the stream output.
    - `enable_filewriter` enables the filewriter output.

    - Replace `num` argument with the desired number, for each function.

3. Able to check the options set using the following functions:

  .. code-block:: bash
      $ get_nimages
      $ get_frame_time
      $ get_count_time

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

2. Source the adapted setup script called `adam_setup.sh` and call the download function to start downloading images from `http://10.139.1.5/data/`:
    
    First, 
  
    .. code-block:: bash

        $ cd /home/labuser/Development/adam/vscode/CXFEL

    Then,

    .. code-block:: bash

        $ source Eiger_Setup.sh
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

  .. code-block:: bash

      $ python test_h5_reading.py

Troubleshooting
---------------

- If encountering module errors, check the modules available in reborn:
  
    .. code-block:: bash

        $ conda list

- Check and make sure that the `reborn` conda enviornment is activated:

    .. code-block:: bash

        $ conda list env

- If a module is not installed, install using:

    .. code-block:: bash

        $ conda install module_name

- Replace `module_name` with the desired module.


Filtering Images
----------------
- Using `filter_nimages`: This function will filter the downloaded images based on the number of images in the series.

  .. code-block:: bash

      $ cd /home/labuser/Development/adam/vscode/CXFEL
      $ source Eiger_Setup.sh

  To show all downloaded images, run the following command:

  .. code-block:: bash

      $ filter_nimages

  Example output:

  .. code-block:: bash

      Found file: series_1_data_000001.h5
      Found file: series_1_data_000002.h5

- Using `filter_master_nimages`: This will show all of the master files from using the detector. 

  To show all master files, run the following command:

  .. code-block:: bash

      $ filter_master_nimages

  Example output:
  
  .. code-block:: bash

      Found file: series_1_master.h5

ALBULA Image Viewer
-------------------

- To view images using the ALBULA image viewer, navigate to the directory containing the images, and run the following command:

  .. code-block:: bash

      $ cd /home/labuser/Development/adam/vscode/CXFEL
      $ source Eiger_Setup.sh

  .. code-block:: bash
        
        $ albula_launch

- This function in `Eiger_Setup.sh` will launch the ALBULA image viewer, and display the images in the `temp_data` directory.

- Note that this function will only work if the `temp_data` directory contains images.

- There is also an option to choose between `master` files and individual `data` files.

ADXV Image Viewer
-----------------

- To view images using the ADXV image viewer, navigate to the directory containing the images, and run the following command:

  .. code-block:: bash

      $ cd /home/labuser/Development/adam/vscode/CXFEL
      $ source Eiger_Setup.sh

  .. code-block:: bash
        
        $ adxv_launch
      
- Through the interactive GUI window, you can select the desired image to view.

Additional Resources
--------------------

Please refer to ::ref:`agave` for additional information and troubleshooting while using AGAVE.
