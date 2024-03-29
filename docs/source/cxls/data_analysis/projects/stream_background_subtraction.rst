Water Background Subtraction Project (Stream)
==============================================

This project is an adaptation on :doc:`background_subtraction`. It is intended to analyze the `.stream` after running `indexamajig` from CrystFEL. 

This extension focuses on reading the `.stream` files, makeing a dictionary of the content, and recreating an array of the intensity values. The intensity values are then used to calculate the average surrounding peak value and the intensity peak value.


GitHub Repositories:

- `adamkurth/waterbackground_subtraction on GitHub <https://github.com/adamkurth/waterbackground_subtraction.git>`_


- `amkurth/waterbackground_subtraction on GitLab <https://gitlab.com/amkurth/waterbackground_subtraction.git>`_
 

Imports
-------

The following modules are imported for use in the program:

.. code-block:: python

    import os
    import sys
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
   
    .. py:function:: set_threshold_value(new_threshold_value)
        Set a new threshold value for the image array.

        :param new_threshold_value: The new threshold value to be used for processing the image array.
        :type new_threshold_value: float

    .. py:function:: get_threshold_value()
        
        Getter method which returns the current threshold value for the image array.

        :return: The current threshold value for the image array.
        :rtype: float

.. code-block::python

    class PeakThresholdProcessor: 
        def __init__(self, image_array, threshold_value=0):
            self.image_array = image_array
            self.threshold_value = threshold_value
        def set_threshold_value(self, new_threshold_value):
            self.threshold_value = new_threshold_value
        def get_coordinates_above_threshold(self):  
            coordinates = np.argwhere(self.image_array > self.threshold_value)
            return coordinates


ArrayRegion Class
-----------------

The `ArrayRegion` class is used for processing the image array region, using the coordinate values provided. This class provides functions for setting and retrieving coordinate values these values.

The following functions are defined in the `ArrayRegion` class:

.. py:class:: ArrayRegion(array)
    
    The `ArrayRegion` class is used for processing the image array region.

   :param array: The image array to be processed.
   :type array: numpy.ndarray
   
   .. py:attribute:: x_center 
        First coordinate in tuple
       :type: int

   .. py:attribute:: y_center
        Second coordinate in tuple.
       :type: int

   .. py:attribute:: region_size
        Make region that has radius of size region_size.
       :type: int

   .. py:function:: set_peak_coordinate(x, y)

       Set the x and y coordinates of the center of the region using chosen coordinate.

       :param x: x coordinate of the region
       :type x: int
       :param y: y coordinate of the region
       :type y: int

   .. py:function:: set_region_size(size)

       Make region that is printable for the terminal and has a radius of region_size.

       :param size: The size of the region radius.
       :type size: int

   .. py:function:: get_region()

       Get the region from the image array.

       :return: The region from the image array.
       :rtype: numpy.ndarray

.. code-block:: python 

    class ArrayRegion:
    def __init__(self, array):
        self.array = array
        self.x_center = 0
        self.y_center = 0
        self.region_size = 0
    def set_peak_coordinate(self, x, y):
            self.x_center = x
            self.y_center = y
    def set_region_size(self, size):
        # set limit that is printable in terminal
        self.region_size = size
        max_printable_region = min(self.array.shape[0], self.array.shape[1]) //2
        self.region_size = min(size, max_printable_region)
    def get_region(self):
        x_range = slice(self.x_center - self.region_size, self.x_center + self.region_size+1)
        y_range = slice(self.y_center - self.region_size, self.y_center + self.region_size+1)
        region = self.array[x_range, y_range]
        return region


Helper Functions
----------------

.. py:function:: load_file_h5(filename)

    Left over helper function from :ref::`Water Background Subtraction (Main)` to load the image data. 
    
    This method loads an HDF5 file and prints a success message if the file is loaded successfully. If the file is not found within the working directory, it prints an error message.

    :param filename: The path to the HDF5 file.
    :type filename: str

    .. code-block::python
    
        def load_file_h5(filename):
            if not os.path.exists(filename):
                print("File not found within working directory.")
                return
            try:
                with h5.File(filename, "r") as f: 
                    print("\nLoaded file successfully.", filename)
            except Exception as e:
                print("\nAn error has occurred:", str(e))

