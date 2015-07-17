import pygame , random , sys , math

pygame.init()
width , height = 1000 , 500
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()



def randColor():
	return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def randPos():
	x = random.randint(0,width)
	y = random.randint(0, height)
	return x , y
def randVector():
	x = random.random()*2-1
	y = random.random()*2-1
	return (x , y)	

def collide(circle1,circle2):
	if math.sqrt((circle1.x-circle2.x)**2+(circle1.y-circle2.y)**2) <= circle1.radius+circle2.radius:
		collision = True
	else:
		collision = False
	return collision

def ColorAddition(circle1,circle2):
	color_r = (circle1.color[0] + circle2.color[0])/2
	color_g = (circle1.color[1] + circle2.color[1])/2
	color_b = (circle1.color[2] + circle2.color[2])/2
	return (color_r , color_g , color_b)

class Collider():
	def __init__(self):
		self.x , self.y = randPos()
		self.radius = random.randint(5,30)
		self.vector = randVector()
		self.color = randColor()
	def move(self):
		self.x += self.vector[0]
		self.y += self.vector[1]
	def newVector(self):
		self.vector = randVector()



colliders = []
try:
	for c in range(int(sys.argv[1])):
		x = Collider()
		colliders.append(x)
except:
	for c in range(1000):
		x = Collider()
		colliders.append(x)

background_color = randColor()
screen.fill(background_color)
count = 0
while True:
	count += 1
	#move all colliders
	for c in colliders:
		c.move()
	#generate new vector

	for c in colliders:
		ran = random.randint(1,1000)
		if ran == 100:
			c.newVector()
	#check for collisions and render lines if collision
	for c1 in colliders:
		for c2 in colliders:
			if collide(c1,c2):
				pygame.draw.aaline(screen , ColorAddition(c1,c2) , (c1.x,c1.y),(c2.x,c2.y))
					
	clock.tick()
	pygame.display.flip()

