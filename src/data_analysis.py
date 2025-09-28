#from csv import reader

def load_students():
    with open("data/students.csv", encoding="utf-8") as f:
        lines = f.readlines()

    data = []
    for line in lines[0:]: 
        fields = line.strip().split(",")
        data.append(fields)
    return data

data = load_students()
print(data[0])        ##see the header
print(data[1:5])      ##see what's it looks like


def total_student(data):
    num = []                       ## create an empty list to store the numbers
    for i in data[1:]:           ## skip the header and loop each row
        num.append(i[1])
    return len(num)

print(total_student(data))

def calculate_average_grade(data):
    total_grade = 0
    for row in data[1:]:
        grade = row[2]             ## this means I want the third column which is the grade
        total_grade += int(grade)
    return total_grade / total_student(data)
    
print(calculate_average_grade(data))

def get_all_subjects(data):      ## I put them together since they are doing one thing with two steps
    def get_subject(data):       ## just get the subject
        subject = []
        for row in data[1:]:
            sub = row[3]               ## this means I want the fourth column which is the subject
            subject.append(sub)
        return subject

    def mask(data):              ## masking: count the frequency of each subject
        subject = get_subject(data)
        frequency_table = {}
        for subject in subject:
            if subject in frequency_table:
                frequency_table[subject] += 1
            else:
                frequency_table[subject] = 1
        return frequency_table
    return mask(data)
print(get_all_subjects(data))

def count_math_students(data):
    subject = get_all_subjects(data)
    return subject["Math"]
print(count_math_students(data))

def generate_report(data):
    total_students = total_student(data)
    average_grade = calculate_average_grade(data)
    subject_count = get_all_subjects(data)

    report = f"Total Students: {total_students}\n"
    report += f"Average Grade: {average_grade:.2f}\n"
    report += f"Subject Count:{subject_count}\n"

    return report

def save_report(report, filename="output/analysis_report.txt"):
    with open(filename, "w") as report_file:
        report_file.write(report)
print( "File saved to output" )

def main():
    data = load_students()
    report = generate_report(data)
    save_report(report)

if __name__ == "__main__":
    main()
