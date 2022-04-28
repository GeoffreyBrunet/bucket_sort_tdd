import bucket_sort


def test_sort_empty():
    expected = []
    input = []
    assert bucket_sort.sort(input) == expected


def testSort1Item():
    expected = [1.9]
    input = [1.9]
    assert bucket_sort.sort(input) == expected


def testSort2Item():
    expected = [1.9, 18.12]
    input = [18.12, 1.9]
    assert bucket_sort.sort(input) == expected


def testSort2Item():
    expected = [1.9, 18.12]
    input = [18.12, 1.9]
    assert bucket_sort.sort(input) == expected


def testSort7Items():
    expected = [1.7, 1.9, 2.1, 2.2, 2.3, 4.3, 8.1]
    input = [1.9, 1.7, 4.3, 2.3, 2.2, 2.1, 8.1]
    assert bucket_sort.sort(input) == expected
