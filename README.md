![CI](https://github.com/vvilella/iadt_fase01_final/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)  
![Python](https://img.shields.io/badge/python-3.13.3-blue)  
![Status](https://img.shields.io/badge/status-em%20progresso-yellow)


# IADT Fase 01 — Tech Challenge

## Previsão de Custos Médicos com Modelos de Regressão

Link para o vídeo: https://youtu.be/4Ru3c-8Qk0s

---

## **Autor**

Victor Nardi Vilella  
Projeto desenvolvido como parte do **Tech Challenge — IADT Fase 01**.

---

Este projeto é o trabalho final da Fase 01 do curso **IADT**.  
O desafio consistiu em desenvolver um modelo de **regressão preditiva** para estimar os **custos médicos individuais** cobrados por um seguro de saúde, com base em variáveis demográficas e comportamentais.

---

## **Resumo do que foi feito**

- Análise exploratória completa (EDA)  
- Tratamento de dados categóricos com **One-Hot Encoding**  
- Modelagem utilizando **Regressão Linear**  
- Teste extra com **Árvore de Decisão Regressora**  
- Ajuste manual de **hiperparâmetro** (`max_depth`)  
- Separação dos dados em **treinamento e teste**  
- Avaliação do modelo com **MSE**, **RMSE** e **R²**  
- Validação estatística usando **`statsmodels`**  
- Geração de gráficos e interpretação completa dos resultados  
- Relatório detalhado em **Markdown** no notebook  
- Automação de comandos com **Makefile**

---

## **Objetivos**

- Desenvolver um modelo de regressão preditiva para prever custos médicos.  
- Validar e interpretar os resultados estatísticos.  
- Consolidar os conhecimentos adquiridos nas disciplinas de Python, Machine Learning e Inteligência Artificial.

---

## **Estrutura do Projeto**

```
/iadt_fase01_final
│
├── data/
│   └── insurance.csv              # Base de dados utilizada
│
├── notebook/
│   └── iadt_fase01_final.ipynb    # Notebook com o projeto completo
│
├── README.md                      # Este arquivo
├── requirements.txt               # Dependências do projeto
├── .gitignore                     # Arquivos ignorados no Git
├── Makefile                       # Automação de comandos
└── LICENSE                        # Licença MIT
```

---

## **Como executar o projeto**

1. Clone o repositório:  
```bash
git clone https://github.com/seu-usuario/iadt_fase01_final.git
```

2. Acesse a pasta:  
```bash
cd iadt_fase01_final
```

3. Utilize o **Makefile** para automatizar as tarefas:  

- Instalar dependências:  
```bash
make install
```

- Rodar o Jupyter Notebook:  
```bash
make run
```

- Limpar arquivos desnecessários (`__pycache__`, checkpoints):  
```bash
make clean
```

- Atualizar o requirements.txt:  
```bash
make freeze
```

---

## **Resultados**

- **Regressão Linear:** R²: 0.78  
- **Árvore de Decisão (sem ajuste):** → R²: 0.73  
- **Árvore de Decisão (ajustada, `max_depth=3`):** R²: 0.85  

**ajuste de hiperparâmetro** melhorou significativamente a performance!  

---

## **Próximos passos (possíveis evoluções para melhorar o aprendizado)**

- Explorar outros **hiperparâmetros** (`min_samples_split`, `max_features`, etc).  
- Testar outros modelos como **Random Forest** ou **XGBoost**.  
- Criar uma **API** para expor o modelo como serviço.  

---

## **Entrega**

- Notebook completo e comentado.  
- Teste extra com Árvore de Decisão e análise comparativa.  
- Ajuste manual de hiperparâmetro com melhoria clara de performance.  
- Automação de comandos com **Makefile**.  
- Vídeo explicativo mostrando:  
  - Análise do problema  
  - Passo a passo da modelagem  
  - Resultados obtidos  
  - Conclusão e próximos passos

---
