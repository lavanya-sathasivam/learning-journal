# Program 1: Student Marks Analyzer
marks=[78,65,89,90,55,72]
print("Highest:",max(marks))
print("Lowest:",min(marks))
print("Average:",sum(marks)/len(marks))



# Program 2: Remove Duplicates
nums=[1,2,3,2,4,5,1,6]
uniq=[]
for num in nums:
    if num not in uniq:
        uniq.append(num)
print("Unique Numbers:",uniq)



# Program 3: Second Largest Number
num=[10,45,67,23,89,34]
num.sort()
print("Second Largest:",num[-2])