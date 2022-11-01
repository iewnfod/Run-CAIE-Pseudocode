import os

def main(file_path):
    with open(file_path, 'r') as f:
        file = f.read().strip().split('\n')
    
    name = os.path.basename(file_path)

    include = ['<iostream>', '<string>']
    head = ''
    for i in include:
        head += '#include ' + i + '\n'
    
    head += '\nusing namespace std; '

    variables = {} # name : type

    front = 0
    last = 0

    types = {
        'STRING': 'string', 
        'BOOLEAN': 'bool', 
        'CHAR': 'char', 
        'INTEGER': 'int', 
        'REAL': 'double'
    }

    def correct(t:str, _if = True):
        if _if:
            t = t.replace('=', '==')
        t = t.replace('<>', '!=').replace('AND', '&&').replace('OR', '||').replace('NOT', '!').replace('&', '+').replace('BREAK', 'break').replace('CONTINUE', 'continue')
        return t


    for i in range(len(file)):
        text = file[i]
        explain = '//' + '//'.join(text.split('//')[1:])
        text = text.split('//')[0]
        text = text.split()

        text_length = len(text)

        # declare
        if text[0] == 'DECLARE':
            type_ = text[2]
            name = text[1]
            text = f'{name} {types[type_]}; '
            variables[name] = type_
        
        # if 
        elif text[0] == 'IF':
            statement = ' '.join(text[1:text_length-1])

        # else if
        elif text[0] == 'ELSE' and text[1] == 'IF':
            v = ' '.join(text[2:text_length-1])
            pass

    father_path = os.path.abspath(os.path.dirname(file_path) + os.path.sep+'.')

    with open(os.path.join(father_path, name+'.cpp'), 'w') as f:
        pass
