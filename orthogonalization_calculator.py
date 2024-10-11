import argparse 
import vector_operations as vecop


# default settings for the application are as follows 

# default_normalisation will normalise the output set (to give an orthonormal set) when True, False will not carry out the final normalisation
default_normalisation = True       
# default_accuracy is an integer for the number of decimal places the output will be rounded to. This can also be set to False to prevent any rounding.
default_accuracy = 3     


def parser():
    """
    Uses the argparse module to add support for a command line interface.
    """

    parse = argparse.ArgumentParser(description="Find the orthogonal set of a vector set")

    parse.add_argument('input_type_of_set',type=int,help = "Where the input vector set will come from, 0 is from a file - filename must be provided\ 1 is a manual input")

    parse.add_argument('settings', type = int, help = "The settings that will be used for the orthogonalisation, 0 is default settings\ 1 is custom settings. \ Defaults to 0 ",default = 0)

    parse.add_argument('save_output', type=int, help = "Should the output be saved as a CSV file or not, True will save the output\ False wil not save the output. \ Defaults to True")
    
    return parse


def get_input(arguments):
    """ 
    Retrieves the vector set depending on the options specified in the CLI by the user.

    Parameters
    ------------
    args : argparse.Namespace
        The arguments from the CLI input. 

    Returns
    ---------
    user_vector_set : list
        The vector set provided by the user.
    user_normalisation : bool
        Value of True if an orthonormal set is desired. False if only an orthogonal set is required.
    user_accuracy : bool, int  
        Value of False if the user does not want rounded entries. Integer value if user requires rounding. The integer is the number of decimal places required.
    save_output : bool
        Value of False if user does not want the output saved as a file. True if a saved file is required.
    user_new_filename : str
        Name of the output file.
    """

    input_type = arguments.input_type_of_set
    settings = arguments.settings
    save_output = arguments.save_output

    correct_inputs = [0,1,'0','1']

    # get the vector set depending on the users requirements
    if input_type == 0:

        # take the vector set from a filename that has to be inputted
        filename = input("Give the name of the file which contains the vector set: ")

        # check that the file exists in the current working directory
        try:
            f = open(filename,'r')
            f.close()
        except:
            print("Error: The chosen file does not exist in the current directory. Check the filename.")
            exit()

        user_vector_set =  vecop.file_parser(filename = filename)

        # check that the inputted vector set contains the correct dimensions
        try:
            vecop.Vector_Set.set_dimensions(user_vector_set)
        except:
            print("""Error: There is an error in the dimensions of the inputted set.
                  Likelihood is that not all vectors have the same number of entries""")
            exit()
   
    # obtain the vector set by user input
    elif input_type == 1:
        "Ask user to input vector set as a list of lists, incorporate a (case-sensitive called) help statement, may be good to use np.shape to help you"
        
        print("Enter the vector set manually as desired. Remember that any complex values should be added as j instead of i")
        print("""Type 'help' (case sensitive) for additional information""")

        # obtain the user input
        user_input = input("\nEnter the vector set: ")

        # check if the user asked for help and provide it if needed
        if user_input == 'help':
            print("""Enter the vector set as a list of lists.
                  Each inner list will be a vector in the vector set. 
                  The entries in each vector must be seperated with commas.
                  Complex numbers should be added as 'j' not 'i'.
                  Lists should be made using square brackets '[ ]'
                  Do not include spaces between characters

                  An example Vector Set is: '[[1,0,1j],[-1,1j,1],[0,-1,1j+1]]'
                  """)
            user_input = input("\nEnter the vector set: ")
        
        user_input.replace(' ','')
        
        # check there are no characters other than j [ ] , ( ) in the string
        if not user_input.translate({ord(x): None for x in '[]+-j,.()'}).isnumeric():
            print("Error: The input contains unexpected characters. \nOnly characters expected are: ] [ + - j , . ) ( ")
            exit()
            
        # convert the vector set from a sting into a list
        user_vector_set = eval(user_input)

        # check that the inputted vector set contains the correct dimensions
        try:
            vecop.Vector_Set.set_dimensions(user_vector_set)
        except:
            print("""Error: There is an error in the dimensions of the inputted set.
                  Likelihood is that not all vectors have the same number of entries""")
            exit()

    else:
        print("Error: The input_type_of_set attribute should only take values of 0 or 1. An incorrect value of {0} has been inputted".format(input_type))
        exit()
    
    # obtain the correct settings needed depending on user requirements 
    if settings == 0:
        # using default settings
        user_normalisation = default_normalisation
        user_accuracy = default_accuracy
        
    elif settings == 1:
        # obtain settings by user input 
        user_normalisation = input("""Should the resulting orthogonal set be normalised to provide an orthogonal set?
                                   Type 0 for NO (orthogonal set)
                                   Type 1 for YES (orthonormal set) """)
        
        if user_normalisation not in correct_inputs:
            print("Error: A value other than 0 or 1 was provided")
            exit()
        
        user_normalisation = int(user_normalisation)
        user_normalisation = bool(user_normalisation)

        user_accuracy = input("""Should the output vectors be rounded
                              Type 0 for NO
                              Type 1 for YES """)
        if user_accuracy not in correct_inputs:
            print("Error: A value other than 0 or 1 was provided")
            exit()
        
        user_accuracy = int(user_accuracy)
        
        if user_accuracy == 0:
            user_accuracy = False
        
        elif user_accuracy == 1:
            accuracy_amount = input("Type in the desired extent of rounding in decimal places: ")
            try:
                accuracy_amount = int(accuracy_amount)
            except:
                print("Error: The input given is not an integer")
                exit()
            accuracy_amount = int(accuracy_amount)
            user_accuracy = accuracy_amount
        
    else:
        print("Error: The settings attribute should only take values of 0 or 1. An incorrect value of {0} has been inputted".format(settings))
        exit()

    save_output = int(save_output)

    if save_output == 1:
        save_output = bool(save_output)
        user_new_filename = input("Type in the name of the new file. Include .csv file extension at the end: ")
    elif save_output == 0:
        user_new_filename = False
        save_output = bool(save_output)
    else:
        print("Error: The save_output attribute should only take values of 0 or 1. An incorrect value of {0} has been inputted".format(save_output))
        exit()

    return user_vector_set,user_normalisation,user_accuracy,save_output,user_new_filename


# run the program 
if __name__ == "__main__":
    parsed = parser()
    given_args = parsed.parse_args()
    user_vector_set,user_normalisation,user_accuracy,save_output,user_new_filename = get_input(given_args)

    orthogonal_set = vecop.Vector_Set.orthogonalisation(input_set=user_vector_set, normalised = user_normalisation, accuracy = user_accuracy)

    print("The orthogonal/orthonormal set is: ")
    print(orthogonal_set)

    if user_new_filename:
        vecop.csv_file_creater(vector_set = orthogonal_set,new_filename = user_new_filename)

