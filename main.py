class Student:
    def __init__(self, name, class_name="", id=0):
        self.name = name
        self.id = id
        self.class_name = class_name
        self.record = []

    def set_class(self, name, class_name):
        self.class_name = class_name

    def display_details(self):
        print("Student name:", self.name, " Student ID:", self.id, " Student class:", self.class_name)


class Section:
    def __init__(self, name, teacher_id=0):
        self.class_name = name
        self.teacher = teacher_id  # CHANGE to integer ID system
        self.students = {}  # dict containing attendance record

    def add_teacher(self, teacher_id):
        self.teacher = teacher_id

    def add_student(self, student_id, attendance=None):
        if attendance is None:
            attendance = [0, 0, 0, 0, 0, 0, 0, 0]
        self.students[student_id] = attendance  # Add the student with an empty attendance record

    def set_attendance(self):
        for id in self.students:  # Potensh replace with lambda
            input_atten = []
            for i in range(0, 8):
                print("Attendance for student:", id, ", week:", i)
                input_atten.append(int(input()))
            self.students[id] = input_atten  # Set attendance

    def get_no_students(self):
        return len(self.students)

    def get_class_name(self):
        return self.class_name

    def display_details(self):
        print("Class name:", self.class_name, " Teacher:", self.teacher, " Students:", self.students)


class User:
    students = {}
    teachers = {}
    classes = {1: [], 2: [], 3: [], 4: []}
    no_classes = 4

    def get_student_name(self, id):
        return self.students[id]

    def get_teacher_name(self, id):
        return self.teachers[id]

    def print_students(self):
        for sid in self.students:
            self.students[sid].display_details()

    def print_classes(self):
        for l in self.classes:
            for i in self.classes[l]:
                i.display_details()

    # Method of writing student attendance
    def take_attendance(self):
        while True:
            input_class = input("Enter section to take attendance:")
            try:
                print(input_class[0], input_class[1])
                selected_class = self.classes[int(input_class[0])]
                selected_sect = selected_class[0]
                for c in selected_class:
                    if c.class_name == input_class:
                        selected_sect = c

                print(selected_sect.class_name)
                break
            except IndexError:
                print("Invlalid try again!")

        selected_sect.set_attendance()


class Admin(User):
    def __init__(self):
        teacher_list = [[1, "Mr. Macdonald"], [2, "Ms. Rolex"], [3, "Mr. Airbus"], [4, "Ms. Amadeus"], [5, "Mr. Bose"],
                        [6, "Ms. Wiley"]]
        list(filter(lambda teacher_info: self.add_teachers(teacher_info[0], teacher_info[1]), teacher_list))

        sect_list = [[1, "A"], [1, "B"], [1, "C"], [2, "A"], [3, "A"], [3, "B"]]
        list(filter(lambda sect_info: self.add_sect(sect_info[0], sect_info[1]), sect_list))

        teacher_number = 1
        for c in super().classes:
            for n in super().classes[c]:
                n.add_teacher(teacher_number)
                teacher_number = teacher_number + 1

        stud_list = [["Toaster", 1, 6], ["Biscuit", 1, 7], ["Book", 1, 8], ["Radiator", 1, 9], ["Webcam", 1, 10], ["Clock", 1, 11], ["Toilet", 2, 12]]
        list(filter(lambda stud_info: self.add_students(stud_info[0], stud_info[1], stud_info[2]), stud_list))

    def add_students(self, name, class_no, id):
        for c in self.classes[class_no]:
            if c.get_no_students() < 5:  # Find class with space
                s = Student(name, c.get_class_name(), id)
                super().students[id] = s
                c.add_student(id)
                break
            else:
                print("No space") # CHANGE make new section in class

    def add_teachers(self, id, name):
        super().teachers[id] = name

    def add_sect(self, class_no, sect_name):
        s = Section(str(class_no) + sect_name)
        super().classes[class_no].append(s)

    def assign_teacher(self, class_no, sect_name, teacher_id):
        super().classes[class_no][sect_name].add_teacher(teacher_id)

    def add_class(self):
        self.no_classes = self.no_classes + 1
        self.classes[self.no_classes] = []

    def print(self):
        print("Hello Admin yes")
        super().print_students()
        super().print_classes()
        print(super().teachers)


admin = Admin()
user = User()
# admin.add_sect(1, "A", 5)
# create lambdas to add classes and sections
# admin.add_students("Toaster", 1, 6)
# Create lambda to add students
admin.print()
user.take_attendance()
admin.print()
user.print()


