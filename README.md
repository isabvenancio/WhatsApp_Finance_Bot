# 💰 WhatsApp Finance Bot

Um sistema desenvolvido em **Python** que permite registrar despesas diretamente pelo **WhatsApp**. Basta enviar uma mensagem informando um gasto, e o sistema interpreta a informação, classifica a categoria, salva em um banco de dados e atualiza automaticamente um dashboard financeiro.

> Exemplo:
>
> ```
> Gastei R$ 15,90 com almoço
> ```
>
> O sistema identifica:
> - Valor: R$ 15,90
> - Categoria: Alimentação
> - Descrição: almoço

---

## 🚀 Funcionalidades

- 📲 Registro de despesas via WhatsApp
- 🤖 Interpretação automática das mensagens
- 🏷️ Categorização automática dos gastos
- 💾 Armazenamento em banco de dados SQLite
- 📊 Dashboard interativo para visualização dos gastos
- 📅 Histórico completo das despesas
- 📈 Resumo por categoria
- 📉 Total gasto por período

---

## 🛠️ Tecnologias Utilizadas

- Python
- Selenium
- SQLite
- Pandas
- Streamlit
- Regular Expressions (Regex)

---

## 📱 Exemplo de Uso

### Registrar um gasto

```
Gastei 20 reais com Uber
```

Resultado:

```
✔ Gasto registrado!

Valor: R$20,00
Categoria: Transporte
Descrição: Uber
```

---

### Consultar resumo

```
Resumo
```

Resposta:

```
Resumo Financeiro

Total gasto: R$ 520,00

🍔 Alimentação: R$180,00
🚗 Transporte: R$120,00
🎮 Lazer: R$90,00
🛒 Mercado: R$130,00
```

---

## 📊 Dashboard

O dashboard apresenta:

- Total gasto
- Gastos por categoria
- Evolução mensal
- Histórico de despesas
- Gráficos interativos

---

## 🎯 Objetivo

O objetivo deste projeto é praticar conceitos intermediários de Python, integrando automação, manipulação de dados, banco de dados e desenvolvimento de dashboards em uma aplicação útil para o dia a dia.

---

## 📚 Conceitos Aplicados

- Automação de processos
- Manipulação de arquivos
- Banco de dados SQLite
- Expressões Regulares (Regex)
- Orientação a Objetos
- Tratamento de exceções
- Integração entre módulos
- Visualização de dados

---

## 🔮 Melhorias Futuras

- Login de usuários
- Suporte para múltiplos usuários
- Reconhecimento de voz
- Exportação para Excel e PDF
- Relatórios mensais automáticos
- Metas de gastos
- Alertas quando o orçamento for ultrapassado
- Inteligência Artificial para categorização mais precisa
- Dashboard online
- API REST para integração com outros sistemas
