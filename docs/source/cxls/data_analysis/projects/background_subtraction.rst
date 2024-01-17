Water Background Subtraction Project (Main)
============================================

This project is a simple implementation of background subtraction.

Within the project, there are three main project files: 
    
    - `h5_background_subtraction_10_2_23.py`
    
    - `h5_stream_background_subtraction_10_2_23.py`

    - `overwrite_10_2_23.py`. 

All of these are found under the `src/` directory. The first file contains the main code for this page, while the others were adaptations on this.


GitHub Repositories:

- `adamkurth/waterbackground_subtraction on GitHub <https://github.com/adamkurth/waterbackground_subtraction.git>`_


- `amkurth/waterbackground_subtraction on GitLab <https://gitlab.com/amkurth/waterbackground_subtraction.git>`_
 

Imports
-------

The following modules are imported for use in the program:

.. code-block:: python
 
    import os
    import numpy as np
    import h5py as h5
    import matplotlib.pyplot as plt

PeakThresholdProcessor Class 
----------------------------

The `PeakThresholdProcessor ` class is used for processing the image peak values in the image array, above or at a specified threshold value. This class provides functions for setting and retrieving coordinate values these values.

The following functions are defined in the `PeakThresholdProcessor` class:

.. py:class:: PeakThresholdProcessor(image_array, threshold_value=0)
    
    Initialize the `PeakThresholdProcessor` with the image array and coordinate threshold value.

   :param image_array: The image array to be processed.
   :type image_array: numpy.ndarray
   :param threshold_value: The threshold value to be used for processing the image array, defaults to 0.
   :type threshold_value: float, optional
   
   :return: Returns coordinate list of x and y values above the threshold value.
   :rtype: list
   
    .. py:method:: set_threshold_value(new_threshold_value)
        Set a new threshold value for the image array.

        :param new_threshold_value: The new threshold value to be used for processing the image array.
        :type new_threshold_value: float

    .. py:method:: get_threshold_value()
        Getter method which returns the current threshold value for the image array.

        :return: The current threshold value for the image array.
        :rtype: float

ArrayRegion Class
-----------------

The `ArrayRegion` class is used for processing the image array region, using the coordinate values provided. This class provides functions for setting and retrieving coordinate values these values.

The following functions are defined in the `ArrayRegion` class:

.. py:class:: ArrayRegion(array)
    
    The `ArrayRegion` class is used for processing the image array region.

   :param array: The image array to be processed.
   :type array: numpy.ndarray
   
   .. py:attribute:: x_center
       The x coordinate of the center of the region. First coordinate in tuple.
       :type: int

   .. py:attribute:: y_center
       The y coordinate of the center of the region. Second coordinate in tuple.
       :type: int

   .. py:attribute:: region_size
        Make region that has radius of size region_size.
       :type: int

   .. py:method:: set_peak_coordinate(x, y)
       Set the x and y coordinates of the center of the region using chosen coordinate.

       :param x: The x coordinate of the center of the region.
       :type x: int
       :param y: The y coordinate of the center of the region.
       :type y: int

   .. py:method:: set_region_size(size)
       Make region that is printable for the terminal and has a radius of region_size.

       :param size: The size of the region radius.
       :type size: int

   .. py:method:: get_region()
       Get the region from the image array.

       :return: The region from the image array.
       :rtype: numpy.ndarray


Helper Functions
----------------

.. py:method:: load_h5(filename)

    This method loads an HDF5 file and prints a success message if the file is loaded successfully. If the file is not found within the working directory, it prints an error message.

    :param filename: The path to the HDF5 file.
    :type filename: str

.. py:method:: extract_region(image_array, region_size, x_center, y_center)
    
    This function calls the `ArrayRegion` class to extract the region from the image array.

    :param image_array: The image array to be processed.
    :type image_array: numpy.ndarray
    :param region_size: The size of the region radius.
    :type region_size: int
    :param x_center: The x coordinate of the center of the region.
    :type x_center: int
    :param y_center: The y coordinate of the center of the region.
    :type y_center: int

    :return: The extracted region from the image array.
    :rtype: numpy.ndarray
    
Coordinate Menu Function
------------------------

`coordinate_menu` is the focus of this program, is used interactively with the user to display the chosen coordiante value. Visualizing the region of the chosen coordinate value, and displaying the average surrounding peak value and the intensity peak value.

