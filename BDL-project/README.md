# Book Development Lifecycle (BDL) v0.5.1

[![Version](https://img.shields.io/badge/version-0.5.1-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#licença)
[![AI Agents](https://img.shields.io/badge/agents-7-orange.svg)](#agentes-especializados)

# 🤖 BDL AI Agent System - Book Development Lifecycle AI Writers

A sophisticated system of AI agents designed to collaborate on book writing projects with professional-grade quality control and workflow management.

## Overview

O **Book Development Lifecycle (BDL) v0.5.1** é um framework completo para criação, desenvolvimento e refinamento de obras literárias utilizando agentes de IA especializados. Cada agente possui expertise específica no processo de escrita, desde a catalogação de lore até a análise crítica final.

## 🎯 Visão Geral

O BDL v0.5.1 transforma o processo de escrita em um workflow estruturado e profissional, onde cada etapa é otimizada por agentes de IA especializados que trabalham em colaboração para produzir conteúdo de alta qualidade.

### ✨ Principais Características

- **7 Agentes Especializados** com funções distintas e complementares
- **Workflow Integrado** com Git Flow para controle de versão profissional
- **Validação Automática** de estilo, coesão e qualidade narrativa
- **Gestão de Lore** avançada com catalogação inteligente
- **Análise Crítica** com integração de feedback de leitores beta
- **Documentação Completa** de todo o processo de desenvolvimento

## 🤖 Agentes Especializados

### 📚 Guardião do Lore (Arquivista)

- **Função**: Catalogação e gestão da base de conhecimento
- **Especialidade**: Consistência narrativa e worldbuilding
- **Arquivo**: [`arquivista.prompt.md`](.github/prompts/arquivista.prompt.md)

### 🎭 Editor Chefe

- **Função**: Orquestração completa do workflow
- **Especialidade**: Coordenação de agentes e gestão de branches
- **Arquivo**: [`editor.prompt.md`](.github/prompts/editor.prompt.md)

### ✍️ Escritor Fantasma

- **Função**: Transformação de rascunhos em prosa refinada
- **Especialidade**: Expansão narrativa e aplicação de revisões
- **Arquivo**: [`escritor.prompt.md`](.github/prompts/escritor.prompt.md)

### 🎯 Crítico Literário

- **Função**: Análise de qualidade e estrutura narrativa
- **Especialidade**: Avaliação técnica e integração de feedback beta
- **Arquivo**: [`critico.prompt.md`](.github/prompts/critico.prompt.md)

### 🏗️ Construtor de Projeto

- **Função**: Setup inicial e estruturação do ambiente
- **Especialidade**: Configuração automática e templates
- **Arquivo**: [`construtor.prompt.md`](.github/prompts/construtor.prompt.md)

### 🛡️ Guardião do Estilo

- **Função**: Validação de aderência às regras de estilo
- **Especialidade**: Compliance com constitution.md
- **Arquivo**: [`guardiao_estilo.prompt.md`](.github/prompts/guardiao_estilo.prompt.md)

### 🔗 Guardião da Coesão

- **Função**: Verificação de consistência narrativa global
- **Especialidade**: Integridade do lore e continuidade
- **Arquivo**: [`guardiao_coesao.prompt.md`](.github/prompts/guardiao_coesao.prompt.md)

## 🚀 Início Rápido

### Pré-requisitos

- Git instalado e configurado
- Editor de texto compatível com Markdown
- Acesso a agentes de IA compatíveis (Claude, ChatGPT, Gemini, etc.)

### Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/bdl-project.git
   cd bdl-project
   ```

2. **Execute o Construtor de Projeto:**
   - Carregue o prompt [`construtor.prompt.md`](.github/prompts/construtor.prompt.md)
   - Execute o comando de setup automático
   - Siga as instruções de personalização

3. **Configure sua Constitution:**
   - Edite o arquivo `constitution.md` gerado
   - Defina regras de estilo, POV e diretrizes específicas

4. **Inicie seu primeiro capítulo:**

   ```bash
   # Via Editor Chefe
   /iniciar 01
   ```

## 📖 Workflow Básico

### 1. Desenvolvimento de Capítulo

```bash
# 1. Criar rascunho inicial
@agente construtor -> /setup-chapter 01

# 2. Expandir rascunho
@agente escritor -> capitulos/rascunhos/01_rascunho.md

# 3. Revisão e refinamento
@agente editor -> /revisar 01a

# 4. Validação de estilo
@agente guardiao_estilo -> /validar 01b

# 5. Verificação de coesão
@agente guardiao_coesao -> /verificar 01c

# 6. Análise crítica final
@agente critico -> /criticar 01_final
```

### 2. Comandos Principais

| Comando                 | Agente            | Descrição              |
| ----------------------- | ----------------- | ---------------------- |
| `/iniciar [numero]`     | Editor Chefe      | Inicia novo capítulo   |
| `/revisar [arquivo]`    | Escritor Fantasma | Aplica revisões        |
| `/finalizar [numero]`   | Editor Chefe      | Finaliza capítulo      |
| `/criticar [numero]`    | Crítico Literário | Análise crítica        |
| `/validar [arquivo]`    | Guardião Estilo   | Validação de regras    |
| `/verificar [arquivo]`  | Guardião Coesão   | Consistência narrativa |
| `/catalogar [elemento]` | Arquivista        | Atualiza lore          |

## 📁 Estrutura do Projeto

```
projeto/
├── .github/
│   └── prompts/              # Agentes especializados
│       ├── arquivista.prompt.md
│       ├── editor.prompt.md
│       ├── escritor.prompt.md
│       ├── critico.prompt.md
│       ├── construtor.prompt.md
│       ├── guardiao_estilo.prompt.md
│       ├── guardiao_coesao.prompt.md
│       └── workflow.md
├── capitulos/
│   ├── rascunhos/           # Rascunhos humanos
│   ├── ia/                  # Versões IA
│   └── finalizados/         # Versões aprovadas
├── lore/                    # Base de conhecimento
├── feedback/                # Feedback de leitores beta
├── docs/                    # Documentação adicional
├── constitution.md          # Regras do projeto
├── roadmap.md              # Planejamento
└── CHANGELOG.md            # Histórico de versões
```

## 🔧 Configuração Avançada

### Constitution.md

O arquivo `constitution.md` é o coração do seu projeto. Configure:

- **POV e Narrador**: Primeira pessoa, terceira pessoa limitada, etc.
- **Tom e Atmosfera**: Formal, coloquial, épico, intimista
- **Regras de Estilo**: Vocabulário, estrutura, formatação
- **Diretrizes Específicas**: Regras únicas do seu universo

### Integração com Git Flow

```bash
# Branches principais
main          # Versão estável
develop       # Desenvolvimento ativo
feature/cap-* # Capítulos específicos
hotfix/*      # Correções urgentes
```

### Personalização de Agentes

Cada agente pode ser personalizado editando seu arquivo `.prompt.md`:

1. Ajuste o tom e estilo de comunicação
2. Modifique critérios de avaliação
3. Adicione regras específicas do seu projeto
4. Configure integrações com ferramentas externas

## 📊 Métricas e Qualidade

O BDL v0.5.1 inclui sistema de métricas para acompanhar:

- **Progresso de Escrita**: Palavras, capítulos, milestones
- **Qualidade Narrativa**: Scores de análise crítica
- **Consistência**: Aderência às regras de estilo e lore
- **Feedback**: Consolidação de opiniões de leitores beta

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

### Diretrizes para Contribuição

- Mantenha compatibilidade com a versão 0.5.1
- Documente todas as mudanças no CHANGELOG.md
- Teste com múltiplos agentes de IA
- Siga as convenções de nomenclatura existentes

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🆘 Suporte e Comunidade

- **Documentação**: [Wiki do Projeto](wiki/)
- **Issues**: [GitHub Issues](issues/)
- **Discussões**: [GitHub Discussions](discussions/)
- **Email**: [suporte@bdl-project.com](mailto:suporte@bdl-project.com)

## 🏆 Créditos

### Desenvolvimento

- **v0.5.1**: Desenvolvimento atual e consolidação
- **v0.0.1-0.5.0**: Desenvolvimento colaborativo com Gemini e ChatGPT
- **Conceito Original**: Evolução iterativa multi-IA

### Agradecimentos

- Comunidade de desenvolvedores de IA
- Contribuidores de feedback e testes
- Escritores que validaram o workflow
- Comunidade open source

---

## 📈 Roadmap

### v0.5.2 (Próxima)

- [ ] Interface web para gerenciamento
- [ ] Integração com APIs de IA
- [ ] Sistema de templates expandido
- [ ] Métricas avançadas

### v0.6.0 (Futuro)

- [ ] Suporte a múltiplos idiomas
- [ ] Colaboração em tempo real
- [ ] Integração com editoras
- [ ] Sistema de publicação automatizado

---

## Sobre o Projeto

Desenvolvido com ❤️ para a comunidade de escritores.

Transformando a arte da escrita através da inteligência artificial.
