from math import*
import random

# Motion Planning Technique

def search(grid,init,goal):
		
	# open list items are of type [g,x,y]
	
	closed=[[0 for x in range(len(grid[0]))] for y in range(len(grid))]
	expand=[[-1 for x in range(len(grid[0]))] for y in range(len(grid))]
	policy=[[' ' for x in range(len(grid[0]))] for y in range(len(grid))]
	action=[[-1 for x in range(len(grid[0]))] for y in range(len(grid))]
	
	closed[init[0]][init[1]]=1
	g=0
	x=init[0]
	y=init[1]
	cost=1
	open=[[g,x,y]]
	delta=[[-1,0],[0,-1],[1,0],[0,1]]
	delta_name=['^','<','v','>']
	found=0
	resign=0
	count=0
	
	while(found==0 and resign==0):
	    
       # no element in next element list	
		if len(open)==0:
			resign=1
			print 'fail'
		else :
	   		
			open.sort()
			open.reverse()
			next=open.pop()  #list element with minimum g value
			#print next
			x=next[1]
			y=next[2]
			g=next[0]
			expand[x][y]=count
			count+=1
			if x==goal[0] and y==goal[1]:	
				found=1
				print next
			else:
				for i in range(len(delta)): # 4 directions
					x2=x+delta[i][0]    
					y2=y+delta[i][1]
					if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]): # grid range
						if closed[x2][y2]==0 and grid[x2][y2]==0:
							g2=g+cost
							open.append([g2,x2,y2])
							closed[x2][y2]=1
							action[x2][y2]=i
	
	# expansion grid
	for i in range(len(grid)):
		print expand[i]		
	
	#print path
	#---------------------------------------------------------------------------------------------
	x=goal[0]
	y=goal[1]
	policy[x][y]='*'
	while x!=init[0] or y!=init[1]:
		x2=x-delta[action[x][y]][0]
		y2=y-delta[action[x][y]][1]
		policy[x2][y2]=delta_name[action[x][y]]
		x=x2
		y=y2
	
	for i in range(len(grid)):
		print policy[i]		
	
	#------------------------------------------------------------------------------------

def A_star_search(grid,init,goal):
		
	# open list items are of type [g,x,y]
	
	heuristic=[[9,8,7,6,5,4],
			   [8,7,9,5,4,3],
			   [7,6,5,4,3,2],
			   [6,5,4,3,2,1],
			   [5,4,3,2,1,0]]
			   
	closed=[[0 for x in range(len(grid[0]))] for y in range(len(grid))]
	expand=[[-1 for x in range(len(grid[0]))] for y in range(len(grid))]
	policy=[[' ' for x in range(len(grid[0]))] for y in range(len(grid))]
	action=[[-1 for x in range(len(grid[0]))] for y in range(len(grid))]
	
	closed[init[0]][init[1]]=1
	g=0
	x=init[0]
	y=init[1]
	cost=1
	f=g+heuristic[x][y]
	open=[[f,g,x,y]]
	delta=[[-1,0],[0,-1],[1,0],[0,1]]
	delta_name=['^','<','v','>']
	found=0
	resign=0
	count=0
	
	while(found==0 and resign==0):
	    
       # no element in next element list	
		if len(open)==0:
			resign=1
			print 'fail'
		else :
	   		
			open.sort()
			open.reverse()
			next=open.pop()  #list element with minimum g value
			#print next
			x=next[2]
			y=next[3]
			g=next[1]
			expand[x][y]=count
			count+=1
			if x==goal[0] and y==goal[1]:	
				found=1
				print next
			else:
				for i in range(len(delta)): # 4 directions
					x2=x+delta[i][0]    
					y2=y+delta[i][1]
					if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]): # grid range
						if closed[x2][y2]==0 and grid[x2][y2]==0:
							g2=g+cost
							open.append([g2+heuristic[x2][y2],g2,x2,y2])
							closed[x2][y2]=1
							action[x2][y2]=i
	
	# expansion grid
	for i in range(len(grid)):
		print expand[i]		
	
	#print path
	#---------------------------------------------------------------------------------------------
	x=goal[0]
	y=goal[1]
	policy[x][y]='*'
	while x!=init[0] or y!=init[1]:
		x2=x-delta[action[x][y]][0]
		y2=y-delta[action[x][y]][1]
		policy[x2][y2]=delta_name[action[x][y]]
		x=x2
		y=y2
	
	for i in range(len(grid)):
		print policy[i]		
	
	#------------------------------------------------------------------------------------
