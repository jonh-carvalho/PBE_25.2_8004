# Especificação de Requisitos

## 1. Introdução
Descreve o objetivo do documento, escopo do sistema e definições importantes.

## 2. Visão Geral do Sistema
Apresenta uma visão geral do sistema, contexto, principais funcionalidades e restrições.

## 3. Requisitos Funcionais
Lista e detalha os requisitos funcionais, agrupados por módulos ou funcionalidades.

### Exemplo
### RF01 - Cadastro de Usuário

O sistema deve permitir que novos usuários realizem seu cadastro informando nome, e-mail, senha e perfil de acesso. Após o cadastro, o usuário receberá um e-mail de confirmação para ativar sua conta.

## 4. Requisitos Não Funcionais
Especifica requisitos de desempenho, segurança, usabilidade, confiabilidade, entre outros.

### Exemplo
### RNF01 - Segurança

O sistema deve criptografar todas as senhas dos usuários utilizando algoritmo de hash seguro (ex: bcrypt) antes de armazená-las no banco de dados.

## 5. Regras de Negócio
Define regras e políticas que o sistema deve seguir.

Regra de negócio é uma diretriz ou política que define como os processos e operações devem ocorrer dentro de uma organização ou sistema. Ela estabelece restrições, condições e procedimentos que garantem o correto funcionamento do sistema conforme os objetivos e necessidades do negócio, orientando tomadas de decisão e validações durante o desenvolvimento e uso do software.

### Exemplo

### RN01 - Validação de Dados de Cadastro

O sistema deve garantir que o e-mail informado pelo usuário seja único e válido, impedindo o cadastro de contas duplicadas ou com e-mails inválidos.

### RN02 - Recuperação de Senha

O sistema deve permitir que o usuário solicite a recuperação de senha por meio do e-mail cadastrado, enviando um link seguro para redefinição da senha.



### RN02 - Perfil de Acesso

Usuários cadastrados devem ser atribuídos a perfis de acesso (administrador, usuário comum) conforme regras definidas pela organização, limitando funcionalidades disponíveis conforme o perfil.


## 6. Interfaces Externas
Descreve integrações com outros sistemas, APIs, hardware ou bancos de dados.

## 7. Restrições
Lista limitações técnicas, legais ou de negócio.

## 8. Critérios de Aceitação
Define condições para validação dos requisitos e aceitação do sistema.

## 9. Glossário
Explica termos técnicos ou específicos do domínio.

## 10. Referências
Relaciona documentos, normas e materiais utilizados.