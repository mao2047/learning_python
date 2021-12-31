class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point(10, 20)
print(point1.x, point1.y)

#point1.x = 10
#point1.y = 20

#print(point1.x)
#point1.draw()

'''
This is a totally different object
and has its own atributes.
'''

#point2 = Point()
#point2.x = (1)
#print(point2.x)
