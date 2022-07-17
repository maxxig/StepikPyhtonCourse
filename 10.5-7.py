words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
#words = ['yes', 'hello']
result = {w: [ord(k) for k in w] for w in words}
print(result)