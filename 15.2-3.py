import statistics
def mean(*args):
    t = [float(i) for i in args if type(i) in [int, float]]
    if len(t) == 0:
        return 0.0
    else:
        return statistics.mean(t)
    #return statistics.mean([i for i in args if type(i) is int])
    # return mean([i for i in args])

print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

