# what is first sum appended twice
def sum_appender():
    result_freq = 0
    freq_list = []
    iter = 0
    freq_list.append(0)
    while True:
        iter += 1
        print(f"loop: {iter} len: {len(freq_list)} biggest: {max(freq_list)}")
        with open('1.input') as f:
            for line in f:
                result_freq += int(line)
                if result_freq in freq_list:
                    print(freq_list)
                    return result_freq
                freq_list.append(result_freq)


if __name__ == '__main__':
    print('result')
    print(sum_appender())
