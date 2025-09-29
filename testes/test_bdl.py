import os
import shutil
import subprocess
import sys
import tempfile
import pytest


def run_cli(args, cwd=None):
    """
    Executa o CLI bdlcli com os argumentos fornecidos em um diretório específico.
    Retorna o resultado do subprocesso (stdout, stderr, returncode).
    """
    # Usa o executável Python do ambiente virtual
    python_exec = "/home/jjunho/SDD-Book/.venv/bin/python"
    cmd = [python_exec, "-m", "bdlcli"] + args
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return result


def test_init_cria_estrutura():
    """
    Testa se o comando 'bdl init' cria corretamente toda a estrutura do projeto:
    - Diretório BDL na raiz
    - .github/prompts com todos os arquivos de prompt
    - BDL.yaml com metadados
    - .gitignore
    Também verifica se o conteúdo de BDL.yaml contém o título e autor informados.
    """
    with tempfile.TemporaryDirectory() as tmp:
        nome = "BDL"
        result = run_cli(
            ["init", nome, "--title", "Livro Teste", "--author", "Autor Teste"], cwd=tmp
        )
        assert result.returncode == 0
        livro_dir = os.path.join(tmp, nome)
        assert os.path.isdir(livro_dir)
        assert os.path.isdir(os.path.join(livro_dir, ".github", "prompts"))
        assert os.path.isfile(os.path.join(livro_dir, "BDL.yaml"))
        assert os.path.isfile(os.path.join(livro_dir, ".gitignore"))
        # Checa prompts
        for prompt in [
            "arquivista.prompt.md",
            "construtor.prompt.md",
            "critico.prompt.md",
            "editor.prompt.md",
            "escritor.prompt.md",
            "guardiao_coesao.prompt.md",
            "guardiao_estilo.prompt.md",
            "workflow.md",
        ]:
            assert os.path.isfile(os.path.join(livro_dir, ".github", "prompts", prompt))
        # Checa conteúdo do BDL.yaml
        with open(os.path.join(livro_dir, "BDL.yaml"), encoding="utf-8") as f:
            content = f.read()
            assert "title: Livro Teste" in content
            assert "author: Autor Teste" in content


def test_init_diretorio_existente():
    """
    Testa se o comando 'bdl init' retorna erro ao tentar criar um projeto em um diretório já existente.
    Deve exibir a mensagem de erro correta e retornar código diferente de zero.
    """
    with tempfile.TemporaryDirectory() as tmp:
        nome = "BDL"
        os.makedirs(os.path.join(tmp, nome))
        result = run_cli(["init", nome], cwd=tmp)
        assert result.returncode != 0
        assert "Erro: diretório 'BDL' já existe." in result.stdout


def test_stats_sem_prompts():
    """
    Testa se o comando 'bdl stats' retorna erro quando a estrutura de prompts não existe.
    Deve exibir a mensagem de erro correta e retornar código diferente de zero.
    """
    with tempfile.TemporaryDirectory() as tmp:
        result = run_cli(["stats"], cwd=tmp)
        assert result.returncode != 0
        assert "Erro: BDL/.github/prompts não encontrado." in result.stdout


def test_stats_sem_capitulos():
    """
    Testa se o comando 'bdl stats' retorna aviso quando não há capítulos no projeto.
    Deve exibir a mensagem de aviso e retornar código zero.
    """
    with tempfile.TemporaryDirectory() as tmp:
        # Cria estrutura mínima de prompts
        os.makedirs(os.path.join(tmp, "BDL", ".github", "prompts"))
        result = run_cli(["stats"], cwd=tmp)
        assert result.returncode == 0
        assert "Aviso: nenhum capítulo encontrado." in result.stdout


def test_compile_sem_prompts():
    """
    Testa se o comando 'bdl compile' retorna erro quando a estrutura de prompts não existe.
    Deve exibir a mensagem de erro correta e retornar código diferente de zero.
    """
    with tempfile.TemporaryDirectory() as tmp:
        result = run_cli(["compile", "--pdf"], cwd=tmp)
        assert result.returncode != 0
        assert "Erro: BDL/.github/prompts não encontrado." in result.stdout


def test_compile_sem_capitulos():
    """
    Testa se o comando 'bdl compile' retorna erro quando não há capítulos para compilar.
    Deve exibir a mensagem de erro correta e retornar código diferente de zero.
    """
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(os.path.join(tmp, "BDL", ".github", "prompts"))
        result = run_cli(["compile", "--pdf"], cwd=tmp)
        assert result.returncode != 0
        assert "Erro: não há conteúdo para compilar." in result.stdout


def test_compile_gera_arquivos():
    """
    Testa se o comando 'bdl compile' gera corretamente os arquivos de saída (PDF, ePub) quando há capítulos presentes.
    Deve criar os arquivos vazios no diretório output/ e exibir mensagem de sucesso.
    """
    with tempfile.TemporaryDirectory() as tmp:
        os.makedirs(os.path.join(tmp, "BDL", ".github", "prompts"))
        # Cria um capítulo fake
        cap_dir = os.path.join(tmp, "BDL", "capitulos")
        os.makedirs(cap_dir)
        with open(os.path.join(cap_dir, "capitulo01.md"), "w") as f:
            f.write("# Capítulo 1")
        result = run_cli(["compile", "--pdf", "--epub"], cwd=tmp)
        assert result.returncode == 0
        output_dir = os.path.join(tmp, "BDL", "output")
        assert os.path.isfile(os.path.join(output_dir, "livro.pdf"))
        assert os.path.isfile(os.path.join(output_dir, "livro.epub"))
        assert "Arquivos criados em" in result.stdout
