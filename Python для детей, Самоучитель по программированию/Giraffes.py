class Things:
    pass

class Animate(Things):
    pass

class Animals(Animate):
    def breathe(self):
        print('дышит')
    def move(self):
        print('двигается')
    def eat_food(self):
        print('ест')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('кормит деденышей молоком')

class Giraffes(Mammals):
    def __init__(self, spots):
        self.giraffe_spots = spots
    def find_food(self):
        self.move()
        print('Я нашел еду')
        self.eat_food()
    def eat_leaves_from_threes(self):
        self.eat_food()
    def dance_a_jig(self):
        for i in range (4):
            self.move()
    def left_foot_forward(self):
        print('Левая нога вперед')
    def left_food_back(self):
        print('Левая нога назад')
    def right_foot_forward(self):
        print('Правая нога вперед')
    def right_foot_back(self):
        print('Правая нога назад')
    def dance(self):
        self.left_foot_forward()
        self.left_food_back()
        self.right_food_forward()
        self.right_food_back()
        self.left_food_back()
        self.right_food_back()
        self.right_food_forward()
        self.left_foot_forward()
