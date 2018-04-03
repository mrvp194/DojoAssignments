import random

def grades() :
    print "Scores and Grades"
    for num in range(10) :
        score = random.randint(60, 100)
        if score >= 60 and score <= 69 :
            grade = "D"
        elif score >= 70 and score <= 79 :
            grade = "C"
        elif score >= 80 and score <= 89 :
            grade = "B"
        elif score >= 90 and score <= 100 :
            grade = "A"
        print "Score: {}; Your grade is {}".format(score, grade)
    print "End of the program. Bye!"

grades()