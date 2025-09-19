# Processo de Pair Programming e TDD no Dojo

## Pair Programming (Programação em Pares)

### O que é:

Duas pessoas trabalhando juntas em uma única estação de trabalho:

- **Piloto (Driver)**: Quem digita o código
- **Co-piloto (Navigator)**: Quem guia, revisa e pensa estrategicamente

### Como funciona a rotação:

**Tempo**: A cada 5-7 minutos (ou após cada teste passar)
**Sistema de rotação**:

```
Round 1: Pessoa A → Piloto, Pessoa B → Co-piloto
Round 2: Pessoa B → Piloto, Pessoa C → Co-piloto  
Round 3: Pessoa C → Piloto, Pessoa A → Co-piloto
```

### Regras básicas:

- ✅ Apenas o piloto toca no teclado
- ✅ Co-piloto foca na estratégia e qualidade
- ✅ Discussão é encorajada, mas decisão final do piloto
- ✅ Respeito mútuo pelas ideias

## 🔴🟢🔁 Processo TDD (Test-Driven Development)

### Ciclo Red-Green-Refactor:

#### 1. 🔴 **RED** - Escrever um teste que falha

```python
def test_multiplicacao_simples():
    assert calcular_rpn("2 3 *") == 6  # Este teste vai falhar inicialmente
```

**Por quê?**: Definimos o comportamento desejado antes da implementação

#### 2. 🟢 **GREEN** - Implementação mínima para passar

```python
def calcular_rpn(expressao):
    # Implementação mais simples possível
    if expressao == "2 3 *":
        return 6
    # ... resto do código existente
```

**Por quê?**: Foco em fazer o teste passar, não em perfeição

#### 3. 🔁 **REFACTOR** - Melhorar o código sem quebrar testes

```python
def calcular_rpn(expressao):
    # Refatoração: generalizar a multiplicação
    pilha = []
    for token in expressao.split():
        if token == "*":
            b, a = pilha.pop(), pilha.pop()
            pilha.append(a * b)
        else:
            pilha.append(int(token))
    return pilha[0]
```

**Por quê?**: Melhorar a qualidade mantendo a funcionalidade

## 🎯 Fluxo Completo do Dojo

### Pré-dojo:

1. Configurar ambiente (VS Code + pytest)
2. Explicar o problema (Calculadora RPN)
3. Formar pares iniciais

### Durante o dojo:

```
┌─────────────────────────────────────────────────┐
│ 1. ESCREVER TESTE (RED) - Co-piloto sugere      │
│    - Novo teste deve falhar                     │
│    - Foco em um requisito de cada vez           │
├─────────────────────────────────────────────────┤
│ 2. IMPLEMENTAR (GREEN) - Piloto codifica        │
│    - Implementação mais simples possível        │
│    - "Cheat" permitido para fazer teste passar  │
├─────────────────────────────────────────────────┤
│ 3. TESTAR - Ambos verificam                     │
│    - pytest deve mostrar verde                  │
│    - Celebrar! 🎉                               │
├─────────────────────────────────────────────────┤
│ 4. REFATORAR (REFACTOR) - Co-piloto guia        │
│    - Melhorar código sem quebrar testes         │
│    - Remover duplicação, melhorar legibilidade  │
├─────────────────────────────────────────────────┤
│ 5. ROTACIONAR - Trocar papéis                   │
│    - Novo piloto → teclado                      │
│    - Novo co-piloto → estratégia                │
└─────────────────────────────────────────────────┘
```

## 💡 Papéis em Cada Fase

### **Piloto (Driver)**:

- ✍️ Escreve o código
- 🎯 Foca no "como" implementar
- ⚡ Mantém o ritmo
- ✅ Garante que testes passem

### **Co-piloto (Navigator)**:

- 🧭 Pensa no "o quê" e "por quê"
- 🔍 Revise o código em tempo real
- 🚨 Identifica possíveis problemas
- 📝 Sugere próximos passos

## 🎪 Exemplo Prático de um Ciclo

### Round 1:

**Co-piloto**: "Vamos testar a multiplicação: `2 3 *` deve retornar 6"
**Piloto**: Escreve o teste que falha

```python
def test_multiplicacao():
    assert calcular_rpn("2 3 *") == 6  # 🔴 FALHA
```

### Round 2:

**Piloto**: Implementa solução mínima

```python
def calcular_rpn(expressao):
    if expressao == "2 3 *":
        return 6  # 🟢 FUNCIONA (mas é trapaça!)
    # ... código existente
```

### Round 3:

**Co-piloto**: "Agora vamos generalizar para qualquer multiplicação"
**Piloto**: Refatora para implementação correta

```python
def calcular_rpn(expressao):
    pilha = []
    for token in expressao.split():
        if token == "*":
            b, a = pilha.pop(), pilha.pop()
            pilha.append(a * b)  # 🟢✅ FUNCIONA GENERALIZADO
        else:
            pilha.append(int(token))
    return pilha[0]
```

## 🚨 Regras de Ouro

1. **Nunca escrever código sem teste falhando primeiro**
2. **Rotação frequente (5-7 min)**
3. **Celebrar cada teste que passa** 🎉
4. **Respeitar o par atual - sem interferência da plateia**
5. **Baby steps: um pequeno passo de cada vez**

## 🏆 Benefícios desta Abordagem

- **🎓 Aprendizado coletivo**: Todos participam e aprendem
- **🔍 Qualidade**: Dois pares de olhos veem mais que um
- **💡 Criatividade**: Diferentes perspectivas trazem soluções inovadoras
- **🚀 Velocidade**: Menos bugs, menos retrabalho

Este processo transforma a programação de uma atividade solitária em uma experiência colaborativa e de alto aprendizado! 🤝✨