import bucket_sort

def test_sort_empty():
    expected = []
    input = []
    assert bucket_sort.sort(input) == expected
    
def testSort1Item():
    expected = [1.9]
    input = [1.9]
    assert bucket_sort.sort(input) == expected