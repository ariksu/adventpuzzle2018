# what is first sum appended twice
from solutions.tools import open_input


def sum_appender()->int:
    result_freq = 0
    freq_list = set()
    iter = 0
    freq_list.update([0])
    while True:
        iter += 1
        print(f"loop: {iter} len: {len(freq_list)} biggest: {max(freq_list)}")
        f = open_input("1")
        for line in f:
            result_freq += int(line)
            if result_freq in freq_list:
                print(freq_list)
                return result_freq
            freq_list.update([result_freq])


if __name__ == '__main__':
    print('result')
    print(sum_appender())
