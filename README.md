# � BDL Workflow - Book Development Lifecycle

> A complete ecosystem for AI-powered book writing and project management

## 🏗️ Architecture Overview

This repository contains **two complementary but independent projects**:

| Project | Purpose | Technology | Distribution |
|---------|---------|------------|--------------|
| **[bdlcli-project/](./bdlcli-project/)** | Project Management | Python CLI | PyPI Package |
| **[BDL-project/](./BDL-project/)** | AI Writing System | Agent Prompts | Template/Framework |

## 🚀 Quick Start

### 1. Install the CLI Tool

```bash
# From PyPI (future)
pip install bdlcli

# Or from source
cd bdlcli-project/
pip install -e .
```

### 2. Initialize a Book Project  

```bash
bdl init my-book --title "My Amazing Book" --author "Your Name"
```

### 3. Add AI Agents (Optional)

Copy the BDL agent system to your project for AI-powered writing workflows.

## 📖 What Each Project Does

### 📱 BDL CLI (`bdlcli-project/`)

**The "Plumbing"** - Handles file management and project operations:

- ✅ Project initialization with proper structure
- 📊 Statistics and progress tracking  
- 📚 Compilation to PDF/EPUB/HTML
- 🔧 Simple, reliable, minimal dependencies

### 🤖 BDL AI Agents (`BDL-project/`)  

**The "Creative Brain"** - AI-powered writing workflows:

- ✍️ 8 specialized writing agents (Writer, Critic, Archivist, etc.)
- 🔄 Structured workflow: `/iniciar` → `/revisar` → `/criticar` → `/finalizar`
- 🎨 Style governance and consistency validation
- 🌿 Git branching integration for collaborative writing

## 🔄 How They Work Together

```mermaid
graph LR
    A[bdl init] --> B[Project Structure]
    B --> C[AI Agents]
    C --> D[/iniciar workflow]
    D --> E[bdl stats]
    E --> F[bdl compile]
```

1. **CLI creates structure**: `bdl init` sets up directories and metadata
2. **Agents create content**: AI workflows produce and refine chapters  
3. **CLI manages output**: `bdl compile` generates final manuscripts

## 📁 Generated Project Structure

```

| **Aspecto**       | **Descrição**                                                                                                                                                                     |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pré-condições** | - O diretório `livro/` não deve existir.<br>- `--title` e `--author` são opcionais.                                                                                               |
| **Ação**          | - Cria o diretório `livro/`.<br>- Copia os arquivos-base do `/src/BDL`.<br>- Sempre cria um arquivo `BDL.yaml` com metadados do projeto.                                          |
| **Pós-condições** | - Estrutura inicial criada.<br>- Arquivos de prompts em `.github/prompts`.<br>- Arquivo `.gitignore`.<br>- Arquivo `BDL.yaml` gerado (com título/autor preenchidos ou em branco). |

**Estrutura criada:**

```

livro/
├── .github/prompts/
│   ├── arquivista.prompt.md
│   ├── construtor.prompt.md
│   ├── critico.prompt.md
│   ├── editor.prompt.md
│   ├── escritor.prompt.md
│   ├── guardiao_coesao.prompt.md
│   ├── guardiao_estilo.prompt.md
│   └── workflow.md
├── .gitignore
└── BDL.yaml

```

### 📑 Exemplo de `BDL.yaml`

* **Com título e autor informados:**

```yaml
title: "Livro de Teste"
author: "Autor de Teste"
version: "0.1.0"
created_at: "2025-09-29"
```

- **Sem título e autor:**

```yaml
title: ""
author: ""
version: "0.1.0"
created_at: "2025-09-29"
```

---

## 🔹 2. Estatísticas

```bash
bdl stats
```

| **Aspecto**       | **Descrição**                                                                                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pré-condições** | - Projeto inicializado com `bdl init`.<br>- Pelo menos um capítulo deve existir.                                                                              |
| **Ação**          | Analisa capítulos e gera estatísticas.                                                                                                                        |
| **Pós-condições** | Relatório no terminal:<br>• Número de capítulos.<br>• Palavras/toques por capítulo.<br>• Capítulos mais editados.<br>• Rascunhos e capítulos não finalizados. |

---

## 🔹 3. Compilação

```bash
bdl compile --pdf
bdl compile --epub
bdl compile --html
```

| **Aspecto**       | **Descrição**                                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Pré-condições** | - Projeto inicializado.<br>- Conteúdo disponível nos capítulos.<br>- Dependências de compilação instaladas (LaTeX/pandoc). |
| **Ação**          | Converte capítulos em formatos finais.                                                                                     |
| **Pós-condições** | - Arquivos criados em `livro/output/`:<br>• `livro.pdf`<br>• `livro.epub`<br>• `livro.html`                                |

---

## ⚠️ Erros Comuns e Mensagens de Falha

| **Comando**   | **Situação de Erro** | **Mensagem Possível**                            | **Como Resolver**                         |
| ------------- | -------------------- | ------------------------------------------------ | ----------------------------------------- |
| `bdl init`    | Diretório já existe  | `Erro: diretório 'livro' já existe.`             | Escolha outro nome ou remova o existente. |
| `bdl init`    | Sem permissões       | `Erro: não foi possível criar diretório.`        | Verifique permissões do SO.               |
| `bdl stats`   | Projeto não iniciado | `Erro: .github/prompts não encontrado.`          | Execute `bdl init`.                       |
| `bdl stats`   | Sem capítulos        | `Aviso: nenhum capítulo encontrado.`             | Crie capítulos antes de rodar.            |
| `bdl compile` | Projeto vazio        | `Erro: não há conteúdo para compilar.`           | Escreva/import capítulos antes.           |
| `bdl compile` | Dependência ausente  | `Erro: ferramenta de compilação não encontrada.` | Instale LaTeX/pandoc.                     |
| `bdl compile` | Falha no build       | `Erro: compilação falhou.`                       | Verifique sintaxe ou logs.                |

---

✅ **Fluxo Operacional**

1. `bdl init` → Cria estrutura inicial **+ BDL.yaml** (sempre).
2. `bdl stats` → Mostra estatísticas.
3. `bdl compile` → Gera PDF/EPUB/HTML.
4. Consulte erros comuns em caso de falha.
