from solutions.tools import open_input


def freq_sum():
    result_freq = 0
    f = open_input("1")
    for line in f:
        result_freq += int(line)
    print(result_freq)


# what is the sum of input
freq_sum()
