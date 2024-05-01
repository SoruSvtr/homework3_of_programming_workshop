suspect_statements = {'a': [1, 2, 3], 'b': [1, 3, 6], 'c': [1, 2, 4], 'd': [1, 2, 5]}
'''
the numbers within the lists are a measure to the statements of the suspects which is indicated from 1 to 6
up to 3 indicates an almost truth and 4 to 6 indicates a lie
'''
Max = max(suspect_statements.values())
# this line of code is showing the suspect which lied too much and will be our very wanted whief !!

for key, value in suspect_statements.items():
    if value == Max:
        print(f'According to detective\'s investigation the thief is {key}.')