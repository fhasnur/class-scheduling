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
    """"""


class Population:
    """"""


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
