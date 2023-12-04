Water Background Subtraction (Overwrite)
===========================================

This module contains the adaptation of the previous background subtraction programs, and is called `overwrite_10_2_23.py` in the Git repositories.

The rational behind this is to take two stream files, one with "high" keV values and one with "low" keV values, and analyze their respective `.stream` files.
The program will then take the background from the "low" keV stream file and overwrite the background in the "high" keV stream file.

The program will then "overwrite" the "low" keV stream file, as the "high" keV stream, with the new more accurate peak values.

Please refer to :doc:`stream_background_subtraction` for information about the foundational coding structure.

The GitHub repository for this project can be found at: 
    - https://github.com/adamkurth/waterbackground_subtraction.git
    - https://gitlab.com/amkurth/waterbackground_subtraction.git.
 
Imports
^^^^^^^

Most notably, we inherit the `h5_stream_background_subtraction_10_2_23.py` program, to simplify the code. 

We also import `os`, `shutil`, `numpy`, and `h5py` as `h5`.

.. code-block:: python
    
    import os
    import shutil
    import numpy as np
    import h5py as h5
    import h5_stream_background_subtraction_10_2_23 as streampy

Duplicate Function
^^^^^^^^^^^^^^^^^^

To compare the two stream files before and after the the overwrite process, we need to duplicate the stream files.

We do this by using the `shutil.copyfile()` function, which takes two arguments, the source file and the destination file.

.. py:function:: duplicate_before_overwrite(filename):

    Duplicates a file by creating a copy with a modified name.

    :param filename: The name of the file to duplicate.
    :type filename: str

    :return: The path of the duplicated file.
    :rtype: str

    .. code-block:: python

        def duplicate_before_overwrite(filename):
            # taking filename and adding copy extension to it.
            base_file, extension = filename.rsplit('.',1)
            new_base_file = f'{base_file}_copy'
            new_filename = f'{new_base_file}.{extension}'
            duplicate = shutil.copyfile(filename, new_filename)
            return duplicate


Debugging Functions
^^^^^^^^^^^^^^^^^^^

- `compare_high_low()` is used to compare the two stream file contents to ensure that they're loaded and read properly. 

- `retrieve()` is used to retrieve the columns of data to retrieve, and append to a list.

.. py:function:: compare_high_low(high_data, low_data, *columns)

    Compare the high and low data and return the compared data.

    :param high_data: The high keV file to compare.
    :type high_data: dict
    :param low_data: The low keV file to compare.
    :type low_data: dict
    :option columns: The columns desired to be compared.
    :type columns: str

    :return: The columns desired to be compared.
    :rtype: dict

    .. code-block:: python

        def compare_high_low(high_data, low_data, *columns):
            """
            Compare the high and low data and return the compared data.
            """
            compared_data = {}
            for col in columns:
                if col in high_data and col in low_data:
                    print(f'High: {high_data[col]} \n')
                    print(f'Low: {low_data[col]} \n')
                    print()
                    compared_data[col] = (high_data[col], low_data[col])
                    retrieve(list(high_data), list(low_data), *columns)
            return compared_data

This function directly appends certain columns in `data_columns` for ease of use and debugging purposes.

.. py:function:: retrieve(data_columns, *args)

    Retrieve the columns of data to retrieve.

    :param data_columns: The columns of data to retrieve.
    :type data_columns: dict
    :param args: Takes the desired columns to be retrieved, appends to list. 
    :type args: list

    :return: The columns of data to retrieve.
    :rtype: list

    .. code-block:: python

        def retrieve(data_columns, *args):
            result = []
            try:
                # taking in data_columns and selecting the desired columns to retrieve
                result = [data_columns[col] for col in args if col in data_columns]
            except Exception as e:
                pass
            return result
    

Overwrite Function
^^^^^^^^^^^^^^^^^^

This function executes the overwriting procedure of the "high" keV stream file with the "low" keV stream file.

