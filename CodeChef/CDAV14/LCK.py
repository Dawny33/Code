import random

def MillerRabinPrimalityTest(number):
    '''
    because the algorithm input is ODD number than if we get
    even and it is the number 2 we return TRUE ( spcial case )
    if we get the number 1 we return false and any other even 
    number we will return false.
    '''
    if number == 2:
        return True
    elif number == 1 or number % 2 == 0:
        return False
    
    oddPartOfNumber = number - 1
    
    timesTwoDividNumber = 0
    
    while oddPartOfNumber % 2 == 0:
        oddPartOfNumber = oddPartOfNumber / 2
        timesTwoDividNumber = timesTwoDividNumber + 1 

    for time in range(3):
        
        while True:
            randomNumber = random.randint(2, number)-1
            if randomNumber != 0 and randomNumber != 1:
                break
        
        randomNumberWithPower = pow(randomNumber, oddPartOfNumber, number)
        
        if (randomNumberWithPower != 1) and (randomNumberWithPower != number - 1):
            # number of iteration
            iterationNumber = 1
            
            while (iterationNumber <= timesTwoDividNumber - 1) and (randomNumberWithPower != number - 1):
                randomNumberWithPower = pow(randomNumberWithPower, 2, number)
                
                # inc the number of iteration
                iterationNumber = iterationNumber + 1

            if (randomNumberWithPower != (number - 1)):
                return False
            
    return True 

def sum_digits3(n):
   r = 0
   while n:
       r, n = r + n % 10, n / 10
   return r

T = input()
strr = ""
while(T):
    T -= 1
    s = raw_input()
    s = int(s)
    if MillerRabinPrimalityTest(sum_digits3(s))==True:
        strr += "1"
    else:
        strr += "0"

print int(strr,2)
