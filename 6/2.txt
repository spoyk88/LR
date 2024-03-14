class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def work(self):
        print(f"{self.name} works as a {self.position}.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} studies with student ID: {self.student_id}.")


class University:
    def __init__(self):
        self.employees = []
        self.students = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_student(self, student):
        self.students.append(student)

    def remove_employee(self, name_or_id):
        for employee in self.employees:
            if employee.name == name_or_id or employee.position == name_or_id:
                self.employees.remove(employee)
                print(f"{employee.name} has been removed from the university employees.")
                return
        print(f"No employee found with name or position: {name_or_id}")

    def remove_student(self, name_or_id):
        for student in self.students:
            if student.name == name_or_id or student.student_id == name_or_id:
                self.students.remove(student)
                print(f"{student.name} has been removed from the university students.")
                return
        print(f"No student found with name or ID: {name_or_id}")

    def find_person(self, name_or_id):
        for person in self.employees + self.students:
            if person.name == name_or_id or person.student_id == name_or_id or person.position == name_or_id:
                return person
        return None

    def show_info(self):
        print("University Employees:")
        for employee in self.employees:
            employee.introduce()
            employee.work()
        print("University Students:")
        for student in self.students:
            student.introduce()
            student.study()


# Create objects
john = Employee("John Doe", 30, "Professor")
emma = Student("Emma Smith", 21, "2023001")
dmitro = Employee("Dmitro СЕГЕН", 25, "Research Assistant")

# Create university
university = University()

# Add employees and students to university
university.add_employee(john)
university.add_student(emma)
university.add_employee(dmitro)

# Show university info
university.show_info()

# Remove employee
university.remove_employee("John Doe")

# Remove student
university.remove_student("2023001")

# Show updated info
university.show_info()
