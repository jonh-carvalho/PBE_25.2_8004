# Tema para Dojo de Python: **Calculadora de Notação Polonesa Reversa (RPN)**

## Conceito Introdutório:
A Notação Polonesa Reversa (RPN) é um método de representação de expressões matemáticas onde os operadores seguem os operandos. É ideal para aprender TDD e Baby Steps porque:

1. ✅ Problema bem definido com requisitos claros
2. ✅ Permite implementação incremental
3. ✅ Fácil de testar com casos simples
4. ✅ Boa para praticar estrutura de dados (pilha)

## Problema:
Implementar uma calculadora RPN que processe expressões como: `"3 4 +"` → `7` ou `"5 1 2 + 4 * + 3 -"` → `14`

## Estrutura do Dojo (90 minutos):

### 1. **Aquecimento (10 min)**
- Explicação do problema RPN
- Demonstração de exemplo: `"2 3 +"` = `5`
- Discussão sobre pilha LIFO

### 2. **Primeiro Ciclo TDD (15 min)**
**Teste 1 - Caso mais simples:**
```python
def test_soma_simples():
    assert calcular_rpn("2 3 +") == 5
```

**Baby Step 1 - Implementação mínima:**
```python
def calcular_rpn(expressao):
    return 5  # Implementação mais simples possível
```

### 3. **Segundo Ciclo (15 min)**
**Teste 2 - Adicionando outro operador:**
```python
def test_subtracao():
    assert calcular_rpn("5 3 -") == 2
```

**Baby Step 2:**
```python
def calcular_rpn(expressao):
    if "+" in expressao:
        return 5
    elif "-" in expressao:
        return 2
```

### 4. **Terceiro Ciclo (15 min)**
**Teste 3 - Múltiplas operações:**
```python
def test_multiplas_operacoes():
    assert calcular_rpn("2 3 + 4 *") == 20  # (2+3)*4
```

**Baby Step 3 - Implementar pilha:**
```python
def calcular_rpn(expressao):
    pilha = []
    tokens = expressao.split()
    
    for token in tokens:
        if token == "+":
            b = pilha.pop()
            a = pilha.pop()
            pilha.append(a + b)
        elif token == "-":
            b = pilha.pop()
            a = pilha.pop()
            pilha.append(a - b)
        elif token == "*":
            b = pilha.pop()
            a = pilha.pop()
            pilha.append(a * b)
        else:
            pilha.append(int(token))
    
    return pilha[0]
```

### 5. **Ciclos Adicionais (20 min)**
- Adicionar divisão
- Tratar números decimais
- Lidar com erro (pilha vazia, divisão por zero)
- Expressões mais complexas

### 6. **Retrospectiva (15 min)**
- O que aprendemos sobre TDD?
- Como os baby steps ajudaram?
- Quais desafios encontramos?

## Regras do Dojo:
- 🚫 Não pular etapas
- ✅ Sempre escrever o teste primeiro
- 🔄 Ciclos curtos (teste → implementação → refatoração)
- 👥 Pair programming rotativo

## Exemplos de Testes para Expandir:
```python
def test_divisao():
    assert calcular_rpn("6 2 /") == 3

def test_expressao_complexa():
    assert calcular_rpn("5 1 2 + 4 * + 3 -") == 14

def test_numero_decimal():
    assert calcular_rpn("3.5 2.5 +") == 6.0

def test_erro_divisao_zero():
    with pytest.raises(ValueError):
        calcular_rpn("5 0 /")
```

Este tema é excelente para iniciantes porque começa super simples e gradualmente introduz conceitos mais complexos, sempre mantendo os baby steps! 🐍🚀