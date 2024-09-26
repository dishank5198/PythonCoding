def percentage_calculator(marks_obtained, max_marks):
    if marks_obtained > max_marks:
        print("Marks obtained cannot be greater than max marks")
        return '-1'
    percent = (marks_obtained/max_marks)*100
    if percent >= 90:
        return 'A'
    elif 90 > percent >= 80:
        return 'B'
    elif 80 > percent >= 70:
        return 'C'
    elif 70 > percent >= 60:
        return 'D'
    elif 60 > percent >= 40:
        return 'E'
    elif percent < 40:
        return 'F'


if __name__ == '__main__':
    print("**********************************************")
    max_marks_pyh = int(input("Enter maximum marks for Physics: "))
    marks_obtained_phy = int(input("Enter marks obtained in Physics: "))
    grade_phy = percentage_calculator(marks_obtained_phy, max_marks_pyh)

    max_marks_chem = int(input("Enter maximum marks for Chemistry: "))
    marks_obtained_chem = int(input("Enter marks obtained in Chemistry: "))
    grade_chem = percentage_calculator(marks_obtained_chem, max_marks_chem)

    max_marks_bio = int(input("Enter maximum marks for Biology: "))
    marks_obtained_bio = int(input("Enter marks obtained in Biology: "))
    grade_bio = percentage_calculator(marks_obtained_bio, max_marks_bio)

    max_marks_math = int(input("Enter maximum marks for Maths: "))
    marks_obtained_math = int(input("Enter marks obtained in Maths: "))
    grade_math = percentage_calculator(marks_obtained_math, max_marks_math)

    max_marks_comp = int(input("Enter maximum marks for Computer: "))
    marks_obtained_comp = int(input("Enter marks obtained Computer: "))
    grade_comp = percentage_calculator(marks_obtained_comp, max_marks_comp)

    print("Grade obtained in Physics: " + grade_phy)
    print("Grade obtained in Chemistry: " + grade_chem)
    print("Grade obtained in Biology: " + grade_bio)
    print("Grade obtained in Maths: " + grade_math)
    print("Grade obtained in Computer: " + grade_comp)
