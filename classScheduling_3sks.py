import prettytable as prettytable
import random as rnd

POPULATION_SIZE = 10
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.2


class Data:
    ROOMS = [
        ["FG 202", 50],
        ["FG 204", 45],
        ["FG 205", 45],
        ["FG 303B", 45],
        ["FG 305", 42],
        ["Aula FH", 60],
        ["Workshop", 42],
        ["Mandiri 2", 22],
    ]
    MEETING_TIMES = [
        ["J1", "I-III"],
        ["J2", "IV-VI"],
        ["J3", "VII-IX"],

    ]
    MEETING_DAYS = [
        ["H1", "Senin"],
        ["H2", "Selasa"],
        ["H3", "Rabu"],
        ["H4", "Kamis"],
        ["H5", "Jum'at"],
    ]
    INSTRUCTORS = [
        ["D0", "1118"], #Prof. Dr. H. Hamzah Upu, M.Ed.
        ["D1", "1121"], #Dr. Ilham Minggi, M.Si.
        ["D2", "1110"], #Dr. Muhammad Darwis M., M.Pd.
        ["D3", "1127"], #Drs. Hamda, DipKom, M.Pd.
        ["D4", "1123"], #Dr. Rusli, M.Si.
        ["D5", "1117"], #Dr. Alimuddin, M.Si.
        ["D6", "1136"], #Dr. Asdar, S.Pd., M.Pd.
        ["D7", "1122"], #Dr. Ahmad Talib, M.Si
        ["D8", "1125"], #Dr. Hisyam Ihsan, M.Si.
        ["D9", "1111"], #Dr. H. Bernard, M.S.
        ["D10", "1146"], #Sahid, S.Pd., M.Pd
        ["D11", "1114"], #Prof. Dr. Baso Intang Sappaile, M.Pd.
        ["D12", "1107"], #Dr. H. Djadir, M.Pd.
        ["D13", "1108"], #Drs. Muhammad Dinar, M.Pd.
        ["D14", "1113"], #Prof. Dr. Ruslan, M.Pd.
        ["D15", "1119"], #Prof. Dr. H. Suradi, M.S.
        ["D16", "1131"], #Prof. Dr. Syafruddin Side, S.Si., M.Si
        ["D17", "1130"], #Dr. Muhammad Abdy, S.Si., M.Si
        ["D18", "1115"], #Prof. Dr. Abdul Rahman, M.Pd.
        ["D19", "1128"], #Prof. Dr. H. Nurdin, M.Pd.
        ["D20", "1135"], #H. Sukarna, S.Pd.,M.Si.
        ["D21", "1141"], #Sulaiman, S.Si., M.Kom, M.M.
        ["D22", "1133"], #Dr. Wahidah Sanusi, S.Si., M.Si
        ["D23", "1147"], #Nasrullah, S.Pd., M.Pd
        ["D24", "1120"], #Dr. Rosidah, M.Si.
        ["D25", "1134"], #Sabri, S.Pd., M.Sc., Ph.D.
        ["D26", "1154"], #Sutamrin, S.Si., M.Pd.
        ["D27", "1126"], #Dr. Awi, M.Si.
        ["D28", "1138"], #Dr. H. Rahmat Syam, S.T. M.Kom
        ["D29", "1142"], #Ahmad Zaki, S.Si., M.Si.
        ["D30", "1151"], #Sahlan Sidjara, S.Si., M.Si.
        ["D31", "1155"], #Said Fachry Assagaf, S.Pd., M.Sc.
        ["D32", "1150"], #Fajar Arwadi, S.Pd., M.Sc
        ["D33", "1153"], #Irwan, S.Si., M.Si.
        ["D34", "1116"], #Prof. Dr. Usman Mulbar, M.Pd.
        ["D35", "1149"], #Syahrullah Asyari, S.Pd., M.Pd.
        ["D36", "1139"], #Dr. Maya Sari Wahyuni, S.T, M.Kom
        ["D37", "1156"], #Syamsuddin Mas'ud, S.Pd., M.Sc.
        ["D38", "1145"], #Nurwati Djam'an, S.Pd., M.Pd., Ph.D.
        ["D39", "1157"], #Muh. Husnul Khuluq, S.Pd., M.Sc.
        ["D40", "M007"], #Iwan Setiawan HR., S.Pd., M.Pd.
        ["D41", "M008"], #Fauziah Alimuddin, S.Pd., M.Pd.
        ["D42", "TPB1"], #Hartati, S.Si., M.Si., Ph.D.
        ["D43", "TPB2"], # Sulistiawati, S.Si.,M.Si.,M.T.
        ["D44", "TPB3"], #Drs. Muhammad Yunus, M.Si.
        ["D45", "TPB4"], #Rosmini Maru, S.Pd., M.Si.,Ph.D.
        ["D46", "TPB5"], #Dr. S. Salmiah Sari, M.Pd.
        ["D47", "TPB6"], #Vicran Zharvan, S.Si.,M.Si.
        ["D48", "TPB7"], #Suriati Eka Putri, S.Si., M.Si.
        ["D49", "TPB8"], #Diana Eka Pratiwi, S.Si., M.Si.
        ["D50", "TPB9"], #Dr. Andi Faridah, S.Si., M.Si.
        ["D51", "TPB10"], #Dr. Erman Syarif, S.Pd., M.Pd.
        ["D52", "TPB11"], #Iwan Dini, S.Si., M.Si.
        ["D53", "TPB12"], #Arifah Novia Arifin, S.Pd, M.Pd
        ["D54", "TPB13"], #Musfirah, S.Pd.M.Pd.
        ["D55", "TPB14"], #dr. Irma Suryani Idris Arief, M.Kes
        ["D56", "TPB15"], #Yusnaeni Yusuf, S.Si., M.Si
        ["D57", "TPB16"], #Syamsunardi, S.Pd., M.Pd.
        ["D58", "MKU"], #Dosen MKU
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
        # ===================================
        # Course A1 Semester 1 
        courseA1_S1_1 = Course("A1_S1_1", "Landasan Matematika", [self._instructors[1], self._instructors[7]], 40)
        courseA1_S1_2 = Course("A1_S1_2", "Kalkulus Diferensial", [self._instructors[2], self._instructors[31]], 40)
        # Course A1 Semester 3
        courseA1_S3_1 = Course("A1_S3_2", "Strategi Pembelajaran Matematika", [self._instructors[30], self._instructors[39]],40)
        # Course A1 Semester 5
        courseA1_S5_1 = Course("A1_S5_1", "Pengantar Analisis Real", [self._instructors[8], self._instructors[30]], 40)
        courseA1_S5_2 = Course("A1_S5_2", "Struktur Aljabar", [self._instructors[15], self._instructors[5]], 40)
        courseA1_S5_3 = Course("A1_S5_3", "Metodologi Penelitian Kuantitatif", [self._instructors[14], self._instructors[11]], 40)
        courseA1_S5_4 = Course("A2_S5_4", "Pemodelan Matematika", [self._instructors[16]], 30)

        # ===================================
        # Course A2 Semester 1 
        courseA2_S1_1 = Course("A2_S1_1", "Landasan Matematika", [self._instructors[1], self._instructors[7]], 40)
        courseA2_S1_2 = Course("A2_S1_2", "Kalkulus Diferensial", [self._instructors[4], self._instructors[31]], 40)
        # Course A2 Semester 3
        courseA2_S3_1 = Course("A2_S3_1", "Strategi Pembelajaran Matematika", [self._instructors[15], self._instructors[35]], 40)
        # Course A2 Semester 5
        courseA2_S5_1 = Course("A2_S5_1", "Pengantar Analisis Real", [self._instructors[2], self._instructors[1]], 40)
        courseA2_S5_2 = Course("A2_S5_2", "Struktur Aljabar", [self._instructors[15], self._instructors[30]], 40)
        courseA2_S5_3 = Course("A2_S5_3", "Metodologi Penelitian Kuantitatif", [self._instructors[14], self._instructors[11]], 40)
        courseA2_S5_4 = Course("A2_S5_4", "Pemodelan Matematika", [self._instructors[16]], 30)

        # ===================================
        # Course C Semester 1 
        courseC_S1_1 = Course("C_S1_1", "Fundamentals of Mathematics", [self._instructors[7], self._instructors[39]], 40)
        courseC_S1_2 = Course("C_S1_2", "Differensial Calculus", [self._instructors[1], self._instructors[40]], 40)
        # Course C Semester 3
        courseC_S3_1 = Course("C_S3_2", "Mathematics Learning Strategy", [self._instructors[19], self._instructors[39]], 40)
        # Course C Semester 5
        courseC_S5_1 = Course("C_S5_1", "Introduction to Real Analysis", [self._instructors[2], self._instructors[30]], 40)
        courseC_S5_2 = Course("C_S5_2", "Introduction to Modern Algebra", [self._instructors[4], self._instructors[38]], 40)
        courseC_S5_3 = Course("C_S5_3", "Quantitative Research Methodology in Education", [self._instructors[11], self._instructors[31]], 40)
        courseC_S5_4 = Course("C_S5_4", "Mathematical Modeling", [self._instructors[16]], 30)

        # ===================================
        # Course B Semester 1 
        courseB_S1_1 = Course("B_S1_1", "Kalkulus Diferensial", [self._instructors[40], self._instructors[35]], 40)
        courseB_S1_2 = Course("B_S1_2", "Landasan Matematika", [self._instructors[3], self._instructors[32]], 40)
        # Course B Semester 3
        courseB_S3_1 = Course("B_S3_1", "Kalkulus Peubah Banyak", [self._instructors[3], self._instructors[32]], 40)
        courseB_S3_2 = Course("B_S3_2", "Aljabar Linear Lanjut", [self._instructors[6], self._instructors[9]], 40)
        courseB_S3_3 = Course("B_S3_3", "Teori Peluang", [self._instructors[22]], 40)
        courseB_S3_4 = Course("B_S3_4", "Teori Bilangan", [self._instructors[34], self._instructors[33]], 40)
        # Course B Semester 5
        courseB_S5_1 = Course("B_S5_1", "Program Linear", [self._instructors[20], self._instructors[26]], 40)
        courseB_S5_2 = Course("B_S5_2", "Pemodelan Matematika", [self._instructors[16]], 40)
        courseB_S5_3 = Course("B_S5_3", "Kapita Selekta", [self._instructors[16], self._instructors[22], self._instructors[20], self._instructors[28]], 40)
        courseB_S5_4 = Course("B_S5_4", "Statistika Multivariat", [self._instructors[22], self._instructors[33]], 20)
        courseB_S5_5 = Course("B_S5_5", "Sistem Dinamik", [self._instructors[16]], 20)
        self._courses = [
            courseA1_S1_1, courseA1_S1_2,
            courseA1_S3_1, 
            courseA1_S5_1, courseA1_S5_2, courseA1_S5_3, courseA1_S5_4,
            courseA2_S1_1, courseA2_S1_2, 
            courseA2_S3_1,
            courseA2_S5_1, courseA2_S5_2, courseA2_S5_3, courseA2_S5_4, 
            courseC_S1_1, courseC_S1_2, 
            courseC_S3_1, 
            courseC_S5_1, courseC_S5_2, courseC_S5_3, courseC_S5_4, 
            courseB_S1_1, courseB_S1_2, 
            courseB_S3_1, courseB_S3_2, courseB_S3_3, courseB_S3_4, 
            courseB_S5_1, courseB_S5_2, courseB_S5_3, courseB_S5_4, courseB_S5_5
        ]

        A1_S1 = Department("A1 S1", [courseA1_S1_1, courseA1_S1_2])
        A1_S3 = Department("A1 S3", [courseA1_S3_1])
        A1_S5 = Department("A1 S5", [courseA1_S5_1, courseA1_S5_2, courseA1_S5_3, courseA1_S5_4])
        A2_S1 = Department("A2 S1", [courseA2_S1_1, courseA2_S1_2])
        A2_S3 = Department("A2 S3", [courseA2_S3_1])
        A2_S5 = Department("A2 S5", [courseA2_S5_1, courseA2_S5_2, courseA2_S5_3, courseA2_S5_4])
        C_S1 = Department("C S1", [courseC_S1_1, courseC_S1_2])
        C_S3 = Department("C S3", [courseC_S3_1])
        C_S5 = Department("C S5", [courseC_S5_1, courseC_S5_2, courseC_S5_3, courseC_S5_4])
        B_S1 = Department("B S1", [courseB_S1_1, courseB_S1_2])
        B_S3 = Department("B S3", [courseB_S3_1, courseB_S3_2, courseB_S3_3, courseB_S3_4])
        B_S5 = Department("B S5", [courseB_S5_1, courseB_S5_2, courseB_S5_3, courseB_S5_4, courseB_S5_5])
        self._depts = [A1_S1, A1_S3, A1_S5, A2_S1, A2_S3, A2_S5, C_S1, C_S3, C_S5, B_S1, B_S3, B_S5]
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
                        classes[i].get_meetingTime() == classes[j].get_meetingTime()
                        and classes[i].get_meetingDay() == classes[j].get_meetingDay()
                        and classes[i].get_id() != classes[j].get_id()
                    ):
                        if classes[i].get_room() == classes[j].get_room():
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
        print(">All Available Data")
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
                "# of conflicts"
            ]
        )
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            table1.add_row(
                [
                    str(i),
                    round(schedules[i].get_fitness(), 3),
                    schedules[i].get_numbOfConflicts()
                ]
            )
        print(table1)

    def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()
        table = prettytable.PrettyTable(
            [
                "No #",
                "Kelas",
                "Mata Kuliah",
                "Ruangan",
                "Dosen",
                "Waktu",
                "Hari",
            ]
        )
        for i in range(0, len(classes)):
            table.add_row(
                [
                    str(i + 1),
                    classes[i].get_dept().get_name(),
                    classes[i].get_course().get_name(),
                    classes[i].get_room().get_number(),
                    classes[i].get_instructor().get_name(),
                    classes[i].get_meetingTime().get_time(),
                    classes[i].get_meetingDay().get_day()
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
