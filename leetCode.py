nums = int(input("Masukkan jumlah bilangan Fibonacci: "))  
x, y = 0, 1  
i = 0  
while i < nums:  
    print(x, end=" ")
    x, y = y, x + y   
    i += 1  