class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        max_int = pow(2,31) -1
        min_int = - pow(2,31)
        n_digit = int(math.log(abs(x), 10))
        sign = "negative"
        check = False
        if x>0 :
            min_int = 0
            sign = "positive"
            max_n_digit =  int(math.log(max_int, 10))
            if n_digit == max_n_digit :
                max_first_digit = int(max_int/pow(10,max_n_digit))
                if x%10 == max_first_digit:
                    #print("equal first digit as max limit, checks needed.")
                    check = True
                if x%10 > max_first_digit:
                    #print("first digit > limit, program exit - return 0")
                    return 0
                
        else:
            max_n_digit = int(math.log(abs(min_int), 10))
            if n_digit == max_n_digit:
                max_first_digit = int(abs(min_int)/pow(10,max_n_digit))
                print(max_first_digit)
                if abs(x)%10 == max_first_digit: 
                    #print("equal first digit as max limit, checks needed.")
                    check = True
                if abs(x)%10 > max_first_digit:
                    #print("first digit > limit, program exit - return 0")
                    return 0
        result = 0
        if not check :
            #print("Checks not needed")
            while x : 
                lastdigit = abs(x)%10
                result += int(lastdigit * pow(10,n_digit))
                x = int(abs(x)/10)
                n_digit -=1
                #print (f"Result so far : {result}")

        else:
            
            limit = max_int
            if sign == "negative":
                limit = abs(min_int)
            #print(f"careful checks needed for {x} with limit {limit}.")
            while x: 
                lastdigit = abs(x)%10
                if check and lastdigit > int(limit/ pow(10, n_digit)):
                    #print("limit crossed - program exit")
                    return 0
                else:
                    if lastdigit < int(limit/ pow(10, n_digit)):
                        check = False
                    result += int(lastdigit * pow(10,n_digit))
                    #print(f"present result = {result} and limit = {limit}")
                    x = int(abs(x)/10)
                    limit = int(limit% pow(10, n_digit))
                    n_digit -=1
                    
                    
               
                   
        

        if sign == "negative":
            result = result * (-1)
        
        return result





