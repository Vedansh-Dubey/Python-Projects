# function to find frequency of a word in the text
def most_frequent(x, dictionary):
    for i in x:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return sorted(dictionary.items(), key=descending, reverse=True)

#  function to sort dictionary in descending order by frequency
def descending(dictionary):
        return dictionary[1]

dictionary={}
x= input("Enter the string: ")
print(str(most_frequent(x, dictionary)).replace("'", "").replace(",", " ").replace("'", "").replace("[", "").replace("]", ""))

