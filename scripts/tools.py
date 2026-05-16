import dados as dd
import sys
import os
from datetime import datetime
import time
import json

# FUNÇÕES ADMINISTRATIVAS -------------------------------------

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_hora():
    agora = datetime.now()
    br = agora.strftime("%d/%m/%Y - %H:%M:%S")
    return br

def escrever_lento(palavra):
    for letra in palavra:
        print(letra, end='', flush=True)
        time.sleep(0.05)
    print()

def escrever_menu(texto, pular_linha=True):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(0.05)
    
    if pular_linha:
        print()

# Caminho para o arquivo JSON
ARQUIVO_JSON = "votos.json"

def carregar_dados():
    """Lê o arquivo JSON. Se não existir, cria um com dados padrão."""
    if not os.path.exists(ARQUIVO_JSON):
        dados_padrao = [
            {"candidato": "FELIPE", "votos": 0},
            {"candidato": "GONZALEZ", "votos": 0}
        ]
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
            json.dump(dados_padrao, f, indent=4, ensure_ascii=False)
        return dados_padrao
    
    with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(dados):
    """Grava as alterações de volta no arquivo JSON."""
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# SISTEMAS -------------------------------------

def mostrar_candidatos():
    for t, c in enumerate(dd.candidatos, start=1):
        print(f"{t} - {c['candidato']:<14} | N° de votos: {c['votos']}")

def encerrar():
    print("="*10)
    print("ENCERRANDO...")
    print("="*10)
