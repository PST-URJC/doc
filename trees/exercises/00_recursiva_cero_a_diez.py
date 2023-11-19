MAX=10

def recursiva(num, max):
    print(num)
    if num < max:
        recursiva(num+1, max)

recursiva(0, MAX)
