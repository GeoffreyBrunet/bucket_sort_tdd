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