.. py:function:: extract_region(image_array, region_size, x_center, y_center)
    
    This function calls the `ArrayRegion` class to extract the region from the image array.

    :param image_array: The image array to be processed.
    :type image_array: numpy.ndarray
    :param region_size: The size of the region radius.
    :type region_size: int
    :param x_center: x coordinate of the region
    :type x_center: int
    :param y_center: y coordinate of the region
    :type y_center: int

    :return: The extracted region from the image array.
    :rtype: numpy.ndarray

    .. code-block::python
        
        def extract_region(image_array, region_size, x_center, y_center):
            extract = ArrayRegion(image_array)
            extract.set_peak_coordinate(x_center,y_center)
            extract.set_region_size(region_size)
            np.set_printoptions(floatmode='fixed', precision=10)
            np.set_printoptions(edgeitems=3, suppress=True, linewidth=200)
            region = extract.get_region()
            return region      
    
        
        
Coordinate Menu Function
------------------------

`coordinate_menu` is the focus of this program, is used interactively with the user to display the chosen coordiante value. Visualizing the region of the chosen coordinate value, and displaying the average surrounding peak value and the intensity peak value.
.. py:function:: coordinate_menu(image_array, threshold_value, coordinates, radius)

    This function displays the coordinates above the given threshold and radius, and allows the user to interactively select the coordinate for further processing.

    :param image_array: The image array to be processed.
    :type image_array: numpy.ndarray
    :param threshold_value: thresold value to determine the coordiantes.
    :type threshold_value: float
    :param coordinates: tuple list of coordinates (x,y) above thresold.
    :type coordinates: list[tuple[int, int]]
    :param radius: The radius around each coordinate to be processed.
    :type radius: int

    The user is prompted to choose a coordinate. Function displays 9x9 two-dimensional array, the segment, and the boolean array of traversed values. The function then returns the average surrounding peak value and the intensity peak value.

    .. code-block:: python

        def coordinate_menu(image_array, threshold_value, coordinates, radius): 
            print("\nCoordinates above given threshold:", threshold_value, 'with radius: ', radius)
            for i, (x, y) in enumerate(coordinates):
                print(f"{i + 1}. ({x}, {y})")
                
            while True:
                choice = input("\nWhich coordinate do you want to process? (or 'q' to quit)\n")
                if choice == "q":
                    print("Exiting")
                    break
                try: 
                    count = int(choice)-1
                    if 0 <= count < len(coordinates):
                        x,y = coordinates[count]
                        print(f"\nProcessing - ({x}, {y})")
                        print('Printing 9x9 two-dimensional array\n')
                        
                        # creates visualization if the array, of chosen peak
                        print(x,y)
                        display_region = extract_region(image_array, region_size=4, x_center=x, y_center=y)
                        
                        print('DISPLAY REGION \n', display_region, '\n')
                        
                        # segment is the area with the given radius that's passed through the function.
                        segment = extract_region(image_array, region_size=radius, x_center=x, y_center=y)
                        print ('SEGMENT \n', segment, '\n')
                        
                        # returns boolean array of traversed values.
                        bool_square = np.zeros_like(segment, dtype=bool)
                        print('BOOLEAN: before traversing.', '\n', bool_square, '\n') 
                    
                        """ 3 RING INTEGRATION """
                        values_array = extract_region(image_array, region_size=radius, x_center=x, y_center=y)
                        
                        #traverses through (i = row) , (j = column)         

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
                        if count > 0:
                            avg_values = total_sum / count
                        else: 
                            avg_values = "Could not divide by 0."
                        print('Average surrounding peak:',avg_values)
                        print('Peak point:', intensity_peak)
                        return avg_values,intensity_peak
                        break
                    else: 
                        print("Invalid coordinate idex.")
                except ValueError:
                    print("Invalid input. Enter a number of 'q' to quit.")



