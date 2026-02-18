import streamlit as st
import os
import pdfplumber
import ollama

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="IA de leitura de arquivos pdf",
                   layout="wide", page_icon="📊")

# Caminho da sua pasta de PDFs
PASTA_PDFS = r"D:\Propostas"

# --- FUNÇÕES ---


def buscar_pdfs(termo):
    """Retorna os caminhos completos dos arquivos que combinam com a busca."""
    arquivos_completos = []
    if os.path.exists(PASTA_PDFS):
        for raiz, _, arquivos in os.walk(PASTA_PDFS):
            for f in arquivos:
                if termo.lower() in f.lower() and f.lower().endswith(".pdf"):
                    arquivos_completos.append(os.path.join(raiz, f))
    return arquivos_completos


def ler_conteudo_pdf(caminho):
    """Extrai o texto bruto do PDF."""
    texto = ""
    try:
        with pdfplumber.open(caminho) as pdf:
            for pagina in pdf.pages:
                t = pagina.extract_text()
                if t:
                    texto += t + "\n"
    except Exception as e:
        return f"Erro ao ler arquivo: {e}"
    return texto


# --- ESTADO DA SESSÃO ---
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []
if "contexto_pdf" not in st.session_state:
    st.session_state.contexto_pdf = ""

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("🔍 Localizar Proposta")
    termo_busca = st.text_input("Digite o número ou nome:")

    if termo_busca:
        resultados = buscar_pdfs(termo_busca)

        if resultados:
            # format_func garante que apareça apenas o NOME do arquivo, não o caminho
            arquivo_selecionado = st.selectbox(
                "Selecione o arquivo:",
                options=resultados,
                format_func=os.path.basename
            )

            if st.button("Carregar e Resumir"):
                with st.spinner("Processando documento..."):
                    # 1. Extração
                    conteudo = ler_conteudo_pdf(arquivo_selecionado)
                    st.session_state.contexto_pdf = conteudo
                    st.session_state.mensagens = []  # Limpa chat para nova proposta

                    # 2. Resumo Automático
                    try:
                        nome_limpo = os.path.basename(arquivo_selecionado)
                        prompt_resumo = (
                            f"Você é um assistente de IA. Analise o texto do PDF'{nome_limpo}' abaixo "
                            f"e forneça um resumo profissional rápido contendo as principais informações encontradas do PDF \n"
                            # PARA PROPOSTA COMERCIAL
                            # f"- Nome do cliente/empresa\n"
                            # f"- Valor total\n"
                            # f"- Principais produtos/serviços\n"
                            # f"- Prazo de entrega ou validade (se houver).\n\n"
                            f"TEXTO DO PDF:\n{conteudo[:6000]}"
                        )

                        response = ollama.chat(model='llama3.2:1b', messages=[
                            {'role': 'user', 'content': prompt_resumo},
                        ])

                        resumo_ia = response['message']['content']

                        # 3. Salvar no histórico como se fosse a primeira resposta da IA
                        st.session_state.mensagens.append({
                            "role": "assistant",
                            "content": f"### 📝 Resumo Automático do PDF: {nome_limpo}\n\n{resumo_ia}"
                        })
                        st.success("Documento carregado com sucesso!")

                    except Exception as e:
                        st.error(f"Erro ao gerar resumo: {e}")
        else:
            st.warning("Nenhum PDF encontrado.")

# --- CHAT INTERFACE ---
st.title("💬 Chat Inteligente")

# Mostrar histórico (incluindo o resumo automático que geramos acima)
for m in st.session_state.mensagens:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# Campo para novas perguntas
if pergunta := st.chat_input("Deseja saber algo mais sobre esta proposta?"):

    # Adiciona pergunta do usuário
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    # Resposta da IA baseada no contexto
    if not st.session_state.contexto_pdf:
        st.error("Por favor, carregue um arquivo na lateral primeiro.")
    else:
        with st.chat_message("assistant"):
            with st.spinner("Analisando..."):
                try:
                    prompt_chat = (
                        f"Baseado no texto da proposta fornecido abaixo, responda à pergunta do usuário.\n\n"
                        f"TEXTO:\n{st.session_state.contexto_pdf[:6000]}\n\n"
                        f"PERGUNTA: {pergunta}"
                    )

                    response = ollama.chat(model='llama3.2:1b', messages=[
                        {'role': 'user', 'content': prompt_chat},
                    ])

                    resposta_final = response['message']['content']
                    st.markdown(resposta_final)
                    st.session_state.mensagens.append(
                        {"role": "assistant", "content": resposta_final})

                except Exception as e:
                    st.error("Erro ao conectar com Ollama.")
