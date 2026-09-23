# Glossário de referência

Guia rápido do que cada comando faz e **quando usar**. Atualizado a cada aula. Quando tiver dúvida "qual ferramenta eu uso aqui?", comece por aqui.

## Python básico

| Comando | O que é | Quando usar | Exemplo |
|---|---|---|---|
| `variavel = valor` | Guarda um valor com um nome | Sempre que for reutilizar um valor | `massa = 5.85` |
| `print(x)` | Mostra `x` na tela | Ver um resultado. **Nada aparece sem `print`** | `print(media)` |
| `input("texto")` | Pergunta ao usuário e espera ele digitar | Quando o valor não é conhecido de antemão | `input("Massa: ")` |
| `float(x)` | Converte texto em número decimal | Depois de `input()`, ou ao ler número com ponto | `float("5.85")` |
| `[a, b, c]` | Lista: vários valores num nome só | Guardar várias medições juntas | `phs = [6.8, 7.1, 6.9]` |
| `for item in lista:` | Repete um bloco para **cada item** da lista | Quando precisa processar item por item, com lógica própria em cada um | `for ph in phs:` |
| `if condicao:` | Executa um bloco só se a condição for verdadeira | Decisão dentro de um `for` ou sozinho | `if ph > 7.5:` |
| `sum(lista)` | Soma todos os itens | Calcular total | `sum(phs)` |
| `len(lista)` | Conta quantos itens tem | Saber o tamanho, ou calcular média (`sum/len`) | `len(phs)` |
| `max(lista)` / `min(lista)` | Maior / menor valor | Achar extremos rapidamente | `max(phs)` |

## Pandas — ler e explorar dados

| Comando | O que é | Quando usar | Exemplo |
|---|---|---|---|
| `import pandas as pd` | Carrega a biblioteca | No topo de todo script que usa tabelas | — |
| `pd.read_csv("arquivo.csv")` | Lê um arquivo CSV e vira uma tabela (`DataFrame`) | Sempre que o dado vem de um arquivo, e não digitado à mão | `tabela = pd.read_csv("medicoes.csv")` |
| `tabela["coluna"]` | Acessa uma coluna inteira | Ler, calcular ou filtrar com base numa coluna | `tabela["ph"]` |
| `tabela["coluna"].mean()` | Média da coluna | Resumo rápido de uma coluna | `tabela["ph"].mean()` |

## Pandas — criar e filtrar colunas

| Comando | O que é | Quando usar | Exemplo |
|---|---|---|---|
| `tabela["nova"] = conta` | Cria uma coluna calculada, aplicada a **todas as linhas de uma vez** | Transformar um valor existente (unidade, fórmula), sem usar `for` | `tabela["temperatura_k"] = tabela["temperatura"] + 273.15` |
| `tabela[condicao]` | Filtra: devolve só as **linhas** que atendem à condição | Ver um recorte da tabela (ex.: só as amostras fora do padrão) | `tabela[tabela["ph"] > 7.5]` |
| `\| ` e `&` (dentro de parênteses) | "ou" / "e" para **colunas inteiras** | Combinar duas condições numa tabela. Nunca use `or`/`and` aqui | `(tabela["ph"] < 6.5) \| (tabela["ph"] > 7.5)` |
| `tabela.loc[condicao, "coluna"] = valor` | Muda o valor de uma coluna, **só nas linhas** que atendem à condição | Classificar/rotular linhas (ex.: "OK"/"FORA") sem apagar o resto | `tabela.loc[tabela["ph"] > 7.5, "status"] = "FORA"` |

**Armadilha comum:** `tabela["ph"]` é a coluna. `ph` sozinho (sem `tabela[...]`) só existe dentro de um `for`. `"ph"` entre aspas sem `tabela[...]` é só texto solto, sem ligação com a tabela.

## Pandas — agrupar e resumir

| Comando | O que é | Quando usar | Exemplo |
|---|---|---|---|
| `tabela.groupby("coluna")` | Separa a tabela em grupos, um por valor da coluna (como bandejas separadas por lote) | Sempre que quiser uma conta **por categoria**, e não da tabela toda | `tabela.groupby("lote")` |
| `.groupby(...)["col"].mean()` | Uma estatística, por grupo | Resposta rápida e simples ("qual a média por lote?") | `tabela.groupby("lote")["ph"].mean()` |
| `.groupby(...)["col"].agg([...])` | **Várias** estatísticas de uma vez, por grupo | Analisar de verdade: nunca confie numa estatística isolada | `tabela.groupby("lote")["ph"].agg(["count","mean","median","min","max"])` |
| `.groupby(...)["col"].value_counts()` | Conta quantas vezes cada valor de texto aparece, por grupo | Contar categorias (ex.: quantos "OK" e "FORA" por lote) | `tabela.groupby("lote")["status"].value_counts()` |

