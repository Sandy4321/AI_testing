from test_function_generator import GenerateFunctions
import re
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, concatenate

class UnitTestGenerator():
    def __init__(self, data, targets):
        self.test_names, self.fn_signatures, self.intents, self.expected_results = self.parse_intents(data)
        self.assertions, self.optional_results = self.parse_targets(targets)

        self.intent_dict = {x: i for i, x in enumerate(sorted(list(set(self.intents))))}
        self.assertion_dict = {x: i for i, x in enumerate(sorted(list(set(self.assertions))))}
        self.rev_assertion_dict = {i: x for i, x in enumerate(sorted(list(set(self.assertions))))}


        self.inputs_data, self.optional_input = self.one_hot_encoding_inputs(self.intents, self.expected_results)
        self.output_data, self.optional_output = self.one_hot_encoding_targets(self.assertions, self.optional_results)


    def parse_intents(self, data):
        function_signature = []
        function_name = []
        intent = []
        expected_result = []
        for line in data:
            s = re.search(r'^\s+:test: (\w+\(.*\)) (.*) (\w+|\d+)$', line, re.MULTILINE)
            function_signature.append(s.group(1))
            function_name.append(s.group(1).split('(')[0])
            intent.append(s.group(2))
            expected_result.append(s.group(3))
        return function_name, function_signature, intent, expected_result

    def parse_targets(self, targets):
        assertion = []
        optional_result = []
        for line in targets:
            a = re.search(r'^\s+self.(\w+)\(.*\)(.*)\)$', line, re.MULTILINE)
            assertion.append(a.group(1))
            optional_result.append(a.group(2))
        return assertion, optional_result

    def encode_expected_results(self, expected_results):
        bin_target = []
        for line in expected_results:
            try:
                int(line)
                bin_target.append(1)
            except ValueError:
                bin_target.append(line)
        return bin_target

    def one_hot_encoding_inputs(self, intents, expected_results):
        er = self.encode_expected_results(expected_results)
        exp_res = np.zeros((len(intents), 3), dtype='float32')
        for i, line in enumerate(er):
            if line == 1:
                exp_res[i, 0] = 1.
            elif line == 'True':
                exp_res[i, 1] = 1.
            elif line == 'False':
                exp_res[i, 2] = 1.

        ohe = np.zeros((len(intents), len(self.intent_dict)), dtype='float32')
        for i, x in enumerate(intents):
            ohe[i, self.intent_dict[x]] = 1.
        return ohe, exp_res

    def one_hot_encoding_targets(self, assertions, optional_results):
        opt_res = np.array([1. if x else 0. for x in optional_results], dtype='float32')
        ohe = np.zeros((len(assertions), len(self.assertion_dict)), dtype='float32')
        for i, a in enumerate(assertions):
            ohe[i, self.assertion_dict[a]] = 1.
        return ohe, opt_res

    def training(self, epochs=100, batchsize=8, lw=[1., .2]):
        main_input = Input(shape=(4,), name='main_input')
        aux_input = Input(shape=(3,), name='aux_input')
        x = concatenate([main_input, aux_input])
        x = Dense(32, activation='relu')(x)
        x = Dense(32, activation='relu')(x)
        x = Dense(32, activation='relu')(x)
        main_output = Dense(4, activation='sigmoid', name='main_output')(x)
        aux_output = Dense(1, activation='sigmoid', name='aux_output')(x)
        self.model = Model(inputs=[main_input, aux_input], outputs=[main_output, aux_output])

        self.model.compile(optimizer='rmsprop',
                      loss='binary_crossentropy',
                      loss_weights=lw,
                      metrics=['acc'])
        self.model.fit([self.inputs_data, self.optional_input], [self.output_data, self.optional_output],
          epochs=epochs,
          batch_size=batchsize,
          validation_split=0.2)

    def predict(self, text):
        t_name, fn_sign, intent, exp_res = self.parse_intents([text])
        in_data, opt_in = self.one_hot_encoding_inputs(intent, exp_res)
        assertion, option = self.model.predict([in_data, opt_in])
        s = '\n    def test_' + t_name[0] + '(self):\n'
        s += '        self.' +  self.rev_assertion_dict[np.argmax(assertion)] + '('
        s += fn_sign[0]
        s += [', ' + x if np.round(option) else '' for x in exp_res][0] + ')'
        return s

    def batch_predict(self, data, source, test):
        test_function_string_list = [self.predict(x) for x in data]
        with open(source, 'w') as f:
            f.writelines(data)

        with open(test, 'w') as f:
            f.write("from source import *\nimport unittest\n\nclass Test_source(unittest.TestCase):\n")
            f.writelines(test_function_string_list)
            f.write('\nif __name__=="__main__":\n    unittest.main()')
