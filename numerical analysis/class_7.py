def get_word(sentence, n):
    words = sentence. split(" ")
    #splits are use to enter space between the string
    if len(words) > n :
        return words[n]
print(get_word("This is a lesson about lists", 4))
#.append function adds data to end of the list
#.append(data)
fruit = ["apple","melon","kiwi"]
fruit.append("kiwi")
print(fruit)
#.insert(index.data)
#tuples are immutable
#tuples
def covert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600)// 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

#enumerate
q = ["eat", "sleep", "repeat"]
g = "walk"
obj1 = enumerate(q)
obj12 = enumerate(g)
print(list(enumerate(q)))
print(list(enumerate(g)))