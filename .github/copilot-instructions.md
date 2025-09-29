# Copilot Instructions for BDL Workflow (Book Development Lifecycle)

## Project Overview - Separated Architecture
This repository contains **two independent but complementary projects**:

### 1. **`bdlcli-project/`** - Python CLI Tool (Project Management)
- Standalone Python package for initializing, managing, and compiling book projects
- Creates directory structures, handles metadata in `BDL.yaml`, manages file organization
- Minimal dependencies (only `pyyaml`), designed for reliability and simplicity
- Entry point: `python -m bdlcli` or installed as `bdlcli` command
- **Publishable to PyPI** as independent package

### 2. **`BDL-project/`** - AI Agent Ecosystem (Content Creation) 
- Sophisticated prompt system with specialized AI agents for book writing workflow
- **8 specialized agents**: Escritor (Writer), Crítico (Critic), Arquivista (Archivist), etc.
- Complex multi-stage workflow: `/iniciar` → `/revisar` → `/criticar` → `/finalizar`
- Includes governance (style/consistency validation), branching strategy, and compilation pipeline
- **Template/Framework system** for AI-powered book writing

## Architecture Philosophy
- **Complete separation**: Each project has its own README, CHANGELOG, LICENSE
- **CLI tool**: Handles the "plumbing" - file management, structure, basic operations
- **Agent system**: Handles the "creative work" - writing, revision, quality control
- **Independent distribution**: CLI can be pip-installed, agents are templates/prompts

## Key Workflows
- **Initialize a project:** `bdl init <dir> [--title ...] [--author ...]`
  - Creates a new directory, copies base files, generates `BDL.yaml`.
  - Example: `bdl init livro --title "Livro de Teste" --author "Autor de Teste"`
- **Show statistics:** `bdl stats`
  - Analyzes chapters and prints stats (chapter count, word count, edit frequency, etc).
- **Compile book:** `bdl compile --pdf|--epub|--html`
  - Converts chapters to output formats. Requires LaTeX/pandoc for PDF/EPUB/HTML.

## Project Structure

### CLI Tool (`bdlcli-project/`)
```
bdlcli-project/
├── bdlcli/
│   ├── cli.py              # Main CLI entry point
│   ├── __main__.py         # Module entry point
│   └── __init__.py
├── testes/
│   └── test_bdl.py         # Comprehensive CLI tests
├── pyproject.toml          # Package config (only depends on pyyaml)
├── setup.py               # Setup script
├── README.md              # CLI-specific documentation
├── CHANGELOG.md           # CLI version history
└── LICENSE
```

### AI Agent System (`BDL-project/`)
```
BDL-project/
├── .github/prompts/
│   ├── escritor.prompt.md      # Writer agent
│   ├── critico.prompt.md       # Critic agent
│   ├── arquivista.prompt.md    # Archivist agent
│   ├── guardiao_estilo.prompt.md   # Style guardian
│   ├── guardiao_coesao.prompt.md   # Cohesion guardian
│   ├── editor.prompt.md        # Editor orchestrator
│   ├── construtor.prompt.md    # Project constructor
│   └── workflow.md            # Complete v0.5.1 manual
├── README.md                  # Agent system documentation
├── CHANGELOG.md               # Agent system version history
└── LICENSE
```

## Conventions & Patterns
- All project metadata is stored in `BDL.yaml` (YAML format).
- Prompt templates are Markdown files in `.github/prompts/`.
- Output files are placed in `livro/output/` after compilation.
- Error messages are user-friendly and mapped to common failure scenarios (see README for examples).
- All commands are run via the `bdl` CLI; do not invoke scripts directly.

## Testing
- Tests are in `testes/` (e.g., `test_bdl.py`).
- Use `pytest` to run tests: `pytest testes/`

## External Dependencies
- Compilation requires LaTeX and/or pandoc installed on the system.
- No nonstandard Python dependencies are required for CLI usage.

## Examples
- Initialize: `bdl init livro --title "My Book" --author "Me"`
- Compile: `bdl compile --pdf`
- Stats: `bdl stats`

## References
- See `README.md` for detailed workflow and error handling examples.
- See `.github/prompts/` for prompt template structure (created after `bdl init`).

---

**For AI agents:**
- Always use the `bdl` CLI for project operations.
- Follow the structure and error handling patterns in `README.md`.
- When generating new book projects, ensure all required files and folders are created as described above.
