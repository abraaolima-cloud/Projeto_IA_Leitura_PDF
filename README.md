# 🤖 Analisador Inteligente de Propostas com IA Local

Bem-vindo ao meu projeto de **Análise de Documentos Comerciais**. Desenvolvi esta aplicação para resolver um desafio comum no setor de vendas: a necessidade de localizar e extrair informações cruciais de grandes volumes de propostas em PDF de forma rápida e segura.

O grande diferencial deste projeto é o uso de **IA Generativa Local**, o que significa que o processamento dos dados é feito inteiramente na máquina do usuário, garantindo 100% de privacidade e custo zero de API.

---

## 💡 O Problema
No dia a dia comercial, analisar dezenas de propostas PDF exige muito tempo para identificar valores, itens e prazos. Soluções baseadas em nuvem (como OpenAI ou Gemini) podem gerar custos elevados e preocupações sobre o envio de dados sensíveis para servidores externos.

## 🚀 Minha Solução
Criei uma plataforma intuitiva utilizando **Python** e **Streamlit** que oferece:
* **Busca Otimizada:** Localização de arquivos por nome ou número em diretórios locais.
* **Resumo Automático:** Assim que o documento é carregado, a IA realiza uma leitura prévia e gera um resumo executivo (Cliente, Valor, Itens e Prazos) sem que o usuário precise perguntar.
* **Chat Contextual:** Interface de chat para perguntas específicas sobre o conteúdo do PDF selecionado.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.13:** Linguagem principal do projeto.
* **Streamlit:** Framework utilizado para construir a interface web moderna e responsiva.
* **Ollama (Modelo Llama 3.2:1b):** Motor de IA local. Escolhi este modelo por ser extremamente leve, rápido e possuir excelente compreensão do idioma português.
* **pdfplumber:** Biblioteca especializada para extração técnica de texto em arquivos PDF.
* **Session State:** Gerenciamento de estado do Streamlit para persistência do histórico de conversas e contexto.

---

## ⚙️ Arquitetura do Sistema

1.  **Indexação Local:** O sistema realiza uma varredura recursiva no diretório configurado, tratando caminhos de forma robusta com a biblioteca `os`.
2.  **Extração de Contexto:** O texto bruto é extraído e limpo para ser enviado como "base de conhecimento" para a IA.
3.  **Engenharia de Prompt:** Implementei instruções de sistema (System Prompts) para garantir que a IA mantenha um tom profissional e se limite estritamente às informações contidas no documento.

---

## 🔧 Como Rodar Este Projeto

### 1. Pré-requisitos
* Ter o **Python** instalado.
* Instalar o **Ollama** através do site oficial [ollama.com](https://ollama.com).

### 2. Configuração da IA
Abra o seu powershell e baixe o Ollama que utilizei no projeto:
```bash
irm https://ollama.com/install.ps1 | iex
```
### 3. executável
Para facilitar deixei um executável, mas so vai funcionar se tiver o python e o Ollama instalados

### 4. Qualquer dúvida pode entrar em contato
