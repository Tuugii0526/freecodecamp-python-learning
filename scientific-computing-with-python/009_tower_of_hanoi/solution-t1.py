NUMBER_OF_DISKS = 3
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    if n <= 0:
        return
    # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
    # move the nth disk from source to target
    target.append(source.pop())
    
    # display our progress
    # print(A, B, C, '\n')
    
    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)
# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)
# inspect
#initial 1,2,3
#first 1,3,2
#second 2,1,3
move(3,s,a,t)
    move(2,s,t,a)
        move(1,s,a,t)
            move(0,s,t,a) return
            t.a(s.p())
            move(0,a,s,t)
        t.a(s.p())
        move(1,t,s,a)
    t.a(s.p())
    move(2,a,s,t)