Load Stream Function
--------------------

.. py:function:: load_stream()

    This function loads the `.stream` file and prints a success message if the file is loaded successfully. If the file is not found within the working directory, it prints an error message.
    
     It then reads the file line by line and stores the values in a dictionary. The function then returns the dictionary and the x, y, and z values.

    .. code-block:: python

        def load_stream(stream_path):
            global stream_coord
            global result_x, result_y, result_z #for building intensity array
            stream_name = os.path.basename(stream_path)
            full_path = os.path.join(stream_path)
            
            try:
                
                stream = open(full_path, 'r') 
                print("\nLoaded file successfully.", stream_name, '\n')
            except Exception as e: 
                print("\nAn error has occurred:", str(e),'\n')
            
            reading_peaks = False
            reading_geometry = False
            reading_chunks = True 
            global data_columns
            data_columns = {
                'h':[], 'k':[], 'l':[],
                'I':[], 'sigmaI':[], 'peak':[], 'background':[],
                'fs':[],'ss':[], 'panel':[]
                }
            
            for line in stream:
                if reading_chunks:
                if line.startswith('End of peak list'):
                    reading_peaks = False
                elif line.startswith("   h    k    l          I   sigma(I)       peak background  fs/px  ss/px panel"):
                    reading_peaks = True
                elif reading_peaks:
                        try:
                            elements = line.split()
                            data_columns['h'].append(int(elements[0]))
                            data_columns['k'].append(int(elements[1]))
                            data_columns['l'].append(int(elements[2]))
                            data_columns['I'].append(float(elements[3]))
                            data_columns['sigmaI'].append(float(elements[4]))
                            data_columns['peak'].append(float(elements[5]))
                            data_columns['background'].append(float(elements[6]))
                            data_columns['fs'].append(float(elements[7]))
                            data_columns['ss'].append(float(elements[8]))
                            data_columns['panel'].append(str(elements[9]))
                        except:
                            pass
                elif line.startswith('----- End geometry file -----'):
                    reading_geometry = False
                elif reading_geometry:   
                    try:
                        par, val = line.split('=')
                        if par.split('/')[-1].strip() == 'max_fs' and int(val) > max_fs:
                            max_fs = int(val)
                        elif par.split('/')[-1].strip() == 'max_ss' and int(val) > max_ss:
                            max_ss = int(val)
                    except ValueError:
                        pass
                elif line.startswith('----- Begin geometry file -----'):
                    reading_geometry = True
                elif line.startswith('----- Begin chunk -----'):
                    reading_chunks = True   
            result_x = data_columns['fs']; result_y = data_columns['ss']; result_z = data_columns['I']
            return data_columns, result_x, result_y, result_z

Main Function
-------------

The `main` function processes image data from specified HDF5 file for 3-ring integration analysis. Calling `coordinate_menu` for increasing radius value.

.. py:function:: main(filename)

    Loads and processes image data from HDF5 file.

    :param filename: The path to the HDF5 file containing image data.
    :type filename: str

    The function performs the following steps:

    1. **File Loading**: 

        - It calls `load_h5()` to load the specified HDF5 file.

    2. **Image Data Extraction**: 
    
        - Extracts the NumPy array from the HDF5 file, which is 2D array of zeros with shape of (4371, 4150). 
    
    3. **Threshold Processing**: 
    
        - It calls `PeakThresholdProcessor` and creates object with the extracted array region and a threshold of 1000. Then retrieving the coordinates above this threshold.
    
    4. **Ring Integration Analysis**: 
    
        - Interactively calls `coordinate_menu()` for a set of radii (1,2,3,4). And for each value in the list, this calculates and prints the peak estimate by subtracting the average value from the intensity peak value.
   
   The function sets a global variable `intensity_array` to store the image data and `coordinates` to store the coordinates above the threshold. The global variable `intensity_peak` and `avg_values` are used to calculate the peak estimates.

   The script also defines paths for working with image files and calls the `main` function with different image paths for processing. This is done for the next adaptation of the `overwrite_10_2_23.py`.