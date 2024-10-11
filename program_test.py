import vector_operations as vecop

def norm_squared_testing():
    """
    Tests the norm_squared function within the vector_operations python script.

    Returns:
    ---------
    norm_count : int
        The number of passed tests.
    """
    norm_count = 0
    
    integer_example, int_ans = [2,7,14], 249.0
    float_and_integer_example,float_ans = [6,16,3.6,32,1.85], 1332.3825
    complex_example, comp_ans = [3.2+8.6j,-1.1,4.3+75j] , 5728.9
    
    if vecop.Vector.norm_squared(integer_example) == int_ans:
        norm_count += 1
    if vecop.Vector.norm_squared(float_and_integer_example) == float_ans:
        norm_count += 1 
    if vecop.Vector.norm_squared(complex_example) == comp_ans:
        norm_count += 1
    return norm_count


def dot_product_testing():
    """
    Tests the dot_product function within the vector_operations python script.

    Returns:
    ---------
    dot_count : int
        The number of passed tests.
    """
    dot_count = 0

    test_1a,test_1b, test_1_ans = [1,3,9] , [2,7,14] , 149.0
    test_2a,test_2b, test_2_ans = [1.1231,2,9.01,14.14313,22], [6,16,3.633,32,1.8554] , 564.87089
    test_3a,test_3b, test_3_ans = [1+1j, 2-1j], [3-2j, 1+1j] , 2-2j

    if vecop.Vector.dot_product(test_1a,test_1b) == test_1_ans:
        dot_count += 1
    if vecop.Vector.dot_product(test_2a,test_2b) == test_2_ans:
        dot_count += 1
    if vecop.Vector.dot_product(test_3a,test_3b) == test_3_ans:
        dot_count += 1 
    return dot_count

def projection_testing():
    """
    Tests the projection function within the vector_operations python script.

    Returns:
    ---------
    proj_count : int
        The number of passed tests.
    """
    proj_count = 0
    test_1a,test_1b, test_1_ans = [6,5,8],[1.6,5.2,3.1], [2.8992,2.416,3.8656]
    test_2a,test_2b, test_2_ans = [1,2,1],[1,1,3], [1.0,2.0,1.0]

    if vecop.Vector.projection(test_1a,test_1b) == test_1_ans:
        proj_count += 1
    if vecop.Vector.projection(test_2a,test_2b) == test_2_ans:
        proj_count += 1
    return proj_count

def orthogonalisation_testing():
    """
    Tests the orthogonalisation function within the vector_operations python script.

    Returns:
    ---------
    orth_count : int
        The number of passed tests.
    """
    orth_count = 0

    vector_set1 , set1_ans = [[1,2,0],[8,1,6],[0,0,1]]  , [[0.447, 0.894, 0.0], [0.667, -0.333, 0.667], [-0.596, 0.298, 0.745]]
    vector_set2 , set2_ans = [[1,-1,1],[1,0,1],[1,1,2]] , [[0.577, -0.577, 0.577], [0.408, 0.816, 0.408], [-0.707, 0.0, 0.707]]
    vector_set3, set3_ans = [[3,0,4],[-1,0,7],[0,9,0]] , [[0.6, 0.0, 0.8], [-0.8, 0.0, 0.6], [0.0, 1.0, 0.0]]
    complex_vector_set,set4_ans = [[1,0,1j],[-1,1j,1],[0,-1,1j+1]] , [[0.707,0,0.707j],[-0.354 + 0.354j, 0.707j, 0.354+0.354j],[0.5j, -0.5-0.5j, 0.5]]
    ugly_complex_vector_set,set5_ans = [[3.12,0.31,2j],[-1.21,6.1+6j,1.1329],[3.2342+8.75j,-1.1231,4.3211+75.32j]] , [[(0.838949+0j), (0.083357+0j), 0.537788j], [(-0.090224+0.010522j), (0.706009+0.690705j), (0.123474+0.031319j)], [(-0.529543+0.08659j), (0.003855-0.132343j), (0.114567+0.825489j)]]

    if vecop.Vector_Set.orthogonalisation(vector_set1,normalised=True,accuracy = 3) == set1_ans:
        orth_count += 1
    if vecop.Vector_Set.orthogonalisation(vector_set2,normalised=True,accuracy = 3) == set2_ans:
        orth_count += 1
    if vecop.Vector_Set.orthogonalisation(vector_set3,normalised=True,accuracy = 1) == set3_ans:
        orth_count += 1
    if vecop.Vector_Set.orthogonalisation(complex_vector_set,normalised=True,accuracy = 3) == set4_ans:
        orth_count += 1
    if vecop.Vector_Set.orthogonalisation(ugly_complex_vector_set,normalised=True,accuracy = 6) == set5_ans:
        orth_count += 1

    return orth_count

def file_parser_testing():
    """
    Tests the file_parser function within the vector_operations python script.

    Returns:
    ---------
    file_count : int
        The number of passed tests.
    """
    file_count = 0

    example_file_1_output = [[1.0, 2.0, 0.0], [8.0, 1.0, 6.0], [0.0, 0.0, 1.0]]
    example_file_2_output = [[(1.21+0j), (2.01+0j), 1.4j], [-1.0, 2.06j, 1.0], [0.0, -1.0, (2.223+1.005j)]]

    if vecop.file_parser(filename = "example_set.csv") == example_file_1_output:
        file_count += 1
    if vecop.file_parser(filename = "example_complex_set.csv") == example_file_2_output:
        file_count += 1

    return file_count

if __name__ == "__main__":
    total_tests = 15
    norm_tests = norm_squared_testing()
    dot_tests = dot_product_testing()
    proj_tests = projection_testing()
    orth_tests = orthogonalisation_testing()
    file_tests = file_parser_testing()

    total_passed = norm_tests + dot_tests + proj_tests + orth_tests + file_tests
    if total_passed == total_tests:
        print("All {0} tests have passed successfully.".format(total_tests))
    else:
        print("Error: Only {0} tests have passed out of a total of {1} tests.".format(total_passed,total_tests))
        if norm_tests != 3:
            print("Error: The norm_squared function failed to pass all it's tests.")
        if dot_tests != 3:
            print("Error: The dot_product function failed to pass all it's tests.")
        if proj_tests != 2:
            print("Error: The projection function failed to pass all it's tests.")
        if orth_tests != 5: 
            print("Error: The orthogonalisation function failed to pass all it's tests.")
        if file_tests != 2:
            print("Error: The file_parser function failed to pass all it's tests.")
    