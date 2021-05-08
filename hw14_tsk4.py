num = int(input("Enter a number: "))  
  
def isprime(num):
   if num > 1:
      for i in range(2,num):
         if (num % i) == 0:
            return False
      else:
         return True

         
   else:
      return None
print(isprime(num))
