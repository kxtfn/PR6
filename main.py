students = [
    {"id": 1, "name": "Ігор Аксьонов", "group": "КН-45-5/1", "course": 1},
    {"id": 2, "name": "Нікіта Іващенко", "group": "КН-42/2", "course": 2},
    {"id": 3, "name": "Денис Лихацький", "group": "КН-42/2", "course": 2},
    {"id": 4, "name": "Анна Гордієнко", "group": "КН-42/2", "course": 2},
    {"id": 5, "name": "Сергій Денисенко", "group": "КН-42/2", "course": 2}
]

subjects = [
    "Програмування мовою Python",
    "Чисельні методи",
    "Алгоритми і структури даних"
]

for student in students: # применение оценок ко всем студентам
    student["grades"] = subjects.copy()

def view_all_students():
    for student in students:
        print(f"ID: {student['id']}")
        print(f"Ім'я: {student['name']}")
        print(f"Група: {student['group']}")
        print(f"Курс: {student['course']}")
        print("Оцінки:")
        
        if isinstance(student['grades'], list):
            for subject in student['grades']:
                print(f"  {subject}: оцінка відсутня")
        else:
            for subject, grade in student['grades'].items():
                grade_display = grade if grade is not None else "оцінка відсутня"
                print(f"  {subject}: {grade_display}")
        print("--" * 20)

def add_student():
    print("Додавання студентів до словника")

def remove_student():
    print("Видалення студентів зі словника")

def edit_student():
    print("Редагування інформації про студента")

def show_students_by_group():
    print("Відображення студентів конкретної групи")

def show_students_by_course():
    print("Відображення студентів конкретного курсу")

def search_student_by_surname():
    print("Пошук студента по прізвищу та виведення інформації")

def calculate_average_grade():
    print("Підрахунок середнього балу студентів")

def subject_statistics():
    print("Статистика студентів по предмету")

def sort_students_by_average():
    print("Сортування студентів по середньому балу")


def menu():
    while True:
        print("\nОберіть функцію:")
        print("1. Перегляд всіх студентів")
        print("2. Додавання студентів до словника")
        print("3. Видалення студентів зі словника")
        print("4. Редагування інформації про студента")
        print("5. Відображення студентів конкретної групи")
        print("6. Відображення студентів конкретного курсу")
        print("7. Пошук студента по прізвищу та виведення інформації")
        print("8. Підрахунок середнього балу студентів")
        print("9. Статистика студентів по предмету")
        print("10. Сортування студентів по середньому балу")
        print("0. Вихід")

        choice = input("Ваш вибір: ")
        if choice == "1":
            view_all_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            edit_student()
        elif choice == "5":
            show_students_by_group()
        elif choice == "6":
            show_students_by_course()
        elif choice == "7":
            search_student_by_surname()
        elif choice == "8":
            calculate_average_grade()
        elif choice == "9":
            subject_statistics()
        elif choice == "10":
            sort_students_by_average()
        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    menu()
