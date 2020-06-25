def get_input():
    string_array = []
    num_tests = int(input())
    for test in range(num_tests):
        string_array.append(input())
    return string_array

def alternate_characters(string_array):
    for string in string_array:
        num_deletions = 0
        if len(string) == 1:
            return num_deletions
        else:
            for index in range(1, len(string)):
                if string[index-1] == string[index]:
                    num_deletions += 1
        print(num_deletions)
            
def run_test():
    string_array = get_input()
    alternate_characters(string_array)
    
run_test()