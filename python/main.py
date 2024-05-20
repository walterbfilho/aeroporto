import mysql.connector
import streamlit as st
import pandas as pd

connection = mysql.connector.connect(
    user='root',
    password='root',
    host='127.0.0.1',
    port="3306",
    database='db'
    )

print("DB connected")

cursor = connection.cursor()

def close_connection():
    cursor.close()
    connection.close()

def insert_data(table, data):
    placeholders = ', '.join(['%s'] * len(data))
    query = f"INSERT INTO {table} VALUES ({placeholders})"
    cursor.execute(query, data)
    connection.commit()
    st.success(f'Dados inseridos em {table}.')

st.title("Aplicação de Gerenciamento de Dados")
option = st.sidebar.selectbox("Selecione a operação", ("Inserir", "Deletar", "Atualizar", "Select"))
table = st.sidebar.selectbox("Selecione a tabela", ("aviao", "destinos", "funcionario", "passageiro", "reserva", "voo"))

if option == "Inserir":
    if table == "aviao":
        id_aviao = st.number_input("Id do avião", min_value=0)
        modelo_aviao = st.text_input("Modelo do avião")
        if st.button("Inserir"):
            insert_data(table, (id_aviao, modelo_aviao))
    elif table == "destinos":
        id_destino = st.number_input("Id do destino", min_value=0)
        nome_destino = st.text_input("Nome do destino")
        if st.button("Inserir"):
            insert_data(table, (id_destino, nome_destino))
    elif table == "funcionario":
        cpf_funcionario = st.text_input("Cpf do funcionário")
        nome_funcionario = st.text_input("Nome do funcionário")
        cargo_funcionario = st.text_input("Cargo do funcionário")
        aviao_funcionario = st.number_input("Id do avião", min_value=0)
        if st.button("Inserir"):
            insert_data(table, (cpf_funcionario, nome_funcionario, cargo_funcionario, aviao_funcionario))
    elif table == "passageiro":
        cpf_passageiro = st.text_input("Cpf do passageiro")
        nome_passageiro = st.text_input("Nome do passageiro")
        if st.button("Inserir"):
            insert_data(table, (cpf_passageiro, nome_passageiro))
    elif table == "reserva":
        id_voo = st.number_input("Id do Vôo", min_value=0)
        cpf_reserva = st.text_input("Cpf do passageiro")
        if st.button("Inserir"):
            insert_data(table, (cpf_reserva, id_voo))
    elif table == "voo":
        id_voo = st.number_input("Id do Vôo", min_value=0)
        destino_voo = st.number_input("Id do destino", min_value=0)
        aviao_voo = st.number_input("Id do avião", min_value=0)
        if st.button("Inserir"):
            insert_data(table, (id_voo, destino_voo, aviao_voo))



st.sidebar.button("Fechar conexão", on_click=close_connection)