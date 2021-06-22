string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."

patches = [[4, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]

# test=string.replace(string[4:14],"Conquistador")
# print(test)

# def replace_function(start,end,word):
#     global string
#     string2 = string.replace(string[start-1:end], word)
#     return string2
#
# print(replace_function(5, 14, "Conquistador"))

def function(string,patches):
    patches=reversed(patches)

    for item in patches:
        print(item)
        start = item[0]
        end = item[1]
        word = item[2]
        string = string.replace(string[start-1:end], word)
        print(string, string[start-1:end])
    return string

print(function("The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced.",[[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Abacadabra"]]))

# print(string[42:49])
#
# # The Conquistator must meet King on top of Palace battlements to be introduced.
