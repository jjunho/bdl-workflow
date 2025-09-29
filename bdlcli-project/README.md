# 📘 BDL CLI - Book Development Lifecycle Command Line Tool

A simple, reliable Python CLI for managing book projects with the BDL (Book Development Lifecycle) methodology.

## Overview

**BDL CLI** is the "plumbing" component of the BDL ecosystem - it handles project initialization, file management, statistics, and compilation. It's designed to be lightweight, fast, and dependency-minimal.

## Features

- 🏗️ **Project Initialization**: Create new book projects with proper structure
- 📊 **Statistics**: Analyze your writing progress and metrics  
- 📚 **Compilation**: Generate PDF, EPUB, and HTML from your manuscripts
- 🔧 **Simple & Fast**: Minimal dependencies, maximum reliability

## Installation

```bash
pip install bdlcli
```

Or from source:

```bash
git clone <this-repo>
cd bdlcli-project
pip install -e .
```

## Usage

### Initialize a new book project

```bash
bdl init my-book --title "My Amazing Book" --author "Your Name"
```

### Check project statistics  

```bash
bdl stats
```

### Compile your book

```bash
bdl compile --pdf --epub --html
```

## Project Structure Created

When you run `bdl init`, it creates:

```
my-book/
├── .github/prompts/          # AI agent templates (if using BDL agents)
├── .gitignore               
├── BDL.yaml                 # Project metadata
└── (ready for content)
```

## Requirements

- Python 3.7+
- For PDF compilation: LaTeX
- For EPUB/HTML: Pandoc

## BDL Ecosystem

This CLI works perfectly with the **BDL AI Agent System** for automated content creation and editing workflows. The CLI handles file management while the agents handle the creative work.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and guidelines.

## License

[LICENSE](LICENSE)
