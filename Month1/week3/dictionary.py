# Program 1: Student Grade System
students={"Ram":85,"Priya":92,"Kumar":78}
name=input("Enter student name: ")
if name in students:
    print(students[name])
else:
    print("Not Found")



# Program 2: Word Frequency Counter
text="python python java c python java"
words=text.split()
freq={}
for word in words:
    freq[word]=freq.get(word,0)+1
print(freq)



# Program 3: Employee Database
employee={101:"John",102:"David",103:"Sara"}
for id, name in employee.items():
    print(id,name)