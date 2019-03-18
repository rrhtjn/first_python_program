number = input("Enter the number :")

digit_words= {
 "0" : "Zero",
 "1":"one",
 "2":"two",
 "3" : "three",
 "4" : "four",
 "5" : "five",
 "6" : "six",
 "7" : "seven",
 "8" : "eight",
 "9" : "nine"
}
output=""
for ch in number:
    output+=digit_words.get(ch,"! ") +'  '

print(output)