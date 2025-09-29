# Changelog - BDL Workflow (Book Development Lifecycle)

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-09-29 - Major Architecture Separation

### 🏗️ BREAKING CHANGES

- **Complete project restructure**: Separated dual-purpose codebase into two independent projects
- **New architecture**: Clean separation of concerns between CLI tool and AI agent system

### ✨ Added

#### bdlcli-project/ - Python CLI Tool (Project Management)
- **Smart project detection**: Automatic BDL.yaml discovery from current working directory and parents
- **Enhanced statistics**: Rich project metrics with emoji formatting, progress tracking, and detailed chapter analysis
- **Dependency validation**: Automatic detection and validation of LaTeX (PDF) and Pandoc (EPUB/HTML) dependencies
- **Agent integration commands**: 
  - `bdl agent setup` - Configure AI agent system in current project
  - `bdl agent status` - Display comprehensive workflow status
- **Comprehensive error handling**: User-friendly error messages with actionable solutions
- **File-based compilation**: Generate PDF/EPUB/HTML from markdown chapters with proper title handling
- **Cross-platform support**: Works on Linux, macOS, and Windows with proper path handling

#### BDL-project/ - AI Agent System (Content Creation)
- **8 specialized AI agents**: 
  - Escritor (Writer), Crítico (Critic), Arquivista (Archivist)
  - Editor (Orchestrator), Construtor (Setup), Guardião Estilo (Style), Guardião Coesão (Cohesion)
- **Complete workflow system**: `/iniciar` → `/revisar` → `/criticar` → `/finalizar` commands
- **Advanced governance**: Style validation, consistency checking, and quality control
- **Beta reader integration**: Structured feedback collection and analysis
- **Git Flow integration**: Branch management and automated merge workflows
- **Comprehensive documentation**: Complete workflow manual with examples and best practices

### 🔧 Improved

#### CLI Tool Enhancements
- **Project initialization**: Creates proper BDL.yaml configuration with metadata
- **Statistics command**: 
  - Word count across multiple chapter locations
  - Progress tracking with status indicators
  - Chapter categorization (finalized, IA, draft)
- **Compilation system**: 
  - Multi-format support (PDF, EPUB, HTML)  
  - Proper filename handling (spaces → underscores)
  - Dependency validation with installation hints
- **Error messages**: Clear, actionable feedback with solution suggestions

#### Test Infrastructure
- **Fixed virtual environment dependencies**: Tests now use system Python with PYTHONPATH
- **Updated CLI behavior validation**: All tests updated for new smart project detection
- **Comprehensive test coverage**: 7 test cases covering initialization, statistics, and compilation
- **Working directory handling**: Tests properly simulate different project structures

### 🗂️ Restructured

#### Before (Monolithic)
```
/home/jjunho/SDD-Book/
├── bdlcli/           # CLI mixed with everything
├── BDL/              # AI prompts mixed with CLI
├── testes/           # Tests for mixed system
└── [various files]   # Unclear ownership
```

#### After (Clean Separation)
```
/home/jjunho/SDD-Book/
├── bdlcli-project/          # 🔧 CLI Tool (pip installable)
│   ├── bdlcli/              # Clean Python package
│   ├── testes/              # CLI-specific tests  
│   ├── pyproject.toml       # Package config (only pyyaml dependency)
│   └── README.md            # CLI documentation
├── BDL-project/             # 🤖 AI Agent System
│   ├── .github/prompts/     # 8 specialized agent prompts
│   ├── README.md            # Agent system documentation
│   └── CHANGELOG.md         # Agent version history
└── .github/                 # 📚 Shared project documentation
    └── copilot-instructions.md
```

### 🧪 Testing

- **All tests passing**: 7/7 test cases now pass after infrastructure fixes
- **Fixed test execution**: Updated `run_cli()` function to use system Python with PYTHONPATH
- **Updated assertions**: Test expectations now match new CLI behavior and error messages
- **Working directory simulation**: Tests properly handle project detection from various locations

### 📚 Documentation

#### Added New Documentation
- **Root-level copilot instructions**: Comprehensive guidance for AI agents working with both systems
- **Separated READMEs**: Each project has focused, specific documentation
- **Individual CHANGELOGs**: Independent versioning for CLI tool and AI system
- **Architecture philosophy**: Clear explanation of separation rationale and benefits

#### Key Documentation Highlights
- **Installation instructions**: Both pip installation and development setup
- **Usage examples**: Real workflow examples for both systems  
- **Integration guide**: How CLI and AI systems work together
- **Contribution guidelines**: Development setup and testing procedures

### 🚀 Benefits of New Architecture

#### For Developers
- **Clear separation of concerns**: CLI handles file operations, agents handle creativity
- **Independent development**: Each project can evolve at its own pace
- **Easier testing**: Focused test suites for specific functionality
- **Better maintainability**: Reduced complexity in each component

#### For Users  
- **Flexible installation**: Use CLI alone or with full AI system
- **Clearer workflows**: Distinct tools for different aspects of book development
- **Better reliability**: Minimal dependencies for core CLI functionality
- **Easier troubleshooting**: Isolated systems with specific error messages

#### For Distribution
- **PyPI ready**: CLI tool can be published as standalone package
- **Template system**: AI agents can be distributed as templates/frameworks
- **Modular adoption**: Users can adopt components incrementally

### 🔄 Migration Path

Existing users can migrate by:

1. **For CLI usage**: Install new `bdlcli` package from `bdlcli-project/`
2. **For AI agents**: Copy prompts from `BDL-project/.github/prompts/` to your project
3. **For both**: Follow new workflow as documented in respective README files

### ⚡ Performance

- **Faster CLI startup**: Reduced imports and dependencies
- **Better test execution**: No more virtual environment dependencies
- **Cleaner git history**: Separate repositories enable focused development

### 🛡️ Quality Assurance

- **Enhanced error handling**: User-friendly messages with actionable solutions
- **Comprehensive validation**: Dependency checking, project detection, file validation
- **Robust testing**: Updated test suite with 100% pass rate
- **Documentation coverage**: Complete documentation for all features and workflows

---

## Previous Versions

See individual project CHANGELOGs for detailed version history:
- **CLI Tool**: `bdlcli-project/CHANGELOG.md` 
- **AI Agents**: `BDL-project/CHANGELOG.md`
