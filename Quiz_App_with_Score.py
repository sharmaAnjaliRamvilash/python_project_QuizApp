import random
# a terminal quiz that asks multiple-choice questions, checks answers, keeps score, shuffles questions, and saves your high score to a file. It practices lists, dictionaries, loops, functions, input validation, random, and JSON, all common interview topics.

# Plan (about 7 steps):

# Store questions in a list of dictionaries
# Write a function to ask one question
# Loop through all questions and keep score
# Validate user input
# Shuffle the questions
# Show the result and grade
# Save the high score in a file


#   to store the quesstions
Questions = [
     {
         "Question":"Which keyword is used to define a function in Python?",
         "Options": ["def","function","define","func"],
          "Answer":1
     },
     {
          "Question":"What is the output of 10 // 3 ?",
                  "Options":["3.33", "3", "4", "1"],
                   "Answer": 2
         
         
     },
     {
          "Question":"Which brackets are used to create a list in Python?",
          "Options": ["()", "[]", "{}", "<>"],
          "Answer": 2
         
     },
     {
           "Question":"What is the output of len('Python')?",
          "Options": ["5", "6", "7", "Error"],
          "Answer": 2
         
     }
]

random.shuffle(Questions)
first =  Questions[0]
#jis par iterate karna ho uska naam bhi ham likhate h

# print(first["Question"])
# for i,Options in  enumerate( first["Options"],start=1):
#     print(f"{i}.{Options}")

def get_answer(total_options):
     while True:
         try:
             ans = int(input("Enter the answer"))
             if 1<=ans<=total_options:
                 return ans
             else:
                 print("Please enter the answer in valid range")
         except ValueError:
             print("Only numbers are allowed")
        
    


def ask_questions(q):
    print("\n" + q["Question"])
    for i,Options in enumerate(q["Options"],start=1):
        print(f"{i}. {Options}")

    ans = get_answer(len(q["Options"]))

    if ans == q["Answer"]:
        print("Corrected")
        return 1
    else:
        print("Not Corrected")
        return 0

    
        

    

random.shuffle(Questions)
score =0
for q in Questions:
   score += ask_questions(q)


def show_result(scrore,total):
    percent = score/total*100
    print("\n===== RESULT =====")
    print(f"Your score is {score} out of {len(Questions)}")
    if percent>=90:
        print("Grade      : Excellent!")
    elif percent>=80<=90:
        print("Grade      : Very Good!")
    elif percent>=70<=80:
        print("Grade      : Good, keep practising.")


show_result(score, len(Questions))









