#This file contains the unit tests for the random number generator microservice.

#Importing libraries and files
import random
import random_number as rand

#A number of thorough testing has been conducted in this file.
#The testing ensures that the random number generator works correctly

#Defining global variables
tests_passed = 0 #This is the number of tests passed
total_tests = 0 #This is the total number of tests in this file
index=1 #Counter of test number

#This function is used to signal the start of unit testing for the microservice
def start():
    
    print("") #blank line
    print("----------------------------------------------------------------------------------------------------------")
    print("STARTING UNIT TESTS FOR RANDOM NUMBER GENERATOR MICROSERVICE")
    print("") #blank line
    
    return
    #End of function


#Helper function to print the results
def solve(i, array):

    global tests_passed
    global total_tests
    global index

    #Print message for TEST number
    print(f"[INFO]      TEST {i}: ", end="")
    
    count=0
    for i in array:
        if i == 0:
            count += 1
            if count == 10:
                print("FAILED")
                total_tests+=1
                index+=1
                return
        else:
            count = 0

    print("PASSED")
    tests_passed+=1
    
    total_tests+=1
    index+=1

    return
    #End of function


#This function is used to run the main tests and ensure that the microservice is functioning correctly
def run_tests():

    #Testing thoroughly
    global index

    #We are basically testing that if we run a random number generator 100 times over a range of 1 to 100,
    #then we should get a even spread of number where we atleast get 1 number is generated in every
    #consecutive interval of 10 numbers
    #We repeat the test multiple times and check if the generator is working correctly or not
    #Hence, we are basically trying to get a resonable amount of confidence that the random number generator is working correctly

    #Test 1
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)
    
    #Test 2
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 3
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 4
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 5
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 6
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 7
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 8
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 9
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 10
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 11
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 12
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 13
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 14
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 15
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 16
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 17
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 18
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 19
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)

    #Test 20
    array = [0] * 100
    for i in range(0,100):
        result=int(rand.get_random_number())
        array[result-1]+=1
    solve(index, array)
    
    #End of function
    return

#This function is used to signal the end of unit testing for the microservice and print the end results
def end():

    print("") #blank line
    print(f"[INFO]      TESTS PASSED: {tests_passed} / {total_tests}")
    print("") #blank line
    print("END OF UNIT TESTS FOR RANDOM NUMBER GENERATOR MICROSERVICE")
    print("----------------------------------------------------------------------------------------------------------")
    print("") #blank line


#Controlling the execution of the above defined test functions
start() #print function to signal the start of tests
run_tests() #This function runs the main tests for the microservice and ensures that it is functioning properly
end() #print function to signal the end of tests

#End of file