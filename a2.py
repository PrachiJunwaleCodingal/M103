def sum_n(n):
    return n * (n + 1) // 2  

print("Sum of first n numbers (n=5):", sum_n(5))
#space complexity= Θ(1) as there is no repeatation



#part2
def array_sum(a):
    total = 0
    for i in a:
        total += i
    return total
a = [12, 3, 4, 15]
print("Array sum:", array_sum(a))
##space complexity=Θ(n) as there are n numbers in array given as input



#part3
def summ(n):
    if n <= 0:
        return 0
    return n + summ(n - 1)

print("Recursive sum (n=5):", summ(5))
#space complexity=Θ(n)  as summ(5)=5+4+3+2+1, total 5 times