import streamlit as st
from app import responder, carregar_documentos


st.set_page_config(
    page_title="Alura Agent",
    page_icon="🤖"
)


st.title("🤖 Alura Agent")

st.write(
    "Assistente inteligente capaz de responder perguntas "
    "baseadas nos documentos da empresa."
)


st.divider()


@st.cache_resource(show_spinner="Carregando documentos...")
def inicializar():
    return carregar_documentos()


try:
    inicializar()
except Exception as erro:
    st.error(f"Não foi possível carregar os documentos: {erro}")
    st.stop()


pergunta = st.text_input(
    "Digite sua pergunta:"
)


if st.button("Enviar 🚀"):

    if pergunta:

        with st.spinner("Analisando documentos..."):

            resposta = responder(pergunta)

        st.success("Resposta encontrada!")

        st.subheader("Resposta:")

        st.write(resposta)

    else:
        st.warning("Digite uma pergunta antesde enviar.")