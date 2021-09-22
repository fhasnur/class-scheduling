import prettytable as prettytable
import random as rnd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

POPULATION_SIZE = 10
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.2


class FuzzyMamdani:
    def __init__(self):
        self.population_size = ctrl.Antecedent(np.linspace(0, 1000), "Population Size")
        self.generation = ctrl.Antecedent(np.linspace(0, 1000), "Generation")
        self.prob_crossover = ctrl.Consequent(np.linspace(0.6, 0.9), "Prob Crossover")
        self.prob_mutasi = ctrl.Consequent(np.linspace(0, 0.250), "Prob Mutasi")

    def customMembership(self):
        self.population_size["small"] = fuzz.zmf(self.population_size.universe, 50, 250)
        self.population_size["medium"] = fuzz.gaussmf(self.population_size.universe, mean=275, sigma=80)
        self.population_size["large"] = fuzz.smf(self.population_size.universe, 350, 500)

        self.generation["short"] = fuzz.zmf(self.generation.universe, 50, 200)
        self.generation["medium"] = fuzz.gaussmf(self.generation.universe, mean=275, sigma=80)
        self.generation["long"] = fuzz.smf(self.generation.universe, 350, 500)

        self.prob_crossover["small"] = fuzz.zmf(self.prob_crossover.universe, 0.625, 0.7)
        self.prob_crossover["medium"] = fuzz.trapmf(self.prob_crossover.universe, [0.63, 0.7, 0.72, 0.78])
        self.prob_crossover["large"] = fuzz.trapmf(self.prob_crossover.universe, [0.72, 0.78, 0.8, 0.87])
        self.prob_crossover["very_large"] = fuzz.smf(self.prob_crossover.universe, 0.8, 0.875)

        self.prob_mutasi["very_small"] = fuzz.zmf(self.prob_mutasi.universe, 0.025, 0.1)
        self.prob_mutasi["small"] = fuzz.trapmf(self.prob_mutasi.universe, [0.047, 0.083, 0.1, 0.14])
        self.prob_mutasi["medium"] = fuzz.trapmf(self.prob_mutasi.universe, [0.1, 0.14, 0.167, 0.2])
        self.prob_mutasi["large"] = fuzz.smf(self.prob_mutasi.universe, 0.15, 0.225)

    def crossover_rules(self):
        self.customMembership()
        self.crossover_rule1 = ctrl.Rule(self.population_size["small"] and self.generation["short"], self.prob_crossover["medium"])
        self.crossover_rule2 = ctrl.Rule(self.population_size["medium"] and self.generation["short"], self.prob_crossover["small"]
        self.crossover_rule3 = ctrl.Rule(self.population_size["large"] and self.generation["short"], self.prob_crossover["small"])
        self.crossover_rule4 = ctrl.Rule(self.population_size["small"] and self.generation["medium"], self.prob_crossover["large"]
        self.crossover_rule5 = ctrl.Rule(self.population_size["medium"] and self.generation["medium"], self.prob_crossover["large"])
        self.crossover_rule6 = ctrl.Rule(self.population_size["large"] and self.generation["medium"], self.prob_crossover["medium"])
        self.crossover_rule7 = ctrl.Rule(self.population_size["small"] and self.generation["long"], self.prob_crossover["very_large"])
        self.crossover_rule8 = ctrl.Rule(self.population_size["medium"] and self.generation["long"], self.prob_crossover["very_large"])
        self.crossover_rule9 = ctrl.Rule(self.population_size["large"] and self.generation["long"], self.prob_crossover["large"])

    def mutasi_rules(self):
        self.customMembership()
        self.mutasi_rule1 = ctrl.Rule(self.population_size["small"] and self.generation["short"], self.prob_mutasi["large"])
        self.mutasi_rule2 = ctrl.Rule(self.population_size["medium"] and self.generation["short"], self.prob_mutasi["medium"])
        self.mutasi_rule3 = ctrl.Rule(self.population_size["large"] and self.generation["short"], self.prob_mutasi["small"])
        self.mutasi_rule4 = ctrl.Rule(self.population_size["small"] and self.generation["medium"], self.prob_mutasi["medium"])
        self.mutasi_rule5 = ctrl.Rule(self.population_size["medium"] and self.generation["medium"], self.prob_mutasi["small"])
        self.mutasi_rule6 = ctrl.Rule(self.population_size["large"] and self.generation["medium"], self.prob_mutasi["very_small"])
        self.mutasi_rule7 = ctrl.Rule(self.population_size["small"] and self.generation["long"], self.prob_mutasi["small"])
        self.mutasi_rule8 = ctrl.Rule(self.population_size["medium"] and self.generation["long"], self.prob_mutasi["very_small"])
        self.mutasi_rule9 = ctrl.Rule(self.population_size["large"] and self.generation["long"], self.prob_mutasi["very_small"])

    def controlSystem(self):
        self.crossover_rules()
        self.mutasi_rules()
        crossover_value = ctrl.ControlSystem([self.crossover_rule1, self.crossover_rule2, self.crossover_rule3, self.crossover_rule4, self.crossover_rule5, self.crossover_rule6, self.crossover_rule7, self.crossover_rule8, self.crossover_rule9])
        self.ctrl_value = ctrl.ControlSystemSimulation(value)

        self.ctrl_value.input['Population Size'] = 10
        self.ctrl_value.input['Generation'] = 100

        self.ctrl_value.compute()

    def result(self):
        self.controlSystem()
        print(self.ctrl_value.output["Prob Crossover"])
        self.prob_crossover.view(sim=self.ctrl_value)
        


class Data:
    ROOMS = [
        ["FG 202", 35],
        ["FG 204", 35],
        ["FG 205", 35],
        ["FG 303B", 35],
        ["FG 305", 30],
        ["M. Teaching", 30],
        ["MDR2", 15],
        ["Workshop", 35],
        ["Lab", 40],
        ["Aula FH", 45],
    ]
    MEETING_TIMES = [
        ["J1", "07:30 - 08.10"],
        ["J2", "08.10 - 08.50"],
        ["J3", "09:00 - 09.40"],
        ["J4", "09:40 - 10.20"],
        ["J5", "10:30 - 11.10"],
        ["J6", "11:10 - 11.50"],
        ["J7", "13:00 - 13.40"],
        ["J8", "13:40 - 14.20"],
        ["J9", "14:25 - 15.05"],
        ["J10", "16:00 - 16.40"],
        ["J11", "16:40 - 17.20"],
    ]
    MEETING_DAYS = [
        ["H1", "Senin"],
        ["H2", "Selasa"],
        ["H3", "Rabu"],
        ["H4", "Kamis"],
        ["H5", "Jum'at"],
    ]
    INSTRUCTORS = [
        ["I1", "Prof Hamzah Upu"],
        ["I2", "Syahrullah Asyari"],
        ["I3", "Dr Ilham Minggi"],
        ["I4", "Dr Ahmad Talib"],
        ["I5", "Dr Rosidah"],
        ["I6", "Ahmad Zaki"],
        ["I7", "Dr Muhammad Darwis"],
        ["I8", "Said Fachry Assagaf"],
        ["I9", "Dr Hamda"],
        ["I10", "Iwan Setiawan HR"],
        ["I11", "Dr Rusli"],
        ["I12", "Dr Alimuddin"],
        ["I13", "Dr Bernard"],
        ["I14", "Muh. Husnul Khuluq"],
        ["I15", "Dr Asdar"],
        ["I16", "Sabri Ph.D"],
        ["I17", "Dr Hisyam Ihsan"],
        ["I18", "Fajar Arwadi"],
        ["I19", "Dr Rahmat Syam"],
        ["I20", "Prof Abdul Rahman"],
        ["I21", "Dr Djadir"],
        ["I22", "Drs Muhammad Dinar"],
        ["I23", "Prof Usman Mulbar"],
        ["I24", "Syamsuddin Mas'ud"],
        ["I25", "Prof Suradi"],
        ["I26", "Dr Maya Sari Wahyuni"],
        ["I25", "Prof Syafruddin Side"],
        ["I27", "Irwan S.Si"],
        ["I28", "Dr Kamaruddin Hasan"],
        ["I29", "Dr Wahidah Sanusi"],
        ["I30", "Sukarna, S.Pd"],
        ["I31", "Nasrullah, S.Pd"],
        ["I32", "Dr Muhammad Abdy"],
        ["I33", "Dr Awi"],
        ["I34", "Sulaiman, S.Si"],
        ["I35", "Nurwati Djam'an"],
        ["I36", "Prof Baso Intang"],
        ["I37", "Prof Nurdin"],
    ]

    def __init__(self):
        self._rooms = []
        self._meetingTimes = []
        self._meetingDays = []
        self._instructors = []
        for i in range(0, len(self.ROOMS)):
            self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1]))
        for i in range(0, len(self.MEETING_TIMES)):
            self._meetingTimes.append(MeetingTime(self.MEETING_TIMES[i][0], self.MEETING_TIMES[i][1]))
        for i in range(0, len(self.MEETING_DAYS)):
            self._meetingDays.append(MeetingDay(self.MEETING_DAYS[i][0], self.MEETING_DAYS[i][1]))
        for i in range(0, len(self.INSTRUCTORS)):
            self._instructors.append(Instructor(self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1]))
        course1 = Course("C1", "Landasan Matematika", [self._instructors[0], self._instructors[1]], 25)
        course2 = Course("C2", "Kalkulus I", [self._instructors[0], self._instructors[1], self._instructors[2]],35)
        course3 = Course("C3", "Aljabar Elementer", [self._instructors[0], self._instructors[1]], 25)
        course4 = Course("C4", "Pendidikan Agama Islam", [self._instructors[2], self._instructors[3]], 30)
        course5 = Course("C5", "Pendidikan Lingkungan Hidup", [self._instructors[3]], 35)
        course6 = Course("C6", "Statistika Dasar", [self._instructors[0], self._instructors[2]], 45)
        course7 = Course("C7", "Trigonometri", [self._instructors[1], self._instructors[3]], 30)
        course8 = Course("C8", "Analisis Real", [self._instructors[5], self._instructors[6]], 35)
        course9 = Course("C9", "Analisis Kompleks", [self._instructors[3], self._instructors[4]], 45)
        course10 = Course("C10", "Teori Fuzzy", [self._instructors[6], self._instructors[9]], 35)
        course11 = Course("C11", "Teori Bilangan", [self._instructors[6], self._instructors[9]], 35)
        course12 = Course("C12", "Landasan Keguruan", [self._instructors[8], self._instructors[9]], 30)
        course13 = Course("C13", "Geometri Analitik", [self._instructors[8], self._instructors[9]], 40)
        course14 = Course("C14", "Aljabar Linear", [self._instructors[8], self._instructors[9]], 25)
        course15 = Course("C15","Kalkulus Differensial", [self._instructors[8], self._instructors[9]], 40)
        self._courses = [course1, course2, course3, course4, course5, course6, course7, course8, course9, course10, course11, course12, course13, course14, course15]

        A1_S1 = Department("A1 S1", [course1, course3, course5, course12])
        A2_S1 = Department("A2 S1", [course2, course10, course11])
        B_S1 = Department("B S1", [course6, course7, course8])
        C_S1 = Department("C S1", [course6, course7, course8])
        A1_S3 = Department("A1 S3", [course4, course5, course6, course13])
        A2_S3 = Department("A2 S3", [course2, course10, course11])
        B_S3 = Department("B S3", [course6, course7, course9])
        C_S3 = Department("C S3", [course6, course7, course9])
        A1_S5 = Department("A1 S5", [course9, course10, course11, course15])
        A2_S5 = Department("A2 S5", [course8, course10, course11])
        B_S5 = Department("B S5", [course7, course8, course9, course14])
        C_S5 = Department("C S5", [course7, course8, course9, course14])
        self._depts = [A1_S1, A2_S1, B_S1, C_S1, A1_S3, A2_S3, B_S3, C_S3, A1_S5, A2_S5, B_S5, C_S5]
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

    def get_meetingDays(self):
        return self._meetingDays

    def get_numberOfClasses(self):
        return self._numberOfClasses


