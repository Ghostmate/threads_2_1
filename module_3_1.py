calls = 0
def count_calls():
    global calls
    calls += calls


def string_info(string):
    count_calls()
    result = (len(string), string.upper(), string.lower())
    return result


def is_contains(string, list_to_search):
    count_calls()
    loc_str = string.lower()
    for x in list_to_search:
        y = x.lower()
        if loc_str == y:
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
