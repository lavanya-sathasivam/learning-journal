# Program 1: Palindrome Checker
text=input("Enter a word: ")
if text==text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")




# Program 2: Count Vowels
text=input("Enter text: ")
c=0
for ch in text.lower():
    if ch in "aeiou":
        c+=1
print("Vowels:",c)




# Program 3: Character Frequency
text=input("Enter text: ")
freq={}
for ch in text:
    freq[ch]=freq.get(ch,0)+1
print(freq)