.. py:function:: overwrite_low_in_high(filename, overwrite_data)

    Overwrite the low data in the high stream file with the given overwrite data.

    :param filename: The name of the file to overwrite.
    :type filename: str
    :param overwrite_data: A dictionary containing the data to overwrite.
    :type overwrite_data: dict

    :return: None

    .. code-block::python

        def overwrite_low_in_high(filename, overwrite_data):
        """
        Overwrite the low data in the high stream file with the given overwrite data.
        """
        with open(filename, 'r') as f:
            lines = f.readlines()

        with open(filename, 'r+') as f:
            for line in lines:
                if line.startswith("   h    k    l          I   sigma(I)       peak background  fs/px  ss/px panel"):
                    f.write(line)
                    for i in range(len(overwrite_data['h'])):
                        formatted_row = '{:>4} {:>4} {:>4} {:>9} {:>12} {:>12} {:>12} {:>6} {:>6} {:>6}\n'.format(
                            overwrite_data['h'][i],
                            overwrite_data['k'][i],
                            overwrite_data['l'][i],
                            overwrite_data['I'][i],
                            overwrite_data['sigmaI'][i],
                            overwrite_data['peak'][i],
                            overwrite_data['background'][i],
                            overwrite_data['fs'][i],
                            overwrite_data['ss'][i],
                            overwrite_data['panel'][i]
                        )
                        f.write(formatted_row)
                else:
                    # Write the unmodified line to the file
                    f.write(line)

Intenstity Finder Function
^^^^^^^^^^^^^^^^^^^^^^^^^^

This function simply finds the intensity of the peaks in the image, and returns a list of the intensities.
If the x,y coordinates are out of bounds, the function will simply ignore the peak.

.. py:function:: intensity_finder(x_coords, y_coords, image_name)

    Retrieve the intensity values for every x,y coordinate in the image.

    :param x_coords: The x coordinates of the peaks.
    :type x_coords: list
    :param y_coords: The y coordinates of the peaks.
    :type y_coords: list
    :param image_name: The name of the image to find the intensity of the peaks.
    :type image_name: str

    :return: The intensity of the image.
    :rtype: list

    .. code-block:: python

        def intensity_finder(x_coords, y_coords, image_name):
            """
            Retrieve the intensity values for every x,y coordinate in the image.
            """
            with h5.File(image_name, "r") as f:
                intensities = f['/entry/data/data'][()]
            intensities = np.array(intensities)
            found_intensities = []
            for x, y in zip(x_coords, y_coords):
                if x < intensities.shape[0] and y < intensities.shape[1]:
                    found_intensities.append(intensities[int(x), int(y)])
            return found_intensities


Populate Intensity Array Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Populates the intensity array to recreate the array of a loaded image with the stream data.

.. py:function:: populate_intensity_array(data_columns, image_name)

    Populate the intensity array with the intensity values for each x,y coordinate.

    :param data_columns: The columns of data to populate.
    :type data_columns: dict
    :param image_name: The name of the image to populate the intensity array.
    :type image_name: str

    :return: The populated intensity array.
    :rtype: np.array    

    .. code-block:: python

        def populate_intensity_array(data_columns, image_name):
            """
            Populate the intensity array with the intensity values for each x,y coordinate.
            """
            # reads the h5 image
            with h5.File(image_name, "r") as f:
                intensities = f['/entry/data/data'][()]
            intensities = np.array(intensities)
            # generates a new array of zeros with the same shape as the image
            new_intensities = np.zeros((intensities.shape[0], intensities.shape[1]))
            # for each x,y coordinate in the data_columns, set the value in the new array to the intensity value
            # populate the intensity array with corresponding (fs,ss) coordinates
            for i in range(len(data_columns['fs'])):
                x = int(data_columns['fs'][i])
                y = int(data_columns['ss'][i])
                if x < intensities.shape[0] and y < intensities.shape[1]:
                    new_intensities[x][y] = intensities[x][y]
            return new_intensities

