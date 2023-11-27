#This file contains the unit tests for the addition microservice.

#Importing libraries and files
import AdditionService as addition

#A number of thorough testing has been conducted in this file.
#The testing ensures that the correct addition of numbers is conducted

#Defining global variables
tests_passed = 0 #This is the number of tests passed
total_tests = 0 #This is the total number of tests in this file
index=1 #Counter of test number

#This function is used to signal the start of unit testing for addition microservice
def start():
    
    print("") #blank line
    print("----------------------------------------------------------------------------------------------------------")
    print("STARTING UNIT TESTS FOR ADDITION MICROSERVICE")
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


#This function is used to run the main tests and ensure that the addition is functioning correctly
def run_tests():

    #Testing thoroughly / Stress testing with large inputs
    global index

    #Test 1
    data = [1, 2, 3, 4, 5]
    result = addition.add(data)
    expected = sum(data)
    solve(index, result, expected)

    #Test 2
    data = [10, 20, 30, 40, 50]
    result = addition.add(data)
    expected = sum(data)
    solve(index, result, expected)

    #Test 3
    data = [500, 600, 700, 800, 900]
    result = addition.add(data)
    expected = sum(data)
    solve(index, result, expected)

    #Test 4
    data = [1000, 2000, 3000, 4000, 5000]
    result = addition.add(data)
    expected = sum(data)
    solve(index, result, expected)

    #Test 5
    data = [3, 6, 9, 12, 15]
    result = addition.add(data)
    expected = sum(data)
    solve(index, result, expected)

    #Test 6
    data = [125, 250, 375, 500, 625]
    result = addition.add(data)
    expected = sum(data)
    solve(index, result, expected)

    #Test 7
    data = [-25, -50, -75, -100, -125]
    result = addition.add(data)
    expected = sum(data)
    solve(index, result, expected)

    #Test 8
    data = [-3, 6, -9, 12, -15]
    result = addition.add(data)
    expected = sum(data)
    solve(index, result, expected)

    #Test 9
    data = [-250, 350, -450, 550, -650]
    result = addition.add(data)
    expected = sum(data)
    solve(index, result, expected)

    #Test 10
    data = [-75, 150, -225, 300, -375]
    result = addition.add(data)
    expected = sum(data)
    solve(index, result, expected)

    #Test 11
    data = [25, -50, 75, -100, 125]
    result = addition.add(data)
    expected = sum(data)
    solve(index, result, expected)

    #Test 12
    data = []
    result = addition.add(data)
    expected = sum(data)
    solve(index, result, expected)

    #Test 13
    data = [0, 0, 0]
    result = addition.add(data)
    expected = sum(data)
    solve(index, result, expected)

    #Test 14
    data = [100000000000, 80808080800, 23230]
    result = addition.add(data)
    expected = sum(data)
    solve(index, result, expected)

    #Test 15
    data = [-1, 80808080800, -23230]
    result = addition.add(data)
    expected = sum(data)
    solve(index, result, expected)
    

    #End of function
    return

#This function is used to signal the end of unit testing for the addition microservice and print the end results
def end():

    print("") #blank line
    print(f"[INFO]      TESTS PASSED: {tests_passed} / {total_tests}")
    print("") #blank line
    print("END OF UNIT TESTS FOR ADDITION MICROSERVICE")
    print("----------------------------------------------------------------------------------------------------------")
    print("") #blank line


#Controlling the execution of the above defined test functions
start() #print function to signal the start of tests
run_tests() #This function runs the main tests for the addition microservice and ensures that it is functioning properly
end() #print function to signal the end of tests

#End of file