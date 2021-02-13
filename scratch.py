string='banana'
for length in range(len(string)):
    for index in range(len(string) - length):
        print(string[index:index+length+1])