class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._numbOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True

    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes

    def get_numbOfConflicts(self):
        return self._numbOfConflicts

    def get_fitness(self):
        if self._isFitnessChanged == True:
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness

    def initialize(self):
        depts = self._data.get_depts()
        for i in range(0, len(depts)):
            courses = depts[i].get_courses()
            for j in range(0, len(courses)):
                newClass = Class(self._classNumb, depts[i], courses[j])
                self._classNumb += 1
                newClass.set_meetingTime(
                    data.get_meetingTimes()[
                        rnd.randrange(0, len(data.get_meetingTimes()))
                    ]
                )
                newClass.set_meetingDay(
                    data.get_meetingDays()[
                        rnd.randrange(0, len(data.get_meetingDays()))
                    ]
                )
                newClass.set_room(
                    data.get_rooms()[rnd.randrange(0, len(data.get_rooms()))]
                )
                newClass.set_instructor(
                    courses[j].get_instructors()[
                        rnd.randrange(0, len(courses[j].get_instructors()))
                    ]
                )
                self._classes.append(newClass)
        return self

    def calculate_fitness(self):
        self._numbOfConflicts = 0
        classes = self.get_classes()
        for i in range(0, len(classes)):
            if (
                classes[i].get_room().get_seatingCapacity()
                < classes[i].get_course().get_maxNumbOfStudents()
            ):
                self._numbOfConflicts += 1
            for j in range(0, len(classes)):
                if j >= i:
                    if (
                        classes[i].get_meetingDay() == classes[j].get_meetingDay()
                        and classes[i].get_meetingTime() == classes[j].get_meetingTime()
                        and classes[i].get_id() != classes[j].get_id()
                    ):
                        if classes[i].get_id() == classes[j].get_id():
                            self._numbOfConflicts += 1
                        if classes[i].get_instructor() == classes[j].get_instructor():
                            self._numbOfConflicts += 1
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
    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population))

    def _crossover_population(self, pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[0]
            schedule2 = self._select_tournament_population(pop).get_schedules()[0]
            crossover_pop.get_schedules().append(
                self._crossover_schedule(schedule1, schedule2)
            )
            i += 1
        return crossover_pop

    def _mutate_population(self, population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population

    def _crossover_schedule(self, schedule1, schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            if rnd.random() > 0.5:
                crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else:
                crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule

    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(0, len(mutateSchedule.get_classes())):
            if MUTATION_RATE > rnd.random():
                mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule

    def _select_tournament_population(self, pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(
                pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)]
            )
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop


class Course:
    def __init__(self, number, name, instructors, maxNumbOfStudents):
        self._number = number
        self._name = name
        self._instructors = instructors
        self._maxNumbOfStudents = maxNumbOfStudents

    def get_number(self):
        return self._number

    def get_name(self):
        return self._name

    def get_instructors(self):
        return self._instructors

    def get_maxNumbOfStudents(self):
        return self._maxNumbOfStudents

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
    def __init__(self, id, time):
        self._id = id
        self._time = time

    def get_id(self):
        return self._id

    def get_time(self):
        return self._time


class MeetingDay:
    def __init__(self, id, day):
        self._id = id
        self._day = day

    def get_id(self):
        return self._id

    def get_day(self):
        return self._day


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
        self._meetingDay = None
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

    def get_meetingDay(self):
        return self._meetingDay

    def get_room(self):
        return self._room

    def set_instructor(self, instructor):
        self._instructor = instructor

    def set_meetingTime(self, meetingTime):
        self._meetingTime = meetingTime

    def set_meetingDay(self, meetingDay):
        self._meetingDay = meetingDay

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
            + ","
            + str(self._meetingDay.get_id())
        )


class DisplayMgr:
    def print_available_data(self):
        print(">Deklarasikan semua data")
        self.print_dept()
        self.print_course()
        self.print_room()
        self.print_instructor()
        self.print_meeting_times()
        self.print_meeting_days()

    def print_dept(self):
        depts = data.get_depts()
        availableDeptsTable = prettytable.PrettyTable(["prodi", "mata kuliah"])
        for i in range(0, len(depts)):
            courses = depts.__getitem__(i).get_courses()
            tempStr = "["
            for j in range(0, len(courses) - 1):
                tempStr += courses[j].__str__() + ", "
            tempStr += courses[len(courses) - 1].__str__() + "]"
            availableDeptsTable.add_row([depts.__getitem__(i).get_name(), tempStr])
        print(availableDeptsTable)

    def print_course(self):
        availableCoursesTable = prettytable.PrettyTable(
            ["id", "mata kuliah #", "max # of students", "dosen"]
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
                    str(courses[i].get_maxNumbOfStudents()),
                    tempStr,
                ]
            )
        print(availableCoursesTable)

    def print_instructor(self):
        availableInstructorsTable = prettytable.PrettyTable(["id", "dosen"])
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
        rooms = data.get_rooms()
        for i in range(0, len(rooms)):
            availableRoomsTable.add_row(
                [str(rooms[i].get_number()), str(rooms[i].get_seatingCapacity())]
            )
        print(availableRoomsTable)

    def print_meeting_times(self):
        availableMeetingTimeTable = prettytable.PrettyTable(["id", "Meeting Time"])
        meetingTimes = data.get_meetingTimes()
        for i in range(0, len(meetingTimes)):
            availableMeetingTimeTable.add_row(
                [meetingTimes[i].get_id(), meetingTimes[i].get_time()]
            )
        print(availableMeetingTimeTable)

    def print_meeting_days(self):
        availableMeetingDayTable = prettytable.PrettyTable(["id", "Meeting Day"])
        meetingDays = data.get_meetingDays()
        for i in range(0, len(meetingDays)):
            availableMeetingDayTable.add_row(
                [meetingDays[i].get_id(), meetingDays[i].get_day()]
            )
        print(availableMeetingDayTable)

    def print_generation(self, population):
        table1 = prettytable.PrettyTable(
            [
                "schedules #",
                "fitness",
                "# of conflicts",
                # "classes [dept,class, room, instructor, meeting-time]",
            ]
        )
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            table1.add_row(
                [
                    str(i),
                    round(schedules[i].get_fitness(), 3),
                    schedules[i].get_numbOfConflicts(),
                    # schedules[i],
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
                "Instuctors (Id)",
                "Meeting Time (Id)",
                "Meeting Day (Id)",
            ]
        )
        for i in range(0, len(classes)):
            table.add_row(
                [
                    str(i + 1),
                    classes[i].get_dept().get_name(),
                    classes[i].get_course().get_name()
                    + " ("
                    + classes[i].get_course().get_number()
                    + ", "
                    + str(classes[i].get_course().get_maxNumbOfStudents())
                    + ")",
                    classes[i].get_room().get_number()
                    + " ("
                    + str(classes[i].get_room().get_seatingCapacity())
                    + ")",
                    classes[i].get_instructor().get_name()
                    + " ("
                    + str(classes[i].get_instructor().get_id())
                    + ")",
                    classes[i].get_meetingTime().get_time()
                    + " ("
                    + str(classes[i].get_meetingTime().get_id())
                    + ")",
                    classes[i].get_meetingDay().get_day()
                    + " ("
                    + str(classes[i].get_meetingDay().get_id())
                    + ")",
                ]
            )
        print(table)


data = Data()
displayMgr = DisplayMgr()
displayMgr.print_available_data()
generationNumber = 0
print("\n> Generation # " + str(generationNumber))
population = Population(POPULATION_SIZE)
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
displayMgr.print_generation(population)
displayMgr.print_schedule_as_table(population.get_schedules()[0])
genetiAlgorithm = GeneticAlgorithm()
while population.get_schedules()[0].get_fitness() != 1.0:
    generationNumber += 1
    print("\n> Generation # " + str(generationNumber))
    population = genetiAlgorithm.evolve(population)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    displayMgr.print_generation(population)
    displayMgr.print_schedule_as_table(population.get_schedules()[0])
print("\n\n")
