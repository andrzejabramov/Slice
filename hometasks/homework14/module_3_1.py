calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    l = len(string)
    lstr = string.lower()
    ustr = string.upper()
    str_res = (l, ustr, lstr)
    count_calls()
    return str_res

def is_contains(string, l):
    string = string.upper()
    l = list(map(str.upper, l))
    count_calls()
    return True if string in l else False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

