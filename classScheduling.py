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
        self.population = ctrl.Antecedent(np.arange(0, 1000, 1), "Population")
        self.generation = ctrl.Antecedent(np.arange(0, 1000, 1), "Generation")
        self.crossover = ctrl.Consequent(np.arange(0.6, 0.9, 0.01), "Crossover")
        self.mutation = ctrl.Consequent(np.arange(0, 0.25, 0.01), "Mutation")

    def customMembership(self):
        self.population["small"] = fuzz.zmf(self.population.universe, 50, 250)
        self.population["medium"] = fuzz.gaussmf(self.population.universe, mean=275, sigma=80)
        self.population["large"] = fuzz.smf(self.population.universe, 350, 500)

        self.generation["short"] = fuzz.zmf(self.generation.universe, 50, 200)
        self.generation["medium"] = fuzz.gaussmf(self.generation.universe, mean=275, sigma=80)
        self.generation["long"] = fuzz.smf(self.generation.universe, 350, 500)

        self.crossover["small"] = fuzz.zmf(self.crossover.universe, 0.625, 0.7)
        self.crossover["medium"] = fuzz.trapmf(self.crossover.universe, [0.63, 0.7, 0.72, 0.78])
        self.crossover["large"] = fuzz.trapmf(self.crossover.universe, [0.72, 0.78, 0.8, 0.87])
        self.crossover["very_large"] = fuzz.smf(self.crossover.universe, 0.8, 0.875)

        self.mutation["very_small"] = fuzz.zmf(self.mutation.universe, 0.025, 0.1)
        self.mutation["small"] = fuzz.trapmf(self.mutation.universe, [0.047, 0.083, 0.1, 0.14])
        self.mutation["medium"] = fuzz.trapmf(self.mutation.universe, [0.1, 0.14, 0.167, 0.2])
        self.mutation["large"] = fuzz.smf(self.mutation.universe, 0.15, 0.225)

    def crossover_rules(self):
        self.customMembership()
        self.crossover_rule1 = ctrl.Rule(antecedent=(self.population["small"] & self.generation["short"]), consequent=(self.crossover["medium"]))
        self.crossover_rule2 = ctrl.Rule(antecedent=(self.population["medium"] & self.generation["short"]), consequent=(self.crossover["small"]))
        self.crossover_rule3 = ctrl.Rule(antecedent=(self.population["large"] & self.generation["short"]), consequent=(self.crossover["small"]))
        self.crossover_rule4 = ctrl.Rule(antecedent=(self.population["small"] & self.generation["medium"]), consequent=(self.crossover["large"]))
        self.crossover_rule5 = ctrl.Rule(antecedent=(self.population["medium"] & self.generation["medium"]), consequent=(self.crossover["large"]))
        self.crossover_rule6 = ctrl.Rule(antecedent=(self.population["large"] & self.generation["medium"]), consequent=(self.crossover["medium"]))
        self.crossover_rule7 = ctrl.Rule(antecedent=(self.population["small"] & self.generation["long"]), consequent=(self.crossover["very_large"]))
        self.crossover_rule8 = ctrl.Rule(antecedent=(self.population["medium"] & self.generation["long"]), consequent=(self.crossover["very_large"]))
        self.crossover_rule9 = ctrl.Rule(antecedent=(self.population["large"] & self.generation["long"]), consequent=(self.crossover["large"]))

    def mutation_rules(self):
        self.customMembership()
        self.mutation_rule1 = ctrl.Rule(antecedent=(self.population["small"] & self.generation["short"]), consequent=(self.mutation["large"]))
        self.mutation_rule2 = ctrl.Rule(antecedent=(self.population["medium"] & self.generation["short"]), consequent=(self.mutation["medium"]))
        self.mutation_rule3 = ctrl.Rule(antecedent=(self.population["large"] & self.generation["short"]), consequent=(self.mutation["small"]))
        self.mutation_rule4 = ctrl.Rule(antecedent=(self.population["small"] & self.generation["medium"]), consequent=(self.mutation["medium"]))
        self.mutation_rule5 = ctrl.Rule(antecedent=(self.population["medium"] & self.generation["medium"]), consequent=(self.mutation["small"]))
        self.mutation_rule6 = ctrl.Rule(antecedent=(self.population["large"] & self.generation["medium"]), consequent=(self.mutation["very_small"]))
        self.mutation_rule7 = ctrl.Rule(antecedent=(self.population["small"] & self.generation["long"]), consequent=(self.mutation["small"]))
        self.mutation_rule8 = ctrl.Rule(antecedent=(self.population["medium"] & self.generation["long"]), consequent=(self.mutation["very_small"]))
        self.mutation_rule9 = ctrl.Rule(antecedent=(self.population["large"] & self.generation["long"]), consequent=(self.mutation["very_small"]))

    def controlSystem(self):
        self.crossover_rules()
        self.mutation_rules()
        crossover_value = ctrl.ControlSystem([self.crossover_rule1, self.crossover_rule2, self.crossover_rule3, self.crossover_rule4, self.crossover_rule5, self.crossover_rule6, self.crossover_rule7, self.crossover_rule8, self.crossover_rule9])
        mutation_value = ctrl.ControlSystem([self.mutation_rule1, self.mutation_rule2, self.mutation_rule3, self.mutation_rule4, self.mutation_rule5, self.mutation_rule6, self.mutation_rule7, self.mutation_rule8, self.mutation_rule9])
        self.crossover_simulation = ctrl.ControlSystemSimulation(crossover_value)
        self.mutation_simulation = ctrl.ControlSystemSimulation(mutation_value)

        self.crossover_simulation.input['Population'] = 10
        self.crossover_simulation.input['Generation'] = 100

        self.mutation_simulation.input['Population'] = 10
        self.mutation_simulation.input['Generation'] = 100

        self.crossover_simulation.compute()
        self.mutation_simulation.compute()

    def result(self):
        self.controlSystem()
        print(self.crossover_simulation.output["Crossover"])
        print(self.mutation_simulation.output["Mutation"])
        self.prob_crossover.view(sim=self.ctrl_value)
        


