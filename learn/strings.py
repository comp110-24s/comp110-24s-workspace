# String within a string escape method \
    # "The students rejoiced, \"we love programming!\""
    # 'The students rejoiced, "we love programming!"`

# Expressions with strings +
    # "110" + "110" ->'110110`
    # Print(“Howdy!”[1]) -> H: first letter
    # Print(“Howdy!”[3]) -> w: third letter
    # “Hello”*3 -> “HelloHelloHello”
    # “11” + “12” -> 1112
    # 220 >= int ((“1”+”1”+”0)*2) -> 220 >= int ((“110”)*2) => 220 = 110110


# Indexing  len()
    # First item in sequence is at index 0
    # Find last item’s index using len(sequence) – 1
    # len("str!") -> 4
    # "str!"[len("str!") - 1] -> '!'
    # Can only be used on str, not int or float

# Docstrings
    # """This is a docstring.""" at the top of every file describing its purpose

# Method Call Expressions
    # msg: str = "hello, world"
    # msg.upper() -> 'HELLO, WORLD'
    # msg.capitalize() -> 'Hello, world'
    # msg.startswith("help") -> False
    # msg.startswith("hello") -> True 
    # msg -> 'hello, world'

# isalpha - tests if a string is made entirely of alphabetical characters
    # "comp110".isalpha() -> False
    # "100".isalpha() -> False
    # "comp110"[0].isalpha -> True

# random
    #from random import choice
    #print(choice("wxyz"))