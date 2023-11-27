#This file contains the unit tests for the addition microservice.

#Importing libraries and files
import timestamp_service as time_service
from datetime import datetime

#A number of thorough testing has been conducted in this file.
#The testing ensures that the correct timestamp is displayed to user

#Defining global variables
tests_passed = 0 #This is the number of tests passed
total_tests = 0 #This is the total number of tests in this file
index=1 #Counter of test number

#This function is used to signal the start of unit testing for the microservice
def start():
    
    print("") #blank line
    print("----------------------------------------------------------------------------------------------------------")
    print("STARTING UNIT TESTS FOR TIMESTAMP MICROSERVICE")
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


#This function is used to run the main tests and ensure that the microservice is functioning correctly
def run_tests():

    #Testing thoroughly / Stress testing with large inputs
    global index

    #Test 1
    result = time_service.get_timestamp()
    expected = str(datetime.now())
    solve(index, result, expected)

    #Test 2
    result = time_service.get_timestamp() + time_service.get_timestamp()
    expected = str(datetime.now()) + time_service.get_timestamp()
    solve(index, result, expected)

    #Test 3
    result = time_service.get_timestamp() + time_service.get_timestamp() + time_service.get_timestamp()
    expected = str(datetime.now()) + time_service.get_timestamp() + time_service.get_timestamp()
    solve(index, result, expected)

    #Tests 4-8
    for _ in range(0,5):
        result = time_service.get_timestamp()
        expected = str(datetime.now())
        solve(index, result, expected)

    #End of function
    return

#This function is used to signal the end of unit testing for the microservice and print the end results
def end():

    print("") #blank line
    print(f"[INFO]      TESTS PASSED: {tests_passed} / {total_tests}")
    print("") #blank line
    print("END OF UNIT TESTS FOR TIMESTAMP MICROSERVICE")
    print("----------------------------------------------------------------------------------------------------------")
    print("") #blank line


#Controlling the execution of the above defined test functions
start() #print function to signal the start of tests
run_tests() #This function runs the main tests for the microservice and ensures that it is functioning properly
end() #print function to signal the end of tests

#End of file