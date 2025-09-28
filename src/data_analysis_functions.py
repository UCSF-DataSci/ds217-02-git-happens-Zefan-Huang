from csv import reader
from data_analysis import total_student, calculate_average_grade, get_all_subjects

filename = "data/student.csv"
def load_data():
    if filename.lower().endswith('.csv'):
        return load_data(filename)
    elif filename.lower().endswith('.json'):
        return load_data(filename)
    
def load_csv(filename):
    with open("data/students.csv", encoding="utf-8") as f:   ## encoing is important, although here it's not a big dataset since it was created by me
        read_file = reader(f)
        data = list(read_file)
    return data
data = load_csv(filename)
print(data[1:])        

def analyze_grade_range(data):
    grade = []
    for row in data[1:]:
        g = int(row[2])           
        if g in range(90,100):
            grade.append('A')
        elif g in range(80,90):
            grade.append('B')
        elif g in range(70,80):
            grade.append('C')
        elif g in range(60,70):
            grade.append('D')
        else:
            grade.append('F')
    return grade

def analyze_grade_distribution(data):
    grades = analyze_grade_range(data)
    distribution = {}
    for g in grades:
        if g in distribution:
            distribution[g] += 1
        else:
            distribution[g] = 1
    return distribution

def gradePercentage(data, distribution):
    percentage = {}
    for g in distribution:
        val = (distribution[g] / total_student(data)) * 100
        percentage[g] = f"{val:.1f}%"
    return percentage
print(gradePercentage(data, analyze_grade_distribution(data)))

def max_min_grade(data):
    grade = []
    for row in data[1:]:
        g = int(row[2])
        grade.append(g)
    return max(grade), min(grade)
print(max_min_grade(data))

def analyze_data(data,distribution):
    total_students = total_student(data)
    average_grade = calculate_average_grade(data)
    subject_count = get_all_subjects(data)
    grade_distribution = analyze_grade_distribution(data)
    grade_percentage = gradePercentage(data, analyze_grade_distribution(data))

    analyze = {
        "Total Students": total_students,
        "Max and Min Grade": max_min_grade(data),
        "Average Grade": f"{average_grade:.1f}",
        "Subject Count": subject_count,
        "Grade Distribution": grade_distribution,
        "Grade Percentage": grade_percentage
    }
    return analyze

print(analyze_data(data, analyze_grade_distribution(data)))

def generate_report(data):
    report2 = analyze_data(data,analyze_grade_distribution(data))
    return report2

def save_result(report2, filename="output/analysis_report.txt"):
    with open(filename, "w", encoding="utf-8") as report_file:
        report_file.write(str(report2)) 
print( "File saved to output" )

def main():
    data = load_csv(filename)
    report2 = generate_report(data)
    save_result(report2)
    
if __name__ == "__main__":
     main()