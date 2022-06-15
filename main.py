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
        print(self.record)

    def get_attendance(self):
        att_week = (self.record[0]) / 5 * 100
        att_month = (sum(self.record[0:4]) / (5 * 4)) * 100
        att_year = (sum(self.record)) / (5 * 8) * 100
        return att_week, att_month, att_year


class Section:
    def __init__(self, name, teacher_id=0, teacher_name=""):
        self.class_name = name
        self.teacher = teacher_id  # CHANGE to integer ID system
        self.teacher_name = teacher_name
        self.students = {}  # dict containing attendance record

    def add_teacher(self, teacher_id, teacher_name):
        self.teacher = teacher_id
        self.teacher = teacher_name

    def add_student(self, student_id, attendance=None):
        if attendance is None:
            attendance = [0, 0, 0, 0, 0, 0, 0, 0]
        self.students[student_id] = attendance  # Add the student with an empty attendance record

    def set_attendance(self):
        for id in self.students:  # Potensh replace with lambda
            input_atten = []
            for i in range(0, 8):
                while True:
                    print("Attendance for student:", id, " in week:", i + 1)
                    week_atten = int(input())
                    if week_atten < 0 or week_atten > 5:
                        print("Attendance for the week can not be less than 0 or greater than 5")
                    else:
                        input_atten.append(week_atten)
                        break

            self.students[id] = input_atten  # Set attendance

    def get_no_students(self):
        return len(self.students)

    def get_class_name(self):
        return self.class_name

    def display_details(self):
        print("Class name:", self.class_name, " Teacher:", self.teacher_name, "", self.teacher, " Students:",
              self.students)


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

    def print(self):
        self.print_classes()
        self.print_students()

    # Method of writing student attendance
    def take_attendance(self):
        while True:
            input_id = int(input("Enter teacher ID:"))
            try:
                input_class = self.teachers[input_id][1]
                print("You are: ", self.teachers[input_id][0], "For class:", input_class[0], input_class[1])
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
        self.update_attendance()

    def update_attendance(self):
        for sid in self.students:
            try:
                student_current = self.students[sid]
                search_class = student_current.class_name
                selected_class = self.classes[int(search_class[0])]
                # selected_sect = selected_class[0]
                for c in selected_class:
                    if c.class_name == search_class:
                        selected_sect = c
                        break
                # Get attendance record, calculate attendance percentages and update in student object
                # print(selected_sect.class_name)
                # Get the attendance record from the section object and set the attendance record in the student object
                student_current.record = selected_sect.students[sid]
            except(RuntimeError, TypeError, NameError, IndexError):
                print("wrong")

    def display_attendance(self, student_id):
        try:
            # Get attendance by searching the dict for student ID
            student_ob = self.students[student_id]
            student_name = student_ob.name
            student_class = student_ob.class_name
            att_week, att_month, att_year = student_ob.get_attendance()
            print("Attendance information for ", student_name, "from class", student_class, ":")
            print("Weekly:", att_week, "Monthly:", att_month, "Annual:", att_year)
        except KeyError:
            print("ERROR: That student does not exist")


class Admin(User):
    def __init__(self):
        sect_list = [[1, "A"], [1, "B"], [1, "C"], [2, "A"], [3, "A"], [3, "B"]]
        list(filter(lambda sect_info: self.add_sect(sect_info[0], sect_info[1]), sect_list))

        teacher_list = [[1, "Mr. Macdonald", "1A"], [2, "Ms. Rolex", "1B"], [3, "Mr. Airbus", "1C"],
                        [4, "Ms. Amadeus", "2A"], [5, "Mr. Bose", "3A"],
                        [6, "Ms. Wiley", "3B"]]
        list(filter(lambda teacher_info: self.add_teachers(teacher_info[0], teacher_info[1], teacher_info[2]),
                    teacher_list))

        stud_list = [["Toaster", 1, 6], ["Biscuit", 1, 7], ["Book", 1, 8], ["Radiator", 1, 9], ["Webcam", 1, 10],
                     ["Clock", 1, 11], ["Toilet", 2, 12], ["Table", 3, 14], ["Grass", 3, 35], ["Foot", 3, 67],
                     ["Xylophone", 3, 34]]
        list(filter(lambda stud_info: self.add_students(stud_info[0], stud_info[1], stud_info[2]), stud_list))
        super().update_attendance()

    def add_students(self, name, class_no, id):
        if id in self.students:
            print("Student already exists")
            return

        for c in self.classes[class_no]:
            if c.get_no_students() < 5:  # Find class with space
                s = Student(name, c.get_class_name(), id)
                super().students[id] = s
                c.add_student(id)
                break
            else:
                print("")  # CHANGE make new section in class
        super().update_attendance()

    def add_teachers(self, id, name, class_name):
        super().teachers[id] = [name, class_name]
        selected_class = super().classes[int(class_name[0])]
        for c in selected_class:
            if c.class_name == class_name:
                selected_sect = c
                break
        # set the teacher's name in the class
        selected_sect.teacher = id
        selected_sect.teacher_name = name

    def add_sect(self, class_no, sect_name):
        s = Section(str(class_no) + sect_name)
        super().classes[class_no].append(s)

    def assign_teacher(self, class_no, sect_name, teacher_id):
        super().classes[class_no][sect_name].add_teacher(teacher_id, self.teachers[teacher_id])  # add teacher name

    def add_class(self):
        self.no_classes = self.no_classes + 1
        self.classes[self.no_classes] = []

    def print(self):
        print("You are in admin access mode")
        super().print_students()
        super().print_classes()
        print(super().teachers)


def admin_loop(admin):
    a_ch = ""
    while a_ch != 'quit':
        a_ch = str(
            input("add: Add Students  addt: Add Teachers  adds: Add Sect  addc: Add Class  print: Display details"))
        if a_ch == "add":
            while True:
                try:
                    student_name = input("Student Name:")
                    class_num = int(input("Class no:"))
                    student_id = int(input("Student ID:"))
                    admin.add_students(student_name, class_num, student_id)
                    break
                except ValueError:
                    print("Invlalid try again!")
        elif a_ch == "print":
            admin.print()
        elif a_ch == "quit":
            print("Exiting admin control")
        else:
            print("Unknown selection")


def user_loop(user):
    a_ch = ""
    while a_ch != 'quit':
        a_ch = str(
            input(
                "search: Search for Student attendance  take: Take attendance for class  print: Print out class and student information"))
        if a_ch == "search":
            while True:
                try:
                    sid_search = int(input("Enter Student ID to search for:"))
                    user.display_attendance(sid_search)
                    break
                except TypeError:
                    print("Please enter a valid number")
                except IndexError:
                    print("Student with that ID does not exist, please enter a valid Student ID")
        elif a_ch == "take":
            user.take_attendance()
        elif a_ch == "print":
            user.print()
        elif a_ch == "quit":
            print("Exiting user control")
        else:
            print("Unknown selection")


admin = Admin()
user = User()
user.update_attendance()  # temp for debugging
# admin.add_sect(1, "A", 5)
# create lambdas to add classes and sections
# admin.add_students("Toaster", 1, 6)
# Create lambda to add students
ch = ""
while (ch != "quit"):
    try:
        ch = input("Are you admin or user?")
    except TypeError:
        print("Invlalid try again!")
    if ch == "admin":
        admin_loop(admin)
    elif ch == "user":
        user_loop(user)
    elif ch == "quit":
        print("Exiting program")
    else:
        print("Unknown selection")
# user.print()
