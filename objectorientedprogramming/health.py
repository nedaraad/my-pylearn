
""" Checking the height, weight and age of students in two classes (A and B) of two schools. """

class school():
    
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight

    # Calculating the average age of students    
    def age_average(self, age):
        age_avg = sum(age) / len(age)
        return age_avg
     
    # Calculating the average height of students   
    def height_average(self, height):
        height_avg = sum(height) / len(height)
        return height_avg

    # Calculating the average weight of students    
    def weight_average(self, weight):
        weight_avg = sum(weight) / len(weight)
        return weight_avg

# Prints a class with an average height
def max_average():
    if A.height_average(heightA) > B.height_average(heightB):
        print('A')
    elif A.height_average(heightA) == B.height_average(heightB):
        Aw = A.weight_average(weightA)
        Bw = B.weight_average(weightB)
        if Aw < Bw :
            print('A')
        if Aw > Bw :
            print('B')
        if Aw == Bw :
            print('Same')
    elif A.height_average(heightA) < B.height_average(heightB):
        print('B')

numA = int(input("enter the number of students:"))
ageA = list(map(int,input("enter the age of the students: ").split()))
heightA = list(map(int,input("enter the height of the students:").split()))
weightA = list(map(int,input("enter the weight of the students:").split()))

numB = int(input("enter the number of students:"))
ageB = list(map(int,input("enter the age of the students: ").split()))
heightB = list(map(int,input("enter the height of the students:").split()))
weightB = list(map(int,input("enter the weight of the students:").split()))

A = school(ageA, heightA, weightA)
B = school(ageB, heightB, weightB)

print(float(A.age_average(ageA)))
print(float(A.height_average(heightA)))
print(float(A.weight_average(weightA)))

print(float(B.age_average(ageB)))
print(float(B.height_average(heightB)))
print(float(B.weight_average(weightB)))
max_average()