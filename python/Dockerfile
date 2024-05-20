# Use a imagem oficial do Python como base
FROM python:3.9

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o conteúdo do diretório atual para o diretório de trabalho no container
COPY . .

# Exponha a porta que a aplicação Streamlit usará
EXPOSE 8501

# Comando para rodar a aplicação
CMD ["streamlit", "run", "main.py"]
