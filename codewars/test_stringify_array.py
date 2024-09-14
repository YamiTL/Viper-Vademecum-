#Write a function to split a string and convert it into an array of words.
def string_to_array(s):
    return s.split(sep=' ')
    
    

print(string_to_array("Robin Singh"))
print (type(string_to_array))

string_to_array("Robin Singh")

pass

#Examples (Input ==> Output):
#"Robin Singh" ==> ["Robin", "Singh"]

#"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]



def test_basic_test_cases():
        assert string_to_array("Robin Singh") == ["Robin", "Singh"]
        assert string_to_array("CodeWars") == ["CodeWars"]
        assert string_to_array("I love arrays they are my favorite") == ["I", "love", "arrays", "they", "are", "my", "favorite"]
        assert string_to_array("1 2 3") == ["1", "2", "3"]
        assert string_to_array("") == [""]