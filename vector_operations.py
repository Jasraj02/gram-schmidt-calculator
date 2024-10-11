

import numpy as np 
import math


class Vector():
    """
    A class used to represent and handle Vectors.

    Attributes
    --------------
    vector_shape : tuple
        The dimensions of the given vector.
    is_complex : bool
        True or False depending on if the vector contains complex numbers or not.
    real_part : list
        List of all the real components of each entry in the vector.
    imaginary_part : list
        List of all the imaginary components of each entry in the vector.
    
    """

    def __init__(self,vector):
        """
        Constructs all necessary attributes for the Vector object.

        Parameters
        -----------

        vector : list
            The vector that will be passed into the Vector class.
        
        """

        # save the dimensions of the vector as an attribute of the Vector object
        self.vector_shape = np.shape(vector)

        # check if the vector has any imaginary components
        imaginary_component_present = False
        for entry in vector:
            if isinstance(entry,complex):
                imaginary_component_present = True
        
        # split the real and imaginary components into seperate lists and make them attributes of the Vector object
        if imaginary_component_present:
            real_component = []
            imaginary_component = []
            for entry in vector:
                if not isinstance(entry,complex):
                    entry = complex(entry)  # as not all entries in the vector may be complex, they should first be converted to the complex type

                real_component.append(entry.real)
                imaginary_component.append(entry.imag)

            self.real_part = np.array(real_component)
            self.imaginary_part = np.array(imaginary_component)
            self.iscomplex = imaginary_component_present

        # if there is no imaginary components then add the real components and make the imaginary component 0 for all entries 
        else:
            self.real_part = np.array(vector)
            self.imaginary_part = np.zeros(self.vector_shape)
            self.iscomplex = imaginary_component_present

    def norm_squared(vector):
        '''
        Calculates the norm squared of a given vector. 

        Parameters
        -------------
        vector : array 
            The vector that the norm squared will be calculated for.

        Outputs
        ----------
        sum : float
            The norm squared of the vector given. 
        '''

        vector = Vector(vector)

        dimensions = vector.vector_shape
        sum = 0.0

        # if statement checks if the entry is a vector, then adds the square of all entries 
        if len(dimensions) == 1:
            for entry_number in range(dimensions[0]):
                sum += vector.real_part[entry_number]**2
                sum += vector.imaginary_part[entry_number]**2
            return sum 
        

    def dot_product(vector_a,vector_b):
        '''
        Performs the dot product operation on two vectors.
        Note that if vector inputs are complex then the exact procedure used is the inner product,
        which can be seen as a generalisation of the dot product.

        Parameters
        -----------
        vector_a : array
            The first vector to be dotted.
        vector_b : array
            The second vector to be dotted.

        Outputs
        --------
        sum : float
            The dot product of the two vectors,
        '''
        
        vector_a1 = Vector(vector_a)
        vector_b1 = Vector(vector_b)

        dimension_a = vector_a1.vector_shape
        dimension_b = vector_b1.vector_shape

        complex_conjugate_a = []
        
        
        if len(dimension_a) > 1 or len(dimension_b) > 1:
            print("Error: Unable to dot matrices")
            exit()
        if dimension_a != dimension_b:
            print("Error: Unable to perform dot operation as vectors are different size") 
            exit()

        # this calculates the dot product of vectors
        if vector_a1.iscomplex == False and vector_b1.iscomplex == False:
            sum = 0.0
            for i in range(dimension_a[0]):
                sum += (vector_a1.real_part[i] * vector_b1.real_part[i])
            return sum

        # this will calculate the inner product of vectors as the set involves a complex vector
        else:
            if dimension_a == dimension_b:
                sum = 0.0
                for i in range(dimension_a[0]):
                    entry_a = complex(vector_a1.real_part[i],-vector_a1.imaginary_part[i])
                    entry_b = complex(vector_b1.real_part[i],vector_b1.imaginary_part[i])

                    sum += (entry_a * entry_b)
                return sum
                        

    def projection(projection_vector,vector_affected):  
        '''
        Performs vector projection.

        Parameters
        ------------
        projection_vector : array
            The vector that the projection will be based from.

        vector_affected : array 
            The vector that will have the projection applied to it.

        Returns
        ---------
        projection : array
            The vector that is the outcome of the projection.
        '''

        top_line = (Vector.dot_product(projection_vector,vector_affected))/Vector.norm_squared(projection_vector)
        projection = []
        for entry in projection_vector:
            projection.append(top_line * entry)

        return projection  
    
    def vector_round(vector_to_round,accuracy):
        '''
        Rounds all entries in a vector to a given accuracy.

        Parameters
        -----------
        vector_to_round : list
            The vector that will be rounded.
        accuracy : int
            The number of decimal places that each entry in the vector will be rounded to.

        Outputs
        -----------
        vector_to_round : list
            The rounded vector.
        '''
        vector_to_round = Vector(vector_to_round)
        dimensions = vector_to_round.vector_shape
        rounded_vector = []

        # iterate though the real and imaginary components of each vector and round them
        for val in range(dimensions[0]):
            vector_to_round.real_part[val] = round(vector_to_round.real_part[val], accuracy)
            vector_to_round.imaginary_part[val] = round(vector_to_round.imaginary_part[val], accuracy)

        # check if the original vector is complex or not and add the rounded entry to a new list 
        if vector_to_round.iscomplex == False:
            for entry in range(dimensions[0]):
                rounded_vector.append(float(vector_to_round.real_part[entry]))
        else:
            for entry in range(dimensions[0]):
                rounded_vector.append(complex(vector_to_round.real_part[entry],vector_to_round.imaginary_part[entry]))

        return rounded_vector

    
    def vector_alteration(vector,normalised,accuracy_amount):
        '''
        Performs the optional alterations of normalisation and rounding to vectors before adding them to the orthogonal/orthonormal set.

        Parameters
        -------------
        vector : array
            The vector to which the alterations will be made.
        normalised: bool
            Passing True into this argument will normalise the vector. 
        accuracy_amound : int
            The accuracy to which each entry in the vector should be rounded to.
            Value of None or 0 can be input to leave the vector unrounded.

        Outputs
        --------
        vector : array
            The now altered vector. The original vector object is altered.
        ''' 
        if normalised:
            norm = math.sqrt(Vector.norm_squared(vector)) 
            normalised_vector = []
            for entry in vector:
                normalised_vector.append(entry/norm)
            vector = normalised_vector

        if accuracy_amount:     # if a certain accuracy number is given it will be applied here 
            vector = Vector.vector_round(vector,accuracy = accuracy_amount)
        return vector 




