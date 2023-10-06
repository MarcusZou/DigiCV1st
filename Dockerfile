# app/Dockerfile

FROM python:3.10-slim

WORKDIR /app

RUN apt-get update 
#RUN apt-get install -y build-essential curl git software-properties-common && rm -rf /var/lib/apt/lists/*
#RUN git clone https://github.com/streamlit/streamlit-example.git .
COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8501

#HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]