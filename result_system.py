students = {
    "S101": {"name": "Anu", "marks": {"Python": 88, "Maths": 76, "Stats": 92}},
    "S102": {"name": "Binu", "marks": {"Python": 45, "Maths": 38, "Stats": 52}},
    "S103": {"name": "Cathy", "marks": {"Python": 95, "Maths": 91, "Stats": 89}},
    "S104": {"name": "Dev", "marks": {"Python": 60, "Maths": 72, "Stats": 55}},
    "S105": {"name": "Esha", "marks": {"Python": 72, "Maths": 65, "Stats": 80}}
}


def calculate_total(marks):
    return sum(marks.values())


def calculate_average(marks):
    return round(calculate_total(marks) / len(marks), 2)


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def check_result(marks, pass_mark=40):
    for mark in marks.values():
        if mark < pass_mark:
            return "Fail"
    return "Pass"


def student_summary(student):
    marks = student["marks"]
    total = calculate_total(marks)
    average = calculate_average(marks)

    return {
        "name": student["name"],
        "total": total,
        "average": average,
        "grade": get_grade(average),
        "result": check_result(marks)
    }


def add_student(data, student_id, name, **marks):
    if student_id in data:
        return False

    data[student_id] = {
        "name": name,
        "marks": marks
    }
    return True


def update_marks(data, student_id, **changes):
    if student_id not in data:
        return False

    data[student_id]["marks"].update(changes)
    return True


def remove_student(data, student_id):
    if student_id not in data:
        return False

    data.pop(student_id)
    return True


def print_report(data):
    print(f"{'ID':<6}{'Name':<8}{'Total':>6}{'Avg':>8}{'Grade':>7}  Result")
    print("-" * 42)

    averages = []
    for student_id, student in data.items():
        average = calculate_average(student["marks"])
        averages.append((average, student_id))

    averages.sort(reverse=True)

    for average, student_id in averages:
        student = data[student_id]
        summary = student_summary(student)
        print(
            f"{student_id:<6}{student['name']:<8}"
            f"{summary['total']:>6}{summary['average']:>8.2f}"
            f"{summary['grade']:>7}  {summary['result']}"
        )


def class_statistics(data, *subjects):
    if not subjects:
        subjects = tuple(next(iter(data.values()))["marks"].keys())

    topper_id = max(
        data,
        key=lambda student_id: calculate_average(data[student_id]["marks"])
    )
    topper_name = data[topper_id]["name"]

    pass_count = 0
    for student in data.values():
        if check_result(student["marks"]) == "Pass":
            pass_count += 1

    pass_percentage = round((pass_count / len(data)) * 100, 1)

    subject_averages = {}
    for subject in subjects:
        total = sum(student["marks"][subject] for student in data.values())
        subject_averages[subject] = round(total / len(data), 1)

    return {
        "topper": topper_name,
        "pass_percentage": pass_percentage,
        "subject_averages": subject_averages
    }