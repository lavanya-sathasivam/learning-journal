# Program 1: Common Subjects
stud1={"Math","Physics","Python"}
stud2={"Python","Java","Physics"}
print(stud1 & stud2)



# Program 2: Unique Words
sent="python is easy and python is powerful"
word=sent.split()
print(set(word))



# Program 3: Union and Difference
A={1,2,3,4}
B={3,4,5,6}
print("Union:",A|B)
print("Difference:",A-B)