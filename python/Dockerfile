FROM python:3.9

WORKDIR /app

# Copiar o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Atualizar o pip para a versão mais recente
RUN pip install --upgrade pip

# Configurar um espelho de pacotes
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

# Instalar as dependências com timeout e retry
RUN pip install --default-timeout=100 --retries=10 --no-cache-dir -r requirements.txt

# Copiar o restante do código para o diretório de trabalho
COPY . .

# Comando para iniciar o aplicativo
CMD ["streamlit", "run", "main.py"]