Main Function
^^^^^^^^^^^^^
    The main function of the program, which executes the program.

    The function performs the following steps:
    
    1. **File Loading**: 
        
        - Displays the current working directory.

    2. **Setup Paths**:
        
        - Initializes `src_path` to the current working directory. 
        
        - Creates `stream_dir`` and `image_dir` paths by joining `src_path` with respective directory names.

    3. **Initialize Variables**: 
    
        - Initializes `intensities_array` to `None`.
        
        - Initializes `high_stream_name` and `low_stream_name` to the respective stream file names.

    4. **Load and Compare Stream Data**:
    
        - Loads data from the high and low stream files using `load_stream`.
        
        - Compares high and low data using `compare_high_low`.

    5. **Overwrite Data**:
    
        - Overwrites data in the high stream file with data from the low stream.

    6. **Image Processing**:

        - Sets up `image_name` and `image_path` for processing.

        - Finds intensities using `intensity_finder` with high data stream coordinates and image path.
        
        - Populates the `intensities_array` with intensity data using `populate_intensity_array()`.

    7. **Threshold Processing and Coordinate Extraction**:

        - Initializes a `PeakThresholdProcessor` with a very low threshold.

        - Prints the original threshold value.
        
        - Retrieves coordinates above the threshold using `get_coordinates_above_threshold`.

    8. **Coordinate Menu Processing**:

        - Initializes another `PeakThresholdProcessor` with a higher threshold value.
        
        - Iterates through a list of radii, processing coordinates with different threshold values and radii.
        
        - Sets completed to True after processing

.. py:function:: main()

    .. code-block:: python

        def main():
            print("Current working directory:", os.getcwd())
            src_path = os.getcwd()
            stream_dir = os.path.join(src_path, "high_low_stream")
            image_dir = os.path.join(src_path, "images")
            
            intensities_array = None
            high_stream_name = 'test_high.stream'
            low_stream_name = 'test_low.stream'

            high_stream_path = "high_low_stream/test_high.stream"
            low_stream_path = "high_low_stream/test_low.stream"

            if not os.path.exists(high_stream_path):
                print(f"File {high_stream_path} does not exist.")
                return
            elif os.path.exists(low_stream_path) and os.path.exists(high_stream_path):
                print(f"Files {low_stream_path} and {high_stream_path} exist.")

            if not os.path.exists(high_stream_path):
                print(f"File {high_stream_path} does not exist.")
                return
            elif os.path.exists(low_stream_path) and os.path.exists(high_stream_path):
                print(f"Files {low_stream_path} and {high_stream_path} exist.")

            # compare_high_low(high_data, low_data)
            high_data = load_stream(high_stream_path)
            low_data = load_stream(low_stream_path)
            compare_high_low(high_data, low_data)

            # Took low data from low_stream and put in high_stream file.
            overwrite_data = low_data
            overwrite_low_in_high(high_stream_path, overwrite_data)
            
            # compare any columns in data_columns
            # compare_high_low(high_data, low_data, "h")

            # now high_stream has data from low_stream
            
            image_name = '9_18_23_high_intensity_3e8keV-1_test.h5'
            image_path = os.path.join(image_dir, image_name)

            # retrieved from stream coordinate menu
            intensities = intensity_finder(high_data['fs'], high_data['ss'], image_path)

            # populate_inteneity_array is not correctly working
            intensities_array = populate_intensity_array(high_data, image_path)

            print("Number of non-zero values in intensity array\t", np.count_nonzero(intensities_array))

            # for debugging
            # intensities_array = np.array(intensities_array)
            # print(intensities_array)
            # compare_high_low(high_data, low_data, "I")

            threshold_stream = streampy.PeakThresholdProcessor(intensities_array, threshold_value=1e-5) # very low!
            print("Original threshold value: ", threshold_stream.threshold_value, "\n")
            coordinate_list_stream = threshold_stream.get_coordinates_above_threshold()
            
            completed = False
            radius = [1,2,3,4]

            threshold = streampy.PeakThresholdProcessor(intensities_array, threshold_value=9000)
            for r in [1, 2, 3, 4]:
                print(f"Threshold value for radius {r}: {threshold.threshold_value}")
                streampy.coordinate_menu(intensities_array, threshold_value=threshold.threshold_value, coordinates=coordinate_list_stream, radius=r)
                print(f"Completed coordinate menu for radius {r}")
                completed = True
                
        if __name__ == '__main__':           
            main() 