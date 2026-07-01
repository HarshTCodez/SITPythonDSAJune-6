string = "abcd"
print(string)


string2 = "efgh"
result = string + string2

string2 = "   abcdefg     "
string1 = "dummy_string"

string2 = string2.rstrip()

result = string2 + string1
print(result)


string = "a\nb\nc"
string = string.replace("\n", ",")

numbers = "10 9 8 7"
print(string)

res = numbers.split(" ")
print(res)


res = ["a", "b", "c", "d"]
ans = ", ".join(res)
print(ans)


name = "anmol jhamb"
print(name.capitalize())


result = numbers.split()
print(result)

for i in range(len(result)):
    result[i] = int(result[i])


# map function
new_result = list(map(int, numbers.split()))


def add_1(n):
    return n + 1


new_result = list(map(add_1, new_result))

print(new_result)

new_result = list(map(lambda n: n + 2, new_result))

print(new_result)


my_list = [1, 2, 3, 4, 5]
# new_list = [1, 4, 9, 16, 25]
new_list = list(map(lambda n: n * n, my_list))
print(new_list)


# "my name is anmol"
# "My Name Is Anmol"

string = "my name is anmol"
words = string.split()
print(words)

new_words = list(map(lambda x: x.capitalize(), words))
print(new_words)
ans = " ".join(new_words)
print(ans)
