# Workflow BDL v0.5 - O Estúdio de Escrita Completo

Esta é uma demonstração completa e o manual de operação do **Book Development Lifecycle**. O documento começa apresentando um exemplo prático completo da **v0.4** e, em seguida, detalha a evolução para a **v0.5**, que introduz governança, coesão e um pipeline de entrega contínua.

---

## Parte 1: BDL v0.4 - Exemplo Prático em Ação

Esta seção demonstra o fluxo de trabalho do **Book Development Lifecycle v0.4**, com rastreamento de feedback, métricas de progresso e integração com leitores externos.

### Configuração Inicial

#### Setup do Ambiente

**Ação**: Ativação do @agente construtor para configurar o projeto

Você executa o construtor de projeto:

**Construtor de Projeto**:

```text
🏗️ Construtor de Projeto BDL v0.4

Vou criar o seu estúdio de escrita completo com toda a estrutura 
necessária para o Book Development Lifecycle...

[Executa automaticamente todos os comandos de setup]

🎉 Seu Estúdio de Escrita BDL v0.4 Foi Criado com Sucesso!
Próximo passo: Personalize constitution.md com suas diretrizes
```

#### Personalização das Leis do Universo

**Ação**: Configuração do `constitution.md` e lore inicial

Exemplo de Constitution.md Personalizada:

##### Informações Básicas

- **Título**: As Crônicas de Aethermoor
- **Gênero**: Fantasia Épica
- **Tom**: Misterioso e melancólico

##### Diretrizes de Escrita

- **POV**: Terceira pessoa limitada
- **Atmosfera**: Sempre presente, rica em detalhes sensoriais
- **Diálogos**: Naturais, revelam personalidade

##### Temas Centrais

1. Consequências de escolhas do passado
2. Redenção através do sacrifício
3. O peso da memória coletiva

**Criação de Lore Base**:

- `lore/personagens/elara.md` - Protagonista principal
- `lore/locais/floresta-cinzenta.md` - Cenário inicial
- `lore/conceitos/visoes-ancestrais.md` - Sistema mágico

### Fase 1: Criação do Rascunho

#### Escrita Humana Inicial

**Arquivo**: `capitulos/rascunhos/01_rascunho.md`

```markdown
## Capítulo 01 - O Primeiro Eco

### Abertura
Elara entra na Floresta Cinzenta ao entardecer. Ela está procurando 
pistas sobre o desaparecimento de sua irmã. A atmosfera deve ser 
tensa e misteriosa.

### Desenvolvimento
- Ela explora cautelosamente, notando sinais estranhos
- Encontra um altar antigo coberto de runas
- Hesita, mas toca num medalhão que está sobre o altar
- O medalhão ativa uma visão do passado

### Climax
A visão mostra uma batalha antiga no mesmo local. Ela vê guerreiros
com armaduras familiares - parecem com sua irmã.

### Fechamento
Elara se assusta e solta o medalhão. Ela percebe que não está mais
sozinha na floresta. Algo a observa das sombras.

### Elementos de Lore
- Medalhão das Visões (novo artefato)
- Guerra dos Ecos Perdidos (evento histórico)
- Guardiões Sombrios (possível nova facção)

### Tom Desejado
Melancólico, com crescente tensão. Enfatizar os aspectos sensoriais
da floresta e o impacto emocional da visão em Elara.
```

### Fase 2: Expansão Inicial

#### Comando de Inicialização

```text
Você: /iniciar 01

Editor Chefe:
"Analisando rascunho para extrair contexto de lore necessário...
✓ Identificados: Elara, Floresta Cinzenta, conceitos de visão
✓ Contexto compilado: 3 arquivos de lore relevantes

Invocando @agente escritor para expansão do rascunho..."

Escritor Fantasma:
[Produz texto expandido aplicando os princípios de escrita]

Editor Chefe:
"✅ Capítulo 01 processado. Primeira versão 01a.md pronta para 
revisão em /capitulos/ia/"
```

### Fase 3: Ciclo de Revisão (Aprimorado)

#### Adição de Feedback Humano

