def numbers(n):
    if n>0:
        numbers(n-1)
        print(n,end=" ")
    return " "
    
n=int(input())
print(numbers(n))