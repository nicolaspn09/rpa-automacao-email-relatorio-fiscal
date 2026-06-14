#Importações das bibliotecas
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from logExecucaoCodigos import grava_log_execucao_sql
import locale
import smtplib
import time
import os
import requests
import psycopg2


#Envia e-mail para os usuários
def envia_email_execucao(mensagemEmail, destinatarios_email, assunto_email): 
    """
    Envia e-mail para os usuários

    Parameters:
    pass # Logica de negocio removida por seguranca corporativa

def conecta_pg(sql):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_pg_insert(sql):
    pass # Logica de negocio removida por seguranca corporativa

def envia_email(destinatarios, assunto, mensagem_email, cc=None, bcc=None):
    pass # Logica de negocio removida por seguranca corporativa

def envia_backup(assunto, corpo_email, itens, destinatario_principal, destinatario_copia, destinatario_copia_oculta, data_envio, situacao_rpa):
    pass # Logica de negocio removida por seguranca corporativa

def exclui_linha(linha):
    pass # Logica de negocio removida por seguranca corporativa

def obtem_informacoes_envio():
    pass # Logica de negocio removida por seguranca corporativa
