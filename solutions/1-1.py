#what is the sum of input
result_freq = 0
with open('1.input') as f:
    for line in f:
        result_freq += int(line)
print(result_freq)
