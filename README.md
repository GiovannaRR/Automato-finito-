﻿# Automato-finito
 import json
import csv
import time

class AutomatoNFA:
    def __init__(self, transitions):
        self.transitions = transitions
        self.current_states = set()

    def operation(self, input_str):
        Inicializa o conjunto de estados atuais com o estado inicial (0)
        self.current_states = set([0])
        Processa cada caractere da entrada
        for char in input_str:
            self.step(char)  #Atualiza os estados atuais com base na transição para o caractere
        Verifica se algum dos estados atuais é um estado final
        return 1 if any(state in self.transitions['final'] for state in self.current_states) else 0

    def step(self, char):
        next_states = set()
        Para cada estado atual, encontra as próximas transições possíveis para o caractere
        for state in self.current_states:
            for transition in self.transitions['transitions']:
                Verifica se a transição é válida para o estado atual e o caractere atual
                if transition['from'] == str(state) and (transition['read'] == char or transition['read'] is None):
                    next_states.add(int(transition['to']))  # Adiciona o próximo estado
        self.current_states = next_states  # Atualiza o conjunto de estados atuais

def automata_file(file_path):
    try:
        Lê o arquivo JSON e retorna os dados do autômato
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
        Lê o arquivo CSV e extrai os casos de teste
        with open(file_path, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            next(csv_reader)  # Ignora o cabeçalho
            for row in csv_reader:
                input_str = row[0]  # Entrada do caso de teste
                expected_result = int(row[1])  # Resultado esperado
                test_cases.append((input_str, expected_result))  # Adiciona o caso de teste à lista
        return test_cases
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado.")
        return []
    except csv.Error:
        print(f"Erro ao ler o arquivo CSV {file_path}. Verifique o formato.")
        return []

def main():
    Caminhos dos arquivos de entrada
    file_aut_path = 'ex1/ex1.json'  # Arquivo JSON com a definição do autômato
    file_teste_path = 'ex1/ex1_input.csv'  # Arquivo CSV com os casos de teste

    Cria uma instância do autômato com base no arquivo JSON
    automata = AutomatoNFA(automata_file(file_aut_path))
    Obtém os casos de teste do arquivo CSV
    case_test = cases(file_teste_path)

    Para cada caso de teste, executa o autômato e mede o tempo de execução
    for str_in_input, expected_result in case_test:
        start_time = time.perf_counter()  # Marca o início da execução
        result = automata.operation(str_in_input)  # Executa o autômato com a entrada atual
        end_time = time.perf_counter()  # Marca o final da execução

        execution_time = "{:.5f}".format(end_time - start_time)  # Calcula o tempo de execução
        Imprime o resultado do teste, o tempo de execução e a entrada
        print(f"Entrada: {str_in_input} - Resultado obtido: {result} - Tempo de execução: {execution_time} segundos")

if __name__ == "__main__":
    main()


Em um teste as entradas foram:

ba;1
aaaabbbbbaaaaa;1
abababab;0
bbbbbbbb;0
aaaaaaaaaaaa;0
aaaaabaaaaa;1

As saidas esperadas são representadas po 1 e 0

as saidas obtidas foram:
obs: as saidas estão com bugs!!

Entrada: aaaabbbbbaaaaa - Resultado obtido: 1 - Tempo de execução: 0.00006 segundos
Entrada: abababab - Resultado obtido: 0 - Tempo de execução: 0.00003 segundos
Entrada: bbbbbbbb - Resultado obtido: 0 - Tempo de execução: 0.00003 segundos
Entrada: aaaaaaaaaaaa - Resultado obtido: 0 - Tempo de execução: 0.00004 segundos
Entrada: aaaaabaaaaa - Resultado obtido: 1 - Tempo de execução: 0.00005 segundos



