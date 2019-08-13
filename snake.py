import pygame, random, time
DIMENSION = 100
pygame.init()
screen = pygame.display.set_mode((DIMENSION, DIMENSION))
clock = pygame.time.Clock()
direction = 0 # initial direction is 'right'
X = []
Y = []
done = False
rand = 0


class Apple:
    x = 0
    y = 0

    def __init__(self):
        self.x = random.randint(1,10) * 10
        self.y = random.randint(1,10) * 10
    
    def regenerate(self):
        rand = random.randint(1,10) * 10
        self.x = rand
        self.y = rand

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Player:
    length = 5
    def __init__(self, clock):
            for i in range(0,self.length):
                X.append(0)
                Y.append(i * 10)

            #for l in range(self.length):
            #    snake = pygame.Rect(X[l]%DIMENSION, Y[l]%DIMENSION, 10, 10 )
            #    pygame.draw.rect(screen, (255, 0, 0), snake)
                #pygame.display.flip()
                #clock.tick(60)
                #time.sleep(1)

    def getLength(self):
        return self.length

    def increaseLength(self):
        self.length += 1

    def update(self, direction, enlarge):
        for i in range(self.length-2):
            # collision check
            if(X[-1]%DIMENSION == X[i]%DIMENSION and Y[-1]%DIMENSION == Y[i]%DIMENSION):
                exit()
        if(direction == 0):
            if(enlarge == False):
                X.pop(0)
                Y.pop(0)
            X.append(X[-1]+10)
            Y.append(Y[-1])  
        if(direction == 1): 
            if(enlarge == False):
                X.pop(0)
                Y.pop(0)
            X.append(X[-1])
            Y.append(Y[-1]+10)  
        if(direction == 2): #works LEFT
            if(enlarge == False):
                X.pop(0)
                Y.pop(0)
            X.append(X[-1]-10)
            Y.append(Y[-1])  
        if(direction == 3):
            if(enlarge == False):
                X.pop(0)
                Y.pop(0)
            X.append(X[-1])
            Y.append(Y[-1]-10)  


p = Player(clock)
ap = Apple()

while not done:
    screen.fill((0, 0, 0))
    p.update(direction, False)

    print(p.getLength())
    for l in range(p.getLength()):
        snake = pygame.Rect(X[l]%DIMENSION, Y[l]%DIMENSION, 10, 10 )
        pygame.draw.rect(screen, (255, 0, 0), snake)
    
    if(ap.getX()%DIMENSION == X[-1]%DIMENSION and ap.getY()%DIMENSION == Y[-1]%DIMENSION):
        ap.regenerate()
        p.increaseLength()
        p.update(direction, True)

    apple = pygame.Rect(ap.getX()%DIMENSION, ap.getY()%DIMENSION, 10, 10)
    print("apple: " + str(ap.getX()), str(ap.getY()))
    print("dot: " + str(X[-1]%DIMENSION) +" " + str(Y[-1]%DIMENSION))
    pygame.draw.rect(screen, (0, 255, 0), apple)


    pygame.display.flip() # updates the screen
    clock.tick(60)
    time.sleep(0.5 - (p.getLength() * 0.02))

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            done = True
            exit()
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
                direction = 3              
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
                direction = 1             
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                direction = 0                                         
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                direction = 2             
