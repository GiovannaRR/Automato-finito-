import json
import csv
import time

class AutomatoNFA:
    def __init__(self, transitions):
        self.transitions = transitions
        self.current_states = set()

    def operation(self, input_str):
        self.current_states = set([0])
        for char in input_str:
            self.step(char)
        return 1 if any(state in self.transitions['final'] for state in self.current_states) else 0

    def step(self, char):
        next_states = set()
        for state in self.current_states:
            for transition in self.transitions['transitions']:
                if transition['from'] == str(state) and (transition['read'] == char or transition['read'] is None):
                    next_states.add(int(transition['to']))
        self.current_states = next_states

def automata_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            automaton_data = json.load(json_file)
        return automaton_data
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo JSON {file_path}. Verifique o formato.")
        return None

def cases(file_path):
    test_cases = []
    try:
        with open(file_path, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            next(csv_reader) 
            for row in csv_reader:
                input_str = row[0]
                expected_result = int(row[1])
                test_cases.append((input_str, expected_result))
        return test_cases
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado.")
        return []
    except csv.Error:
        print(f"Erro ao ler o arquivo CSV {file_path}. Verifique o formato.")
        return []

def main():
    file_aut_path = 'ex1/ex1.json'
    file_teste_path = 'ex1/ex1_input.csv'

    automata = AutomatoNFA(automata_file(file_aut_path))
    case_test = cases(file_teste_path)

    for str_in_input, expected_result in case_test:
        start_time = time.perf_counter()
        result = automata.operation(str_in_input)
        end_time = time.perf_counter()

        execution_time = "{:.5f}".format(end_time - start_time) 
        print(f"Entrada: {str_in_input} - Resultado obtido: {result} - Tempo de execução: {execution_time} segundos")

if __name__ == "__main__":
    main()
