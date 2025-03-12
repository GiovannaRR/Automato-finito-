# Autômato Finito Não Determinístico (NFA)

Este projeto implementa uma classe `NFA` em Python que simula um **Autômato Finito Não Determinístico (NFA)**, utilizado para processar cadeias de entrada e verificar se pertencem à linguagem definida pelo autômato.

## Funcionalidades

- **Carregar Autômatos a partir de Arquivos JSON**: Define estados e transições do autômato.
- **Ler Casos de Teste de Arquivos CSV**: Contém as cadeias de entrada e seus respectivos resultados esperados.
- **Processar Entradas**: Verifica se as cadeias de entrada são aceitas ou rejeitadas com base no autômato carregado.
- **Medir o Tempo de Execução**: Exibe o tempo de execução para cada análise.

## Sobre o Projeto

Este projeto permite carregar um autômato de um arquivo JSON e testar várias cadeias de entrada definidas em um arquivo CSV. O autômato processa cada entrada e retorna o resultado da aceitação, além de exibir o tempo de execução da análise.

## Arquivos Utilizados

O projeto depende de dois arquivos principais para funcionar corretamente:

1. **`ex1.json`**: Este arquivo define os estados e as transições do autômato. Ele descreve o autômato em termos dos estados e transições entre eles. Um exemplo de conteúdo deste arquivo seria o seguinte:

    ```json
    {
      "estados_iniciais": ["q0"],
      "estados_finais": ["q3"],
      "transicoes": {
        "q0": {"a": ["q0", "q1"], "b": ["q0"]},
        "q1": {"a": ["q2"], "b": ["q0"]},
        "q2": {"a": ["q2"], "b": ["q3"]},
        "q3": {}
      }
    }
    ```

2. **`ex1_input.csv`**: Este arquivo contém as cadeias de entrada que serão processadas pelo autômato, juntamente com os resultados esperados (1 para aceitação e 0 para rejeição). Um exemplo de conteúdo deste arquivo seria o seguinte:

    ```csv
    aaaabbbbbaaaaa,1
    abababab,0
    bbbbbbbb,0
    aaaaaaaaaaaa,0
    aaaaabaaaaa,1
    ```

# Exemplo de Uso

```python
import time
import json
import csv

# Carregar o autômato do arquivo JSON
with open("ex1.json", "r") as f:
    nfa_data = json.load(f)

nfa = NFA(nfa_data)

# Processar os casos de teste a partir do arquivo CSV
with open("ex1_input.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        entrada, resultado_esperado = row
        start_time = time.time()
        
        # Verificar se a entrada é aceita pelo autômato
        resultado_obtido = nfa.processar(entrada)
        
        end_time = time.time()
        tempo_execucao = end_time - start_time
        
        print(f"Entrada: {entrada} - Resultado obtido: {resultado_obtido} - Tempo de execução: {tempo_execucao:.5f} segundos")
```

# Estrutura do Projeto

- Carregar o Autômato: O autômato é carregado de um arquivo JSON que define os estados iniciais, finais e as transições.
- Carregar os Casos de Teste: Os casos de teste são carregados de um arquivo CSV contendo cadeias de entrada e seus respectivos resultados esperados.
- Processar as Entradas: O autômato verifica se as entradas são aceitas ou rejeitadas.
- Exibir os Resultados: Para cada entrada, o programa exibe a entrada, o resultado obtido e o tempo de execução.

# Exemplo de Saída do Programa

```python
    Entrada: aaaabbbbbaaaaa - Resultado obtido: 1 - Tempo de execução: 0.00006 segundos
    Entrada: abababab - Resultado obtido: 0 - Tempo de execução: 0.00003 segundos
    Entrada: bbbbbbbb - Resultado obtido: 0 - Tempo de execução: 0.00003 segundos
    Entrada: aaaaaaaaaaaa - Resultado obtido: 0 - Tempo de execução: 0.00004 segundos
    Entrada: aaaaabaaaaa - Resultado obtido: 1 - Tempo de execução: 0.00005 segundos
```
# Problemas Conhecidos

- Bugs nas Transições e Estados: O programa pode não lidar corretamente com alguns estados e transições, causando falhas na análise de cadeias.
- Melhorias Necessárias: A revisão das transições e estados iniciais pode corrigir alguns problemas conhecidos.
