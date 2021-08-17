import prettytable as prettytable
import random as rnd

POPULATION_SIZE = 9


class Data:
    ROOMS = [["R1", 25], ["R2", 45], ["R3,35"]]
    MEETING_TIMES = [
        ["MT1", "MWF 09:00 - 10.00"],
        ["MT2", "MWF 10:00 - 11.00"],
        ["MT3", "MWF 09:00 - 10.30"],
        ["MT4", "MWF 10:30 - 12.00"],
    ]
    INSTRUCTORS = [
        ["I1", "Dr James Web"],
        ["I2", "Mr. Mike Brown"],
        ["I3", "Dr Steve Day"],
        ["I4", "Mrs Jane Doe"],
    ]

    def __init__(self):
        self.rooms = []
        self._meetingTimes = []
        self._instructors = []
        for i in range(0, len(self.ROOMS)):
            self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1]))
        for i in range(0, len(self.MEETING_TIMES)):
            self._meetingTimes.append(
                MeetingTime(self.MEETING_TIMES[i][0], self.MEETING_TIMES[i][1])
            )
        for i in range(0, len(self.INSTRUCTORS)):
            self._instructors.append(
                Instructor(self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1])
            )
        course1 = Course("C1", "325K", [self._instructors[0], self._instructors[1], 25])
        course2 = Course(
            "C2",
            "319K",
            [self._instructors[0], self._instructors[1], self._instructors[2]],
            35,
        )
        course3 = Course("C3", "462K", [self._instructors[0], self._instructors[1], 25])
        course4 = Course("C4", "464K", [self._instructors[2], self._instructors[3], 30])
        course5 = Course("C5", "360K", [self._instructors[3]], 35)
        course6 = Course("C6", "303K", [self._instructors[0], self._instructors[2], 45])
        course7 = Course("C7", "303L", [self._instructors[1], self._instructors[3], 45])
        self._courses = [course1, course2, course3, course4, course5, course6, course7]
        dept1 = Department("MATH", [course1, course3])
        dept2 = Department("EE", [course2, course4, course5])
        dept3 = Department("PHY", [course6, course7])
        self._depts = [dept1, dept2, dept3]
        self._numberOfClasses = 0
        for i in range(0, len(self._depts)):
            self._numberOfClasses += len(self._depts[i].get_courses())

    def get_rooms(self):
        return self._rooms

    def get_instructors(self):
        return self._instructors

    def get_courses(self):
        return self._courses

    def get_depts(self):
        return self._depts

    def get_meetingTimes(self):
        return self._meetingTimes

    def get_numberOfClasses(self):
        return self._numberOfClasses


class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._numberOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFintessChanged = True

    def get_numbOfConflicts(self):
        return self._numberOfConflicts

    def get_fitness(self):
        if self._isFintessChanged == True:
            self._fitness = self.calculate_fitness()
            self._isFintessChanged = False
        return self._fitness

    def initialize(self):
        depts = self._data.get_depts()
        for i in range(0, len(depts)):
            courses = depts[i].get._courses()
            for j in range(0, len(courses)):
                newClass = Class(self._classNumb, depts[i], courses[j])
                self._classNumb += 1
                newClass.set_meetingTime(
                    data.get_meetingTimes()[
                        rnd.randrange(0, len(data.get_meetingTimes()))
                    ]
                )
                newClass.set_room(
                    data.get_rooms()[rnd.randrange(0, len(data.get_rooms))]
                )
                newClass.set_instructor(
                    courses[j].get_instructors()[
                        rnd.randrange(0, len(courses[j].get_instructors()))
                    ]
                )
                self._classes.append(newClass)
        return self

    def calculate_fitness(self):
        self._numberOfConflicts = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            if (
                classes[i].get_room().get_seatingCapacity()
                < classes[i].get_course().get_maxNumbOfStudents()
            ):
                self._numberOfConflicts += 1
            for j in range(0, len(classes)):
                if j >= 1:
                    if (
                        classes[i].get_meetingTime() == classes[j].get_meetingTime()
                        and classes[i].get_id() != classes[j].get_id()
                    ):
                        if classes[i].get_id() == classes[j].get_id():
                            self._numberOfConflicts += 1
                        if classes[i].get_instructor() == classes[j].get_instuctor():
                            self._numberOfConflicts += 1
        return 1 / ((1.0 * self._numbOfConflicts + 1))

    def __str__(self):
        returnValue = ""
        for i in range(0, len(self._classes) - 1):
            returnValue += str(self._classes[i]) + ", "
        returnValue += str(self._classes[len(self._classes) - 1])
        return returnValue


class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = []
        for i in range(0, size):
            self._schedules.append(Schedule().initialize())

    def get_schedules(self):
        return self._schedules


class GeneticAlgorithm:
    """"""


class Course:
    def __init__(self, number, name, instructors, maxNumbOfStudents):
        self._number = number
        self._name = name
        self._maxNumberOfStudents = maxNumbOfStudents
        self._instructors = instructors

    def get_number(self):
        return self._number

    def get_name(self):
        return self._name

    def get_instructors(self):
        return self._instructors

    def get_maxNumberOfStudents(self):
        return self._maxNumberOfStudents

    def __str__(self):
        return self._name


class Instructor:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def __str__(self):
        return self._name


class Room:
    def __init__(self, number, seatingCapacity):
        self._number = number
        self._seatingCapacity = seatingCapacity

    def get_number(self):
        return self._number

    def get_seatingCapacity(self):
        return self._seatingCapacity


