from statistics import mean


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if 0 <= grade <= 10:
            if (
                isinstance(lecturer, Lecturer)
                and course in lecturer.courses_attached
                and course in self.courses_in_progress
            ):
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return "Ошибка"
        else:
            return "Ошибка"

    def mean_grade(self):
        if len(self.grades) != 0:
            return sum(mean(grade) for grade
                       in self.grades.values()) / len(self.grades)
        else:
            return "Нет оценок"

    def __gt__(self, other):
        return self.mean_grade() > other

    def __lt__(self, other):
        return self.mean_grade() < other

    def __ge__(self, other):
        return self.mean_grade() >= other

    def __le__(self, other):
        return self.mean_grade() <= other

    def __eq__(self, other):
        return self.mean_grade() == other

    def __ne__(self, other):
        return self.mean_grade() != other

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: "
            f"{round(self.mean_grade(), 2)}\n"
            f"Курсы в процессе изучения: "
            f"{', '.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {', '.join(self.finished_courses)}"
        )


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def mean_grade(self):
        if len(self.grades) != 0:
            return sum(mean(grade) for grade
                       in self.grades.values()) / len(self.grades)
        else:
            return "Нет оценок"

    def __gt__(self, other):
        return self.mean_grade() > other

    def __lt__(self, other):
        return self.mean_grade() < other

    def __ge__(self, other):
        return self.mean_grade() >= other

    def __le__(self, other):
        return self.mean_grade() <= other

    def __eq__(self, other):
        return self.mean_grade() == other

    def __ne__(self, other):
        return self.mean_grade() != other

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {round(self.mean_grade(), 2)}"
        )


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if 0 <= grade <= 10:
            if (
                isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress
            ):
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return "Ошибка"
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\n" f"Фамилия: {self.surname}"


def calculat_average_grade_for_course(students, name_course):
    total = 0
    mean_grade = 0
    for student in students:
        for course, grade in student.grades.items():
            if course == name_course:
                total += len(grade)
                mean_grade += sum(grade)
    return round(mean_grade / total, 1)


def calculat_average_grade_for_lecture(lectors, name_lecture):
    total = 0
    mean_grade = 0
    for lector in lectors:
        for lecture, grade in lector.grades.items():
            if lecture == name_lecture:
                total = len(grade)
                mean_grade += sum(grade)
    return round(mean_grade / total, 1)


student_1 = Student("Artur", "Gavrilenko", "Man")
student_1.courses_in_progress += ["Python"]
student_1.finished_courses += ["English"]
student_1.courses_in_progress += ["Java"]
student_2 = Student("Yana", "Turchinskaya", "Woman")
student_2.courses_in_progress += ["C++"]
student_2.courses_in_progress += ["C#"]

reviewer_1 = Reviewer("Ivan", "Ivanov")
reviewer_2 = Reviewer("Katya", "Katyanova")
reviewer_1.courses_attached += ["Python"]
reviewer_1.courses_attached += ["C++"]
reviewer_2.courses_attached += ["Java"]
reviewer_2.courses_attached += ["JavaScript"]

lecturer_1 = Lecturer("Petr", "Petrov")
lecturer_2 = Lecturer("Igor", "Igorev")
lecturer_1.courses_attached += ["Python"]
lecturer_1.courses_attached += ["English"]
lecturer_2.courses_attached += ["C++"]
lecturer_2.courses_attached += ["C#"]

reviewer_1.rate_hw(student_1, "Python", 10)
reviewer_1.rate_hw(student_1, "Python", 4)
reviewer_2.rate_hw(student_1, "Java", 8)
reviewer_2.rate_hw(student_1, "Java", 7)
reviewer_1.rate_hw(student_2, "C++", 6)

student_1.rate_lecturer(lecturer_1, "Python", 10)
student_1.rate_lecturer(lecturer_1, "English", 9)
student_1.rate_lecturer(lecturer_1, "Python", 9)
student_2.rate_lecturer(lecturer_2, "C++", 10)
student_2.rate_lecturer(lecturer_2, "C#", 7)

print(f"{student_1}\n")
print(f"{student_2}\n")
print(f"{lecturer_1}\n")
print(f"{lecturer_2}\n")
print(f"{reviewer_1}\n")
print(f"{reviewer_2}\n")

print(student_1 > student_2)
print(student_1 == student_2)
print(lecturer_1 < lecturer_2)
print(lecturer_1 != lecturer_2)

print(calculat_average_grade_for_course([student_1, student_2], "Python"))
print(calculat_average_grade_for_lecture([lecturer_1, lecturer_2], "C++"))