**Ação**: Leitura de `01a.md` e inserção de notas de revisão

```markdown
O crepúsculo tingiu a Floresta Cinzenta... {NOTA: Adicionar mais detalhes sobre os sons da floresta - galhos quebrando, vento nas folhas - para aumentar a tensão}

[...]

O medalhão pulsou em suas mãos... {NOTA: A transição para a visão está muito abrupta. Adicionar sensações físicas - tontura, formigamento, etc. - para tornar mais gradual}
```

#### Aplicação das Revisões (com Log Automático)

```text
Você: /revisar 01a

Editor Chefe:
"Analisando feedback e notas para contexto relevante...
✓ Identificadas: 2 notas de revisão
✓ Foco: Atmosfera sonora e transições
✓ **Log de Feedback:** Notas arquivadas em `docs/revisao_tracker.md` para referência futura.

Invocando @agente escritor para aplicar revisões..."

Escritor Fantasma:
[Reescreve seções específicas integrando o feedback]

Editor Chefe:
"✅ Revisão concluída. Nova versão 01b.md pronta para análise."
```

#### **Novo Artefato:** Rastreamento de Feedback

O sistema agora mantém um registro central de todas as decisões de revisão.

**Arquivo gerado**: `docs/revisao_tracker.md`

```markdown
# Registro de Revisões do Projeto

## Capítulo 01

### Versão: `01a.md`
- **Nota 1:** Adicionar mais detalhes sobre os sons da floresta - galhos quebrando, vento nas folhas - para aumentar a tensão
- **Nota 2:** A transição para a visão está muito abrupta. Adicionar sensações físicas - tontura, formigamento, etc. - para tornar mais gradual
```

### Fase 4: Análise Crítica (Opcional)

*(O processo é o mesmo: O comando `/criticar` invoca o @agente crítico para uma análise de alto nível.)*

...

### Fase 5: Finalização Automática (com Métricas)

#### Comando de Finalização Completa

```text
Você: /finalizar 01

Editor Chefe:
"🔄 INICIANDO CICLO DE FINALIZAÇÃO AUTOMÁTICA

1️⃣ IDENTIFICAÇÃO E MOVIMENTAÇÃO
✓ Localizada versão mais recente: 01b.md
✓ Movendo para: /capitulos/finalizados/01.md

2️⃣ ARQUIVAMENTO DE LORE
Invocando @agente arquivista em modo catalogação..."
```

#### Processo de Catalogação

O processo de catalogação do Guardião do Lore permanece o mesmo da versão anterior.

...

#### Automação Final

```text
Editor Chefe:
"3️⃣ ATUALIZAÇÃO DO CHANGELOG
✓ Entrada criada para 29/09/2025
✓ Resumo do capítulo adicionado ao topo do arquivo

4️⃣ VERSIONAMENTO AUTOMÁTICO
Executando comandos de limpeza e versionamento...

$ rm -f capitulos/ia/01*.md
✓ Arquivos temporários removidos

$ git add .
✓ Mudanças adicionadas ao controle de versão

$ git commit -m 'feat(capitulo): finaliza o Capítulo 01'
✓ Commit criado com sucesso

$ git push
✓ Alterações enviadas para repositório remoto

🚀 **CAPÍTULO 01 FINALIZADO COM SUCESSO!**

✅ **Ações Completadas:**
• Arquivo movido para /capitulos/finalizados/
• @agente arquivista catalogou 3 novas informações
• CHANGELOG.md atualizado
• Arquivos temporários de IA removidos  
• Commit criado: 'feat(capitulo): finaliza o Capítulo 01'
• Mudanças enviadas para repositório remoto

📊 **Relatório de Métricas do Projeto:**
• **Capítulos Finalizados:** 1 de 20 (estimado)
• **Progresso Total:** 5%
• **Contagem de Palavras (Cap. 01):** 2,158
• **Contagem Total de Palavras:** 2,158
• **Novas Entradas de Lore:** 3

🎬 **Status:** Estúdio pronto para o próximo capítulo."
```

