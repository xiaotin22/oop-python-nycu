import lec10_complexity_part1 as lec
import pytest

testlist = [1, 3, 4, 5, 9, 10, 18, 27]
t2 = [1, 2, 5, 8]
t3 = [3, 4, 5, 9]
def test_linear_search():
    assert lec.linear_search(testlist, 10) == True
    assert lec.linear_search(testlist, 12) == False
    print("Test complete")


def test_isSubset():
    assert lec.isSubset(testlist, t2) == False
    assert lec.isSubset(t3, testlist) == True
    print ("t3 is testlist's sublist")


def test_intersect():
    print(lec.intersect(t2, t3))
    assert lec.intersect(t2, t3) == [5]
    print(lec.intersect(testlist, t3))
    assert lec.intersect(testlist, t3) == [3, 4, 5, 9]

if __name__ == "__main__":
    pytest.main([__file__])
    # Alternatively, you can run pytest from the command line:
    # pytest test_lec10-1.py