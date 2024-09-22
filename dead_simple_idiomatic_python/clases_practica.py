# Classes provide a blueprint of an object: helping us construct an object
# with certain characteristics (methods), and this object can be reused easily.
# The basic syntax is:
# class keyword + name of the class + colon at end of header
# suite
# The initializer (similar to the constructor in other OOP langs) is a method (= a function associated w/ a class)
# It needs to have at least 1 parameter: self
class Joke:
    def __init__(self, joke_type):
        if joke_type == "funny":
            self.question = "How can you tell an elephant is in your fridge?"
            self.answer = "There are footprints in the butter!"
        elif joke_type == "lethal":
            self.question = "How can you tell an elephant is in your fridge?"
            self.answer = "There are footprints in the butter!"
        else:
            self.question = "Why did the chicken cross the road?"
            self.answer = "To get to the other side!"


mi_joke = Joke("lethal")
print(mi_joke.answer)
