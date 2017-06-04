source = [4,3,2,1]
target = []
helper = []
posts = [source, helper, target]

def hanoi(n, source, helper, target):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        target.append(source.pop())
        print(posts[0], posts[1], posts[2])
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)


hanoi(len(source),source,helper,target)

print(source, helper, target)
