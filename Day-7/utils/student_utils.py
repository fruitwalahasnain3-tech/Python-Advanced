def student_grade(marks):
    if marks>90:
        return "A"
    elif marks>80:
        return "B"
    elif marks>70:
        return "C"
    elif marks>60:
        return "B"
    else:    
        return "F"
                
def student_status(marks):
    if marks>=50:
        return "Pass"
    else:
        
        return "Fail"