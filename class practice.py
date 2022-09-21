#print reverse ordered list
x=eval(input("your text :"))
print(x)
def reverse_order(a):
    l=[]
    for i in range (len(a)-1,-1,-1):
        l.append(a[i])
    print(l)
reverse_order(x)


#a function that return the GCD/HCF  given two numbers
A=eval(input("your two numbers :"))
print(A)