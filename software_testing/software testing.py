# A sample python code to automate the testing of the sample class having basic functionalities of to perform the mathematical operations on the specified operands of that particular function.

# All the required modules which are required across the program are included at the beginning of the code.
import unittest
import sys

A class is written which has different functions to perform the different mathematical operations depending upon the input provided the mathematical operation is performed on the two operands which are taken as input for each function,  the class which is written below is the child class of the test case class from the unit test module, with the help of this parenting test case class we were able to use various inbuilt functions of the test case class which help us to write various test case function to test the mathematical results which are calculated by the various function written inside this class


class BasicMathOperationsTesting(the unit test.TestCase):
    # Constructor is written which can be used to initialize the various class variable that is required to use throughout this class a variable that is declared inside the constructor of a class can be used across the scope of that particular class
    def __init__(self):
        pass


# A function is written  in which the user is asked for two numbers on which the addition operation is performed,  once the user provides the two numbers on which the addition operation is need to perform,  that particular operation is performed on the provided two numbers and the result of that operation is stored in a resultant variable  and that resultant variable is returned as the return value of this function,  and then this return value can be used in various test function which will validate or test the particular operation performed by this function is correct or not by using various inbuilt methods of the test case class

    def perform_addition(self):
        operation_name = "addition"
        print("Enter the first number for {} operation".format(operation_name))
        num_1 = int(input())
        print("Enter the second number for {} operation".format(operation_name))
        num_2 = int(input())

        resultant = num_1 + num_2
        return resultant

# A function is written  in which the user is asked for two numbers on which the subtraction operation is performed,  once the user provides the two numbers on which the subtraction  operation is need to perform,  that particular operation is performed on the provided two numbers and the result of that operation is stored in a resultant variable  and that resultant variable is returned as the return value of this function,  and then this return value can be used in various test function which will validate or test the particular operation performed by this function is correct or not by using various inbuilt methods of the test case class
    def perform_subtraction(self):
        operation_name = "subtraction"
        print("Enter the first number for {} operation".format(operation_name))
        num_1 = int(input())
        print("Enter the second number for {} operation".format(operation_name))
        num_2 = int(input())

        resultant = num_1 - num_2
        return resultant
# A function is written  in which the user is asked for two numbers on which the multiplication operation is performed,  once the user provides the two numbers on which the multiplication  operation is needed to perform,  that particular operation is performed on the provided two numbers and the result of that operation is stored in a resultant variable  and that resultant variable is returned as the return value of this function,  and then this return value can be used in various test function which will validate or test the particular operation performed by this function is correct or not by using various inbuilt methods of the test case class

    def perform_multiplication(self):
        operation_name = "multiplication"
        print("Enter the first number for {} operation".format(operation_name))
        num_1 = int(input())
        print("Enter the second number for {} operation".format(operation_name))
        num_2 = int(input())

        resultant = num_1 + num_2
        return resultant

# A function is written  in which the user is asked for two numbers on which the division operation is performed,  once the user provides the two numbers on which the division  operation is needed to perform,  that particular operation is performed on the provided two numbers and the result of that operation is stored in a resultant variable  and that resultant variable is returned as the return value of this function,  and then this return value can be used in various test function which will validate or test the particular operation performed by this function is correct or not by using various inbuilt methods of the test case class
    def perform_division(self):
        operation_name = "division"
        print("Enter the first number for {} operation".format(operation_name))
        num_1 = int(input())
        print("Enter the second number for {} operation".format(operation_name))
        num_2 = int(input())

        resultant = num_1 / num_2
        return resultant

# This is a test function which is written for testing the assert equal values which means  this test case will be fast if the two values which are passed as parameters to this function  are equal,  so we have used this assert equal functions to test the various mathematical operations which are performed using the various function which is written above so, for example, let's say perform the addition operation of two variables which are passed as a parameter to that function so to verify that the addition operation performed that particular function is correct or not is then with the help of this function in which first parameter we passed as the actual value will be the value which  is the value which is calculated by the function which is written above and the expected value is the value which is expected to be matched with this function so so if both of these values matches then they assert equal test case will be passed on the other hand if the both of these values are not equal then the assert equal test case will fail
    def the unit test_for_assert_equals(self, actual_value, expected_value):

        actual_value_for_equals = actual_value
        expected_value_for_equals = expected_value
        self.assertEqual(actual_value_for_equals, expected_value_for_equals)


