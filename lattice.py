import turtle
import math
import random

def dist(x1, y1, x2, y2, x3, y3): # x3,y3 is the point
    px = x2-x1
    py = y2-y1

    norm = px*px + py*py

    u =  ((x3 - x1) * px + (y3 - y1) * py) / float(norm)

    if u > 1:
        u = 1
    elif u < 0:
        u = 0

    x = x1 + u * px
    y = y1 + u * py

    dx = x - x3
    dy = y - y3

    # Note: If the actual distance does not matter,
    # if you only want to compare what this function
    # returns to other results of this function, you
    # can just return the squared distance instead
    # (i.e. remove the sqrt) to gain a little performance

    dist = (dx*dx + dy*dy)**.5

    return dist

def slope(x1, y1, x2, y2):
    changeX = x2-x1
    changeY = y2-y1
    ratio = changeY/changeX
    return float(ratio)

class Triangle: 

    def __init__(self, x1, y1, x2, y2, x3, y3):
        
        #probability
        self.pointsThatWork = 0
        self.totalPoints = 0

        #needed for distance() function - slope
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        #most important end result
        self.finalList = list() 

        assign = dict()
        assign[x1]=y1
        assign[x2]=y2
        assign[x3]=y3

        compareX = [x1, x2, x3]
        a = sorted(compareX)
        minX = a[0]
        min2X = a[1]
        maxX = a[2]
        print(a)

        self.t = turtle.Turtle()
        self.t.up()
        self.t.goto(minX, assign[minX])
        self.t.down()
        self.t.dot()

        grid = list()

        grid.append(self.draw(assign, minX, maxX))

        self.t.up()
        self.t.goto(min2X, assign[min2X])
        self.t.down()
        self.t.dot()

        grid.append(self.draw(assign, min2X, maxX))

        self.t.up()
        self.t.goto(minX, assign[minX])
        #don't have to make dot again - repetetive

        self.draw(assign, minX, min2X)

        self.t.up()
        self.t.goto(min2X, assign[min2X])
        #don't have to make dot again - repetetive

        if(len(grid[0])<len(grid[1])):
            for points in range(0, len(grid[0])):
                self.latticeGrid(grid[0][points], grid[1][points])
        else:
            for points in range(0, len(grid[1])):
                self.latticeGrid(grid[1][points], grid[0][points])

    def draw(self, assign, minX, maxX):
        createGrid = list()
        x = minX
        y = assign[minX]
        while(x < maxX):
            x += 0.5
            y += slope(minX, assign[minX], maxX, assign[maxX])/2
            self.t.up()
            self.t.goto(x,y)
            self.t.down()
            self.t.dot()
            tupp = (x,y)
            createGrid.append(tupp)
        return createGrid
            
        print("draw")

    def latticeGrid(self, tup1, tup2):
        if(tup1[0]<tup2[0]):
           rate = 4
        else:
            rate = -4
        x = tup1[0]
        y = tup1[1]
        self.t.up()
        self.t.goto(x,y)
        if(rate>0):
            while(x+rate < tup2[0]):
                x += rate
                y += slope(tup1[0], tup1[1], tup2[0], tup2[1])*rate
                self.lattice(rate, x, y, tup1, tup2)
        else:
            while(x+rate > tup2[0]):
                x += rate
                y += slope(tup1[0], tup1[1], tup2[0], tup2[1])*rate
                self.lattice(rate, x, y, tup1, tup2)

    def lattice(self, rate, x, y, tup1, tup2):
        self.t.up()
        self.t.goto(x,y)
        self.t.down()
        self.t.color("blue")
        self.t.dot()
        tupp = (x,y)
        self.finalList.append(tupp)

    #argument class: triange
    def randomPoint(self, count):
        #Find a random point - pinpoit red on triangle
        print(len(self.finalList))
        for i in range(0, count):
            r = random.randrange(len(self.finalList))
            self.t.up()
            self.t.goto(self.finalList[r][0], self.finalList[r][1])
            self.t.down()
            self.t.color("red")
            self.t.dot()
            self.distance(self.finalList[r][0], self.finalList[r][1])
        print(r)
        print("This finds a random point in the inside of the triangle & red dot")

    def distance(self, pointX, pointY):
        distance1 = dist(self.x1, self.y1, self.x2, self.y2, pointX, pointY)
        distance2 = dist(self.x2, self.y2, self.x3, self.y3, pointX, pointY)
        distance3 = dist(self.x1, self.y1, self.x3, self.y3, pointX, pointY)
        self.inequality(distance1, distance2, distance3)
        #This finds perpendicular distance from each side - appends to list 
        print("Finds perpendicular distance given random point in triangle")

    def inequality(self, a, b, c):
        sides = [a, b, c]
        l = sorted(sides)
        if(l[0]+l[1] > l[2]):
            self.t.down()
            self.t.color("green")
            self.t.dot()
            self.pointsThatWork += 1
            self.totalPoints += 1
        else:
            self.totalPoints += 1
            print("Does not make a triangle")

        #uses distanceFunction
        #sees if this satisfys the triangle inequality 
        #draws a possible triangle that can be formed

    def plot(self):
        #plots all poins that you've found to satisfy triangle inequality - graph
        print("Ooh... visualization")

    def probability(self):
        #all points that satisfied/all points that worked + satisfied
        print(str(float(self.pointsThatWork / self.totalPoints) * 100.0) + "%")

t = Triangle(0, 0, 100, 0, 50, 87)
t.randomPoint(100)
t.probability()
turtle.mainloop()



