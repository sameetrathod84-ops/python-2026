def func(a,b =5, c =10):
    poly=2*a**2-5*b+c
    print("with values",a,b,c)
    print(poly)

func(3,7) #function call 1
func(25,c=24) # function call 2
func(c=50, a=100) #function call 3
