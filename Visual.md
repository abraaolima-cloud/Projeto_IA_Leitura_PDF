
# 📄 Analisador de Documentos com IA

Este projeto é uma aplicação **Streamlit** que automatiza a busca, leitura e resumo inteligente de arquivos PDF.

---

## 🚀 Fluxo de Funcionamento

O sistema opera em 4 etapas principais:

### 1️⃣ Busca e Localização
O sistema varre as pastas locais em busca de arquivos PDF baseados no termo digitado.
> **Status:** Operacional
><img width="1844" height="919" alt="image" src="https://github.com/user-attachments/assets/672d1bbd-4d02-4944-984a-026d2fb39735" />


---

### 2️⃣ Extração de Dados (OCR/Texto)
Utiliza a biblioteca `PyMuPDF` para ler o conteúdo bruto do arquivo sem erros de codificação.
> **Status:** Concluído
> <img width="320" height="338" alt="image" src="https://github.com/user-attachments/assets/a30cb266-685c-4bf7-ab2b-a23ebf3680de" />
> <img width="296" height="328" alt="image" src="https://github.com/user-attachments/assets/9bedf1c8-7201-4fb7-9cd5-6b48a6601736" />


---

### 3️⃣ Resumo Automático (IA)
Assim que o arquivo é carregado, a ia gera um resumo executivo instantâneo.
> **Status:** Inteligência Ativa
> <img width="858" height="469" alt="image" src="https://github.com/user-attachments/assets/e408ba32-53b6-414c-b176-9859ec87f744" />
> <img width="1880" height="780" alt="image" src="https://github.com/user-attachments/assets/06db3f67-08a1-46dc-8aac-30fc0ebd2f6d" />

---

### 4️⃣ Chat Interativo
Espaço para perguntas específicas sobre o documento, mantendo o contexto da leitura.
> **Status:** Disponível
> <img width="1519" height="652" alt="image" src="https://github.com/user-attachments/assets/eb22e0d2-ee6d-4fea-9013-4dc6da04ff8b" />


---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Função |
| :--- | :--- |
| **Python 3.10+** | Linguagem Base |
| **Streamlit** | Interface de Usuário |
| **ollama** | Cérebro da IA |
| **PyMuPDF** | Processamento de PDF |

---
