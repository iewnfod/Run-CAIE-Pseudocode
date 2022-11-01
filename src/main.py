import os
import sys

def translate(file_path):
    variable_types = {}
    with open(file_path, 'r') as f:
        r = [i.strip().replace('\n', '').replace('\t', '').replace('\r', '') for i in f.read().strip().split('\n')]
    with open(file_path, 'r') as f:
        total = f.read()
    name = os.path.basename(file_path)
    tab_num = 0
    next_tab_num = 0
    default_value = {
        'INT': 0,
        'BOOL': False, 
        'REAL': 0, 
        'STRING': '\'\'', 
        'CHAR': '\'\'', 
        'ARRAY': '{}'
    }
    change_ = {
        'INT': 'int', 
        'BOOL': 'bool', 
        'REAL': 'float', 
        'STRING': 'str', 
        'CHAR': 'str', 
        'ARRAY': 'to_dict'
    }

    def correct(t:str, _if = True):
        if _if:
            t = t.replace('=', '==')
        t = t.replace('<>', '!=').replace('AND', 'and').replace('OR', 'or').replace('LENGTH', 'len').replace('NOT', 'not').replace('^', '**').replace('&', '+').replace('BREAK', 'break').replace('CONTINUE', 'continue')
        return t

    for i in range(len(r)):
        tab_num = next_tab_num
        text = r[i]
        # 获取注释
        explain = ('#' + ''.join(text.split('//')[1:])) if '//' in text else ''
        text = text.split('//')[0]
        text = text.split(' ')
        text_length = len(text)
        text += [''] * 5

        # declare
        if text[0] == 'DECLARE':
            variable_types[text[1]] = text[3]
            text = correct(f'{text[1]} = {default_value[text[3]]}', _if=False)

        # if
        elif text[0] == 'IF':
            v = correct(' '.join(text[1:text_length-1]))
            text = f'if {v}:'
            next_tab_num += 1
        # elif
        elif text[0] == 'ELSE' and text[1] == 'IF':
            v = correct(' '.join(text[2:text_length-1]))
            text = f'elif {v}:'
            tab_num -= 1
        # else
        elif text[0] == 'ELSE':
            text = 'else:'
            tab_num -= 1
        # endif
        elif text[0] == 'ENDIF':
            text = ''
            next_tab_num -= 1
        
        # for
        elif text[0] == 'FOR':
            target_variable = text[1]
            for ind in range(len(text)):
                if text[ind] == 'TO' or text[ind] == 'to':
                    break
            to_place = ind
            v1 = ' '.join(text[3:to_place])
            v2 = ' '.join(text[to_place+1:text_length])
            text = correct(f'for {target_variable} in range({v1}, {v2}+1):')
            next_tab_num += 1
        # next
        elif text[0] == 'NEXT':
            text = ''
            tab_num -= 1
            next_tab_num -= 1
        
        # while
        elif text[0] == 'WHILE':
            v = correct(' '.join(text[1:text_length-1]))
            text = f'while {v}:'
            next_tab_num += 1
        # endwhile
        elif text[0] == 'ENDWHILE':
            text = ''
            tab_num -= 1
            next_tab_num -= 1
        
        # repeat
        elif text[0] == 'REPEAT':
            text = f'while True:'
            next_tab_num += 1
        # until
        elif text[0] == 'UNTIL':
            v = correct(' '.join(text[1:text_length]))
            tab_before_break = '\t'*(tab_num+1)
            text = f'if {v}: \n{tab_before_break}break'
            next_tab_num -= 1
        
        # output
        elif text[0] == 'OUTPUT':
            v = correct(' '.join(text[1:text_length]))
            text = f'print({v})'
        elif text[0][:6] == 'OUTPUT':
            text = ' '.join(text[:text_length]).replace('OUTPUT', 'print')
        # input
        elif text[0] == 'INPUT':
            text = f'{text[1]} = {change_[variable_types[text[1]]]}(input())'

        # procedure function
        elif text[0] == 'PROCEDURE' or text[0] == 'FUNCTION':
            v = correct(' '.join(text[1:text_length]))
            text = f'def {v}:'
            next_tab_num += 1
        # endprocedure endfunction
        elif text[0] == 'ENDPROCEDURE' or text[0] == 'ENDFUNCTION':
            text = ''
            next_tab_num -= 1
            tab_num -= 1
        
        # open
        elif text[0] == 'OPEN':
            v = correct(' '.join(text[1:text_length]))
            text = f'temp_file = open({v}, \'w+\')'
        # close
        elif text[0] == 'CLOSE':
            text = 'temp_file.close()'

        # write
        elif text[0] == 'WRITE':
            v = correct(' '.join(text[1:text_length]))
            text = f'temp_file.write(str({v}))'

        # return
        elif text[0] == 'RETURN':
            v = correct(' '.join(text[1:text_length]))
            text = f'return {v}'

        if type(text) == list:
            while '' in text:
                text.remove('')
            text = ' '.join(text)

        # 修改赋值
        text = text.replace('<-', '=') + explain

        # 进退
        r[i] = '\t' * tab_num + text

    addition_file = '''
def READ(f):
    with open(f, 'r') as f:
        return f.read()
    '''

    addition_div = '''
def DIV(a, b):
    return a // b
    '''
    addition_mod = '''
def MOD(a, b):
    return a % b
    '''
    addition_substring = '''
def SUBSTRING(s, start, next):
    return s[start:start+next]
    '''
    addition_lower = '''
def LOWER(s):
    return s.lower()
    '''
    addition_upper = '''
def UPPER(s):
    return s.upper()
    '''
    addition_array = '''
def to_dict(s):
    d = {i:s[i] for i in range(len(s))}
    return d
    '''

    father_path = os.path.abspath(os.path.dirname(file_path) + os.path.sep+'.')
    with open(os.path.join(father_path, name+'.py'), 'w') as f:
        if 'OPEN' and 'CLOSE' in total:
            f.write(addition_file)
        if 'DIV' in total:
            f.write(addition_div)
        if 'MOD' in total:
            f.write(addition_mod)
        if 'SUBSTRING' in total:
            f.write(addition_substring)
        if 'LOWER' in total:
            f.write(addition_lower)
        if 'UPPER' in total:
            f.write(addition_upper)
        if 'ARRAY' in total:
            f.write(addition_array)

        f.write('\n')

        f.write('\n'.join(r)+'\n')

def run(file_path):
    father_path = os.path.abspath(os.path.dirname(file_path) + os.path.sep+'.')
    py_file_path = os.path.join(father_path, os.path.basename(file_path)+'.py')

    platform = sys.platform
    if 'linux' in platform:
        os.system(f'gnome-terminal -e \'python3 {py_file_path}; exit\'')

    elif 'darwin' in platform:
        command = f'python3 {py_file_path}; exit'
        # os.system(command)
        os.system(f'osascript -e \'tell application "Terminal" to do script "{command}"\'')
        # appscript.app('Terminal').do_script(command)

    elif 'win32' in platform or 'win64' in platform:
        os.system('start cmd /c ' + f'python {py_file_path}')
