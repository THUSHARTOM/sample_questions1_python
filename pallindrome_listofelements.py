#Python program to check whether the list of strings given is
#pallindrome or not


def check_pallindrome(inp_str):
    res =[]
    for str in inp_str:
        if str[::-1].lower() == str.lower():
            res.append(str)
    return res

if __name__ == "__main__":
    count = int(input("How many words "))
    inp_str = []
    for i in range(count):
        inp_str.append(input())

    output = check_pallindrome(inp_str)
    if len(output) != 0:
        for i in output:
            print(i)
    else:
        print("No pallindrome Found")

