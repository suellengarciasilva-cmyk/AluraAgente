import os
from pypdf import PdfReader


def ler_pdfs():
    """
    Lê todos os arquivos PDF da pasta 'documentos' e retorna
    o texto extraído de todos eles, concatenado em uma única string.
    """

    pasta_documentos = "documentos"

    if not os.path.isdir(pasta_documentos):
        raise FileNotFoundError(
            f"A pasta '{pasta_documentos}' não foi encontrada. "
            "Crie a pasta e adicione os arquivos PDF antes de executar o agente."
        )

    arquivos = [
        arquivo for arquivo in os.listdir(pasta_documentos)
        if arquivo.lower().endswith(".pdf")
    ]

    if not arquivos:
        raise FileNotFoundError(
            f"Nenhum arquivo PDF foi encontrado na pasta '{pasta_documentos}'."
        )

    texto_completo = ""

    for arquivo in arquivos:
        caminho = os.path.join(pasta_documentos, arquivo)

        try:
            leitor = PdfReader(caminho)

            for pagina in leitor.pages:
                texto = pagina.extract_text()

                if texto:
                    texto_completo += texto + "\n"

        except Exception as erro:
            print(f"⚠️ Não foi possível ler o arquivo '{arquivo}': {erro}")
            continue

    return texto_completo