def Dynamic_progsearch(grid,init,goal):
	
	value=[[99 for x in range(len(grid[0]))] for y in range(len(grid))]
	policy=[[' ' for x in range(len(grid[0]))] for y in range(len(grid))]
	cost_step=1
	change=1
	delta=[[-1,0],[0,-1],[1,0],[0,1]]
	delta_name=['^','<','v','>']
	
	# calcluate optimal value from each location
	while change==1:
		change=0
		
		for x in range(len(grid)):
			for y in range(len(grid[0])):
				
				if goal[0]==x and goal[1]==y:
					if value[x][y]>0:
						value[x][y]=0
						change=1
				
				elif grid[x][y]==0:
					for a in range(len(delta)):
						x2=x+delta[a][0]
						y2=y+delta[a][1]
						if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]) and grid[x2][y2]==0:
							v2=value[x2][y2]+cost_step
							
							if v2<value[x][y]:
								change=1
								value[x][y]=v2
			
	for i in range(len(grid)):
		print value[i]	
	
	# calculate policy matrix in case car reaches any position on grid
		
	for x in range(len(grid)):
			for y in range(len(grid[0])):
				if x==goal[0] and y==goal[1]:
					policy[x][y]='*'	
				elif grid[x][y]==0:
					dir=' '
					val=99
					for i in range(len(delta)):
						x2=x+delta[i][0]
						y2=y+delta[i][1]
						if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]) and grid[x2][y2]==0:
					 		if value[x2][y2]<val:
					 			val=value[x2][y2]
					 			dir=delta_name[i]
					policy[x][y]=dir
					 			
	for i in range(len(grid)):
		print policy[i]	
#-----------------------------------------------------------------------------------------------------
def three_D_Dynamic_prog():
	
	grid=[[1,1,1,0,0,0],
      	  [1,1,1,0,1,0],
      	  [0,0,0,0,0,0],
          [1,1,1,0,1,1],
          [1,1,1,0,1,1]]
          
	value=[[[999 for x in range(len(grid[0]))] for y in range(len(grid))],
		   [[999 for x in range(len(grid[0]))] for y in range(len(grid))],
		   [[999 for x in range(len(grid[0]))] for y in range(len(grid))],
		   [[999 for x in range(len(grid[0]))] for y in range(len(grid))]]
	
	policy=[[[' ' for x in range(len(grid[0]))] for y in range(len(grid))],
		    [[' ' for x in range(len(grid[0]))] for y in range(len(grid))],
		    [[' ' for x in range(len(grid[0]))] for y in range(len(grid))],
		    [[' ' for x in range(len(grid[0]))] for y in range(len(grid))]]
	
	policy2D=[[' ' for x in range(len(grid[0]))] for y in range(len(grid))]	
	goal=[4,5]
	init=[0,0,2]
	cost=[1,1,1]
	action=[-1,0,1]
	action_name=['R','#','L']
	forward=[[-1,0],[0,-1],[1,0],[0,1]]
	change=1
	while change==1:
		change=0
		
		for x in range(len(grid)):
			for y in range(len(grid[0])):
				for orientation in range(4):
					if goal[0]==x and goal[1]==y:
						if value[orientation][x][y]>0:
							value[orientation][x][y]=0
							change=1
							policy[orientation][x][y]='*'
							
					elif grid[x][y]==0:
						for i in range(3):
							o2=(orientation+action[i])%4
							x2=x+forward[o2][0]
							y2=y+forward[o2][1]
							if x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0]) and grid[x2][y2]==0:
								v2=value[o2][x2][y2]+cost[i]
								if v2<value[orientation][x][y]:
									value[orientation][x][y]=v2
									policy[orientation][x][y]=action_name[i]
									change=1
	
	#---------policy 2-D array
	
	x=init[0]
	y=init[1]
	orientation=init[2]
	policy2D[x][y]=policy[orientation][x][y]
	while policy[orientation][x][y]!='*':
		if policy[orientation][x][y]=='#':
			o2=orientation
		elif policy[orientation][x][y]=='R':
			o2=(orientation-1)%4
		elif policy[orientation][x][y]=='L':
			o2=(orientation+1)%4
		x=x+forward[o2][0]
		y=y+forward[o2][1]
		orientation=o2
		policy2D[x][y]=policy[orientation][x][y]
	
	for i in range(len(policy2D)):
		print policy2D[i]

#------------------------------------------------------------------------------------------------		
def func():

	grid=[[1,1,1,0,0,0],
      	  [1,1,1,0,1,0],
      	  [0,0,0,0,0,0],
          [1,1,1,0,1,1],
          [1,1,1,0,1,1]]


	init=[0,0]
	goal=[len(grid)-1,len(grid[0])-1]
	
	#search(grid,init,goal)
	#A_star_search(grid,init,goal)
	#Dynamic_progsearch(grid,init,goal)
	three_D_Dynamic_prog()
func()
