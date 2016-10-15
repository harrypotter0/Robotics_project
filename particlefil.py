from math import*
import random

landmarks  = [[20.0, 20.0], [80.0, 80.0], [20.0, 80.0], [80.0, 20.0]] 
world_size = 100.0

class robot:

	# --------

	# init: 
	#	creates robot and initializes location/orientation 
	#

	def __init__(self):
		self.x = random.random() * world_size # initial x position
		self.y = random.random() * world_size # initial y position
		self.orientation = random.random() * 2.0 * pi # initial orientation
		self.forward_noise  = 0.0
		self.turn_noise = 0.0 
		self.sense_noise = 0.0 
	def __repr__(self):
		return '[x=%.6s y=%.6s orient=%.6s]' % (str(self.x), str(self.y), str(self.orientation))
	# --------
	# set: 
	#	sets a robot coordinate
	#

	def set(self, new_x, new_y, new_orientation):

		if new_orientation < 0 or new_orientation >= 2 * pi:
			raise ValueError, 'Orientation must be in [0..2pi]'
		self.x = float(new_x)
		self.y = float(new_y)
		self.orientation = float(new_orientation)


	# --------
	# set_noise: 
	#	sets the noise parameters
	#

	def set_noise(self, new_f_noise, new_t_noise, new_s_noise):
	
		# makes it possible to change the noise parameters
		self.forward_noise  = float(new_f_noise)
		self.turn_noise = float(new_t_noise)
		self.sense_noise = float(new_s_noise)

	# --------
	# move:
	#   move along a section of a circular path according to motion
	#

	def move(self,turn,forward): 
		
		orientation=self.orientation+float(turn)+random.gauss(0.0,self.turn_noise)
		orientation%=2*pi
		
		dist=float(forward)+random.gauss(0.0,self.forward_noise)
		x=self.x+cos(orientation)*dist
		y=self.y+sin(orientation)*dist
		x%=world_size
		y%=world_size
		
	# set particle
		res=robot()
		res.set(x,y,orientation)
		res.set_noise(self.forward_noise,self.turn_noise,self.sense_noise)
		return res
	
	def sense(self):
		
		Z=[]
		for i in range(len(landmarks)):
			dist=sqrt((self.x-landmarks[i][0])**2+(self.y-landmarks[i][1])**2)
			dist+=random.gauss(0.0,self.sense_noise)
			Z.append(dist)
		return Z
	
	def Gaussian(self,mu,sigma,x):
	
 		return (1/sqrt(2*pi*sigma**2))*exp(-1/2.0*(x-mu)**2/sigma**2)
 		
	def measurement_prob(self,measurement):
	
	#determine how likely a measurement should be
		prob=1.0
		for i in range(len(landmarks)):
			dist=sqrt((self.x-landmarks[i][0])**2+(self.y-landmarks[i][1])**2)
			prob*=self.Gaussian(dist,self.sense_noise,measurement[i])
		return prob

def eval(r,p): #determine the error
 	sum=0.0
 	for i in range(len(p)):
		dx=min(abs(r.x-p[i].x),(world_size-max(r.x,p[i].x)+min(r.x,p[i].x)))
		dy=min(abs(r.y-p[i].y),(world_size-max(r.y,p[i].y)+min(r.y,p[i].y)))
		err=sqrt(dx*dx+dy*dy)
		sum+=err
	sum/=(len(p))
	return sum
	
def func():
 
 	myrobot=robot()
 	
 	#Initial particles
 	
 	N=1000
 	T=100
 	p=[]
	for i in range(N):
 		x=robot()
 		x.set_noise(0.05,0.05,5.0)
 		p.append(x)
 	
 	print eval(myrobot,p)
 	# Particle filtering after T steps : Both position and orientation matter
 	for t in range(T):
 		
 		myrobot=myrobot.move(0.1,5.0)
 		Z=myrobot.sense()
 	
 		p2=[]
 		for i in range(N):
 			x=p[i].move(0.1,5.0)
 			p2.append(x)
 	
 		p=p2
 	
 		w=[]
 		for i in range(N):
 			w.append(p[i].measurement_prob(Z))
 	
 	# Normalisation of intensity weights
 		su=sum(w)
 		for i in range(N):
 			w[i]/=su
 	
 	# Resampling of particles : choosing particle for next state	
 		p3=[]
 		index=int(random.random()*N)
 		beta=0.0
 		mw=max(w)
 		for i in range(N):
 			beta+=(random.random()*2*mw)
 			while w[index]<beta :
 				beta-=w[index]
 				index=(index+1)%N
 			p3.append(p[index])
 		p=p3
 		
 		print eval(myrobot,p)
 		
 
func()