### Variações do Workflow (com Integração Externa)

#### Workflow Simplificado (Rápido)

```text
/iniciar 01 → /finalizar 01
```

#### Workflow Completo (Qualidade Máxima)

```text
/iniciar 01 → /revisar 01a → /revisar 01b → /criticar 01 → /finalizar 01
```

#### Workflow de Desenvolvimento (Experimental)

```text
/iniciar 01 → /criticar 01 → /revisar 01a → /revisar 01b → /finalizar 01
```

#### **Novo:** Workflow Colaborativo (com Leitores Beta)

Este fluxo integra feedback de leitores externos diretamente no processo de análise crítica.

##### Passo 1: Coleta de Feedback

Leitores Beta enviam seus comentários, que são salvos na pasta `/feedback/`.

**Arquivo de Exemplo**: `feedback/beta_reader_ana_cap01.md`

```markdown
# Feedback de Ana - Capítulo 01

**Citação:** "...Elara sentiu o ar frio penetrar através do tecido de sua capa."
**Comentário:** Adorei a atmosfera, mas não ficou claro o quão desesperada Elara está. Talvez uma linha sobre ela não comer há um dia?

**Citação:** "...Ela percebe que não está mais sozinha na floresta."
**Comentário:** O final é ótimo! Arrepiante. Não mude nada aqui.
```

##### Passo 2: Comando de Crítica com Fonte Externa

Você usa uma flag para instruir o @agente crítico a considerar o feedback externo.

```text
Você: /criticar 01 --fonte=beta

Editor Chefe:
"Invocando @agente crítico para análise literária...
✓ **Fonte Adicional:** Carregando notas de feedback da pasta `/feedback/`.
✓ Sintetizando feedback interno e externo..."
```

##### Passo 3: Relatório Crítico Consolidado

O relatório do @agente crítico agora inclui uma seção dedicada ao feedback dos leitores.

```markdown
## Análise Crítica - Capítulo 01 (com Feedback Beta)

[...]

### Feedback Externo Consolidado (Leitores Beta)

- **Ponto Consensual:** A atmosfera da Floresta Cinzenta foi universalmente elogiada.
- **Sugestão Recorrente (de Ana):** A vulnerabilidade de Elara poderia ser mais acentuada no início. A sugestão de mencionar sua exaustão física ou fome é excelente para aumentar as apostas.
- **Ponto a Manter:** O final do capítulo foi considerado impactante e deve ser preservado.
```

**O BDL v0.4 oferece flexibilidade total, mantendo consistência e qualidade profissional, e agora integra rastreamento de decisões, métricas de progresso e colaboração externa.** 🚀

---
---

## Parte 2: Evolução para o BDL v0.5: Governança, Coesão e Entrega Contínua

A versão 0.4 estabeleceu um estúdio funcional. A v0.5 o transforma em uma **plataforma de produção literária profissional e escalável**, adicionando camadas cruciais de governança, validação e gestão de projeto.

### 1. Governança de Estilo (O Guardião do Estilo)

**O Problema:** A `constitution.md` é um guia, mas não há um mecanismo de fiscalização para garantir que o estilo seja seguido.

**A Solução:** Introduzir um novo agente/comando: `/validar-estilo [capitulo]`. Este agente atua como um "linter" de prosa.

**Na Prática:**

```text
Você: /validar-estilo 01

Editor Chefe:
"Invocando o @agente Guardião do Estilo para analisar o Capítulo 01..."

Guardião do Estilo (Relatório):
"📊 **Relatório de Aderência de Estilo - Capítulo 01**

- **POV (Regra: 3ª Pessoa Limitada):** ✅ Consistente.
- **Tom (Regra: Misterioso e melancólico):** ✅ Consistente.
- **Diretrizes Adicionais:**
  - **AVISO:** Foram encontrados 7 advérbios terminados em '-mente'. A constituição sugere moderação.
    - Linha 45: 'rapidamente'
    - Linha 98: 'silenciosamente'
    - ...
  - **SUGESTÃO:** A frase na linha 112 ('Elara pensou que talvez o medalhão fosse perigoso') poderia ser reescrita para 'mostrar' em vez de 'contar', reforçando o POV limitado."
```

