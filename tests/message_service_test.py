#This file contains the unit tests for the message microservice.

#Importing libraries and files
import message_service as message

#A number of thorough testing has been conducted in this file.
#The testing ensures that the message is displayed on the screen properly

#Defining global variables
tests_passed = 0 #This is the number of tests passed
total_tests = 0 #This is the total number of tests in this file
index=1 #Counter of test number

#This function is used to signal the start of unit testing for message microservice
def start():
    
    print("") #blank line
    print("----------------------------------------------------------------------------------------------------------")
    print("STARTING UNIT TESTS FOR MESSAGE MICROSERVICE")
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


#This function is used to run the main tests and ensure that the message service is functioning correctly
def run_tests():

    #Testing starts
    global index

    #Test 1
    result = message.get_message()
    expected = "I love Software Engineering in Industry"
    solve(index, result, expected)

    #Test 2
    result = message.get_message() + message.get_message()
    expected = "I love Software Engineering in IndustryI love Software Engineering in Industry"
    solve(index, result, expected)

    #Test 3
    result = message.get_message() + message.get_message() + message.get_message()
    expected = "I love Software Engineering in IndustryI love Software Engineering in IndustryI love Software Engineering in Industry"
    solve(index, result, expected)

    #End of function
    return

#This function is used to signal the end of unit testing for the message microservice and print the end results
def end():

    print("") #blank line
    print(f"[INFO]      TESTS PASSED: {tests_passed} / {total_tests}")
    print("") #blank line
    print("END OF UNIT TESTS FOR MESSAGE MICROSERVICE")
    print("----------------------------------------------------------------------------------------------------------")
    print("") #blank line


#Controlling the execution of the above defined test functions
start() #print function to signal the start of tests
run_tests() #This function runs the main tests
end() #print function to signal the end of tests

#End of file