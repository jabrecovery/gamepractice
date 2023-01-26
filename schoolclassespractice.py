class School:
    def __init__(self, name, level, numOfStudents):
        self.name = name
        self.level = level
        self.numOfStudents = numOfStudents
    def getName(self):
        return self.name
    def getLevel(self):
        return self.level
    def getNumStudents(self):
        return self.numOfStudents
    def setNumberOfStudents(self, new_numOfStudents):
        self.numOfStudents = new_numOfStudents

    def __repr__(self):
        return 'A {level} school named {name} with {numOfStudents} students.'.format(level=self.level, name=self.name, numOfStudents=self.numOfStudents)


a = School('Codecademy', 'high', 100)
print(a)
print(a.getName())
print(a.getLevel())
a.setNumberOfStudents(150)
print(a.numOfStudents)


class Primary(School):
    def __init__(self, name, numOfStudents, pickupPolicy):
        self.name = name
        self.numOfStudents = numOfStudents
        self.pickupPolicy = pickupPolicy
        super().__init__(name, 'primary', numOfStudents)

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + ' The pickup policy is {pickupPolicy}'.format(pickupPolicy = self.pickupPolicy)
        
b = Primary('CodeElem', 100, 'Pick up allowed after 3PM')
print(b)



class Middle:
    pass


class High:
    pass