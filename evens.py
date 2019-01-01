def number_of_evens(numbers):
    return 0
    
def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

def test_not_equal(a,b):
    assert a != b, "Did not expect {0} but got{1}".format(a,b)
    
    def test_is_in(collection, item):
        assert item in collection, "{0} does not contain [1}".format(collection, item)
    
test_are_equal(number_of_evens([1,2,3,4,5]), 2)



#testing
#def is_even(number):
    #return number % 2 == 0

#def even_number_of_evens(numbers):

    #evens = sum([1 for n in numbers if is_even(n)])
    #return False if evens == 0 else is_even(evens)

    
#assert even_number_of_evens([]) == False, "No Numbers"

#assert even_number_of_evens([2, 4]) == True, "Two even numbers"
#assert even_number_of_evens([2]) == False, "One even number"
#assert even_number_of_evens([1,3, 9]) == False, "Three Numbers"

#print("All tests passed!")