# 🤖 Alura Agent - Assistente Inteligente com Gemini

## 📌 Descrição

Este projeto foi desenvolvido como parte do Challenge Alura Agent.

O objetivo é criar um agente inteligente capaz de responder perguntas sobre documentos PDF de uma empresa utilizando Inteligência Artificial.

O sistema realiza a leitura automática dos arquivos PDF presentes na pasta **documentos**, envia as informações para o modelo Gemini e responde às perguntas feitas pelo usuário utilizando linguagem natural.

A aplicação possui uma interface web desenvolvida com Streamlit, permitindo uma interação simples e intuitiva com o usuário.

---

## 🚀 Tecnologias utilizadas

- Python 3
- Google Gemini API
- PyPDF
- Streamlit
- Python-dotenv
- VS Code

---

## 📁 Estrutura do projeto

AluraAgente/

├── documentos/  
│   ├── Guia Backend.pdf  
│   ├── Manual Onboarding.pdf  
│   ├── Arquitetura.pdf  
│   └── ...

├── app.py  
├── leitor_pdf.py  
├── interface.py  
├── requirements.txt  
├── README.md  
├── .gitignore  
└── .env  

---

## ⚙️ Como executar

Primeiro, clone o repositório:

git clone https://github.com/suellengarciasilva-cmyk/AluraAgente

Instale as dependências:

pip install -r requirements.txt

Configure a API Key do Gemini criando um arquivo chamado:

.env

Adicione sua chave:

GEMINI_API_KEY=SUA_CHAVE_AQUI

Para executar o agente pelo terminal:

python app.py

Para executar a interface web:

python -m streamlit run interface.py

A aplicação será aberta automaticamente no navegador.

---

## 💬 Exemplos de perguntas

- Como funciona o onboarding?
- Explique os procedimentos de engenharia back-end.
- O que são microsserviços?
- Quais são os padrões utilizados pela empresa?
- Como funciona o processo de resposta a incidentes?

---

## 🖥️ Interface da aplicação

O projeto possui uma interface web desenvolvida com Streamlit, permitindo que o usuário envie perguntas e receba respostas baseadas nos documentos disponibilizados.

Funcionalidades:

- Consulta inteligente aos documentos PDF
- Respostas utilizando Inteligência Artificial
- Interface web interativa
- Leitura automática de documentos
- Proteção da API Key através de variáveis de ambiente

---

## 📌 Exemplo de resposta

Pergunta:

Como funciona o onboarding?

Resposta:

O onboarding apresenta os procedimentos necessários para integração de novos desenvolvedores, incluindo configuração do ambiente, padrões de desenvolvimento e boas práticas adotadas pela empresa.

---

## 🔒 Segurança

A API Key do Gemini não fica exposta diretamente no código.

O projeto utiliza um arquivo `.env` para armazenar informações sensíveis e o `.gitignore` impede que esse arquivo seja enviado para o GitHub.

---

## 👩‍💻 Desenvolvido por

Suellen Garcia

Challenge Alura Agent