### 2. Gestão de Branches / Ambientes

**O Problema:** O versionamento é linear (tudo no `main`), o que não é ideal para colaboração ou experimentação.

**A Solução:** Adotar um fluxo de trabalho Gitflow simplificado (`feature` -> `develop` -> `main`). O `Editor Chefe` agora gerencia os branches.

**Na Prática:**

```text
Você: /iniciar 02

Editor Chefe:
"✅ Criando branch 'feature/capitulo-02' a partir de 'develop' e mudando para ele..."

--- (Após o trabalho no capítulo) ---

Você: /finalizar 02

Editor Chefe:
"...
✅ Commit criado em 'feature/capitulo-02'.
✅ Retornando para o branch 'develop'.
✅ Realizando merge de 'feature/capitulo-02' em 'develop'.
✅ Removendo branch 'feature/capitulo-02'.
O ramo 'develop' está atualizado."
```

### 3. Gerenciamento de Prioridades / Roadmap

**O Problema:** Falta uma visão de alto nível do progresso e das prioridades do projeto.

**A Solução:** Formalizar o uso do `docs/roadmap.md` e integrá-lo ao relatório de métricas no final do comando `/finalizar`.

**Na Prática:**

**Arquivo:** `docs/roadmap.md`

```markdown
# Roadmap - As Crônicas de Aethermoor

| Capítulo | Título Provisório       | Prioridade | Status      |
|----------|-------------------------|------------|-------------|
| 01       | O Primeiro Eco          | Alta       | Finalizado  |
| 02       | A Sombra na Estalagem   | Alta       | Em Rascunho |
| 03       | O Segredo das Runas     | Média      | Pendente    |
```

**Comando `/finalizar` (Saída de Métricas Atualizada):**

```text
Editor Chefe (Relatório de Métricas):
"📊 **Relatório de Métricas do Projeto:**
...
📈 **Progresso do Roadmap:**
- **Concluído:** 1/3 capítulos prioritários (Cap. 01)
- **Em Andamento:** 1 capítulo (Cap. 02)
- **Próximo (Prioridade Alta):** Nenhum.
- **Próximo (Prioridade Média):** Capítulo 03 - O Segredo das Runas"
```

### 4. Controle de Inconsistências Globais

**O Problema:** O Guardião do Lore é bom em adicionar, mas não em validar a consistência do que já existe.

**A Solução:** Introduzir o comando `/validar-coesao`.

**Na Prática:**

```text
Você: /validar-coesao

Editor Chefe:
"Invocando o @agente Guardião da Coesão para uma análise global de todos os capítulos finalizados..."

Guardião da Coesão (Relatório):
"🔎 **Relatório de Coesão Narrativa:**
- **ERRO DE CONTINUIDADE (Grave):** O personagem 'Kael' é mencionado como vivo no `capitulo-05.md`, mas seu registro em `lore/personagens/kael.md` indica que ele morreu no `capitulo-03.md`.
- **INCONSISTÊNCIA DE NOME (Menor):** O nome 'Lyra' aparece como 'Lira' duas vezes no `capitulo-04.md`.
- **VERIFICAÇÃO DE CRONOLOGIA:** ✅ Sem conflitos de data encontrados."
```

### 5. Integração com Compilação Final

**O Problema:** O workflow termina no commit, mas não gera um artefato de leitura.

**A Solução:** Adicionar o comando `/compilar`.

**Na Prática:**

```text
Você: /compilar --formatos=epub,pdf

Editor Chefe:
"Iniciando processo de compilação do manuscrito a partir do branch 'develop'...
✓ Encontrados 5 capítulos em /finalizados.
✓ Compilando para formato ePub...
✓ Compilando para formato PDF...

✅ **Manuscrito Compilado com Sucesso!**
- Arquivos gerados na pasta `/entrega/`:
  - `Aethermoor_v0.5.epub`
  - `Aethermoor_v0.5.pdf`"
```

