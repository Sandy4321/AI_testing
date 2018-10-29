import string
import random
import re

OPERATORS = [' = ', ' != ', ' is ', ' is not ']
func_name_len = range(2, 21)
func_name_chars = list(string.ascii_lowercase)+['_']
char_weights = [1]*(len(func_name_chars)-1)+[5]
param_name_len = range(2,11)
n_param = range(1,6)

class GenerateFunctions():
    def __init__(self, n):
        self.function_string_list = []
        self.test_function_string_list = []
        self.n = n

    def rand_func_name(self):
        #function name cannot start with an underscore
        first_letter = random.choice(func_name_chars[:-1])
        s = first_letter + ''.join(random.choices(func_name_chars,
                                      weights=char_weights,
                                      k=random.choice(func_name_len)))
        return s

    def rand_param_name(self):
        return ''.join(random.choices(func_name_chars[:-1], k=random.choice(param_name_len)))

    def rand_params(self):
        return [self.rand_param_name() for _ in range(random.choice(n_param))]

    def inputs_string(self,l):
        return ', '.join([str(random.randint(0, 100)) for _ in range(l)])

    def output_value(self):
        return random.choice([random.randint(0, 100), True, False])

    # comment
    def comments(self, n_inputs, func_name, output_name, output, space='    '):
        ope = random.choice(OPERATORS)
        s = space + '\"\"\"\n    Comment\n    :test: '
        s += func_name + '('
        s += self.inputs_string(n_inputs)
        s += ')'
        s += ope
        if ope in [' is not ', ' != ']:
            if isinstance(output, bool):
                s += str(not output)
            else:
                s += str(output - output)
        else:
            s += str(output)
        s += '\n'
        s += space + '\"\"\"'
        s += '\n'
        s += space + 'return '
        s += output_name
        return s

    def header(self, func_name, param_list, output_name, output):
        s = '\n\ndef '
        s += func_name
        s += '('
        s += ', '.join(param_list)
        s += ', '
        s += output_name
        s += ' = ' + str(output)
        s += '):\n'
        return s

    def print_func(self, funcname, input_params, output_name):
        output = self.output_value()
        s = self.header(funcname, input_params, output_name, output)
        s += self.comments(len(input_params), funcname, output_name, output)
        return s

    def generate_functions(self):
        if self.n > 0:
            for _ in range(self.n):
                func_name = self.rand_func_name()
                input_params = self.rand_params()
                output_name = self.rand_param_name()
                self.function_string_list.append(self.print_func(func_name, input_params, output_name))
        return self.function_string_list

    def assertion_string(self, test_string, output_string):
        if test_string == ' is not ' and output_string == 'False':
            assert_string = 'assertTrue'
        elif test_string == ' is not ' and output_string == 'True':
            assert_string = 'assertFalse'
        elif test_string == ' is ' and output_string == 'False':
            assert_string = 'assertFalse'
        elif test_string == ' is ' and output_string == 'True':
            assert_string = 'assertTrue'
        elif test_string == ' is not ' and re.match(r'\d+', output_string):
            assert_string = 'assertNotEqual'
        elif test_string == ' is ' and re.match(r'\d+', output_string):
            assert_string = 'assertEqual'
        elif test_string == ' != ' and output_string == 'False':
            assert_string = 'assertTrue'
        elif test_string == ' != ' and output_string == 'True':
            assert_string = 'assertFalse'
        elif test_string == ' = ' and output_string == 'False':
            assert_string = 'assertFalse'
        elif test_string == ' = ' and output_string == 'True':
            assert_string = 'assertTrue'
        elif test_string == ' != ' and re.match(r'\d+', output_string):
            assert_string = 'assertNotEqual'
        elif test_string == ' = ' and re.match(r'\d+', output_string):
            assert_string = 'assertEqual'
        else:
            assert_string = None
        return assert_string

    def test_function_string(self, func_name_string, test_string, in_string, output_string, space='    '):
        assertion = self.assertion_string(test_string, output_string)
        s = '\n\n'+space+'def test_'+func_name_string+'(self):\n'
        s += space+space+'self.'
        s += assertion
        s += '(' +func_name_string+'('+in_string+')'
        if (assertion == 'assertEqual') or (assertion == 'assertNotEqual'):
            s += ','+output_string
        s += ')'
        return s

    def generate_test_functions(self):
        for func_string in self.function_string_list:
            # function_name
            func_name_string = re.search(r"^\s+:test:\s+(\w+)", func_string, re.MULTILINE).group(1)
            # inputs
            in_string = re.search(r"^\s+:test:\s+\w+\((.*)\)", func_string, re.MULTILINE).group(1)
            # output
            output_string = re.search(r"^\s+:test:\s+.*\s+(\w+|\d+)$", func_string, re.MULTILINE).group(1)
            # test function
            test_string = re.search(r"^\s+:test:\s+.*\)(\s+[\w!= ]+\s+){1,2}\w+$", func_string, re.MULTILINE).group(1)
            self.test_function_string_list.append(self.test_function_string(func_name_string, test_string, in_string, output_string))
        return self.test_function_string_list

    def write(self):
        with open('source.py','w') as f:
            f.writelines(self.function_string_list)
        with open('test.py', 'w') as f:
            f.write("from source import *\nimport unittest\n\nclass Test_source(unittest.TestCase):\n")
            f.writelines(self.test_function_string_list)
            f.write('\nif __name__=="__main__":\n    unittest.main()')

if __name__ == '__main__':
    gf = GenerateFunctions(100)
    gf.generate_functions()
    gf.generate_test_functions()
    gf.write()