def toh(n,source,auxiliary,target):
    if n<=0:
        return
    toh(n-1,source,target,auxiliary)
    target.append(source.pop())
    toh(n-1,auxiliary,source,target)
    
