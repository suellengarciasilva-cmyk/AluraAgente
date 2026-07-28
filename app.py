import os
from dotenv import load_dotenv
from google import genai
from leitor_pdf import ler_pdfs

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "A variável de ambiente GEMINI_API_KEY não foi encontrada. "
        "Crie um arquivo .env com a linha: GEMINI_API_KEY=sua_chave_aqui"
    )

client = genai.Client(api_key=api_key)

_texto_documentos = None


def carregar_documentos():
    """
    Carrega o texto dos PDFs uma única vez e reaproveita
    nas próximas chamadas (evita reler os arquivos a cada pergunta).
    """
    global _texto_documentos

    if _texto_documentos is None:
        _texto_documentos = ler_pdfs()

    return _texto_documentos


def responder(pergunta):

    texto = carregar_documentos()

    prompt = f"""
    Responda a pergunta usando somente as informações dos documentos:

    {texto}

    Pergunta:
    {pergunta}
    """

    try:
        resposta = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )
        return resposta.text

    except Exception as erro:
        return f"⚠️ Ocorreu um erro ao consultar o modelo Gemini: {erro}"