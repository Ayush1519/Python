n=int(input("Enter n: "))
if n%3==0 and n%6!=0:
    print(n)

n = int(input("Enter n: "))
reverse = 0  

while n > 0:
    digit = n % 10     
    reverse = reverse * 10 + digit  
    n = n // 10            

print("Reversed number:", reverse)  

n= int(input("Enter n: ")) # question no 1
if(n%2 == 0):
    print("Even")
else:   print("Odd")
