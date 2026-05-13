def join_strings(strings):
    joint_string = ""

    for i in range(len(strings)):
        joint_string += strings[i] + ","

    return joint_string[:-1]

##alternatively, never create an unwanted comma instead of creating it > deleting it
#def join_strings(strings):
#    result = ""

#    for i in range(len(strings)):
#        result += strings[i]

#        if i != len(strings) - 1:
#            result += ","

#    return result
