import time
source = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
target = []
helper = []
posts = [source, helper, target]
steps = 0
def hanoi(n, source, helper, target):
    global steps
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        target.append(source.pop())
        print(posts[0], posts[1], posts[2])
        steps=steps+1
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)

starttime = time.clock()
hanoi(len(source),source,helper,target)
endtime = time.clock()
print(source, helper, target)
print("Total Steps: ", steps)
print("Total seconds: ", endtime - starttime)
