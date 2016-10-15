measurement=['r','r']
motion=[1,1]

def sense(p,n,z):
	phit=0.8
	pmiss=0.2
	world=['g','r','r','g','g']
	for i in range(n):
		if(world[i]==z):
			p[i]=p[i]*phit
		else:
		    p[i]=p[i]*pmiss
	s=sum(p)
    	for i in range(n):
    		p[i]/=s
	return p
	
def move(p,u):
    q = []
    pexact=0.8
    punder=0.1
    pover=0.1
    for i in range(len(p)):
    	s=pexact*p[(i-u)%len(p)]
    	s=s+punder*p[(i-u+1)%len(p)]
    	s=s+pover*p[(i-u-1)%len(p)]
    	q.append(s)	
		
    return q
	
def func():
	p=[]
	n = input()
	for i in range(n):
		p.append(1.0/n)
		
	print(p)
	for i in range(len(measurement)):
    		p=sense(p,n,measurement[i])
    		print p
    		p=move(p,motion[i])
    		print p
    	#print p;
  
	#return p 

func()
