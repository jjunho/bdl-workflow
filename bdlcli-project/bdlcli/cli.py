import argparse
import os
import sys
import yaml
import re
import subprocess
import shutil
from datetime import datetime
from pathlib import Path

PROMPTS = [
    "arquivista.prompt.md",
    "construtor.prompt.md",
    "critico.prompt.md",
    "editor.prompt.md",
    "escritor.prompt.md",
    "guardiao_coesao.prompt.md",
    "guardiao_estilo.prompt.md",
    "workflow.md",
]


def find_project_root():
    """Encontra a raiz do projeto BDL procurando por BDL.yaml"""
    current = Path.cwd()
    for parent in [current] + list(current.parents):
        if (parent / "BDL.yaml").exists():
            return parent
    return None


def get_project_config(project_root=None):
    """Carrega configuração do projeto do BDL.yaml"""
    if project_root is None:
        project_root = find_project_root()

    if project_root is None:
        return None

    config_path = project_root / "BDL.yaml"
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception:
        return None


def validate_dependencies():
    """Valida se dependências externas estão disponíveis"""
    deps = {}

    # Verifica LaTeX (para PDF)
    try:
        result = subprocess.run(
            ["pdflatex", "--version"], capture_output=True, text=True, timeout=5
        )
        deps["latex"] = result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        deps["latex"] = False

    # Verifica pandoc (para EPUB/HTML)
    try:
        result = subprocess.run(
            ["pandoc", "--version"], capture_output=True, text=True, timeout=5
        )
        deps["pandoc"] = result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        deps["pandoc"] = False

    return deps


