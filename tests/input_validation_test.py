#This file contains the unit tests for the input validation microservice.

#Importing libraries and files
import InputValidationService as input_service

#A number of thorough testing has been conducted in this file.
#The testing ensures that the correct input validation of numbers is conducted

#Defining global variables
tests_passed = 0 #This is the number of tests passed
total_tests = 0 #This is the total number of tests in this file
index=1 #Counter of test number

#This function is used to signal the start of unit testing for input validation microservice
def start():
    
    print("") #blank line
    print("----------------------------------------------------------------------------------------------------------")
    print("STARTING UNIT TESTS FOR INPUT VALIDATION MICROSERVICE")
    print("") #blank line
    
    return
    #End of function


#Helper function to print the results
def solve(i, result, expected):

    global tests_passed
    global total_tests
    global index

    #Print message for TEST number
    print(f"[INFO]      TEST {i}: ", end="")
    if result==expected:
        print("PASSED")
        tests_passed+=1
    else:
        print("FAILED")
    
    total_tests+=1
    index+=1

    return
    #End of function


#This function is used to run the main tests and ensure that the input validation is functioning correctly
def run_tests():

    #Testing thoroughly / Stress testing with large inputs
    global index

    #Test 1
    data = [1, 2, 3, 4, 5]
    result = input_service.validate(data)
    expected = True
    solve(index, result, expected)

    #Test 2
    data = [1, 2.5, 3, 4.2, 5]
    result = input_service.validate(data)
    expected = True
    solve(index, result, expected)

    #Test 3
    data = [0.5, 1.5, 2.5, 3.5, 4.5]
    result = input_service.validate(data)
    expected = True
    solve(index, result, expected)

    #Test 4
    data = [10, 20, 30.5, 40, 50]
    result = input_service.validate(data)
    expected = True
    solve(index, result, expected)

    #Test 5
    data = [-45251, 395638562, 4543, 4534534, -4455]
    result = input_service.validate(data)
    expected = True
    solve(index, result, expected)

    #Test 6
    data = []
    result = input_service.validate(data)
    expected = True
    solve(index, result, expected)

    #Test 7
    data = [None]
    result = input_service.validate(data)
    expected = False
    solve(index, result, expected)

    #Test 8
    data = ['hi', 'hello', 'Software Engineering', '!@#$%^&*()']
    result = input_service.validate(data)
    expected = False
    solve(index, result, expected)

    #Test 9
    data = [""]
    result = input_service.validate(data)
    expected = False
    solve(index, result, expected)

    #Test 10
    data = [3.09877]
    result = input_service.validate(data)
    expected = True
    solve(index, result, expected)

    #Test 11
    data = [5]
    result = input_service.validate(data)
    expected = True
    solve(index, result, expected)

    #Test 12
    data = "             "
    result = input_service.validate(data)
    expected = False
    solve(index, result, expected)

    #End of function
    return

#This function is used to signal the end of unit testing for the input validation microservice and print the end results
def end():

    print("") #blank line
    print(f"[INFO]      TESTS PASSED: {tests_passed} / {total_tests}")
    print("") #blank line
    print("END OF UNIT TESTS FOR INPUT VALIDATION MICROSERVICE")
    print("----------------------------------------------------------------------------------------------------------")
    print("") #blank line


#Controlling the execution of the above defined test functions
start() #print function to signal the start of tests
run_tests() #This function runs the main tests for the input validation microservice and ensures that it is functioning properly
end() #print function to signal the end of tests

#End of file