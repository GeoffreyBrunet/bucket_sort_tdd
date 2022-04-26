import bucket_sort

def test_sort_empty():
    expected = []
    input = []
    assert bucket_sort.sort(input) == expected