class Vector_Set:
    """
    A class used to represent and handle Vectors.

    Attributes
    --------------
    all_vectors : list
        The original vector set.
    contains_complex  : bool
        True or False depending on if any Vectors in the Vector Set contain any complex values.
    """

    def __init__(self,vector_set):
        """
        Constructs all necessary attributes for the Vector_Set object.

        Parameters
        -----------
        vector_set : list
            The list of lists which contains all Vectors in the Vector Set.
        """

        self.all_vectors = vector_set

        # check if the vector set contains any complex values 
        contains_complex = False
        for vector in vector_set:
            vector = Vector(vector)
            if vector.iscomplex == True:
                contains_complex = True

        self.contains_complex = contains_complex

    def set_dimensions(input_set):
        """
        Gives the dimensions of a given Vector Set.

        Parameters
        -------------
        input_set : list
            The vector set for which the dimensions will be found.

        Outputs
        --------
        dimensions : tuple
            The dimensions of the given vector set.

        """
        input_set = Vector_Set(input_set)
        dimensions = np.shape(input_set.all_vectors)

        return dimensions

    def orthogonalisation(input_set,normalised = True,accuracy = 3):
        """
        Takes in a vector set and outputs the orthogonal set. The orthogonal set can be normalised and all vectors can be rounded to a specific accuracy.

        Parameters
        ------------
        vector_set : list
            A nested list of all vectors present in the vector set.
        normalised : bool
            Set to True as default. If value is True then the orthogonal set will be normalised. If value is False then no final normalisation will occur.
        accuracy : int
            The number of decimal places to which each entry in the output set will be rounded to. 
        
        Outputs
        --------
        orthogonal_set : list
            The final orthogonal or orthonormal set. 
        """
        vector_set = Vector_Set(input_set)

        orthogonal_set = []
        for i in list(enumerate(vector_set.all_vectors)):   # enumerate all vectors in the set to give a number to all the vectors (useful when perfoming all required projections)
            if i[0] == 0:
                # this sets the first vector in the orthogonal set
                if vector_set.contains_complex == False:
                    vector1 = np.array(i[1],dtype = float)
                else:
                    vector1 = np.array(i[1],dtype = complex)

                orthogonal_set.append(Vector.vector_alteration(vector1,normalised=True,accuracy_amount=False))

            else:
                # this will produce a list of the sum of all projections that have to be applied (called vector_to_subtract)
                # first check if the vector set contains complex values or not
                dimensions = np.shape(i[1])
                if vector_set.contains_complex == False:
                    vector_to_subtract = np.zeros(dimensions,dtype=float)
                    original_vector = np.array(i[1],dtype=float)
                else:
                    vector_to_subtract = np.zeros(dimensions,dtype=complex)
                    original_vector = np.array(i[1],dtype=complex)

                for x in range(i[0]):
                    vector_to_subtract += Vector.projection(orthogonal_set[x],original_vector)

                new_vector = original_vector - vector_to_subtract
                orthogonal_set.append(Vector.vector_alteration(new_vector,normalised=False,accuracy_amount=False))

        # normalise the vector set if required and also round the entire set if an accuracy argument is given
        if normalised or accuracy:
            for index in range(len(orthogonal_set)):
                orthogonal_set[index] = Vector.vector_alteration(orthogonal_set[index],normalised = normalised,accuracy_amount=accuracy)
                
        return orthogonal_set


