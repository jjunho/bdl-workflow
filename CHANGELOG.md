# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [0.5.2] - 2025-09-29

### Adicionado

- **Empacotamento Python**: Projeto reestruturado como pacote instalável (`bdlcli`) com `setup.py`, `pyproject.toml` e `MANIFEST.in`.
- **CLI Unificado**: Código do CLI migrado para `bdlcli/cli.py` com entry point `bdlcli`.
- **Distribuição**: Geração de arquivos `.whl` e `.tar.gz` para redistribuição via pip.
- **Testes Automatizados**: Testes para o CLI em `testes/` usando pytest.
- **.gitignore Moderno**: Ignora ambientes virtuais, builds, dist, cache, VSCode e saídas temporárias.

### Alterado

- **Estrutura de Diretórios**: Separação clara entre código (`bdlcli/`), dados (`BDL/`) e testes (`testes/`).
- **Documentação**: Atualização do README e CHANGELOG para refletir empacotamento e uso do CLI.

### Corrigido

- **Caminhos e Imports**: Ajustes para garantir funcionamento do CLI e testes sempre dentro de `BDL/`.

### Técnico

- **Compatibilidade**: Pacote pronto para instalação local e futura publicação no PyPI.

## [0.5.1] - 2025-09-29

### Adicionado

- **Sistema BDL v0.5.1 Completo**: Implementação da versão mais avançada do Book Development Lifecycle
- **7 Agentes Especializados**:
  - `arquivista.prompt.md` - Guardião do Lore para catalogação avançada
  - `editor.prompt.md` - Editor Chefe com orquestração completa do workflow
  - `escritor.prompt.md` - Escritor Fantasma para expansão de rascunhos
  - `critico.prompt.md` - Crítico Literário com integração de feedback beta
  - `construtor.prompt.md` - Construtor de Projeto para setup automatizado
  - `guardiao_estilo.prompt.md` - Guardião do Estilo para validação de regras
  - `guardiao_coesao.prompt.md` - Guardião da Coesão para consistência narrativa
- **Documentação Completa**: `workflow.md` com especificações técnicas do BDL v0.5.1
- **Configuração de Projeto**: `.gitignore` abrangente para projetos de escrita
- **YAML Front Matter**: Metadados padronizados em todos os prompts

### Melhorado

- **Estrutura de Arquivos**: Organização limpa em `.github/prompts/`
- **Consistência de Versioning**: Todas as referências atualizadas para v0.5.1
- **Formatação Markdown**: Compliance com padrões de linting
- **Integração de Sistema**: Agentes projetados para trabalhar em conjunto

### Corrigido

- **Eliminação de Duplicidades**: Remoção de conteúdo duplicado nos prompts
- **Correção de Lint**: Resolução de problemas de formatação Markdown
- **Padronização YAML**: Estrutura uniforme nos metadados
- **Referências de Versão**: Atualização de todas as menções à versão anterior

### Técnico

- **Formato de Arquivo**: Todos os prompts em `.prompt.md`
- **Estrutura de Diretório**: `.github/prompts/` para organização
- **Versionamento**: Semantic versioning aplicado consistentemente
- **Documentação**: Especificações técnicas detalhadas

---

## [0.1.0 - 0.5.0] - Desenvolvimento Anterior

### Contexto de Desenvolvimento

Versões anteriores do sistema BDL foram desenvolvidas em colaboração com diferentes IAs:

- **Gemini & ChatGPT**: Responsáveis pelo desenvolvimento iterativo das versões 0.1.0 até 0.5.0
- **Evolução Automática**: Cada IA gerenciou autonomamente a evolução dos números de versão a cada iteração
- **Registros Perdidos**: Não há documentação detalhada dessas versões anteriores
- **Base Fundacional**: Essas versões serviram como experimentos e prototipagem para o sistema atual

### Características das Versões Anteriores

- **Desenvolvimento Experimental**: Testes de conceitos e abordagens
- **Múltiplas IAs**: Colaboração entre diferentes modelos de linguagem
- **Iteração Rápida**: Versionamento automático sem documentação formal
- **Aprendizado Gradual**: Refinamento progressivo dos prompts e workflows

### Migração para v0.5.1

- **Consolidação**: Unificação de todo o aprendizado anterior em uma versão estável
- **Refatoração Completa**: Sistema completamente reescrito e padronizado
- **Documentação Formal**: Primeira versão com documentação técnica adequada
- **Padronização**: Estabelecimento de convenções e estrutura consistente

---

## Convenções de Versionamento

### Formato: [MAJOR.MINOR.PATCH]

- **MAJOR**: Mudanças incompatíveis na API/estrutura
- **MINOR**: Funcionalidades adicionadas de forma compatível
- **PATCH**: Correções de bugs compatíveis

### Tipos de Mudanças

- **Adicionado** - para novas funcionalidades
- **Melhorado** - para mudanças em funcionalidades existentes
- **Descontinuado** - para funcionalidades que serão removidas
- **Removido** - para funcionalidades removidas
- **Corrigido** - para correções de bugs
- **Segurança** - para correções relacionadas à segurança

### Links de Referência

- [Documentação Completa](workflow.md)
- [Especificações BDL v0.5.1](https://github.com/usuario/projeto/releases/tag/v0.5.1)
- [Guias de Contribuição](CONTRIBUTING.md)

---

**Mantido pela equipe de desenvolvimento BDL**  
*Última atualização: 29 de setembro de 2025*
