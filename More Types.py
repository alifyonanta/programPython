#TUPLES
words = ("spam", "eggs", "sausages",)
print(words[0])

my_tuple = "one", "two", "three"
print(my_tuple[0])

#List Slices
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:10])
print(squares[3:10])
print(squares[5:10])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[5:1:-2])


#List Comprehensions
# a list comprehension
cubes = [i**3 for i in range(5)]
print(cubes)

evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)


# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

a = "{x}, {y}".format(x=5, y=12)
print(a)

#String Functions
print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ello", " Alif"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

#Numeric Functions
print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))
#List Functions
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")

for v in enumerate(nums):
    print(v)