class Data:
    ROOMS = [
        ["FG 202", 45],
        ["FG 204", 40],
        ["FG 205", 40],
        ["FG 303B", 40],
        ["FG 305", 30],
        ["Aula FH", 50],
        ["Workshop", 25],
    ]
    MEETING_TIMES = [
        ["J1", "07:30 - 10.00"],
        ["J2", "10.10 - 12.30"],
        ["J3", "13:00 - 15.30"],
        # ["J4", "15:45 - 17.30"]
    ]
    MEETING_DAYS = [
        ["H1", "Senin"],
        ["H2", "Selasa"],
        ["H3", "Rabu"],
        ["H4", "Kamis"],
        ["H5", "Jum'at"],
    ]
    INSTRUCTORS = [
        ["D0", "Prof Dr. H. Hamzah Upu, M.Ed."],
        ["D1", "Dr. Ilham Minggi, M.Si."],
        ["D2", "Dr. Muhammad Darwis M, M.Pd."],
        ["D3", "Drs. Hamda, DipKom, M.Pd."],
        ["D4", "Dr. Rusli, M.Si."],
        ["D5", "Dr. Alimuddin, M.Si."],
        ["D6", "Dr. Asdar, S.Pd., M.Pd."],
        ["D7", "Dr. Ahmad Talib, M.Si"],
        ["D8", "Dr. Hisyam Ihsan, M.Si."],
        ["D9", "Dr. H. Bernard, M.S."],
        ["D10", "Sahid, S.Pd., M.Pd."],
        ["D11", "Prof. Dr. Baso Intang Sappaile, M.Pd."],
        ["D12", "Dr. H. Djadir, M.Pd."],
        ["D13", "Drs. Muhammad Dinar, M.Pd."],
        ["D14", "Prof. Dr. Ruslan, M.Pd."],
        ["D15", "Prof. Dr. H. Suradi, M.S."],
        ["D16", "Prof. Dr. Syafruddin Side, S.Si., M.Si."],
        ["D17", "Dr. Muhammad Abdy, S.Si., M.Si."],
        ["D18", "Prof. Dr. Abdul Rahman, M.Pd."],
        ["D19", "Prof. Dr. H. Nurdin, M.Pd."],
        ["D20", "H. Sukarna, S.Pd., M.Si."],
        ["D21", "Sulaiman, S.Si., M.Kom, M.M."],
        ["D22", "Dr. Wahidah Sanusi, S.Si., M.Si."],
        ["D23", "Nasrullah, S.Pd., M.Pd."],
        ["D24", "Dr. Rosidah, M.Si."],
        ["D25", "Sabri, S.Pd., M.Sc., Ph.D."],
        ["D26", "Sutamrin, S.Si., M.Pd."],
        ["D27", "Dr. Awi, M.Si."],
        ["D28", "Dr. H. Rahmat Syam, S.T. M.Kom."],
        ["D29", "Ahmad Zaki, S.Si., M.Si."],
        ["D30", "Sahlan Sidjara, S.Si., M.Si."],
        ["D31", "Said Fachry Assagaf, S.Pd., M.Sc."],
        ["D32", "Fajar Arwadi, S.Pd., M.Sc."],
        ["D33", "Irwan, S.Si., M.Si."],
        ["D34", "Prof. Dr. Usman Mulbar, M.Pd."],
        ["D35", "Syahrullah Asyari, S.Pd., M.Pd."],
        ["D36", "Dr. Maya Sari Wahyuni, S.T, M.Kom"],
        ["D37", "Syamsuddin Mas'ud, S.Pd., M.Sc."],
        ["D38", "Nurwati Djam'an, S.Pd., M.Pd., Ph.D."],
        ["D39", "Muh. Husnul Khuluq, S.Pd., M.Sc."],
        ["D40", "Iwan Setiawan HR., S.Pd., M.Pd."],
        ["D41", "Fauziah Alimuddin, S.Pd., M.Pd."],
        ["D42", "Hartati, S.Si., M.Si., Ph.D."],
        ["D43", "Sulistiawati, S.Si.,M.Si.,M.T."],
        ["D44", "Drs. Muhammad Yunus, M.Si."],
        ["D45", "Rosmini Maru, S.Pd., M.Si.,Ph.D."],
        ["D46", "Dr. S. Salmiah Sari, M.Pd."],
        ["D47", "Vicran Zharvan, S.Si.,M.Si."],
        ["D48", "Suriati Eka Putri, S.Si., M.Si."],
        ["D49", "Diana Eka Pratiwi, S.Si., M.Si."],
        ["D50", "Dr. Andi Faridah, S.Si., M.Si."],
        ["D51", "Dr. Erman Syarif, S.Pd., M.Pd."],
        ["D52", "Iwan Dini, S.Si., M.Si."],
        ["D53", "Arifah Novia Arifin, S.Pd, M.Pd"],
        ["D54", "Musfirah, S.Pd.M.Pd."],
        ["D55", "dr. Irma Suryani Idris Arief, M.Kes"],
        ["D56", "Yusnaeni Yusuf, S.Si., M.Si"],
        ["D57", "Syamsunardi, S.Pd., M.Pd."],
        ["D58", "Dosen MKU"],
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
        courseA1_S1_1 = Course("A1_S1_1", "Bahasa Inggris Matematika", [self._instructors[0], self._instructors[35]], 25)
        courseA1_S1_2 = Course("A1_S1_2", "Landasan Matematika", [self._instructors[1], self._instructors[7]], 25)
        courseA1_S1_3 = Course("A1_S1_3", "Statistika Dasar", [self._instructors[24], self._instructors[29]], 25)
        courseA1_S1_4 = Course("A1_S1_4", "Kalkulus Diferensial", [self._instructors[2], self._instructors[31]], 25)
        courseA1_S1_5 = Course("A1_S1_5", "Aljabar Elementer", [self._instructors[3], self._instructors[40]], 25)
        courseA1_S1_6 = Course("A1_S1_6", "Biologi Dasar", [self._instructors[42]], 25)
        courseA1_S1_7 = Course("A1_S1_7", "Fisika Dasar", [self._instructors[43]], 25)
        courseA1_S1_8 = Course("A1_S1_8", "Kimia Dasar", [self._instructors[44], self._instructors[52]], 25)
        courseA1_S1_9 = Course("A1_S1_9", "Pendidikan Lingkungan Hidup", [self._instructors[45], self._instructors[9]], 25)
        # Course A1 Semester 3
        courseA1_S3_1 = Course("A1_S3_1", "Pengantar Pendidikan Matematika", [self._instructors[9], self._instructors[32]], 25)
        courseA1_S3_2 = Course("A1_S3_2", "Strategi Pembelajaran Matematika", [self._instructors[10], self._instructors[39]], 25)
        courseA1_S3_3 = Course("A1_S3_3", "Trigonometri", [self._instructors[6], self._instructors[31]], 25)
        courseA1_S3_4 = Course("A1_S3_4", "Matematika Sekolah Dasar dan Pembelajarannya", [self._instructors[18], self._instructors[40]], 25)
        courseA1_S3_5 = Course("A1_S3_5", "Geometri Analitik Datar", [self._instructors[12], self._instructors[13]], 25)
        courseA1_S3_6 = Course("A1_S3_6", "Filsafat Pendidikan Matematika", [self._instructors[2], self._instructors[35]], 25)
        courseA1_S3_7 = Course("A1_S3_7", "Teori Peluang", [self._instructors[24], self._instructors[33]], 25)
        courseA1_S3_8 = Course("A1_S3_8", "Aljabar Linear Lanjut", [self._instructors[5], self._instructors[41]], 25)
        courseA1_S3_9 = Course("A1_S3_9", "Pengantar Teori Fuzzy", [self._instructors[17], self._instructors[27]], 25)
        courseA1_S3_10 = Course("A1_S3_10", "Sejarah Matematika", [self._instructors[34], self._instructors[35]], 25)
        courseA1_S3_11 = Course("A1_S3_11", "Analisis Kompleks", [self._instructors[18], self._instructors[37]], 25)
        # Course A1 Semester 5
        courseA1_S5_1 = Course("A1_S5_1", "Pengantar Analisis Real", [self._instructors[8], self._instructors[30]], 25)
        courseA1_S5_2 = Course("A1_S5_2", "Struktur Aljabar", [self._instructors[15], self._instructors[5]], 25)
        courseA1_S5_3 = Course("A1_S5_3", "Statistika Terapan Pendidikan", [self._instructors[22], self._instructors[29]], 25)
        courseA1_S5_4 = Course("A1_S5_4", "Metodologi Penelitian Kuantitatif", [self._instructors[14], self._instructors[11]], 25)
        courseA1_S5_5 = Course("A1_S5_5", "Media Pembelajaran Manipulatif", [self._instructors[12], self._instructors[23]], 25)
        courseA1_S5_6 = Course("A1_S5_6", "Program Linear", [self._instructors[9], self._instructors[10]], 25)
        courseA1_S5_7 = Course("A1_S5_7", "Belajar dan Pembelajaran", [self._instructors[4], self._instructors[38]], 25)
        courseA1_S5_8 = Course("A1_S5_8", "Teori Graf", [self._instructors[19], self._instructors[37]], 25)
        courseA1_S5_9 = Course("A1_S5_9", "Masalah Syarat Batas", [self._instructors[7], self._instructors[37]], 25)

        # ===================================
        # Course A2 Semester 1 
        courseA2_S1_1 = Course("A2_S1_1", "Bahasa Inggris Matematika", [self._instructors[0], self._instructors[25]], 25)
        courseA2_S1_2 = Course("A2_S1_2", "Landasan Matematika", [self._instructors[1], self._instructors[7]], 25)
        courseA2_S1_3 = Course("A2_S1_3", "Statistika Dasar", [self._instructors[24], self._instructors[29]], 25)
        courseA2_S1_4 = Course("A2_S1_4", "Kalkulus Diferensial", [self._instructors[4], self._instructors[31]], 25)
        courseA2_S1_5 = Course("A2_S1_5", "Aljabar Elementer", [self._instructors[5], self._instructors[24]], 25)
        courseA2_S1_6 = Course("A2_S1_6", "Biologi Dasar", [self._instructors[53]], 25)
        courseA2_S1_7 = Course("A2_S1_7", "Fisika Dasar", [self._instructors[43]], 25)
        courseA2_S1_8 = Course("A2_S1_8", "Kimia Dasar", [self._instructors[44], self._instructors[52]], 25)
        courseA2_S1_9 = Course("A2_S1_9", "Pendidikan Lingkungan Hidup", [self._instructors[45], self._instructors[9]], 25)
        # Course A2 Semester 3
        courseA2_S3_1 = Course("A2_S3_1", "Pengantar Pendidikan Matematika", [self._instructors[9], self._instructors[32]], 25)
        courseA2_S3_2 = Course("A2_S3_2", "Strategi Pembelajaran Matematika", [self._instructors[15], self._instructors[35]], 25)
        courseA2_S3_3 = Course("A2_S3_3", "Trigonometri", [self._instructors[6], self._instructors[31]], 25)
        courseA2_S3_4 = Course("A2_S3_4", "Matematika Sekolah Dasar dan Pembelajarannya", [self._instructors[18], self._instructors[39]], 25)
        courseA2_S3_5 = Course("A2_S3_5", "Geometri Analitik Datar", [self._instructors[13]], 25)
        courseA2_S3_6 = Course("A2_S3_6", "Filsafat Pendidikan Matematika", [self._instructors[2], self._instructors[35]], 25)
        courseA2_S3_7 = Course("A2_S3_7", "Teori Peluang", [self._instructors[22], self._instructors[20]], 25)
        courseA2_S3_8 = Course("A2_S3_8", "Aljabar Linear Lanjut", [self._instructors[23], self._instructors[41]], 25)
        courseA2_S3_9 = Course("A2_S3_9", "Pengantar Teori Fuzzy", [self._instructors[27], self._instructors[17]], 25)
        courseA2_S3_10 = Course("A2_S3_10", "Sejarah Matematika", [self._instructors[34], self._instructors[35]], 25)
        courseA2_S3_11 = Course("A2_S3_11", "Analisis Kompleks", [self._instructors[18], self._instructors[37]], 25)
        # Course A2 Semester 5
        courseA2_S5_1 = Course("A2_S5_1", "Pengantar Analisis Real", [self._instructors[2], self._instructors[1]], 25)
        courseA2_S5_2 = Course("A2_S5_2", "Struktur Aljabar", [self._instructors[15], self._instructors[30]], 25)
        courseA2_S5_3 = Course("A2_S5_3", "Statistika Terapan Pendidikan", [self._instructors[8], self._instructors[29]], 25)
        courseA2_S5_4 = Course("A2_S5_4", "Metodologi Penelitian Kuantitatif", [self._instructors[14], self._instructors[11]], 25)
        courseA2_S5_5 = Course("A2_S5_5", "Media Pembelajaran Manipulatif", [self._instructors[12], self._instructors[10]], 25)
        courseA2_S5_6 = Course("A2_S5_6", "Program Linear", [self._instructors[14], self._instructors[10]], 25)
        courseA2_S5_7 = Course("A2_S5_7", "Belajar dan Pembelajaran", [self._instructors[4], self._instructors[38]], 25)
        courseA2_S5_8 = Course("A2_S5_8", "Teori Graf", [self._instructors[19], self._instructors[40]], 25)
        courseA2_S5_9 = Course("A2_S5_9", "Pemodelan Matematika", [self._instructors[16]], 25)
        courseA2_S5_10 = Course("A2_S5_10", "Masalah Syarat Batas", [self._instructors[7], self._instructors[37]], 25)

        # ===================================
        # Course C Semester 1 
        courseC_S1_1 = Course("C_S1_1", "English for Mathematics", [self._instructors[0], self._instructors[25]], 25)
        courseC_S1_2 = Course("C_S1_2", " Fundamentals of Mathematics", [self._instructors[7], self._instructors[39]], 25)
        courseC_S1_3 = Course("C_S1_3", "Elementary Statistics", [self._instructors[8], self._instructors[29]], 25)
        courseC_S1_4 = Course("C_S1_4", "Differensial Calculus", [self._instructors[1], self._instructors[25]], 25)
        courseC_S1_5 = Course("C_S1_5", "Elementary Algebra", [self._instructors[5], self._instructors[41]], 25)
        courseC_S1_6 = Course("C_S1_6", "Biology", [self._instructors[55], self._instructors[56]], 25)
        courseC_S1_7 = Course("C_S1_7", "Physics", [self._instructors[43]], 25)
        courseC_S1_8 = Course("C_S1_8", "Chemistry", [self._instructors[48], self._instructors[49]], 25)
        courseC_S1_9 = Course("C_S1_9", "Environmental Education", [self._instructors[13], self._instructors[57]], 25)
        # Course C Semester 3
        courseC_S3_1 = Course("C_S3_1", "Introduction to Mathematics Education", [self._instructors[23], self._instructors[32]], 25)
        courseC_S3_2 = Course("C_S3_2", "Mathematics Learning Strategy", [self._instructors[19], self._instructors[39]], 25)
        courseC_S3_3 = Course("C_S3_4", "Trigonometry", [self._instructors[6], self._instructors[25]], 25)
        courseC_S3_4 = Course("C_S3_5", "Primary School Mathematics and Learning", [self._instructors[18], self._instructors[38]], 25)
        courseC_S3_5 = Course("C_S3_6", " Plane Analytical Geometry", [self._instructors[13], self._instructors[32]], 25)
        courseC_S3_6 = Course("C_S3_7", "Philosopy of Mathematics Education", [self._instructors[0], self._instructors[35]], 25)
        courseC_S3_7 = Course("C_S3_8", "Probability Theory", [self._instructors[20], self._instructors[33]], 25)
        courseC_S3_8 = Course("C_S3_9", "Intermediate Linear Algebra", [self._instructors[5], self._instructors[23]], 25)
        courseC_S3_9 = Course("C_S3_10", "Introduction to Fuzzy Theory", [self._instructors[19], self._instructors[17]], 25)
        courseC_S3_10 = Course("C_S3_11", "The History of Mathematics", [self._instructors[34], self._instructors[39]], 25)
        # Course C Semester 5
        courseC_S5_1 = Course("C_S5_1", "Introduction to Real Analysis", [self._instructors[2], self._instructors[30]], 25)
        courseC_S5_2 = Course("C_S5_2", "Introduction to Modern Algebra", [self._instructors[4], self._instructors[38]], 25)
        courseC_S5_3 = Course("C_S5_3", "Applied Statistics in Education", [self._instructors[11], self._instructors[33]], 25)
        courseC_S5_4 = Course("C_S5_4", "Quantitative Research Methodology in Education", [self._instructors[11], self._instructors[31]], 25)
        courseC_S5_5 = Course("C_S5_5", "Manipulative Learning Media", [self._instructors[12], self._instructors[3]], 25)
        courseC_S5_6 = Course("C_S5_6", "Linear Programming", [self._instructors[14], self._instructors[10]], 25)
        courseC_S5_7 = Course("C_S5_7", "Teaching and Learning", [self._instructors[4], self._instructors[38]], 25)
        courseC_S5_8 = Course("C_S5_8", "Graph Theory", [self._instructors[19], self._instructors[37]], 25)
        courseC_S5_9 = Course("C_S5_9", "Mathematical Modeling", [self._instructors[16]], 25)
        courseC_S5_10 = Course("C_S5_10", "Boundary Value Problem", [self._instructors[7], self._instructors[37]], 25)

        # ===================================
        # Course B Semester 1 
        courseB_S1_1 = Course("B_S1_1", "Kalkulus Diferensial", [self._instructors[25], self._instructors[35]], 25)
        courseB_S1_2 = Course("B_S1_2", "Fisika Dasar", [self._instructors[46], self._instructors[47]],35)
        courseB_S1_3 = Course("B_S1_3", "Kimia Dasar", [self._instructors[48], self._instructors[49]], 25)
        courseB_S1_4 = Course("B_S1_4", "Biologi Dasar", [self._instructors[50]], 30)
        courseB_S1_5 = Course("B_S1_5", "Pendidikan Lingkungan Hidup", [self._instructors[13], self._instructors[51]], 35)
        courseB_S1_6 = Course("B_S1_6", "Pendidikan Agama Islam", [self._instructors[52]], 45)
        courseB_S1_7 = Course("B_S1_7", "Statistika Dasar", [self._instructors[20], self._instructors[33]], 30)
        courseB_S1_8 = Course("B_S1_8", "Landasan Matematika", [self._instructors[3], self._instructors[32]], 35)
        courseB_S1_9 = Course("B_S1_9", "Aljabar Elementer", [self._instructors[3], self._instructors[30]], 45)
        # Course B Semester 3
        courseB_S3_1 = Course("B_S3_1", "Kalkulus Peubah Banyak", [self._instructors[3], self._instructors[32]], 35)
        courseB_S3_2 = Course("B_S3_2", "Aljabar Linear Lanjut", [self._instructors[6], self._instructors[9]], 35)
        courseB_S3_3 = Course("B_S3_3", "Teori Peluang", [self._instructors[22]], 30)
        courseB_S3_4 = Course("B_S3_4", "Geometri Analitik Datar", [self._instructors[2], self._instructors[23]], 30)
        courseB_S3_5 = Course("B_S3_5", "Teori Bilangan", [self._instructors[34], self._instructors[33]], 30)
        courseB_S3_6 = Course("B_S3_6", "Trigonometri", [self._instructors[12], self._instructors[40]], 25)
        courseB_S3_7 = Course("B_S3_7","Matematika Keuangan", [self._instructors[8], self._instructors[29]], 40)
        courseB_S3_8 = Course("B_S3_8","Simulasi Komputer", [self._instructors[36]], 40)
        courseB_S3_9 = Course("B_S3_9","Statistika Pengendalian Mutu", [self._instructors[24], self._instructors[33]], 40)
        # Course B Semester 5
        courseB_S5_1 = Course("B_S5_1","Program Linear", [self._instructors[20], self._instructors[26]], 40)
        courseB_S5_2 = Course("B_S5_2","Analisis Real II", [self._instructors[1], self._instructors[37]], 40)
        courseB_S5_3 = Course("B_S5_3","Struktur Aljabar II", [self._instructors[15], self._instructors[30]], 40)
        courseB_S5_4 = Course("B_S5_4","Metodologi Penelitian", [self._instructors[8], self._instructors[17]], 40)
        courseB_S5_5 = Course("B_S5_5","Pemodelan Matematika", [self._instructors[16]], 40)
        courseB_S5_6 = Course("B_S5_6","Kapita Selekta", [self._instructors[16], self._instructors[22], self._instructors[20], self._instructors[28]], 40)
        courseB_S5_7 = Course("B_S5_7","Matematika Aktuaria", [self._instructors[8], self._instructors[21]], 40)
        courseB_S5_8 = Course("B_S5_8","Statistika Multivariat", [self._instructors[22], self._instructors[33]], 40)
        courseB_S5_9 = Course("B_S5_9","Sistem Dinamik", [self._instructors[16]], 40)
        courseB_S5_10 = Course("B_S5_10","Teori Modul", [self._instructors[17], self._instructors[30]], 40)
        self._courses = [
            courseA1_S1_1, courseA1_S1_2, courseA1_S1_3, courseA1_S1_4, courseA1_S1_5, courseA1_S1_6, courseA1_S1_7, courseA1_S1_8, courseA1_S1_9,
            courseA1_S3_1, courseA1_S3_2, courseA1_S3_3, courseA1_S3_4, courseA1_S3_5, courseA1_S3_6, courseA1_S3_7, courseA1_S3_8, courseA1_S3_9, courseA1_S3_10, courseA1_S3_11,
            courseA1_S5_1, courseA1_S5_2, courseA1_S5_3, courseA1_S5_4, courseA1_S5_5, courseA1_S5_6, courseA1_S5_7, courseA1_S5_8, courseA1_S5_9,
            courseA2_S1_1, courseA2_S1_2, courseA2_S1_3, courseA2_S1_4, courseA2_S1_5, courseA2_S1_6, courseA2_S1_7, courseA2_S1_8, courseA2_S1_9,
            courseA2_S3_1, courseA2_S3_2, courseA2_S3_3, courseA2_S3_4, courseA2_S3_5, courseA2_S3_6, courseA2_S3_7, courseA2_S3_8, courseA2_S3_9, courseA2_S3_10, courseA2_S3_11,
            courseA2_S5_1, courseA2_S5_2, courseA2_S5_3, courseA2_S5_4, courseA2_S5_5, courseA2_S5_6, courseA2_S5_7, courseA2_S5_8, courseA2_S5_9, courseA2_S5_10,
            courseC_S1_1, courseC_S1_2, courseC_S1_3, courseC_S1_4, courseC_S1_5, courseC_S1_6, courseC_S1_7, courseC_S1_8, courseC_S1_9,
            courseC_S3_1, courseC_S3_2, courseC_S3_3, courseC_S3_4, courseC_S3_5, courseC_S3_6, courseC_S3_7, courseC_S3_8, courseC_S3_9, courseC_S3_10,
            courseC_S5_1, courseC_S5_2, courseC_S5_3, courseC_S5_4, courseC_S5_5, courseC_S5_6, courseC_S5_7, courseC_S5_8, courseC_S5_9, courseC_S5_10,
            courseB_S1_1, courseB_S1_2, courseB_S1_3, courseB_S1_4, courseB_S1_5, courseB_S1_6, courseB_S1_7, courseB_S1_8, courseB_S1_9,
            courseB_S3_1, courseB_S3_2, courseB_S3_3, courseB_S3_4, courseB_S3_5, courseB_S3_6, courseB_S3_7, courseB_S3_8, courseB_S3_9,
            courseB_S5_1, courseB_S5_2, courseB_S5_3, courseB_S5_4, courseB_S5_5, courseB_S5_6, courseB_S5_7, courseB_S5_8, courseB_S5_9, courseB_S5_10,
        ]

        A1_S1 = Department("A1 S1", [courseA1_S1_1, courseA1_S1_2, courseA1_S1_3, courseA1_S1_4, courseA1_S1_5, courseA1_S1_6, courseA1_S1_7, courseA1_S1_8, courseA1_S1_9])
        A1_S3 = Department("A1 S3", [courseA1_S3_1, courseA1_S3_2, courseA1_S3_3, courseA1_S3_4, courseA1_S3_5, courseA1_S3_6, courseA1_S3_7, courseA1_S3_8, courseA1_S3_9, courseA1_S3_10, courseA1_S3_11])
        A1_S5 = Department("A1 S5", [courseA1_S5_1, courseA1_S5_2, courseA1_S5_3, courseA1_S5_4, courseA1_S5_5, courseA1_S5_6, courseA1_S5_7, courseA1_S5_8, courseA1_S5_9])
        A2_S1 = Department("A2 S1", [courseA2_S1_1, courseA2_S1_2, courseA2_S1_3, courseA2_S1_4, courseA2_S1_5, courseA2_S1_6, courseA2_S1_7, courseA2_S1_8, courseA2_S1_9])
        A2_S3 = Department("A2 S3", [courseA2_S3_1, courseA2_S3_2, courseA2_S3_3, courseA2_S3_4, courseA2_S3_5, courseA2_S3_6, courseA2_S3_7, courseA2_S3_8, courseA2_S3_9, courseA2_S3_10, courseA2_S3_11])
        A2_S5 = Department("A2 S5", [courseA2_S5_1, courseA2_S5_2, courseA2_S5_3, courseA2_S5_4, courseA2_S5_5, courseA2_S5_6, courseA2_S5_7, courseA2_S5_8, courseA2_S5_9, courseA2_S5_10])
        C_S1 = Department("C S1", [courseC_S1_1, courseC_S1_2, courseC_S1_3, courseC_S1_4, courseC_S1_5, courseC_S1_6, courseC_S1_7, courseC_S1_8, courseC_S1_9])
        C_S3 = Department("C S3", [courseC_S3_1, courseC_S3_2, courseC_S3_3, courseC_S3_4, courseC_S3_5, courseC_S3_6, courseC_S3_7, courseC_S3_8, courseC_S3_9, courseC_S3_10])
        C_S5 = Department("C S5", [courseC_S5_1, courseC_S5_2, courseC_S5_3, courseC_S5_4, courseC_S5_5, courseC_S5_6, courseC_S5_7, courseC_S5_8, courseC_S5_9, courseC_S5_10])
        B_S1 = Department("B S1", [courseB_S1_1, courseB_S1_2, courseB_S1_3, courseB_S1_4, courseB_S1_5, courseB_S1_6, courseB_S1_7, courseB_S1_8, courseB_S1_9])
        B_S3 = Department("B S3", [courseB_S3_1, courseB_S3_2, courseB_S3_3, courseB_S3_4, courseB_S3_5, courseB_S3_6, courseB_S3_7, courseB_S3_8, courseB_S3_9])
        B_S5 = Department("B S5", [courseB_S5_1, courseB_S5_2, courseB_S5_3, courseB_S5_4, courseB_S5_5, courseB_S5_6, courseB_S5_7, courseB_S5_8, courseB_S5_9, courseB_S5_10])
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
                "Class #",
                "Dept",
                "Course",
                "Room",
                "Instuctors",
                "Meeting Time",
                "Meeting Day",
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