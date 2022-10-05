class Animals():
    def __init__(self,weight,height,age, sex,speed,jump):
        self.weight = weight
        self.height = height
        self.age = age
        self.sex = sex
        self.speed = speed
        self.jump = jump
    def walk(self):
        print('Скорость ходьбы животного', self.speed)
Rabbit = Animals (weight=80, height = 213, sex='male', age=9, speed = 2, jump = 1)
print(Rabbit.age)
print(Rabbit.jump)
Rabbit.walk()