### 6. Padronização do Feedback Externo

**O Problema:** O feedback dos leitores beta é desestruturado.

**A Solução:** Criar um template de feedback (`feedback/_TEMPLATE.md`) que os leitores devem usar. O `@agente crítico` é otimizado para extrair dados deste formato.

**Na Prática:**

**Arquivo:** `feedback/_TEMPLATE.md`

```markdown
# Feedback sobre [Título do Livro] - Capítulo [Número]
- **Leitor:** [Seu Nome]

## 1. Impressões Gerais (1 a 5 estrelas)
- **Ritmo:** ★★★☆☆
- **Clareza:** ★★★★★
- **Imersão:** ★★★★☆

## 2. Comentário Geral
*O que você mais gostou? O que menos gostou?*

## 3. Feedback Específico por Citação
**Citação:** "[Copie aqui o trecho do texto]"
**Comentário:** [Seu feedback sobre este trecho específico]

**Citação:** "[...]"
**Comentário:** [...]
```

---

## 📘 Manual de Operações: Book Development Lifecycle (BDL) v0.5.1

Este documento é a referência técnica oficial para todos os comandos do **Book Development Lifecycle v0.5.1**. Cada comando é definido com sua finalidade, pré-condições, resultados esperados e tratamento de erros. A padronização da estrutura e das saídas em tabelas Markdown visa garantir um fluxo de trabalho previsível, automatizável e facilmente interpretável por agentes de inteligência artificial.

## Estrutura de Comandos

Cada comando segue um formato padronizado para clareza e consistência:

```markdown
### /comando [parâmetros]

**Descrição:** O que o comando faz.
**Pré-condições:** O que precisa existir antes de executar.
**Pós-condições:** O que muda/é criado depois da execução.
**Artefatos Atualizados:** Arquivos que recebem alterações diretas.
**Erros Possíveis:** Lista de erros e mensagens padronizadas.
**Exemplo de Saída:** Saída esperada em Markdown tabelado para fácil parseamento.
```

---

## 🏛️ Comandos de Configuração e Manutenção

### `/setup-projeto [nome]`

**Descrição:** Inicializa um novo estúdio de escrita com toda a estrutura BDL.
**Pré-condições:** Nenhuma. O comando deve ser executado em um diretório vazio.
**Pós-condições:** Estrutura de pastas criada, `constitution.md` e `roadmap.md` gerados, repositório Git inicializado com branches `main` e `develop`.
**Artefatos Atualizados:**

- `/docs/constitution.md`
- `/docs/roadmap.md`
- Estrutura de pastas `/capitulos`, `/lore`, `/feedback`, `/entrega`
**Erros Possíveis:**
- `❌ Erro: Pasta já contém um projeto BDL inicializado.`

**Exemplo de Saída:**

| Status | Mensagem                                                  |
| :----- | :-------------------------------------------------------- |
| ✅     | Projeto criado com sucesso: **As Crônicas de Aethermoor** |
| 📂    | Estrutura de diretórios pronta                            |
| 📝    | Arquivos `constitution.md` e `roadmap.md` inicializados   |
| 🌿    | Branches criados: `main`, `develop`                       |

---

## ✍️ Comandos do Ciclo de Escrita

### `/iniciar [capítulo]`

**Descrição:** Expande um rascunho (`xx_rascunho.md`) para uma primeira versão IA (`xxa.md`) dentro de um branch de feature dedicado.
**Pré-condições:**

- `capitulos/rascunhos/[xx]_rascunho.md` deve existir.
- O branch `develop` deve estar atualizado e sem modificações pendentes.
**Pós-condições:**
- Um novo branch `feature/capitulo-xx` é criado a partir de `develop`.
- O arquivo `capitulos/ia/xxa.md` é gerado com o texto expandido.
**Artefatos Atualizados:**
- `/capitulos/ia/xxa.md`
- Logs Git (criação de novo branch)
**Erros Possíveis:**
- `❌ Erro: Rascunho não encontrado em capitulos/rascunhos/[xx]_rascunho.md`
- `❌ Erro: Branch feature/capitulo-xx já existe.`

