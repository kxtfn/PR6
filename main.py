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

def show_students_by_group(): # Гордієнко Анна - Відображення студентів конкретної групи
    print("Відображення студентів конкретної групи")
    group = input("Введіть назву групи: ").strip()

    if not group:
        print("Помилка: назву групи не введено.")
        return

    matched = [s for s in students if s.get("group", "").lower() == group.lower()]

    if not matched:
        print(f"Студентів групи '{group}' не знайдено.")
        return

    print("\n" + "-" * 48)
    print(f"Студенти групи: {group}")
    for s in matched:
        print(f"\nID: {s['id']}")
        print(f"Ім'я: {s['name']}")
        print(f"Курс: {s['course']}")
        print("Оцінки:")
        g = s.get("grades")
        if isinstance(g, dict):
            for subj, grade in g.items():
                print(f"  {subj}: {grade}")
    print("-" * 48)

def show_students_by_course(): # Гордієнко Анна - Відображення студентів конкретного курсу
    print("Відображення студентів конкретного курсу")
    course_input = input("Введіть номер курсу: ").strip()

    try:
        course_num = int(course_input)
    except ValueError:
        print("Помилка: номер курсу введено неправильно.")
        return

    matched = [s for s in students if s.get("course") == course_num]

    if not matched:
        print(f"Студентів {course_num} курсу не знайдено.")
        return

    print("\n" + "-" * 48)
    print(f"Студенти {course_num} курсу")
    for s in matched:
        print(f"\nID: {s['id']}")
        print(f"Ім'я: {s['name']}")
        print(f"Група: {s['group']}")
        print("Оцінки:")
        g = s.get("grades")
        if isinstance(g, dict):
            for subj, grade in g.items():
                print(f"  {subj}: {grade}")
    print("-" * 48)

def search_student_by_surname(): # Іващенко Нікіта - Пошук студентів за прізвищем
    search_query = input("Введіть прізвище студента якого ви хочете знайти. -> ").lower().strip() 
    for student in students:
        surname = student["name"].split(" ")[1].lower()  
        if search_query == surname:
                print("- "*30)    
                print(f"Студента з прізвищем {search_query.capitalize()} успішно знайдено.")
                print(f"ID: {student['id']}")
                print(f"Група: {student['group']}")
                print(f"Курс: {student['course']}")
                grade_string = "".join(f"  {subject} - {score}\n" for subject,score in student["grades"].items())
                print(f"Оцінки по предметам:\n{grade_string}")
                print("- "*30)    
                return
    print(f"Студента з прізвищем {search_query.capitalize()} не знайдено.")
    
    

def calculate_average_grade(): #  Іващенко Нікіта - Підрахунок середнього балу студентів
    for student in students:
        grades = list(student["grades"].values())
        average = sum(grades)/len(grades)
        print(f"Студент {student["name"]}")
        print(f"Середній балл - {average:.1f}")
        print("- "*30)        
        
        

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
def subject_statistics():  # Денисенко Сергій - Статистика студентів по предмету
    print("\nОберіть предмет для статистики:")
    for i, subj in enumerate(subjects, start=1):
        print(f"{i}. {subj}")

    try:
        idx = int(input("Введіть номер предмета: "))
        if not (1 <= idx <= len(subjects)):
            print("Помилка: невірний номер предмета.")
            return
    except ValueError:
        print("Помилка: введіть число.")
        return

    subject_name = subjects[idx - 1]

    graded = []
    not_graded = []

    for s in students:
        g = s.get("grades")

        grade_val = g.get(subject_name) if isinstance(g, dict) else None
        if isinstance(grade_val, int):
            graded.append((s["name"], grade_val))
        else:
            not_graded.append(s["name"])

    total = len(students)
    n_graded = len(graded)
    n_missing = len(not_graded)

    print("\n" + "-" * 48)
    print(f"Статистика по предмету: {subject_name}")
    print(f"Всього студентів: {total}")
    print(f"З оцінкою: {n_graded}")
    print(f"Без оцінки: {n_missing}")

    if n_graded == 0:
        print("Поки що немає жодної оцінки за цим предметом.")
        if not_graded:
            print("\nСтуденти без оцінки:")
            for name in not_graded:
                print(f"  - {name}")
        print("-" * 48)
        return

    grades_only = [g for _, g in graded]
    avg = sum(grades_only) / n_graded
    name_min, min_g = min(graded, key=lambda x: x[1])
    name_max, max_g = max(graded, key=lambda x: x[1])

    print(f"Середній бал: {avg:.2f}")
    print(f"Мінімальна оцінка: {min_g} — {name_min}")
    print(f"Максимальна оцінка: {max_g} — {name_max}")

    print("\nРейтинг студентів за цим предметом:")
    for i, (name, g) in enumerate(sorted(graded, key=lambda x: x[1], reverse=True), start=1):
        print(f"{i:>2}. {name}: {g}")

    if not_graded:
        print("\nСтуденти без оцінки:")
        for name in not_graded:
            print(f"  - {name}")
    print("-" * 48)


def sort_students_by_average():  # Денисенко Сергій - Сортування студентів по середньому балу
    def compute_avg(student):
        g = student.get("grades")

        if not isinstance(g, dict):
            return None

        nums = [val for val in g.values() if isinstance(val, int)]
        if not nums:
            return None
        return sum(nums) / len(nums)

    table = []
    for s in students:
        avg = compute_avg(s)
        table.append({
            "id": s["id"],
            "name": s["name"],
            "group": s["group"],
            "course": s["course"],
            "avg": avg
        })

    table_sorted = sorted(
        table,
        key=lambda x: ((x["avg"] is None), -(x["avg"] or 0), x["name"])
    )

    print("\n" + "-" * 48)
    print("Рейтинг студентів за середнім балом:")
    for i, row in enumerate(table_sorted, start=1):
        avg_str = f"{row['avg']:.2f}" if row["avg"] is not None else "немає оцінок"
        print(f"{i:>2}. ID:{row['id']} | {row['name']} | Група: {row['group']} | Курс: {row['course']} | Середній: {avg_str}")
    print("-" * 48)



if __name__ == "__main__":
    menu()
