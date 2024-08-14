FROM mcr.microsoft.com/vscode/devcontainers/python:3.9-buster
RUN apt update 
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
