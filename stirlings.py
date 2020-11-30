# Python3 program for calculating  
# factorial of a number using  
# Stirling Approximation  
import math

# Function for calculating factorial 
def stirlingLowerBound(n): 
    if (n == 1): 
        return 1
      
    # value of natural e 
    e = 2.71828
    pi = 3.141592653589793

      
    # evaluating lower bound of inequality using 
    # stirling approximation 
    a = (math.sqrt(2 * pi * n) * math.pow((n / e), n)) * math.pow(e, 1/((12*n)+1))
    return math.floor(a)

def stirlingUpperBound(n): 
    if (n == 1): 
        return 1
      
    # value of natural e 
    e = 2.71828
    pi = 3.141592653589793

      
    # evaluating upper bound of inequality using 
    # stirling approximation 
    a = (math.sqrt(2 * pi * n) * math.pow((n / e), n)) * math.pow(e, 1/((12*n)))
    return math.floor(a)
  
# Main Code 
print(str(stirlingLowerBound(1)) + " < "   + "1!" + " < " + str(stirlingUpperBound(1))) 
print(str(stirlingLowerBound(2)) + " < "   + "2!" + " < " + str(stirlingUpperBound(2))) 
print(str(stirlingLowerBound(3)) + " < "   + "3!" + " < " + str(stirlingUpperBound(3))) 
print(str(stirlingLowerBound(4)) + " < "   + "4!" + " < " + str(stirlingUpperBound(4))) 
print(str(stirlingLowerBound(5)) + " < "   + "5!" + " < " + str(stirlingUpperBound(5))) 
print(str(stirlingLowerBound(6)) + " < "   + "6!" + " < " + str(stirlingUpperBound(6))) 
print(str(stirlingLowerBound(7)) + " < "   + "7!" + " < " + str(stirlingUpperBound(7))) 
print(str(stirlingLowerBound(8)) + " < "   + "8!" + " < " + str(stirlingUpperBound(8))) 
print(str(stirlingLowerBound(9)) + " < "   + "9!" + " < " + str(stirlingUpperBound(9))) 
