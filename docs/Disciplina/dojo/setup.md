# Configurando Ambiente de Testes para Python

Vou te mostrar como configurar um ambiente de testes para Python usando pytest, que é uma das ferramentas mais populares e fáceis de usar.

## 1. Configuração Básica

### Instalação do pytest
```bash
pip install pytest
```

### Estrutura de arquivos
```
projeto_rpn/
├── calculadora_rpn.py   # Nosso código principal
├── test_calculadora.py  # Nossos testes
└── requirements.txt     # Dependências do projeto
```

## 2. Configuração do requirements.txt
```
pytest==7.4.0
```

## 3. Escrevendo nosso primeiro teste

### test_calculadora.py
```python
import pytest
from calculadora_rpn import calcular_rpn

def test_soma_simples():
    """Teste mais simples: soma de dois números"""
    assert calcular_rpn("2 3 +") == 5

def test_subtracao():
    """Teste de subtração"""
    assert calcular_rpn("5 3 -") == 2

def test_expressao_vazia():
    """Teste com expressão vazia"""
    assert calcular_rpn("") == 0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

### calculadora_rpn.py (implementação inicial)
```python
def calcular_rpn(expressao):
    """
    Calculadora de Notação Polonesa Reversa (RPN)
    
    Args:
        expressao (str): Expressão matemática em RPN (ex: "2 3 +")
    
    Returns:
        int/float: Resultado do cálculo
    """
    if not expressao.strip():
        return 0
    
    # Implementação mínima para passar no primeiro teste
    return 5
```

## 4. Executando os testes

### Opção 1: Pela linha de comando
```bash
# Executar todos os testes
pytest

# Executar com detalhes
pytest -v

# Executar um arquivo específico
pytest test_calculadora.py

# Executar um teste específico
pytest test_calculadora.py::test_soma_simples -v
```

### Opção 2: Pelo próprio arquivo de testes
```bash
python test_calculadora.py
```

### Opção 3: Configurando no IDE (VS Code)
1. Instale a extensão Python
2. Crie uma pasta `.vscode` no seu projeto
3. Crie o arquivo `.vscode/settings.json`:
```json
{
    "python.testing.pytestArgs": [
        "."
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```

## 5. Configuração Avançada (opcional)

### pytest.ini (configurações personalizadas)
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
```

### .coveragerc (para análise de cobertura)
```ini
[run]
source = .
omit = tests/*, venv/*

[report]
show_missing = true
fail_under = 80
```

### Executando com cobertura
```bash
pip install pytest-cov
pytest --cov=calculadora_rpn --cov-report=html
```

## 6. Exemplo de Desenvolvimento com Baby Steps

### Primeiro ciclo: fazer o primeiro teste passar
```python
# calculadora_rpn.py (após primeiro ciclo)
def calcular_rpn(expressao):
    if not expressao.strip():
        return 0
    
    # Implementação específica para o primeiro teste
    if expressao == "2 3 +":
        return 5
    
    return 0
```

### Segundo ciclo: generalizar a implementação
```python
# calculadora_rpn.py (após segundo ciclo)
def calcular_rpn(expressao):
    if not expressao.strip():
        return 0
    
    pilha = []
    tokens = expressao.split()
    
    for token in tokens:
        if token == "+":
            b = pilha.pop()
            a = pilha.pop()
            pilha.append(a + b)
        else:
            pilha.append(int(token))
    
    return pilha[0] if pilha else 0
```

## 7. Dicas para o Dojo

1. **Mantenha os testes visíveis**: Use um projetor ou compartilhamento de tela
2. **Rotação de pares**: A cada 5-7 minutos, troque quem está digitando
3. **Siga estritamente o TDD**: 
   - Vermelho (teste falha)
   - Verde (implementação mínima)
   - Refatoração (melhorar o código)
4. **Comemore os pequenos sucessos**: Cada teste que passa é uma vitória!

Este setup é simples mas eficaz para dojos, permitindo que o foco fique na prática do TDD e baby steps rather than na complexidade da configuração. 🐍🧪