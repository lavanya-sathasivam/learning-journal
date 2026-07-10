# Program 1: Product Information
prod=("Laptop",55000,"Dell")
print("Name:",prod[0])
print("Price:",prod[1])
print("Brand:",prod[2])



# Program 2: Swap Values Using Tuple Packing
a=10
b=20
a,b=b,a
print(a,b)




# Program 3: Student Records
students=(("Ram",85),("Priya",92),("Kumar",78))
for name,mark in students:
    print(name,mark)