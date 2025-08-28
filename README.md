# Projeto Python com GitHub Actions

Este é um projeto de exemplo em Python que demonstra a configuração e uso do GitHub Actions para automação de pipelines CI/CD.

# 📋 Descrição
O projeto contém um script Python simples que gera um arquivo `output.txt` com a data e hora da última execução. O GitHub Actions é configurado para executar automaticamente este script a cada push para a branch principal.

# 🚀 Como Executar Localmente

### Pré-requisitos

 - Python 3.9 ou superior instalado

 - Git instalado

### Passo a Passo

1. Clone o repositório
```
git clone https://github.com/RodrigoFCC/pipeline-ci-cd
cd seu-repositorio
```

2. Execute o script Python

```
python main.py
```
3. Verifique o resultado

```
cat output.txt
```

O comando acima mostrará algo como: `Última execução: 2024-01-15 14:30:45`


# 🔧 Estrutura do Projeto
```
seu-repositorio/
├── .github/
│   └── workflows/
│       └── python-app.yml    # Configuração do GitHub Actions
├── main.py                   # Script principal
├── requirements.txt          # Dependências (vazio neste projeto)
└── README.md                 # Este arquivo
```

# 🤖 GitHub Actions

### O projeto está configurado com uma pipeline automática que:

1. Executa o script Python em um ambiente Ubuntu

2. Gera um arquivo de saída

3. Disponibiliza o resultado como um artefato para download

### Como ver as execuções:
1. Acesse a aba "Actions" no seu repositório GitHub

2. Clique na execução mais recente

3. Explore os logs de cada etapa

4. Baixe o artefato "output-result" para ver o arquivo gerado

### Fluxo da Pipeline:
 - Trigger: Push para a branch main ou criação de pull requests

 - Ambiente: Ubuntu latest

 - Passos:

    1. Checkout do código

    2. Configuração do Python 3.9

    3. Execução do script main.py

    4. Upload do arquivo output.txt como artefato


# 📝 Personalização

### Para adaptar este projeto para suas necessidades:

1. Modifique o script main.py para realizar suas tarefas

2. Ajuste o arquivo requirements.txt se precisar de dependências

3. Personalize o workflow em .github/workflows/python-app.yml


# 🆘 Solução de Problemas

Se encontrar erros na execução:

1. Verifique se o Python está instalado localmente: python --version

2. Confirme a indentação correta no arquivo YAML (use espaços, não tabs)

3. Verifique os logs detalhados na aba "Actions" do GitHub

# 📞 Suporte

Se precisar de ajuda, consulte a documentação do GitHub Actions ou abra uma issue no repositório.