**Exemplo de Saída:**

| Status | Ação                                                            |
| :----- | :-------------------------------------------------------------- |
| 🌱    | Branch `feature/capitulo-01` criado com sucesso                 |
| 📖    | Rascunho analisado (Contexto: Elara, Floresta Cinzenta, Visões) |
| ✍️   | Arquivo `01a.md` expandido e salvo em `/capitulos/ia/`          |

---

### `/revisar [versão]`

**Descrição:** Aplica as notas de revisão (`{NOTA: ...}`) contidas em um arquivo de capítulo e gera a próxima versão iterativa.
**Pré-condições:**

- A versão especificada (`xxa.md`, `xxb.md`, etc.) deve existir em `/capitulos/ia/`.
- Devem existir uma ou mais tags `{NOTA: ...}` no texto do arquivo.
**Pós-condições:**
- Uma nova versão (`xxb.md`, `xxc.md`, etc.) é criada.
- As notas utilizadas são arquivadas em `docs/revisao_tracker.md` para rastreabilidade.
**Artefatos Atualizados:**
- `/capitulos/ia/[nova_versao].md`
- `/docs/revisao_tracker.md`
**Erros Possíveis:**
- `❌ Erro: Nenhuma nota de revisão encontrada no arquivo.`
- `❌ Erro: Arquivo [versão] não existe em /capitulos/ia/`.

**Exemplo de Saída:**

| Status | Detalhes                                                    |
| :----- | :---------------------------------------------------------- |
| 🔎    | 2 notas identificadas e arquivadas em `revisao_tracker.md`  |
| ✍️   | Revisões aplicadas (sons da floresta, transição para visão) |
| ✅     | Nova versão `01b.md` criada com sucesso                     |

---

## ✅ Comandos de Validação e Qualidade

### `/validar-estilo [versão]`

**Descrição:** Verifica a aderência do texto de um capítulo às regras de estilo definidas em `constitution.md`.
**Pré-condições:**

- A versão especificada do capítulo deve existir.
- O arquivo `docs/constitution.md` deve estar configurado com as regras.
**Pós-condições:**
- Um relatório de aderência é exibido na tela (não realiza alterações automáticas).
**Artefatos Atualizados:**
- Nenhum.
**Erros Possíveis:**
- `❌ Erro: Arquivo docs/constitution.md não encontrado.`
- `❌ Erro: Arquivo de capítulo [versão] não encontrado.`

**Exemplo de Saída:**

| Critério | Regra                   | Resultado | Observação                                        |
| :------- | :---------------------- | :-------- | :------------------------------------------------ |
| POV      | 3ª pessoa limitada      | ✅        | Consistente                                       |
| Tom      | Misterioso, melancólico | ✅        | Coerente                                          |
| Estilo   | Advérbios em "-mente"   | ⚠️      | Encontrados: 4 (`rapidamente`, `silenciosamente`) |

---

### `/criticar [versão] --fonte=[beta]`

**Descrição:** Invoca o Agente Crítico para uma análise literária de alto nível, opcionalmente incorporando feedback externo de leitores beta.
**Pré-condições:**

- A versão do capítulo deve existir em `/capitulos/ia/`.
- Se `--fonte=beta` for usado, arquivos de feedback devem existir em `/feedback/`.
**Pós-condições:**
- Um relatório crítico consolidado é exibido na tela.
**Artefatos Atualizados:**
- Nenhum.
**Erros Possíveis:**
- `❌ Erro: Arquivo de capítulo [versão] não encontrado.`
- `❌ Erro: Nenhuma fonte de feedback 'beta' encontrada em /feedback/`.

**Exemplo de Saída:**

| Seção            | Resumo da Análise                                                         |
| :--------------- | :------------------------------------------------------------------------ |
| Pontos Fortes    | Atmosfera da Floresta Cinzenta universalmente elogiada. Final impactante. |
| Sugestões        | Aumentar a vulnerabilidade da protagonista no início (sugestão de Ana).   |
| Feedback Externo | Consolidado com sucesso a partir de 1 arquivo de leitor beta.             |