## Visualização (matplotlib)

| Comando | O que é | Quando usar | Exemplo |
|---|---|---|---|
| `import matplotlib.pyplot as plt` | Carrega a biblioteca de gráficos | No topo do script, junto com pandas | — |
| `plt.bar(x, y)` | Gráfico de barras | Comparar valores entre categorias/amostras | `plt.bar(tabela["amostra"], tabela["ph"])` |
| `plt.axhline(valor)` | Linha horizontal no gráfico | Marcar um limite ou faixa aceitável | `plt.axhline(7.5, color="red")` |
| `plt.savefig("nome.png")` | Salva o gráfico como imagem | Guardar para usar no README ou relatório | `plt.savefig("grafico.png")` |
| `plt.show()` | Abre a janela com o gráfico | Ver o gráfico ao rodar o script | — |

## SQL (via sqlite3 + pandas)

| Comando | O que é | Quando usar | Exemplo |
|---|---|---|---|
| `import sqlite3` | Carrega a ferramenta de banco de dados SQLite | No topo do script, quando for usar SQL | — |
| `sqlite3.connect("arquivo.db")` | Abre (ou cria) um banco de dados num arquivo | Antes de qualquer consulta SQL | `conexao = sqlite3.connect("lab.db")` |
| `tabela.to_sql("nome", conexao, if_exists="replace", index=False)` | Copia um DataFrame para dentro do banco, como uma tabela | Para colocar dados (de um CSV, por exemplo) num banco de verdade | `medicoes.to_sql("medicoes", conexao, if_exists="replace", index=False)` |
| `pd.read_sql("SQL...", conexao)` | Manda uma consulta SQL e devolve o resultado como DataFrame | Sempre que quiser rodar uma pergunta em SQL | `pd.read_sql("SELECT * FROM medicoes", conexao)` |
| `SELECT col1, col2 FROM tabela` | Escolhe quais colunas mostrar, de qual tabela | Início de toda consulta | `SELECT amostra, ph FROM medicoes` |
| `WHERE condicao` | Filtra linhas | Igual ao `if`, mas para SQL. Texto usa aspas **simples** | `WHERE status = 'FORA'` |
| `GROUP BY coluna` | Agrupa linhas por valor da coluna | Antes de usar `COUNT`, `AVG`, etc | `GROUP BY lote` |
| `COUNT(*)` / `AVG(col)` | Conta linhas / calcula média, dentro de cada grupo | Junto com `GROUP BY` | `AVG(ph)` |
| `AS apelido` | Dá um nome novo a uma coluna calculada | Deixar o resultado mais legível | `AVG(ph) AS media_ph` |
| `ORDER BY coluna DESC` | Ordena o resultado (`DESC` = do maior para o menor) | Quando quer ver do "pior" para o "melhor", ou o inverso | `ORDER BY media_ph DESC` |
| `LIMIT n` | Mostra só as primeiras `n` linhas | Junto com `ORDER BY`, para pegar só o topo | `LIMIT 3` |
| `JOIN outra_tabela ON t1.col = t2.col` | Junta duas tabelas, casando pela coluna em comum | Quando o dado que você precisa está espalhado em tabelas diferentes | `JOIN lotes ON medicoes.lote = lotes.lote` |
| `conexao.close()` | Fecha a conexão com o banco | Ao terminar de usar o banco de dados | — |

**Armadilha comum:** SQL usa aspas **simples** (`'FORA'`) para texto, nunca duplas. E `WHERE`/`ON` sempre precisam de **coluna + operador + valor** juntos — nunca só o valor sozinho.

## Git / GitHub

| Comando | O que é | Quando usar |
|---|---|---|
| `git add arquivo` | Separa o arquivo para o próximo registro | Depois de salvar uma alteração |
| `git commit -m "mensagem"` | Registra a alteração no histórico | Depois do `add`, com uma frase clara do que mudou |
| `git push` | Envia os commits para o GitHub | Depois do `commit`, para publicar |
| `git pull --rebase` | Traz commits do GitHub que faltam no seu computador | Quando o `push` é rejeitado (`fetch first`) |
| `git status` | Mostra o que mudou e o que falta registrar | Sempre que estiver em dúvida do estado atual |

---
*Este arquivo cresce a cada aula. Se usar um comando novo, adicione uma linha aqui.*