def count_words_in_file(filepath):
    """Conta palavras em um arquivo markdown"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        # Remove markdown syntax e conta palavras
        text = re.sub(r"[#*`_\[\]()]", "", content)
        words = len(text.split())
        return words
    except Exception:
        return 0


def criar_estrutura_livro(nome, title, author):
    # Cria a estrutura sempre dentro de BDL/ na raiz
    try:
        base = os.path.join(nome)
        os.makedirs(os.path.join(base, ".github", "prompts"))
        for prompt in PROMPTS:
            open(os.path.join(base, ".github", "prompts", prompt), "w").close()
        open(os.path.join(base, ".gitignore"), "w").close()
        # BDL.yaml
        bdl_yaml = {
            "title": title or "",
            "author": author or "",
            "version": "0.1.0",
            "created_at": datetime.now().strftime("%Y-%m-%d"),
        }
        with open(os.path.join(base, "BDL.yaml"), "w", encoding="utf-8") as f:
            yaml.dump(bdl_yaml, f, allow_unicode=True)
        print(f"✅ Projeto '{nome}' criado com sucesso.")
    except Exception as e:
        print(f"Erro: não foi possível criar diretório. {e}")
        sys.exit(1)


def init_cmd(args):
    nome = args.nome
    title = args.title
    author = args.author
    if os.path.exists(nome):
        print(f"Erro: diretório '{nome}' já existe.")
        sys.exit(1)
    criar_estrutura_livro(nome, title, author)


def stats_cmd(args):
    # Busca pela raiz do projeto
    project_root = find_project_root()
    if project_root is None:
        print("Erro: Projeto BDL não encontrado. Execute 'bdl init' primeiro.")
        sys.exit(1)

    config = get_project_config(project_root)
    if config is None:
        print("Erro: Não foi possível carregar BDL.yaml.")
        sys.exit(1)

    # Busca capítulos em várias localizações possíveis
    capitulo_dirs = [
        project_root / "capitulos" / "finalizados",
        project_root / "capitulos" / "ia",
        project_root / "capitulos" / "rascunhos",
        project_root / "capitulos",
    ]

    all_chapters = []
    for cap_dir in capitulo_dirs:
        if cap_dir.exists():
            for f in cap_dir.glob("*.md"):
                if "capitulo" in f.name.lower() or f.name.lower().startswith("cap"):
                    all_chapters.append(f)

    if not all_chapters:
        print("📊 Estatísticas do Projeto")
        print("=" * 40)
        print(f"📖 Título: {config.get('title', 'Não definido')}")
        print(f"✍️  Autor: {config.get('author', 'Não definido')}")
        print(f"📅 Criado: {config.get('created_at', 'N/A')}")
        print("⚠️  Aviso: nenhum capítulo encontrado.")
        return

    # Calcula estatísticas
    total_words = 0
    chapter_stats = []

    for chapter_path in all_chapters:
        words = count_words_in_file(chapter_path)
        total_words += words

        # Determina status baseado no diretório
        if "finalizados" in str(chapter_path):
            status = "✅ Finalizado"
        elif "ia" in str(chapter_path):
            status = "🤖 Em revisão IA"
        elif "rascunhos" in str(chapter_path):
            status = "📝 Rascunho"
        else:
            status = "📄 Em progresso"

        chapter_stats.append(
            {
                "name": chapter_path.name,
                "words": words,
                "status": status,
                "path": chapter_path,
            }
        )

    # Ordena capítulos por nome
    chapter_stats.sort(key=lambda x: x["name"])

    # Exibe estatísticas
    print("📊 Estatísticas do Projeto")
    print("=" * 40)
    print(f"📖 Título: {config.get('title', 'Não definido')}")
    print(f"✍️  Autor: {config.get('author', 'Não definido')}")
    print(f"📅 Criado: {config.get('created_at', 'N/A')}")
    print(f"🔢 Total de capítulos: {len(all_chapters)}")
    print(f"📝 Palavras totais: {total_words:,}")

    if total_words > 0:
        avg_words = total_words // len(all_chapters)
        print(f"📊 Média por capítulo: {avg_words:,} palavras")

    print("\n📚 Detalhes por Capítulo:")
    print("-" * 40)

    for chapter in chapter_stats:
        print(
            f"{chapter['status']:<15} {chapter['name']:<25} {chapter['words']:>6,} palavras"
        )

    # Status por categoria
    finalizados = len([c for c in chapter_stats if "Finalizado" in c["status"]])
    em_ia = len([c for c in chapter_stats if "Em revisão IA" in c["status"]])
    rascunhos = len([c for c in chapter_stats if "Rascunho" in c["status"]])

    print(f"\n📈 Progresso:")
    print("-" * 40)
    if finalizados > 0:
        print(f"✅ Finalizados: {finalizados}")
    if em_ia > 0:
        print(f"🤖 Em revisão IA: {em_ia}")
    if rascunhos > 0:
        print(f"📝 Rascunhos: {rascunhos}")


def compile_cmd(args):
    # Busca pela raiz do projeto
    project_root = find_project_root()
    if project_root is None:
        print("❌ Erro: Projeto BDL não encontrado. Execute 'bdl init' primeiro.")
        sys.exit(1)

    config = get_project_config(project_root)
    if config is None:
        print("❌ Erro: Não foi possível carregar BDL.yaml.")
        sys.exit(1)

    # Busca capítulos finalizados primeiro, depois outros
    chapter_paths = [
        project_root / "capitulos" / "finalizados",
        project_root / "capitulos" / "ia",
        project_root / "capitulos",
    ]

    chapters = []
    for cap_dir in chapter_paths:
        if cap_dir.exists():
            for f in sorted(cap_dir.glob("*.md")):
                if "capitulo" in f.name.lower() or f.name.lower().startswith("cap"):
                    chapters.append(f)

    if not chapters:
        print("❌ Erro: não há capítulos para compilar.")
        print("   Dica: Adicione arquivos .md em capitulos/finalizados/ ou capitulos/")
        sys.exit(1)

    # Determina formatos solicitados
    formatos = []
    if args.pdf:
        formatos.append("pdf")
    if args.epub:
        formatos.append("epub")
    if args.html:
        formatos.append("html")
    if not formatos:
        formatos = ["pdf"]  # PDF como padrão

    # Valida dependências
    deps = validate_dependencies()
    missing_deps = []

    if "pdf" in formatos and not deps["latex"]:
        missing_deps.append(
            "LaTeX (para PDF) - instale: apt-get install texlive-latex-base"
        )
    if ("epub" in formatos or "html" in formatos) and not deps["pandoc"]:
        missing_deps.append("Pandoc (para EPUB/HTML) - instale: apt-get install pandoc")

    if missing_deps:
        print("❌ Dependências faltando:")
        for dep in missing_deps:
            print(f"   • {dep}")
        print("\n💡 Dica: Instale as dependências e tente novamente.")
        sys.exit(1)

    # Cria diretório de saída
    output_dir = project_root / "output"
    output_dir.mkdir(exist_ok=True)

    # Prepara título do livro
    title = config.get("title", "Livro")
    safe_title = re.sub(r"[^\w\s-]", "", title).strip().replace(" ", "_")
    if not safe_title:
        safe_title = "livro"

    print("📚 Compilando manuscrito...")
    print(f"   📖 Título: {title}")
    print(f"   📄 Capítulos encontrados: {len(chapters)}")
    print(f"   📁 Saída: {output_dir}")

    # Simula compilação (substitua por implementação real)
    success_files = []
    for fmt in formatos:
        output_file = output_dir / f"{safe_title}.{fmt}"

        # Por enquanto, cria arquivo vazio (implementar compilação real depois)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"Compilado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            for i, chapter in enumerate(chapters, 1):
                f.write(f"## Capítulo {i}: {chapter.stem}\n\n")
                try:
                    content = chapter.read_text(encoding="utf-8")
                    f.write(content)
                    f.write("\n\n")
                except Exception as e:
                    f.write(f"[Erro ao ler capítulo: {e}]\n\n")

        success_files.append(output_file.name)

    print("✅ Compilação concluída!")
    print(f"   📦 Arquivos gerados: {', '.join(success_files)}")
    print(f"   📁 Localização: {output_dir}")

    # Exibe estatísticas finais
    total_words = sum(count_words_in_file(ch) for ch in chapters)
    print(f"   📊 Total de palavras: {total_words:,}")


def check_cmd(args):
    """Verifica status do projeto e dependências"""
    print("🔍 Verificação do Ambiente BDL")
    print("=" * 40)

    # Verifica projeto
    project_root = find_project_root()
    if project_root:
        print(f"✅ Projeto encontrado: {project_root}")
        config = get_project_config(project_root)
        if config:
            print(f"📖 Título: {config.get('title', 'Não definido')}")
            print(f"✍️  Autor: {config.get('author', 'Não definido')}")
        else:
            print("⚠️  Aviso: BDL.yaml não pôde ser carregado")
    else:
        print("❌ Nenhum projeto BDL encontrado no diretório atual ou pais")

    print(f"\n🔧 Dependências Externas:")
    print("-" * 40)

    deps = validate_dependencies()

    if deps["latex"]:
        print("✅ LaTeX disponível (para compilação PDF)")
    else:
        print("❌ LaTeX não encontrado")
        print("   💡 Instale: apt-get install texlive-latex-base")

    if deps["pandoc"]:
        print("✅ Pandoc disponível (para EPUB/HTML)")
    else:
        print("❌ Pandoc não encontrado")
        print("   💡 Instale: apt-get install pandoc")

    print(f"\n📊 Resumo:")
    print("-" * 40)
    ready_formats = []
    if project_root:
        ready_formats.append("Estrutura de projeto")
    if deps["latex"]:
        ready_formats.append("PDF")
    if deps["pandoc"]:
        ready_formats.append("EPUB/HTML")

    if ready_formats:
        print(f"✅ Pronto para: {', '.join(ready_formats)}")
    else:
        print("❌ Configure um projeto BDL e instale dependências para começar")


def agent_setup_cmd(args):
    """Configura sistema de agentes no projeto atual"""
    project_root = find_project_root()
    if project_root is None:
        print("❌ Erro: Projeto BDL não encontrado. Execute 'bdl init' primeiro.")
        sys.exit(1)

    print("🤖 Configurando Sistema de Agentes BDL")
    print("=" * 40)

    # Verifica se já existe sistema de agentes
    prompts_dir = project_root / ".github" / "prompts"
    if prompts_dir.exists() and any(prompts_dir.glob("*.md")):
        print("✅ Sistema de agentes já configurado!")
        print(f"   📁 Localização: {prompts_dir}")

        # Lista agentes existentes
        agents = list(prompts_dir.glob("*.md"))
        if agents:
            print(f"   🤖 Agentes disponíveis: {len(agents)}")
            for agent in agents:
                print(f"      • {agent.stem}")
    else:
        print("⚠️  Sistema de agentes não encontrado.")
        print("💡 Para usar agentes BDL:")
        print("   1. Copie os prompts do BDL-project para .github/prompts/")
        print("   2. Personalize constitution.md com suas diretrizes")
        print("   3. Use 'bdl agent status' para verificar configuração")

    # Verifica estrutura de diretórios para agentes
    required_dirs = [
        "capitulos/rascunhos",
        "capitulos/ia",
        "capitulos/finalizados",
        "lore",
        "docs",
    ]
    missing_dirs = []

    for dir_name in required_dirs:
        dir_path = project_root / dir_name
        if not dir_path.exists():
            missing_dirs.append(dir_name)

    if missing_dirs:
        print(f"\n📁 Diretórios recomendados faltando:")
        for missing in missing_dirs:
            print(f"   • {missing}/")

        print(f"\n💡 Criar diretórios? (s/n): ", end="")
        response = input().strip().lower()
        if response in ["s", "sim", "y", "yes"]:
            for missing in missing_dirs:
                dir_path = project_root / missing
                dir_path.mkdir(parents=True, exist_ok=True)
                print(f"   ✅ Criado: {missing}/")


def agent_status_cmd(args):
    """Mostra status do workflow de agentes"""
    project_root = find_project_root()
    if project_root is None:
        print("❌ Erro: Projeto BDL não encontrado. Execute 'bdl init' primeiro.")
        sys.exit(1)

    print("🤖 Status do Sistema de Agentes")
    print("=" * 40)

    config = get_project_config(project_root)
    if config:
        print(f"📖 Projeto: {config.get('title', 'Sem título')}")

    # Verifica agentes disponíveis
    prompts_dir = project_root / ".github" / "prompts"
    if not prompts_dir.exists():
        print("❌ Sistema de agentes não configurado")
        print("   💡 Execute: bdl agent setup")
        return

    agents = list(prompts_dir.glob("*.md"))
    if not agents:
        print("❌ Nenhum agente encontrado")
        print("   💡 Copie os prompts do BDL-project para .github/prompts/")
        return

    print(f"✅ Agentes configurados: {len(agents)}")

    # Categoriza agentes por tipo
    agent_categories = {
        "Core": ["escritor", "editor", "critico", "arquivista"],
        "Governance": ["guardiao_estilo", "guardiao_coesao"],
        "Setup": ["construtor"],
        "Other": [],
    }

    found_agents = {}
    for agent in agents:
        agent_name = agent.stem.replace(".prompt", "")

        # Encontra categoria
        category = "Other"
        for cat, agent_list in agent_categories.items():
            if any(a in agent_name.lower() for a in agent_list):
                category = cat
                break

        if category not in found_agents:
            found_agents[category] = []
        found_agents[category].append(agent_name)

    # Exibe agentes por categoria
    for category, agent_list in found_agents.items():
        if agent_list:
            print(f"\n🏷️  {category}:")
            for agent in sorted(agent_list):
                print(f"   • {agent}")

    # Verifica estrutura de workflow
    workflow_dirs = {
        "capitulos/rascunhos": "Rascunhos humanos",
        "capitulos/ia": "Versões IA",
        "capitulos/finalizados": "Capítulos aprovados",
        "lore": "Base de conhecimento",
        "docs": "Documentação",
    }

    print(f"\n📁 Estrutura de Workflow:")
    for dir_name, description in workflow_dirs.items():
        dir_path = project_root / dir_name
        if dir_path.exists():
            file_count = len(list(dir_path.glob("*")))
            print(f"   ✅ {dir_name:<20} ({file_count} arquivos)")
        else:
            print(f"   ❌ {dir_name:<20} (não existe)")

    # Verifica arquivos de configuração importantes
    config_files = {
        "docs/constitution.md": "Diretrizes de estilo",
        "docs/roadmap.md": "Planejamento do projeto",
    }

    print(f"\n⚙️  Configuração:")
    for file_path, description in config_files.items():
        file_full_path = project_root / file_path
        if file_full_path.exists():
            print(f"   ✅ {description}")
        else:
            print(f"   ⚠️  {description} (recomendado: {file_path})")


def main():
    parser = argparse.ArgumentParser(
        description="BDL Workflow CLI - Ferramenta de linha de comando para Book Development Lifecycle",
        epilog="Para mais informações, visite: https://github.com/seu-usuario/bdl-workflow",
    )
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponíveis")

    # Comando init
    parser_init = subparsers.add_parser(
        "init",
        help="Inicializa um novo projeto BDL",
        description="Cria a estrutura inicial de um projeto de livro com BDL",
    )
    parser_init.add_argument("nome", help="Nome do diretório do projeto")
    parser_init.add_argument("--title", help="Título do livro")
    parser_init.add_argument("--author", help="Autor do livro")
    parser_init.set_defaults(func=init_cmd)

    # Comando stats
    parser_stats = subparsers.add_parser(
        "stats",
        help="Mostra estatísticas do livro",
        description="Analisa capítulos e exibe estatísticas de progresso",
    )
    parser_stats.set_defaults(func=stats_cmd)

    # Comando compile
    parser_compile = subparsers.add_parser(
        "compile",
        help="Compila o livro em formatos finais",
        description="Gera manuscrito final em PDF, EPUB ou HTML",
    )
    parser_compile.add_argument(
        "--pdf", action="store_true", help="Gerar PDF (requer LaTeX)"
    )
    parser_compile.add_argument(
        "--epub", action="store_true", help="Gerar ePub (requer Pandoc)"
    )
    parser_compile.add_argument(
        "--html", action="store_true", help="Gerar HTML (requer Pandoc)"
    )
    parser_compile.set_defaults(func=compile_cmd)

    # Comando check
    parser_check = subparsers.add_parser(
        "check",
        help="Verifica status do projeto e dependências",
        description="Diagnóstica ambiente e mostra o que está pronto para uso",
    )
    parser_check.set_defaults(func=check_cmd)

    # Comando agent (integração com sistema de agentes)
    parser_agent = subparsers.add_parser(
        "agent",
        help="Interface com sistema de agentes BDL",
        description="Comandos para integração com agentes de IA para escrita",
    )
    agent_subparsers = parser_agent.add_subparsers(
        dest="agent_command", help="Comandos de agentes"
    )

    # bdl agent setup
    parser_agent_setup = agent_subparsers.add_parser(
        "setup", help="Configura sistema de agentes no projeto atual"
    )
    parser_agent_setup.set_defaults(func=agent_setup_cmd)

    # bdl agent status
    parser_agent_status = agent_subparsers.add_parser(
        "status", help="Mostra status do workflow de agentes"
    )
    parser_agent_status.set_defaults(func=agent_status_cmd)

    args = parser.parse_args()
    if hasattr(args, "func"):
        try:
            args.func(args)
        except KeyboardInterrupt:
            print("\n\n⚠️  Operação interrompida pelo usuário.")
            sys.exit(1)
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            print(
                "💡 Se o problema persistir, reporte em: https://github.com/seu-usuario/bdl-workflow/issues"
            )
            sys.exit(1)
    else:
        parser.print_help()
