import math

print("============================")
print("STUDENT PERFORMANCE ANALYZER")
print("============================")
print()

student_name = input("Enter student name: ")
try:
    quiz1_score = float(input("Enter Quiz 1 score: "))
    quiz2_score = float(input("Enter Quiz 2 score: "))
    quiz3_score = float(input("Enter Quiz 3 score: "))
    quiz4_score = float(input("Enter Quiz 4 score: "))
    quiz5_score = float(input("Enter Quiz 5 score: "))
    
    total = quiz1_score + quiz2_score + quiz3_score + quiz4_score + quiz5_score
    average = total/5
    highest = max(quiz1_score, quiz2_score, quiz3_score, quiz4_score, quiz5_score)
    lowest = min(quiz1_score, quiz2_score, quiz3_score, quiz4_score, quiz5_score)
    
    print()
    print("==================")
    print("PERFORMANCE REPORT")
    print("==================")
    print()
    print("Student: ", student_name)
    print("Total Score: ", total)
    print("Average Score: ", average)
    print("Highest Score: ", highest)
    print("Lowest Score: ", lowest)
    if average >= 90:
        print("Performance: Excellent")
    elif average >= 80 and average < 89.99:
        print("Performance: Very Good")
    elif average >= 75 and average < 79.99:
        print("Performance: Good")
    elif average < 75:
        print("Performance: Needs Improvement")
    print("==================================")
    print("Report Generated: August 14, 2026")
    print("==================================")
        
except ValueError:
    print("Enter numbers only.")