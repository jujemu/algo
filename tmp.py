import sys
sys.stdin = open('./implementation/input_bj_2504.txt')
string = sys.stdin.readline().rstrip()

def bracket():
    global i
    start = string[i]
    
    result = 0
    while True:
        i += 1
        c = string[i]
        if c in ['(', '[']:
            result += bracket()
        result = 1 if not result else result
        return 2*result if c == ')' else 3*result

i = 0
print(bracket()) # result 28
