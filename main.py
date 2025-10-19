students = [
    {
        "id": 1,
        "name": "Ігор Аксьонов",
        "group": "КН-45-5/1",
        "course": 1,
        "grades": {
            "Програмування мовою Python": 85,
            "Чисельні методи": 78,
            "Алгоритми і структури даних": 92
        }
    },
    {
        "id": 2,
        "name": "Нікіта Іващенко",
        "group": "КН-42/2",
        "course": 2,
        "grades": {
            "Програмування мовою Python": 74,
            "Чисельні методи": 88,
            "Алгоритми і структури даних": 69
        }
    },
    {
        "id": 3,
        "name": "Денис Лихацький",
        "group": "КН-42/2",
        "course": 2,
        "grades": {
            "Програмування мовою Python": 91,
            "Чисельні методи": 64,
            "Алгоритми і структури даних": 77
        }
    },
    {
        "id": 4,
        "name": "Анна Гордієнко",
        "group": "КН-42/2",
        "course": 2,
        "grades": {
            "Програмування мовою Python": 82,
            "Чисельні методи": 73,
            "Алгоритми і структури даних": 85
        }
    },
    {
        "id": 5,
        "name": "Сергій Денисенко",
        "group": "КН-42/2",
        "course": 2,
        "grades": {
            "Програмування мовою Python": 79,
            "Чисельні методи": 92,
            "Алгоритми і структури даних": 88
        }
    }
]


subjects = [
    "Програмування мовою Python",
    "Чисельні методи",
    "Алгоритми і структури даних"
]

def view_all_students(): # Ігор Аксьонов - Перегляд всіх студентів
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

def add_student(): # Ігор Аксьонов - Додавання студентів до списку
    name = input("Введіть ім'я та прізвище студента: ")
    group = input("Введіть групу студента: ")
    course = input("Введіть курс студента (число): ")
    
    try:
        course = int(course)
    except ValueError:
        print("Курс повинен бути числом. Спробуйте ще раз.")
        return
    
    if students:
        new_id = max(student['id'] for student in students) + 1

    grades_template = {subject: None for subject in subjects} # шаблон оценок
    
    new_student = {
        "id": new_id,
        "name": name,
        "group": group,
        "course": course,
        "grades": grades_template
    }
    
    students.append(new_student)
    print(f"Студент {name} успішно доданий з ID {new_id}.")


def remove_student():# Денис Лихацький - Видалення студентів зі списку

    try:
        student_id = int(input("Введіть ID студента, якого потрібно видалити: "))
    except ValueError:
        print("Помилка: ID має бути числом.")
        return

    student_to_remove = None
    for student in students:
        if student['id'] == student_id:
            student_to_remove = student
            break

    if student_to_remove:
        students.remove(student_to_remove)
        print(f"Студент з ID {student_id} (Ім'я: {student_to_remove['name']}) був успішно видалений.")
    else:
        print(f"Помилка: Студента з ID {student_id} не знайдено.")


def edit_student():# Денис Лихацький - Редагування інформації про студента
    
    try:
        student_id = int(input("Введіть ID студента для редагування: "))
    except ValueError:
        print("Помилка: ID має бути цілим числом.")
        return

    student_to_edit = None
    for s in students:
        if s['id'] == student_id:
            student_to_edit = s
            break
    
    if not student_to_edit:
        print(f"Помилка: Студента з ID {student_id} не знайдено.")
        return

    while True:
        print(f"\nРедагування студента: {student_to_edit['name']} (ID: {student_to_edit['id']})")
        print(f"1. ПІБ: {student_to_edit['name']}")
        print(f"2. Група: {student_to_edit['group']}")
        print(f"3. Курс: {student_to_edit['course']}")
        print("4. Редагувати оцінки")
        print("0. Повернутися до головного меню")
        
        choice = input("Оберіть поле для редагування: ")

        if choice == '1':
            new_name = input(f"Введіть нове ПІБ (поточне: {student_to_edit['name']}): ")
            if new_name: 
                student_to_edit['name'] = new_name
                print("ПІБ оновлено.")
            else:
                print("ПІБ не змінено.")
        
        elif choice == '2':
            new_group = input(f"Введіть нову групу (поточна: {student_to_edit['group']}): ")
            if new_group:
                student_to_edit['group'] = new_group
                print("Групу оновлено.")
            else:
                print("Групу не змінено.")

        elif choice == '3':
            try:
                new_course_input = input(f"Введіть новий курс (поточний: {student_to_edit['course']}): ")
                if new_course_input:
                    new_course = int(new_course_input)
                    student_to_edit['course'] = new_course
                    print("Курс оновлено.")
                else:
                    print("Курс не змінено.")
            except ValueError:
                print("Помилка: Курс має бути числом.")

        elif choice == '4':
            
            if isinstance(student_to_edit['grades'], list):
                print("Ініціалізація системи оцінок (конвертація)...")
                student_to_edit['grades'] = {subject: None for subject in subjects}

            print("\nРедагування оцінок")
            subject_list = list(student_to_edit['grades'].keys())
            
            if not subject_list:
                print("Список предметів порожній.")
                continue 

            for i, subject in enumerate(subject_list):
                grade = student_to_edit['grades'][subject]
                grade_display = grade if grade is not None else "оцінка відсутня"
                print(f"  {i+1}. {subject}: {grade_display}")

            try:
                subject_choice = int(input("\nВведіть номер предмету (або 0 для скасування): "))
                
                if subject_choice == 0:
                    continue 
                
                subject_name = subject_list[subject_choice - 1] 

            except (ValueError, IndexError):
                print("Помилка: Невірний номер предмету.")
                continue 
            
            new_grade_input = input(f"Введіть нову оцінку для '{subject_name}' (пусто = видалити): ")

            if not new_grade_input:
                student_to_edit['grades'][subject_name] = None
                print(f"Оцінку видалено.")
            else:
                try:
                    new_grade = int(new_grade_input)
                    if 1 <= new_grade <= 100:
                        student_to_edit['grades'][subject_name] = new_grade
                        print(f"Оцінку оновлено на {new_grade}.")
                    else:
                        print("Помилка: Оцінка має бути від 1 до 100.")
                except ValueError:
                    print("Помилка: Оцінка має бути числом.")

        elif choice == '0':
            print(f"Завершено редагування студента {student_to_edit['name']}.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

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