.. py:method:: coordinate_menu(image_array, threshold_value, coordinates, radius)

    This function displays the coordinates above the given threshold and radius, and allows the user to interactively select the coordinate for further processing.

    :param image_array: The image array to be processed.
    :type image_array: numpy.ndarray
    :param threshold_value: The thresold value used to determine the coordiantes.
    :type threshold_value: float
    :param coordinates: A tuple list of coordinates (x,y) above the thresold.
    :type coordinates: list[tuple[int, int]]
    :param radius: The radius around each coordinate to be processed.
    :type radius: int

    The user is prompted to choose a coordinate. Function displays 9x9 two-dimensional array, the segment, and the boolean array of traversed values. The function then returns the average surrounding peak value and the intensity peak value.

    :return: The average surrounding peak value and the intensity peak value.
    :rtype: tuple[float, float]

    .. code-block:: python

        def coordinate_menu(image_array, threshold_value, coordinates, radius):
            print("\nCoordinates above given threshold:", threshold_value, 'with radius: ', radius)
            for i, (x, y) in enumerate(coordinates):
                print(f"{i + 1}. ({x}, {y}")

            while True:
                choice = input("\nWhich coordinate do you want to process? (or 'q' to quit)\n")
                if choice == "q":
                    print("Exiting")
                    break
                try:
                    count = int(choice) - 1
                    if 0 <= count < len(coordinates):
                        x, y = coordinates[count]
                        print(f"\nProcessing - ({x}, {y})")
                        print('Printing 9x9 two-dimensional array\n')

                        # creates visualization if the array, of chosen peak
                        display_region = extract_region(image_array, region_size=4, x_center=x, y_center=y)
                        print('DISPLAY REGION \n', display_region, '\n')

                        # segment is the area with the given radius that's passed through the function.
                        segment = extract_region(image_array, region_size=radius, x_center=x, y_center=y)
                        print ('SEGMENT \n', segment, '\n')

                        # returns boolean array of traversed values.
                        bool_square = np.zeros_like(segment, dtype=bool)
                        print('BOOLEAN', '\n', bool_square, '\n')

                        values_array = extract_region(image_array, region_size=radius, x_center=x, y_center=y)

                        global avg_values, intensity_peak
                        total_sum = 0; skipped_point = None; count = 0; intensity_peak = 0
                        for col_index in range(values_array.shape[0]):
                            for row_index in range(values_array.shape[1]):
                                if values_array[row_index, col_index] >= 0:
                                    count += 1
                                    bool_square[row_index, col_index] = True
                                    if row_index == radius and col_index == radius:
                                        skipped_point = (row_index, col_index)
                                        intensity_peak = values_array[row_index, col_index]
                                        print(f'Peak point to be skipped: ({row_index}, {col_index}) ', values_array[radius,radius])
                                    elif abs(row_index - radius) <= 1 and abs(col_index - radius) <=1:
                                        print(f'Passed (row, col) ({row_index}, {col_index})', values_array[row_index,col_index])
                                        pass
                                    else:
                                        print(f'(row,col) ({row_index}, {col_index}) with a value of ', values_array[row_index, col_index])
                                        total_sum += values_array[row_index, col_index]
                        print('\n######################')
                        print(bool_square)
                        print('Number of traversed cells', count)
                        print('Peak point to be skipped:', skipped_point)
                        print('Total sum:',total_sum)
                        avg_values = total_sum / count
                        print('Average surrounding peak:',avg_values)

                        build_coord_intensity()

                        create_scatter(result_x, result_y, result_z, highlight_x=x, highlight_y=y)
                        return avg_values,intensity_peak
                        break
                    else:
                        print("Invalid coordinate index.")
                except ValueError:
                    print("Invalid input. Enter a number or 'q' to quit.")

.. py:method:: build_coord_intensity()

    This function builds the intensity peak value for the chosen coordinate, used in the `create_scatter` function. 

    :return: A tuple containing four lists: x values, y values, z values, and columns needed for `create_scatter`.
    :rtype: tuple[list, list, list, list]

    .. code-block:: python

        def build_coord_intensity():
            global result_x, result_y, result_z, coordinates_and_intensities
            result_z = []
            threshold = PeakThresholdProcessor(image_array, threshold_value=.01)
            coord_above_threshold = threshold.get_coordinates_above_threshold()
            coord_above_threshold = np.array(coord_above_threshold)
            
            for i in coord_above_threshold: 
                result_x = coord_above_threshold[:,0]
                result_y = coord_above_threshold[:,1]
            
            result_x = np.array(result_x)
            result_y = np.array(result_y)
            
            for i in range(len(coord_above_threshold)):
                x = result_x[i]
                y = result_y[i]
                z = image_array[x,y]
                result_z.append(z)
            # creating a coordinate and intensity array to store the values we want to plot.
            coordinates_and_intensities = np.column_stack((result_x, result_y, result_z))
            return result_x, result_y, result_z, coordinates_and_intensities

.. py:method:: create_scatter(x, y, z, highlight_x=None, highlight_y=None)
    `create_scatter ` creates visualization for chosen highlighted coordinate, using matplotlib.pyplot.

    :param x: list of x coordinate values.
    :type x: list
    :param y: list of y coordinate values.
    :type y: list
    :param z: list of z coordinate values, intensities.
    :type z: list
    :param highlight_x: The x coordinate of the center of the region.
    :type highlight_x: int
    :param highlight_y: The y coordinate of the center of the region.
    :type highlight_y: int

Main Function
-------------

The `main` function processes image data from specified HDF5 file for 3-ring integration analysis. Calling `coordinate_menu` for increasing radius value.

.. py:method:: main(filename)

    Loads and processes image data from HDF5 file.

    :param filename: The path to the HDF5 file containing image data.
    :type filename: str

    The function performs the following steps:

    1. **File Loading**: 
    
        - It calls `load_h5` to load the specified HDF5 file.

    2. **Image Data Extraction**: 
    
        - Extracts the NumPy array from the HDF5 file, which is 2D array of zeros with shape of (4371, 4150). 
    
    3. **Threshold Processing**: 
    
        - It calls `PeakThresholdProcessor` and creates object with the extracted array region and a threshold of 1000. Then retrieving the coordinates above this threshold.
    
    4. **Ring Integration Analysis**: 

        - Interactively calls `coordinate_menu` for a set of radii (1,2,3,4). And for each value in the list, this calculates and prints the peak estimate by subtracting the average value from the intensity peak value.
   
   The function sets a global variable `image_array` to store the image data and `coordinates` to store the coordinates above the threshold. The global variable `intensity_peak` and `avg_values` are used to calculate the peak estimates.

   The script also defines paths for working with image files and calls the `main` function with different image paths for processing.
