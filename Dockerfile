# 1. Escolhe a imagem base (o sistema operacional + linguagem)
FROM python:3.10-slim

# 2. Define o diretório de trabalho dentro do container
WORKDIR /app

# 3. Copia o arquivo de dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia o restante do código do seu projeto para o container
COPY . .

# 5. Expõe a porta que a sua aplicação usa (ex: 8000 para um app web)
EXPOSE 8000

# 6. Comando para iniciar a aplicação
CMD ["python", "meu_app.py"]