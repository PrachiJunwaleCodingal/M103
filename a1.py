def prints(n):
    if n <= 0:
        return

    print("Hello")
    prints(n // 2)
    prints(n // 2)


prints(4)

#This recursive function will take Time= T(n)=T(n/2)+T(n/2)+Θ(1)   for 2 recursive calls and 1 constant which is if n<0. 
# here n is input number