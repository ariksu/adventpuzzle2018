def test_1_1():
    assert True
    pass


def test_1_2():
    assert True
    pass


def test_2_1():
    from solutions.q2_1 import contain23s
    twos, threes = contain23s("abcdef")
    # abcdef contains no letters that appear exactly two or three times.
    assert (twos, threes) == (False, False)
    twos, threes = contain23s("bababc")
    # bababc contains two a and three b, so it counts for both.
    assert (twos, threes) == (True, True)
    twos, threes = contain23s("abbcde")
    # abbcde contains two b, but no letter appears exactly three times.
    assert (twos, threes) == (True, False)
    twos, threes = contain23s("abcccd")
    # abcccd contains three c, but no letter appears exactly two times.
    assert (twos, threes) == (False, True)
    twos, threes = contain23s("aabcdd")
    # aabcdd contains two a and two d, but it only counts once.
    assert (twos, threes) == (True, False)
    twos, threes = contain23s("aaaaee")
    # abcdee contains two e and four a.
    assert (twos, threes) == (True, False)
    twos, threes = contain23s("ababab")
    # ababab contains three a and three b, but it only counts once.
    assert (twos, threes) == (False, True)
    from solutions.q2_2 import find_similarish
    source = [
        "abcde",
        "fghij",
        "klmno",
        "pqrst",
        "fguij",
        "axcye",
        "wvxyz",
    ]
    assert ("fghij", "fguij") == find_similarish(source)
    pass


def test3_1():
    source = [
        "# 1 @ 1,3: 4x4",
        "# 2 @ 3,1: 4x4",
        "# 3 @ 5,5: 2x2",
    ]
    from solutions.q3_1 import Claims
    field = Claims(source)
    assert field.Count_Intesections() == 4
    pass