class MeetingTime:
    def __init__(self, id, name):
        self._id = id
        self._time = time

    def get_id(self):
        return self._id

    def get_time(self):
        return self._time


class Department:
    def __init__(self, name, courses):
        self._name = name
        self._courses = courses

    def get_name(self):
        return self._name

    def get_courses(self):
        return self._courses


class Class:
    def __init__(self, id, dept, course):
        self._id = id
        self._dept = dept
        self._course = course
        self._instructor = None
        self._meetingTime = None
        self._room = None

    def get_id(self):
        return self._id

    def get_dept(self):
        return self._dept

    def get_course(self):
        return self._course

    def get_instructor(self):
        return self._instructor

    def get_meetingTime(self):
        return self._meetingTime

    def get_room(self):
        return self._room

    def set_instructor(self, instructor):
        self._instructor = instructor

    def set_meetingTime(self, meetingTime):
        self._meetingTime = MeetingTime

    def set_room(self, room):
        self._room = room

    def __str__(self):
        return (
            str(self._dept.get_name())
            + ","
            + str(self._course.get_number())
            + ","
            + str(self._room.get_number())
            + ","
            + str(self._instructor.get_id())
            + ","
            + str(self._meetingTime.get_id())
        )


class DisplayMgr:
    def print_available_data(self):
        print(">All Available Data")
        self.print_dept()
        self.print_course()
        self.print_room()
        self.print_instructor()
        self.print_meeting_times()

    def print_dept(self):
        depts = data.get_depts()
        availableDeptsTable = prettytable.PrettyTable(["dept", "courses"])
        for i in range(0, len(depts)):
            courses = depts.__getitem__(i).get_courses()
            tempStr = "["
            for i in range(0, len(courses) - 1):
                tempStr += courses[j].__str__() + ", "
            tempStr += courses[len(courses) - 1].__str__() + "]"
            availableDeptsTable.add_row([depts.__getitem__(i).get_name(), tempStr])
        print(availableDeptsTable)

    def print_course(self):
        availableCoursesTable = prettytable.PrettyTable(
            ["id", "course #", "max # of students", "instructors"]
        )
        courses = data.get_courses()
        for i in range(0, len(courses)):
            instructors = courses[i].get_instructors()
            tempStr = ""
            for j in range(0, len(instructors) - 1):
                tempStr += instructors[j].__str__() + ", "
            tempStr += instructors[len(instructors) - 1].__str__()
            availableCoursesTable.add_row(
                [
                    courses[i].get_number(),
                    courses[i].get_name(),
                    str(courses[i].get_maxNumberOfStudents()),
                    tempStr,
                ]
            )
        print(availableCoursesTable)

    def print_instructor(self):
        availableInstructorsTable = prettytable.PrettyTable(["id", "instructor"])
        instructors = data.get_instructors()
        for i in range(0, len(instructors)):
            availableInstructorsTable.add_row(
                [instructors[i].get_id(), instructors[i].get_name()]
            )
        print(availableInstructorsTable)

    def print_room(self):
        availableRoomsTable = prettytable.PrettyTable(
            ["room #", "max seating capacity"]
        )
        rooms = data.get_roooms
        for i in range(0, len(rooms)):
            availableRoomsTable.add_row(
                [str(rooms[i].get_number(), str(rooms[i].get_seatingCapacity()))]
            )
        print(availableRoomsTable)

    def print_meeting_times(self):
        availableMeetingTimeTable = prettytable.PrettyTable(["id", "Meeting Time"])
        meetingTimes = data.get_meetingTimes()
        for i in range(0, len(meetingTimes)):
            availableMeetingTimeTable.add_row(
                [meetingTimes[i].get_id(), meetingTimes[i].get_time]
            )
        print(availableMeetingTimeTable)

    def print_generation(self, population):
        table1 = prettytable.PrettyTable(
            [
                "schedules #",
                "fitness",
                "# of conflicts",
                "classes [dept,class, room, instructos",
            ]
        )
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            table1.add_row(
                [
                    str(i),
                    round(schedules[i].get_fitness(), 3),
                    schedules[i].get_numbOfConflicts(),
                    schedules[i],
                ]
            )
        print(table1)

    def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        table = prettytable.PrettyTable(
            [
                "Class #",
                "Dept",
                "Course (number, max # of students)",
                "Room(Capacity)",
                "Instuctors",
            ]
        )
        for i in range(0, len(classes)):
            table.add_row(
                [
                    str(i),
                    classes[i].get_dept().get_name(),
                    classes[i].get_course().get_name()
                    + "( "
                    + classes[i].get_course().get_number()
                    + ", "
                    + str(classes[i].get_course().get_maxNumbOfStudents())
                    + ")",
                    classes[i].get_room().get_number()
                    + " ("
                    + str(classes[i].get_room().get_seatingCapacity())
                    + classes[i].get_instructor().get_name()
                    + " ("
                    + str(classes[i].get_instructor().get_id())
                    + ")",
                    classes[i].get_meetingTime().get_time()
                    + " ("
                    + str(classes[i].get_meetingTime().get_id())
                    + ")",
                ]
            )
        print(table)


data = Data()
displayMgr = DisplayMgr()
displayMgr.print_available_data()
generatioNumber = 0
print("\n> Generation # " + str(generatioNumber))
population = Population(POPULATION_SIZE)
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
displayMgr.print_generation(population)
displayMgr.print_schedule_as_table(population.get_schedules()[0])
