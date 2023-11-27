#This file contains the unit tests for the return service microservice.

#Importing libraries and files
import ReturnService as return_service

#A number of thorough testing has been conducted in this file.
#The testing ensures that the return service is displayed on the screen properly

#Defining global variables
tests_passed = 0 #This is the number of tests passed
total_tests = 0 #This is the total number of tests in this file
index=1 #Counter of test number

#This function is used to signal the start of unit testing for return service microservice
def start():
    
    print("") #blank line
    print("----------------------------------------------------------------------------------------------------------")
    print("STARTING UNIT TESTS FOR RETURN SERVICE MICROSERVICE")
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


#This function is used to run the main tests and ensure that the return service service is functioning correctly
def run_tests():

    #Testing starts
    global index

    #Test 1
    result = return_service.format_result({'addition_result': 42})
    expected = ['{"result": 42}', 200, {'X-Custom-Header': 'custom-value'}, 'application/json; charset=utf-8']
    solve(index, result, expected)

    #Test 2
    result = return_service.format_result({'addition_result': 100000000000})
    expected = ['{"result": 100000000000}', 200, {'X-Custom-Header': 'custom-value'}, 'application/json; charset=utf-8']
    solve(index, result, expected)

    #Test 3
    result = return_service.format_result({'addition_result': 'hello world'})
    expected = ['{"result": hello world}', 200, {'X-Custom-Header': 'custom-value'}, 'application/json; charset=utf-8']
    solve(index, result, expected)

    #Test 4
    result = return_service.format_result({'addition_result': '!@#$%^&*()'})
    expected = ['{"result": !@#$%^&*()}', 200, {'X-Custom-Header': 'custom-value'}, 'application/json; charset=utf-8']
    solve(index, result, expected)

    #Test 5
    result = return_service.format_result({'addition_result': 1345679878946321})
    expected = ['{"result": 1345679878946321}', 200, {'X-Custom-Header': 'custom-value'}, 'application/json; charset=utf-8']
    solve(index, result, expected)

    #Test 6
    result = return_service.format_result({'addition_result': -8764287})
    expected = ['{"result": -8764287}', 200, {'X-Custom-Header': 'custom-value'}, 'application/json; charset=utf-8']
    solve(index, result, expected)

    #Test 7
    result = return_service.format_result({'addition_result': 'THIS IS A REALLY LONG STRING COMPARED TO WHAT WILL USUALLY BE GIVEN !!!!! THIS IS A REALLY LONG STRING COMPARED TO WHAT WILL USUALLY BE GIVEN !!!!! THIS IS A REALLY LONG STRING COMPARED TO WHAT WILL USUALLY BE GIVEN !!!!!'})
    expected = ['{"result": THIS IS A REALLY LONG STRING COMPARED TO WHAT WILL USUALLY BE GIVEN !!!!! THIS IS A REALLY LONG STRING COMPARED TO WHAT WILL USUALLY BE GIVEN !!!!! THIS IS A REALLY LONG STRING COMPARED TO WHAT WILL USUALLY BE GIVEN !!!!!}', 200, {'X-Custom-Header': 'custom-value'}, 'application/json; charset=utf-8']
    solve(index, result, expected)

    #Test 8
    result = return_service.format_result({'addition_result': None})
    expected = ['{"result": None}', 200, {'X-Custom-Header': 'custom-value'}, 'application/json; charset=utf-8']
    solve(index, result, expected)

    #Test 9
    result = return_service.format_result({'addition_result': ''})
    expected = ['{"result": }', 200, {'X-Custom-Header': 'custom-value'}, 'application/json; charset=utf-8']
    solve(index, result, expected)

    #Test 10
    result = return_service.format_result({'addition_result': '-----'})
    expected = ['{"result": -----}', 200, {'X-Custom-Header': 'custom-value'}, 'application/json; charset=utf-8']
    solve(index, result, expected)

    #Test 11
    result = return_service.format_result({'addition_result': 3|4})
    expected = ['{"result": 7}', 200, {'X-Custom-Header': 'custom-value'}, 'application/json; charset=utf-8']
    solve(index, result, expected)

    #End of function
    return

#This function is used to signal the end of unit testing for the return service microservice and print the end results
def end():

    print("") #blank line
    print(f"[INFO]      TESTS PASSED: {tests_passed} / {total_tests}")
    print("") #blank line
    print("END OF UNIT TESTS FOR RETURN SERVICE MICROSERVICE")
    print("----------------------------------------------------------------------------------------------------------")
    print("") #blank line


#Controlling the execution of the above defined test functions
start() #print function to signal the start of tests
run_tests() #This function runs the main tests
end() #print function to signal the end of tests

#End of file