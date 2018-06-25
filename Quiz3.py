# This function takes two vectors, and returns the dot product of vector01
# and vector02.

def dot(vector01,vector02):
    """
    This function does the following.
    1: The function first checks to see if the vectors are list if they
       are not list the function prints Invalid Input and retruns None.
    2: The function defines a variable as isvalid and states the
       length of vector01 is equal to vector02 if the variable is False
       the function prints out Invalid Input and returns None
    3: The function then sets a variable titled answer.
    4: The function then implements a for loop and goes through the numbers in
       the entire length of the vectors and multiplies each element of vector1
       to each element of vector 2 and returns the dot product in the variable
       answer. 
    """
    if type(vector01) !=list or type(vector02) != list:
        print("Invalid Input")
        return None
    isvalid=len(vector01)==len(vector02)
    if isvalid is False:
        print("Invalid Input")
        return None
    answer=0
    for i in range(len(vector01)):
        answer+= vector01[i]*vector02[i]
    return answer

"""
1: Test 1 is the representation of vector one
2: Test 2 is the representation of vector two
3: the print function prints out the result for the function
   dot(vector01,vector02)
"""
test1=[1,2,3]
test2=[3,4,5]
print(dot(test1,test2))


# this function takes two vectors, and returns the vector that is equal to
# vector01-vector02


def vecsubtract(vector01,vector02):
    """
    The function vecsubtract(vector01,vector02) does the following.
    1: The function checks to see if vector01 or vector 02 is a list
       if its not a list the function prints out Invalid Input and returns
       None.
    2: The function sets a variable titled isvalid and states that
       the length of vector01 is equal to vector02. If the lenghts are not
       equal the function prints Invalid Input and returns None.
    3: The function sets a variable titled answer as an empty list.
    4: the function then goes through a for loop and goes through the numbers
       in the entire length of vector01, it then sets a variable titled
       addedanswer and in the variable addedanswer subtracts the elements in
       vector02 from the elements in vector01
       the results from addedanswer are then appended to the emptylist in the
       variable answer and returns the updated list in the variable answer. 
    """
    if type(vector01) != list or type(vector02) != list:
        print("Invalid Input")
        return None
    isvalid=len(vector01)==len(vector02)
    if isvalid is False:
        print("Invalid Input")
        return None
    answer=[]
    for i in range(len(vector01)):
        addedanswer = vector01[i]-vector02[i]
        answer.append(addedanswer)
    return answer
"""
test3 is the representation of vector01
test4 is the representation of vector02
the print function prints out the results from the function vecsubtract(vector01,vector02)
"""
test3=[1,2,3]
test4=[3,4,5]
print(vecsubtract(test3,test4))


# This function takes a scalar and a vector and multiplies them together.

def scalarvecmulti(scalar,vector):
    """
    The function scalarvecmulti(scalar,vector)
    1: The function first goes through and makes sure that the scalar is an
       integer and that the vector is a list. If the scalar is not an integer or
       the vector is not a list the function prints out "Invalid Input"
    2: The function then sets a variable titled sclaranswer as an empty list.
       The function then goes through a for loop and goes through all the
       numbers in the entire length of the vector
    4: the function then sets a variable as scalaranswer1 and in the variable
       multiplies the scalar by all the elements in the vector.
       the function then appends the results in scalaranswer1 to scalaranswer
       and returns the updated list in scalaranswer. 
       
    """
    if type(scalar) != int or type(vector) != list:
        print("Invalid Input")
        return None
    scalaranswer=[]
    for i in range(len(vector)):
        scalaranswer1=scalar*vector[i]
        scalaranswer.append(scalaranswer1)
    return scalaranswer

"""
test 5 is the representation of a scalar
test 6 is the representation of the vector
the print function then prints out the results in the function
scalarvecmulti(scalar,vector)
"""
test5=1
test6=[1,2,3]
print(scalarvecmulti(test5,test6))

# This function takes a vector and returns the infinity norm of that vector.

import math

def infnorm(vector):
    """
    The function infnorm(vector) does the following.
    1: The function first makes sure that the vector is a list if its not
       a list it prints out invalid Input and returns none.
    2: The function then sets a variable titled max_num and in the variable
       sets the vector in the first index.
    3: The function then goes through a for loop and goes through all the
       elements in the vector through the entire lenth. The for loop
       looks at every element starting with the first index and using the
       absolutevalue function imported from math checks every index
       and returns the largest absolute value element it finds throughout
       the entire length of the vector. 
    """
    if type(vector) != list:
        print("Invalid Input")
        return None
    max_num = vector[0]
    for i in range(len(vector)):
        if abs(vector[i]) > max_num:
            max_num = abs(vector[i])
    return max_num
"""
test7 is the representation of the vector.
the print function prints the result from the function infnorm(vector)
"""
test7 = [1,2,3]
print(infnorm(test7))

# This function takes a vector and returns the normalized vector with respect
# to the infinity norm.

def normalize(vector):
    """
    The Function normalize(vector) does the following
    1: The function first makes sure that the vector is a list if its not a list
       the function prints out Invalid Input and returns None
    2: the function sets a variable titled result_normalized as an empty list.
    3: The function then goes through a for loop and goes through all the
       elements through the entire length of the vector.
    4: a variable titled normalization is set and the vector is divided by
       the function infnorm(vector) defined earlier as a function.
    5: The program then appends the result in normalization to the empty list
       in the variable result_normalized and returns the updated list.
    """
    if type(vector) != list:
        print("Invalid Input")
        return None
    result_normalized=[]
    for i in range(len(vector)):
        normalization=vector[i]/infnorm(vector)
        result_normalized.append(normalization)
    return result_normalized
            
"""
the variable test is thr representation of the vector
the print function returns the result from the function normalize(vector)
"""
test8=[1,2,-3]
print(normalize(test8))
        
























































        