# This is another unit test case which we have written named assert true that means this function will return require a Boolean value and depending upon the value of the that boolean variable the nature of the resultant test case is dertemined so in this function we are using the assert false functionality of the unit test case class to test the actual and expected output of a mathematical operations so we are passing the oeprand one as the actual value by actual value we mean the value which is actually calculated by the any of the above written mathematical operation let's say multiplication so the resultant of the multiplication function is passed as the first operand to this function and the second operand which is passed to this function is the expected value or which is meant to be the actual output of that function and both of these operations are compared and stored into a variable since the comparison is done on two operands return type is a Boolean value show the variable storing those values will be a Boolean variable and that Boolean variable will be passed to the assert false function if that  Boolean variable is having the true value then the test function will be passed on the other hand if the value is fasle the assert true unit test case will be failed

    def the unit test_for_assert_true(self, operand1, operand2):

        boolean_resultant = operand1 == operand2
        self.assertTrue(boolean_resultant)


# This is another unit test case which we have written named assert false that means this function will return require a Boolean value and depending upon the value of the that boolean variable the nature of the resultant test case is dertemined so in this function we are using the assert false functionality of the unit test case class to test the actual and expected output of a mathematical operations so we are passing the oeprand one as the actual value by actual value we mean the value which is actually calculated by the any of the above written mathematical operation let's say multiplication so the resultant of the multiplication function is passed as the first operand to this function and the second operand which is passed to this function is the expected value or which is meant to be the actual output of that function and both of these operations are compared and stored into a variable since the comparison is done on two operands return type is a Boolean value show the variable storing those values will be a Boolean variable and that Boolean variable will be passed to the assert false function if that  Boolean variable is having the fasle value then the test function will be passed on the other hand if the value is true the assert fasle unit test case will be failed

    def the unit test_for_assert_false(self, operand1, operand2):

        boolean_resultant = operand1 != operand2
        self.assertFalse(boolean_resultant)


#  In The End the main function is written,  which has the object of the above-written class Which is used to call all the methods which are written inside the class. the user is provided with the list of menus from which he has to select the mathematical operation which he performs on the two inputs which are going he is going to provide after selecting the appropriate mathematical operation the result of that mathematical operation is presented to the user and another menu is printed from which the type of unit test which needs to be Run on that obtained result is  shown,  on selecting the appropriate unit test which will run on the result of the mathematical operation that particular test case is Run and depending upon the unit test which is selected by the user appropriate message is shown,  that means if the test case is passed it is shown that that particular test case has been passed successfully on the other hand if the test case is failed due to some exception or error that has been encountered during the execution of that particular unit test case,  then that particular exception or error message is printed to the user and which line has caused that an exception message is also presented to the user this helps in the debugging so that user can understand by which particular line of code that particular unit test is failing this printing of the menu is done in a recursive manner until the user exits the code execution by selecting the last option which is to exit the code execution.
def main():

    run_the unit test = BasicMathOperationsTesting()

    while (True):

        # from the listed below the list of operations select any one of the operations
        print("Select any of the mathematical operations which are listed below:")
        print("1. To perform the addition operation and then perform the unit test on the result obtained.")
        print("2. To perform the subtraction operation and then perform the unit test on the result obtained.")
        print("3. To perform the multiplication operation and then perform the unit test on the result obtained.")
        print("4. To perform the division operation and then perform the unit test on the result obtained.")
        print("5. To exit from the code execution.")

        menu_choice = input()
        menu_choice = int(menu_choice)

        if menu_choice == 1:
            result = run_the unit test.perform_addition()
        elif menu_choice == 2:
            result = run_the unit test.perform_subtraction()
        elif menu_choice == 3:
            result = run_the unit test.perform_multiplication()
        elif menu_choice == 4:
            result = run_the unit test.perform_division()
        elif menu_choice == 5:
            sys.exit()

        print("Select any of the unit tests to perform which are listed below:")
        print("1. To perform the assertEqual the unit test on the above done mathematical operation.")
        print("2. To perform the assertTrue the unit test on the above done mathematical operation.")
        print("3. To perform the assertFalse the unit test on the above done mathematical operation.")

        menu_choice_for_unitttest = input()
        menu_choice_for_unitttest = int(menu_choice_for_unitttest)

        if menu_choice_for_unitttest == 1:
            print("Expected value for test to pass:")
            expected_value = int(input())
            run_the unit test.the unit test_for_assert_equals(result, expected_value)
        elif menu_choice_for_unitttest == 2:
            print("Expected value for test to pass:")
            expected_value = int(input())
            run_the unit test.the unit test_for_assert_true(result, expected_value)
        elif menu_choice_for_unitttest == 3:
            print("Expected value for test to pass:")
            expected_value = int(input())
            run_the unit test.the unit test_for_assert_false(result, expected_value)

        print(
            "To go on with the code getting executed, enter input [y] or [n]")
        continue_or_exit = input()

        if continue_or_exit == 'y' or continue_or_exit == 'Y':
            pass
        elif continue_or_exit == 'n' or continue_or_exit == 'N':
            sys.exit()


if __name__ == '__main__':
    main()
