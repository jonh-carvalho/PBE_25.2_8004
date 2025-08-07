---
id: as
title: Avaliação Substitutiva(AS)
---

# **Desenvolvimento de API REST com Django + Metodologia RUP/UP**

**Tema: "FitLife — Plataforma de Treinos e Bem-Estar"**

**Tempo de Avaliação: (3h 40min)**

---

# **Fases da Avaliação**

## **0. Configuração Inicial (30 minutos)**

**Objetivo:** Preparar o ambiente de desenvolvimento, repositório GitHub e documentação online.

### **Atividades:**

* Clonar o repositório inicial fornecido pelo avaliador (repositório start no GitHub).
    * [repositório start](https://github.com/jonh-carvalho/PBE_25.1_8002_AS) - Convite enviado para ser um colaborador do repositório.

* Configurar ambiente de desenvolvimento local:
    * Python + Virtualenv
    * Instalação das dependências do projeto

* Criar um **site de documentação usando MkDocs** 'mkdocs new .'

    * Página inicial descrevendo o projeto.
    * Publicar a documentação no GitHub Pages 'mkdocs gh-deploy'

* Configurar o **GitHub Project** (Kanban):

    * Colunas sugeridas: `Backlog`, `Em desenvolvimento`,  `Concluído`.
  
* Criar **Issues no GitHub** para cada tarefa relevante:

    * Modelagem
    * Implementação de cada entidade (models, serializers, views)
    * Configuração do Swagger
    * Documentação, etc.

* Associar cada Issue às etapas no GitHub Projects.

### **Entregáveis:**

* Repositório GitHub atualizado com Issues criadas.
* Site da documentação (MkDocs via GitHub Pages).
* GitHub Projects com tarefas.

---

## **1. Concepção (30 minutos)**

**Objetivo:** Compreender o problema, definir requisitos e mapear os atores.

### **Atividades:**

* Descrição do problema (documentar no MkDocs).
* Lista de requisitos funcionais e não funcionais.
* Atores principais:

    * Usuário
    * Sistema

* Descrição textual de 3 casos de uso.
* (Opcional) Diagrama de caso de uso.

### **Entregáveis:**

* Documento no MkDocs: `docs/_Iniciação/5w2h.md`, `docs/_Iniciação/DesignThinking.md2`.

---

## **2. Elaboração (50 minutos)**

**Objetivo:** Planejar o desenvolvimento, modelar dados e definir a arquitetura da API.

### **Atividades:**

* Diagrama de Classes (PlantUML).
* Definir principais endpoints da API.
* Relacionamentos entre entidades:

    * Usuário → Playlist
    * Playlist → Treino → Exercícios

* Documentar arquitetura no MkDocs.

### **Entregáveis:**

* Documento no MkDocs: `docs/__Elaboração/index.md`.
* Diagrama de classes. `docs/__Elaboração/Diagramas/Classes/diagrama_de_classes.md`.

---

## **3. Construção (1 hora e 40 minutos)**

**Objetivo:** Implementar a API Django REST.

### **Atividades:**

* Criar models no Django.
* Criar serializers.
* Criar views e routers.
* Configurar Django Admin.
* Instalar e Documentar endpoints no Swagger.
* Comitar e referenciar as Issues no GitHub.

### **Entregáveis:**

* Código no GitHub.
* Endpoints funcionando localmente.
* Documentação Swagger gerada automaticamente.

---

## **4. Transição (10 minutos)**

**Objetivo:** Testar, documentar e preparar para entrega.

### **Atividades:**

* Testar todos os endpoints.
* Atualizar documentação no MkDocs:

    * Guia de uso da API.
    * Endpoints principais.

* Checklist de funcionalidades concluído.
* Preparar README final no repositório.

### **Entregáveis:**

* Site MkDocs atualizado.
* Código no GitHub com README.
* Checklist preenchido.

---

## **Modelo de Checklist Geral de Entrega**

| Item                              | Obrigatório | Entregue |
| --------------------------------- | ----------- | -------- |
| Ambiente de desenvolvimento OK    | ✔️          | ⬜        |
| Clone do repositório inicial      | ✔️          | ⬜        |
| GitHub Project configurado        | ✔️          | ⬜        |
| Issues criadas e usadas           | ✔️          | ⬜        |
| Site MkDocs publicado             | ✔️          | ⬜        |
| Descrição do problema             | ✔️          | ⬜        |
| Requisitos funcionais e não func. | ✔️          | ⬜        |
| Casos de uso                      | ✔️          | ⬜        |
| Diagrama de Classes               | ✔️          | ⬜        |
| Definição dos endpoints           | ✔️          | ⬜        |
| Models implementados              | ✔️          | ⬜        |
| Serializers implementados         | ✔️          | ⬜        |
| Views e URLs                      | ✔️          | ⬜        |
| Admin configurado                 | ✔️          | ⬜        |
| Swagger funcionando               | ✔️          | ⬜        |
| README completo                   | ✔️          | ⬜        |

---
