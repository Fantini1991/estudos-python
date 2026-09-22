# Estudos de Python

Repositório de estudos de programação em Python, com foco em **análise de dados aplicada a química e materiais**.

Sou químico com pós-graduação em Engenharia de Materiais, em transição de carreira para a área de dados. Cada script abaixo resolve um problema típico de laboratório.

📖 [Glossário de referência](GLOSSARIO.md) — comandos de Python, pandas e Git explicados, com exemplos.

## Conteúdo

| Arquivo | Tema | Conceitos |
|---|---|---|
| `aula1.py` | Concentração molar e diluição | variáveis, operações, `print` |
| `aula2.py` | Cálculo interativo | `input()`, conversão com `float()` |
| `aula3.py` | Controle de qualidade de pH | listas, laço `for`, condicionais `if` |
| `aula4.py` | Tabelas de medições | pandas, DataFrame, filtros |
| `aula5.py` | Leitura de CSV e gráfico | `read_csv`, `groupby`, matplotlib |
| `revisao1.py` | Temperaturas de um forno | `sum`, `len`, contador, `max` |
| `aula6b.py` | Colunas calculadas e classificação | colunas com pandas, `.loc`, condições vetorizadas |

## Exemplo: controle de pH por amostra

![Gráfico de pH](grafico_ph.png)

## Como executar

Requer Python 3.10 ou superior.

```bash
pip install pandas
python aula4.py
```

## Próximos passos

- Leitura de arquivos CSV e gráficos com matplotlib
- Estatística aplicada a dados experimentais
- Projeto final: análise de um conjunto de dados real de materiais
