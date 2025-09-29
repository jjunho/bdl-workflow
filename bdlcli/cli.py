import argparse
import os
import sys
import yaml
from datetime import datetime

PROMPTS = [
    'arquivista.prompt.md', 'construtor.prompt.md', 'critico.prompt.md',
    'editor.prompt.md', 'escritor.prompt.md', 'guardiao_coesao.prompt.md',
    'guardiao_estilo.prompt.md', 'workflow.md'
]

def criar_estrutura_livro(nome, title, author):
    # Cria a estrutura sempre dentro de BDL/ na raiz
    try:
        base = os.path.join(nome)
        os.makedirs(os.path.join(base, '.github', 'prompts'))
        for prompt in PROMPTS:
            open(os.path.join(base, '.github', 'prompts', prompt), 'w').close()
        open(os.path.join(base, '.gitignore'), 'w').close()
        # BDL.yaml
        bdl_yaml = {
            'title': title or '',
            'author': author or '',
            'version': '0.1.0',
            'created_at': datetime.now().strftime('%Y-%m-%d')
        }
        with open(os.path.join(base, 'BDL.yaml'), 'w', encoding='utf-8') as f:
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
    # Sempre busca dentro de BDL/
    base = 'BDL'
    if not os.path.exists(os.path.join(base, '.github', 'prompts')):
        print("Erro: BDL/.github/prompts não encontrado.")
        sys.exit(1)
    # Busca capítulos (stub)
    capitulos = []
    for root, dirs, files in os.walk(base):
        for f in files:
            if f.endswith('.md') and 'capitulo' in root:
                capitulos.append(os.path.join(root, f))
    if not capitulos:
        print("Aviso: nenhum capítulo encontrado.")
        return
    print(f"Número de capítulos: {len(capitulos)}")
    # Outras estatísticas podem ser implementadas aqui

def compile_cmd(args):
    base = 'BDL'
    if not os.path.exists(os.path.join(base, '.github', 'prompts')):
        print("Erro: BDL/.github/prompts não encontrado.")
        sys.exit(1)
    # Busca capítulos (stub)
    capitulos = []
    for root, dirs, files in os.walk(base):
        for f in files:
            if f.endswith('.md') and 'capitulo' in root:
                capitulos.append(os.path.join(root, f))
    if not capitulos:
        print("Erro: não há conteúdo para compilar.")
        sys.exit(1)
    # Dependências (stub)
    # Aqui seria feita a checagem de LaTeX/pandoc
    formatos = []
    if args.pdf:
        formatos.append('PDF')
    if args.epub:
        formatos.append('ePub')
    if args.html:
        formatos.append('HTML')
    if not formatos:
        formatos = ['PDF', 'ePub']
    output_dir = os.path.join(base, 'output')
    os.makedirs(output_dir, exist_ok=True)
    for fmt in formatos:
        out = os.path.join(output_dir, f'livro.{fmt.lower()}')
        open(out, 'w').close()  # stub: cria arquivo vazio
    print(f"Arquivos criados em {output_dir}/: {', '.join([f'livro.{fmt.lower()}' for fmt in formatos])}")

def main():
    parser = argparse.ArgumentParser(description='BDL Workflow CLI')
    subparsers = parser.add_subparsers(dest='command')

    parser_init = subparsers.add_parser('init', help='Inicializa um novo projeto BDL')
    parser_init.add_argument('nome', help='Nome do diretório do projeto')
    parser_init.add_argument('--title', help='Título do livro')
    parser_init.add_argument('--author', help='Autor do livro')
    parser_init.set_defaults(func=init_cmd)

    parser_stats = subparsers.add_parser('stats', help='Mostra estatísticas do livro')
    parser_stats.set_defaults(func=stats_cmd)

    parser_compile = subparsers.add_parser('compile', help='Compila o livro em formatos finais')
    parser_compile.add_argument('--pdf', action='store_true', help='Gerar PDF')
    parser_compile.add_argument('--epub', action='store_true', help='Gerar ePub')
    parser_compile.add_argument('--html', action='store_true', help='Gerar HTML')
    parser_compile.set_defaults(func=compile_cmd)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
