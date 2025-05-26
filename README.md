
# IADT Fase 01 — Tech Challenge

## Previsão de Custos Médicos com Modelos de Regressão

Este projeto é o trabalho final da Fase 01 do curso **IADT**.  

O desafio consistiu em desenvolver um modelo de **regressão preditiva** para estimar os **custos médicos individuais** cobrados por um seguro de saúde, com base em variáveis demográficas e comportamentais.

---

## **Resumo do que foi feito**

- Análise exploratória completa (EDA)  
- Tratamento de dados categóricos com **One-Hot Encoding**  
- Modelagem utilizando **Regressão Linear**  
- Separação dos dados em **treinamento e teste**  
- Avaliação do modelo com **MSE**, **RMSE** e **R²**  
- Validação estatística usando **`statsmodels`**  
- Geração de gráficos e interpretação completa dos resultados  
- Relatório detalhado em **Markdown** no notebook  
- Roteiro de vídeo preparado  

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
├── src/
│   └── utils.py                   # funções auxiliares
│
├── README.md                      # Este arquivo
├── requirements.txt               # Dependências do projeto
└── .gitignore                     # Arquivos ignorados no Git
```

---

## **Como executar o projeto**

1. Clone o repositório:  
```bash
git clone https://github.com/vvilella/iadt_fase01_final
```

2. Acesse a pasta:  
```bash
cd iadt_fase01_final
```

3. (Opcional) Crie um ambiente virtual:  
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

4. Instale as dependências:  
```bash
pip install -r requirements.txt
```

5. Execute o Jupyter Notebook:  
```bash
jupyter notebook
```

6. Abra o notebook `notebook/iadt_fase01_final.ipynb` e siga o passo a passo.

---

## **Resultados**

- **RMSE:** ~ R$ 5.800 → erro médio aceitável para o contexto.  
- **R²:** ~ 75% → modelo explica bem a variação nos custos médicos.  
- **Variáveis mais relevantes:** ser **fumante**, **IMC** e **idade**.  
- **Visualização:** Gráfico de valores **reais vs previstos** mostrando boa aderência.  
- **Validação estatística:** confirmou a significância das principais variáveis.

---

## **Próximos passos (possíveis evoluções)**

- Testar modelos mais **complexos**: Árvores de Decisão, Random Forest, XGBoost.  
- Ajustar **hiperparâmetros** para melhorar performance.  
- Aplicar transformações para tratar **outliers** (ex.: log nos encargos).  
- Criar uma **API** para expor o modelo como serviço.  
- Fazer o **deploy** em ambiente real.

---

## **Autor**

Victor Nardi Vilella  
Projeto desenvolvido como parte do **Tech Challenge — IADT Fase 01**.

---

## **Entrega**

- Notebook completo e comentado.  
- Roteiro de vídeo preparado.  
- Vídeo explicativo mostrando:  
  - Análise do problema  
  - Passo a passo da modelagem  
  - Resultados obtidos  
  - Conclusão e próximos passos

