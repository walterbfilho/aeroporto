import streamlit as st
import mysql.connector
import pandas as pd
import os

# FUNCAO para selecionar os dados OBS: NGM MEXE NESSE CONN AQUI OU EU MATO


def select_data(query):
    conn = mysql.connector.connect(
    user='root',
    password='root',
    host='mysql',
    database='db',
    port="3306"
    )
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

st.title("Operações no Banco de Dados")

operation = st.selectbox("Escolha a operação", ["Select Table", "Join Operation"])

# Seleção da tabela
table = st.selectbox("Escolha a tabela", ["aviao", "passageiro", "funcionario", "destinos", "voo", "reserva"])

# Seleção do join
if operation == "Join Operation":
    join_option = st.selectbox("Escolha o tipo de join", ["voo_aviao"])

# Realizar operações
if st.button("Executar"):
    if operation == "Select Table":
        query = f"SELECT * FROM {table}"
        data = select_data(query)
        st.write(f"Dados da tabela {table}:")
        if table == "aviao":
            df = pd.DataFrame(data, columns=["ID", "Modelo"])
        elif table == "passageiro":
            df = pd.DataFrame(data, columns=["CPF", "Nome"])
        elif table == "funcionario":
            df = pd.DataFrame(data, columns=["CPF", "Nome", "Cargo", "ID do Avião"])
        elif table == "destinos":
            df = pd.DataFrame(data, columns=["ID", "Local"])
        elif table == "voo":
            df = pd.DataFrame(data, columns=["ID", "ID do Destino", "ID do Avião"])
        elif table == "reserva":
            df = pd.DataFrame(data, columns=["ID do Voo", "CPF do Passageiro"])
        st.dataframe(df, width=800)
    
    elif operation == "Join Operation" and join_option == "voo_aviao":
        query = """
        SELECT voo.id AS VooID, destinos.local AS Destino, aviao.modelo AS AviaoModelo
        FROM voo
        JOIN destinos ON voo.fk_destinos_id = destinos.id
        JOIN aviao ON voo.fk_aviao_id = aviao.id
        """
        data = select_data(query)
        df = pd.DataFrame(data, columns=["VooID", "Destino", "AviaoModelo"])
        st.dataframe(df, width=800)
