NUMBER_OF_DISKS=9
number_of_moves=2** NUMBER_OF_DISKS -1
rods={
    'A':list(range(NUMBER_OF_DISKS,0,-1)),
    'B':[],
    'C':[]
}
def move(rod1,rod2):
    forward=False
    if not rods[rod1]:
        forward=True
    elif rods[rod2] and rods[rod2][-1]<rods[rod1][-1]:
        forward=True
    if forward :
        rods[rod1].append(rods[rod2].pop())
    else:
        rods[rod2].append(rods[rod1].pop())
def tower(n,source,auxiliary,target):
    for i in range(number_of_moves):
        if (i+1)%3==1:
            if n%2!=0:
                move(source,target)
            else:
                move(source,auxiliary)
        elif (i+1)%3==2:
            if n%2!=0:
                move(source,auxiliary)
            else:
                move(source,target)
        elif (i+1)%3==0:
            move(auxiliary,target)
    print('rods:',rods)
tower(NUMBER_OF_DISKS,'A','B','C')            
# source --> target
# source --> auxiliary
# target --> auxiliary

# move n-1 disks from source to auxiliary using target
# move a disk from source to target 
# move n-1 disks from auxiliary to target using source

# first 
# [3,2,1] [] [] 
# [3,2] [] [1] #1 
# [3] [2] [1]  #2
# [3] [2,1] [] #0 

# [] [2,1] [3] #1
# [1] [2] [3] #2
# [1] [] [3,2] #0

# [] [] [3,2,1] #1


# second
# [4,3,2,1][][] 
# [4,3,2][1][] #1
# [4,3][1][2] #2
# [4,3][][2,1] #0 
# [4][3][2,1] #1
# [4,1][3][2] #2
# [4,1][3,2,][] #0
# [4][3,2,1][] #1
# [][3,2,1][4]#2 
# [1][3,2][4]#0
# [1][3][4,2]#1
# [1][3][4,2]#2
# [2][3,1][4]#0
# [2,1][3][4]#1
# [2,1][][4,3]#2
# [2][1][4,3]#0
# [][1][4,3,2]#1
# [][][4,3,2,1]#2



