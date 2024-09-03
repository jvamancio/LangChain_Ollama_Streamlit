import streamlit as st
from teste import generate_response

# Título da aplicação
st.title("LangChain com Ollama e Streamlit")

# Entrada de texto para a pergunta do usuário
question = st.text_input("Digite sua pergunta:")

# Botão para submeter a pergunta
if st.button("Enviar"):
    # Se uma pergunta for submetida, gerar a resposta
    if question:
        response = generate_response(question)
        # Exibir a resposta na interface
        st.write(f"**Resposta:** {response}")
    else:
        st.write("Por favor, insira uma pergunta.")
