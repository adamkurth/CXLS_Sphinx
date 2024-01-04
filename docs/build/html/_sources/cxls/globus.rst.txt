Globus File Sharing
====================

Globus is the primary file sharing program used by CXLS. This application is available on the command line, GUI, and web application. It is a command line application as well as a web application. The web application is available at https://www.globus.org/app/transfer. The command line application is available on the CXLS cluster at `/usr/local/bin/globus`.

Before using Globus, you must create an account at https://www.globus.org/. Once you have created an account, you can use the web application or the command line application.

.. code-block:: bash

    $ cd /home/labuser/Public/globusconnectpersonal-3.2.2
    $ ./globusconnectpersonal -setup <your username>

Run Application (with GUI)
---------------------------

To run the application with the GUI, follow these steps:

1. Make sure and `cd` into the directory where the Globus application is located.

2. To start the application, run the following command:

.. code-block:: bash

    $ cd /home/labuser/Public/globusconnectpersonal-3.2.2
    $ ./globusconnectpersonal

3. This will open the GUI for Globus. This will display the current status of the application. Click `Connect` to activate the endpoint.

4. Next please refer to the `Web Application` section for how to use Globus Website.

Run Application (No GUI)
------------------------

To run the application without the GUI, follow these steps:

1. Make sure and `cd` into the directory where the Globus application is located.

2. To start the application, run the following command:

.. code-block:: bash

    $ cd /home/labuser/Public/globusconnectpersonal-3.2.2
    $ ./globusconnectpersonal -start

- Other helpful commands are listed below:

    - To see all the commands, run the following command:

.. code-block:: bash

    $ ./globusconnectpersonal -help

- To start the application in the background, run the following command:

.. code-block:: bash

    $ ./globusconnectpersonal -start &

    
- To deactivate the application, run the following command:

.. code-block:: bash

    $ ./globusconnectpersonal -stop

    
- To check the status of the application, run the following command:

.. code-block:: bash

    $ ./globusconnectpersonal -status   
    
    
- To pause/resume the application, run the following command:

.. code-block:: bash

    $ ./globusconnectpersonal -pause
    
Or 
        
.. code-block:: bash

    $ ./globusconnectpersonal -unpause

    
- To see the version of the application, run the following command:

.. code-block:: bash

    $ ./globusconnectpersonal -version


Globus Setup in Command Line (No GUI)
-------------------------------------

To use Globus without the interactive GUI, follow these steps:

1. Make sure and `cd` into the directory where the Globus application is located.

.. code-block:: bash 

    $ cd /home/labuser/Public/globusconnectpersonal-3.2.2
    $  ./globusconnect -setup --no-gui 

2. After running this command, you will be asked to enter your Globus username and password with a link given in the command line.

3. In the drop-down menu, select the `Arizona State University` option and press continue. 

4. This will navigate you to login using `ASURITE` credentials.

5. After logging in, you will be asked to enter a display name for your Globus account. Enter a display name and press continue.

6. Please make reference to the code in the field. This will be used in future steps. Click continue.

7. You must copy the code given in the field and paste it in the command line to authenticate.

8. After authenticating, then enter the `Endpoint Name`, for example `cxls_guest` and press enter. This is where you will be able to access your Globus account and transfer files.

9. As of now, Globus should be up and running. Please refer to the next section for how to use Globus.


Web Application
---------------

1. Go to https://www.globus.org/globus-connect-personal and click the login button, and login using your Globus credentials.

2. On the left panel, click `Collection` and enter the `Endpoint Name` you created in the previous section. For example, `cxls_guest`.

3. If this is online, the endpoint should be highlighted in green. 

    - If it is not, please restart the Globus application on the command line using the following command.
        
.. code-block:: bash

    $ ./globusconnectpersonal -stop
    $ ./globusconnectpersonal -start &

    - This will start the Globus application in the background while still accessing the currently used terminal window.

4. After the endpoint is highlighted in green, navigate to the directory you want to transfer files from and click the `Start` button.

5. Now in the right panel, navigate to the directory you want to transfer files to and click the `Start` button *ON THE LEFT PANEL*.

    - If you want to transfer files from the right panel to the left panel, click the `Start` button *ON THE RIGHT PANEL*.

    - This will start the transfer process, and you can monitor the progress in the `Activity` tab.

Accessing AGAVE with Globus
---------------------------

1. Refer to the `Web Application` section for how to access the Globus web application.

2. To use AGAVE cluster, then on the left panel, click `Collection` and enter `ASU Data Transfer Node DTN1`.

3. This should immediately activate the endpoint and highlight it in green.

4. Now, navigate to the directory you want to transfer files and select the files you want to transfer.

5. Now in the right panel, navigate to the directory you want to transfer files to and click the `Start` button *ON THE LEFT PANEL*.

    - If you want to transfer files from the right panel to the left panel, click the `Start` button *ON THE RIGHT PANEL*.

    - This will start the transfer process, and you can monitor the progress in the `Activity` tab.