def file_parser(filename,delimiter = ","):
    '''
    Parses a CSV file and converts the vector set within the file to a nested list.
    Compatible with vector set files output by NumPy. 

    Parameters
    ------------
    filename : str
        The name of the file to be parsed. The file extension should be included within this string.
    delimiter : str
        The delimiter used to seperate entries within a vector. Standard delimiter is a comma.
    
    Outputs
    --------
    vector_set : list
        The vector set contained within the file.
    '''
    with open(filename) as file:
        vector_set = []
        for line in file:
            add = False
            # check if the first character of the line is a number or symbol
            if line[0].isnumeric() or line[0] == "-" or line[0] == "+" or line[0] == "(":
                add = True
            if add:
                line = line.replace('\n','')
                split_line = line.split(delimiter)
                for x in range(len(split_line)):
                    # check if the entry consists of only real numbers
                    if split_line[x].translate({ord(x): None for x in '+-'}).isnumeric():
                        split_line[x] = float(split_line[x])
                    # if above is not true then check if the entry instead consists of only real and imaginary numbers
                    elif split_line[x].translate({ord(x): None for x in '()+-j.'}).isnumeric():
                        split_line[x] = complex(split_line[x])
                    # if the above two are not satisfied then the entry contains letters or other characters and cannot be parsed into a vector set
                    else:
                        print("Unable to parse letters into a vector")
                        exit()
                vector_set.append(split_line)
    return vector_set


def csv_file_creater(vector_set, new_filename, delimiter = "," ):
    '''
    Takes a vector set and converts it into a CSV file. 

    Parameters
    ------------
    vector_set : list
        The vector set that will be converted to a CSV file.
    new_filename : str
        The name of the file that will be created. The file extension should be included within this string.
    delimiter : str
        The delimiter used to seperate entries within a vector. Standard delimiter is a comma.
    
    Outputs
    --------
    CSV file
    '''
    # create the new file
    with open(new_filename,"w") as file:
        #create the file contents
        for vector in vector_set:
            new_line = ""
            for entry in vector:
                entry = str(entry)
                new_line = new_line + entry + delimiter
            new_line = new_line[:-1]  # remove the final excess delimiter 
            file.write(new_line + "\n")