---

### `/validar-coesao`

**Descrição:** Realiza uma varredura global em todos os capítulos finalizados e no lore para detectar inconsistências de continuidade, nomes e cronologia.
**Pré-condições:**

- Pelo menos um capítulo deve existir em `/capitulos/finalizados/`.
- Entradas de lore devem existir em `/lore/`.
**Pós-condições:**
- Um relatório de coesão é exibido na tela.
**Artefatos Atualizados:**
- Nenhum.
**Erros Possíveis:**
- `❌ Erro: Nenhum capítulo finalizado encontrado para análise.`

**Exemplo de Saída:**

| Tipo         | Severidade | Descrição                                                    |
| :----------- | :--------- | :----------------------------------------------------------- |
| Continuidade | 🚨 Grave  | Kael está vivo no cap. 5 mas seu lore indica morte no cap. 3 |
| Nomenclatura | ⚠️ Menor | 'Lyra' aparece como 'Lira' (2 vezes) no cap. 4               |
| Cronologia   | ✅ OK      | Sem conflitos de data detectados entre os eventos            |

---

## 🚀 Comandos de Integração e Entrega

### `/finalizar [capítulo]`

**Descrição:** Finaliza o trabalho em um capítulo, movendo-o para a pasta `/finalizados`, catalogando o lore, atualizando o changelog e integrando o branch de feature em `develop`.
**Pré-condições:**

- A última versão do capítulo (`xx*.md`) deve existir em `/capitulos/ia/`.
- Deve estar no branch `feature/capitulo-xx` correspondente.
**Pós-condições:**
- O capítulo é movido e renomeado para `/capitulos/finalizados/xx.md`.
- O branch de feature é mergeado em `develop` e depois removido.
- Novas entradas de lore são catalogadas.
- O `CHANGELOG.md` e o `roadmap.md` são atualizados.
**Artefatos Atualizados:**
- `/capitulos/finalizados/xx.md`
- `/lore/*`
- `/CHANGELOG.md`
- `/docs/roadmap.md`
**Erros Possíveis:**
- `❌ Erro: Nenhuma versão do capítulo [capítulo] encontrada em /capitulos/ia/`.
- `❌ Erro: Conflito de merge detectado. Por favor, resolva manualmente.`

**Exemplo de Saída:**

| Status | Ação                                                        |
| :----- | :---------------------------------------------------------- |
| 📂    | Capítulo 01 movido para `/finalizados/`                     |
| 📜    | Lore atualizado (3 novos elementos catalogados)             |
| 📝    | `CHANGELOG.md` e `roadmap.md` incrementados                 |
| 🌿    | Merge de `feature/capitulo-01` em `develop` concluído       |
| 📊    | Métricas: 2.158 palavras adicionadas, 5% do progresso total |

---

### `/compilar --formatos=[...] --versao=[...]`

**Descrição:** Compila todos os capítulos finalizados em um único manuscrito, gerando arquivos nos formatos especificados (e.g., ePub, PDF).
**Pré-condições:**

- Pelo menos um capítulo deve existir em `/capitulos/finalizados/`.
**Pós-condições:**
- Arquivos do manuscrito compilado são gerados na pasta `/entrega/`.
**Artefatos Atualizados:**
- `/entrega/[nome_do_livro]_[versao].epub`
- `/entrega/[nome_do_livro]_[versao].pdf`
**Erros Possíveis:**
- `❌ Erro: Nenhum capítulo finalizado disponível para compilação.`
- `❌ Erro: Formato solicitado não é suportado (Formatos válidos: epub, pdf, md).`

**Exemplo de Saída:**

| Status | Detalhes                                                            |
| :----- | :------------------------------------------------------------------ |
| 📚    | 5 capítulos finalizados foram compilados com sucesso                |
| 📦    | Arquivos gerados: `Aethermoor_v0.5.1.epub`, `Aethermoor_v0.5.1.pdf` |
| ✅     | Compilação concluída e arquivos salvos em `/entrega/`               |
