def average(marks):
    return sum(marks)/len(marks)

def display(stud):
    print("STUDENT REPORT")
    print(f"Name       : {stud['name']}")
    print(f"Roll No    : {stud['roll_no']}")
    print(f"Marks      : {stud['marks']}")
    print(f"Average    : {stud['average']:.2f}")
    print(f"Grade      : {stud['grade']}")

def grade(avg):
    if avg>=90:
        return "A+"
    elif avg>=80:
        return "A"
    elif avg>=70:
        return "B"
    elif avg>=60:
        return "C"
    elif avg>=50:
        return "D"
    else:
        return "F"
    
def main():
    name=input("Enter student name: ")
    roll_no=input("Enter roll number: ")
    marks=[]
    sub=["Python","Java","C","AIML"]
    for i in sub:
        mark=int(input(f"Enter marks for {i}: "))
        marks.append(mark)

    avg=average(marks)
    grd=grade(avg)
    student={
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "average": avg,
        "grade": grd
    }
    display(student)

if __name__=="__main__":
    main()