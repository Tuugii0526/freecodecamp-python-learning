def guess_square_root(square_target,tolerance=1e-7,max_iterations=100):
    root=None
    if square_target<0:
        raise ValueError("Negative number doesn't have square root")
    if square_target==1:
        root=1
    elif square_target==0:
        root=0
    else :
        low=0
        high=square_target
        mid=0
        for _ in range(max_iterations):
            mid=(high+low)/2
            square_mid=mid**2
            if abs(square_target-square_mid)<tolerance:
                root=mid
                break
            elif square_mid <square_target:
                low=mid
            else:
                high=mid
    if root is None :
        print('Square root not found')
    else:
        print(f'Square root found:{root}')
    return root
N=10
guess_square_root(N)
