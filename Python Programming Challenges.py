# Exercise 1
def freeFall(val, isD):
    # g = 9.81 (m/s2)
    # t is the input value
    # this is a function that allows a user to introduce the distance d (in meters travelled by an object falling, or the time t (in seconds) taken for an object to fall, but not both.
    g = 9.81
    if isD == True:
        answer = round(((2 * val) / g) ** 0.5, 2)  # val is d
    else:
        answer = round(0.5 * (g * (val ** 2)), 2)  # val is t
    return answer


# Exercise 2
def RPS(s):
    # this is a function that, given a player’s strategy for a series of games of RPS as a string, will return the winning strategy as a string
    res = ""
    for l in range(len(s)):
        # for makes a loop, #in looks inside the loop, range checks {(s) the data} with the values of the if/elif statements
        x = s[l]
        # can only have one if statement, elif tells (len(s)) to keep looping to print the winning result
        if x == "R":
            res += "P"
        elif x == "P":
            res += "S"
        elif x == "S":
            res += "R"
    return res


# Exercise 3
def list2str(l):
    # this defines the function that will tell the list to become a string
    str1 = "["  # this sets the stage for an empty string
    # traverses the string to process every character in the string, which is defined in (l)
    for ele in l:  # the for loop checks each and ever item in the list
        if (type(ele) == list):  # if the type of the element in the defined value is a list
            # this is the recursion which sends the second list element (which is ['b', 'c'] ) back to the funtion (def list2str(l):). now the l is represented by the value of ele. we're only sending b and c back through the function. when it goes back through the funtion we see that it's a list, it gets sent through the else statement which makes it a string and then the following variable adds the closing bracket which completes the function
            str1 += list2str(ele)
        else:
            str1 += ele
    str1 += "]"  # this variable closes the string
    return str1  # return string


# Exercise 4
def textPreprocessing(text):
    # function which applies various preprocessing to a string text and returns a list
    punctuation = [
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        "_",
        "+",
        "<",
        ">",
        "?",
        ":",
        ".",
        ",",
        ";",
    ]

    for a in text:
        if a in punctuation:
            # moved the lower function to be part of the remove punctionation variable to shorten the code a bit
            text = text.replace(a, "").lower()

    # splittext is the variable, split command turns the variable text into a list. text.split is the function
    splittext = text.split()

    stopwords = [
        "i",
        "a",
        "about",
        "am",
        "an",
        "are",
        "as",
        "at",
        "be",
        "by",
        "for",
        "from",
        "how",
        "in",
        "is",
        "it",
        "of",
        "on",
        "or",
        "that",
        "the",
        "this",
        "to",
        "was",
        "what",
        "when",
        "where",
        "who",
        "will",
        "with",
    ]  # stop words are in a list, stopwords is the variable

    suffixwords = ["ed", "ing", "s"]

    for a in stopwords:  # stopwords is holding all of the elements, a is the individual element
        for x in splittext:  # using splittext because that is the variable that contains the list of words  # nested for loop;
            if a == x:  # each and every value of elements in splittext are a. and the same for stopwords in x.if and and x match, then below we remove x from the split text
                splittext.remove(a)

    for b in range(0, len(splittext)):  # len is counting the elements in the range of splittext, len times splitext times range; range is the function that tells the loop to go through every element in splittext
        for y in suffixwords:
            # hi.endswith(ed) #endswith is the command
            # https://stackabuse.com/python-remove-the-prefix-and-suffix-from-a-string/ reference link
            if splittext[b].endswith(y):
                # len is the length function that tells the length of the characters to compare the suffixes to the elements in splittext, if the word endings match they will be removed
                line_new = splittext[b][: -len(y)]
                splittext[b] = line_new  # array

    return splittext


# Exercise 5
def isGreaterThan(dict1, dict2):  # a function which takes as input two dictionaries having only string keys and numerical values, and checks if one is greater than the other
    for key in dict2.keys():  # checks the keys in dict2
        if key not in dict1.keys():  # this if statement commands the function to compare the keys in both dictionaries, if the key is not in dict1 our return will be false
            return False
    s = False
    for key in dict2:
        for key2 in dict1:
            if key == key2:  # this loop compares the values of each dictionary
                if dict2[key] > dict1[key2]:
                    return False  # return is sashaying away from the problem and getting me out of the loop
                elif dict1[key2] > dict2[key]:
                    s = True
    if s == True:
        return True
    else:
        return False


# Exercise 6
def CSVsum(filename):
    # a function that reads a CSV file with or without a header, and provides as output a list of the sums of each column
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    results = []
    for line in lines:
        # this for loop makes the data in the file a list
        words = line.split(",")
        results.append(words)
    d = []
    for ele in range(len(results[0])):
        test1 = 0
        for g in range(len(results)):
            try:
                test1 = test1 + float(results[g][ele])
            except:
                continue
        d.append(test1)
    return d


# Exercise 7
def str2list(s):
    return None


# Exercise 8
def spacemonSim(roster1, roster2):
    return None


# Exercise 9
def rewardShortPath(env):
    return None


# Exercise 10
def cliqueCounter(network):
    return None
