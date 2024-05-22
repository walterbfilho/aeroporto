import streamlit as st
import pandas as pd
import mysql.connector
import os

# Conexão com o banco de dados MySQL
conn = mysql.connector.connect(
    user='root',
    password='root',
    host='mysql',
    database='db',
    port="3306"
)
cursor = conn.cursor()

# Insert
def insert_data(table, data):
    query = f"INSERT INTO {table} VALUES ({', '.join(['%s']*len(data))})"
    cursor.execute(query, data)
    conn.commit()
    st.success(f'Dados inseridos em {table}.')

# Delete
def delete_data(table, condition_column, condition_value):
    query = f"DELETE FROM {table} WHERE {condition_column} = %s"
    cursor.execute(query, (condition_value,))
    conn.commit()
    st.success(f'Dados deletados de {table}.')

# Update
def update_data(table, set_column, set_value, condition_column, condition_value):
    query = f"UPDATE {table} SET {set_column} = %s WHERE {condition_column} = %s"
    cursor.execute(query, (set_value, condition_value))
    conn.commit()
    st.success(f'Dados atualizados em {table}.')

# read
def select_data(query):
    cursor.execute(query)
    data = cursor.fetchall()
    return data

# Interface
st.title("Aplicação de Gerenciamento de Dados")
operation = st.sidebar.selectbox("Selecione a operação", ("Inserir", "Deletar", "Atualizar", "Read"))
table = st.sidebar.selectbox("Selecione a tabela", ("aviao", "passageiro", "funcionario", "destinos", "voo", "reserva"))

# Inserir
if operation == "Inserir":
    if table == "aviao":
        id = st.number_input("ID do Avião", min_value=0)
        modelo = st.text_input("Modelo do Avião")
        if st.button("Inserir"):
            insert_data(table, (id, modelo))
    elif table == "passageiro":
        cpf = st.text_input("CPF do Passageiro")
        nome = st.text_input("Nome do Passageiro")
        if st.button("Inserir"):
            insert_data(table, (cpf, nome))
    elif table == "funcionario":
        cpf = st.text_input("CPF do Funcionário")
        nome = st.text_input("Nome do Funcionário")
        cargo = st.text_input("Cargo do Funcionário")
        fk_aviao_id = st.number_input("ID do Avião", min_value=0)
        if st.button("Inserir"):
            insert_data(table, (cpf, nome, cargo, fk_aviao_id))
    elif table == "destinos":
        id = st.number_input("ID do Destino", min_value=0)
        local = st.text_input("Local do Destino")
        if st.button("Inserir"):
            insert_data(table, (id, local))
    elif table == "voo":
        id = st.number_input("ID do Voo", min_value=0)
        fk_destinos_id = st.number_input("ID do Destino", min_value=0)
        fk_aviao_id = st.number_input("ID do Avião", min_value=0)
        if st.button("Inserir"):
            insert_data(table, (id, fk_destinos_id, fk_aviao_id))
    elif table == "reserva":
        fk_voo_id = st.number_input("ID do Voo", min_value=0)
        fk_passageiro_cpf = st.text_input("CPF do Passageiro")
        if st.button("Inserir"):
            insert_data(table, (fk_voo_id, fk_passageiro_cpf))

# Deletar
elif operation == "Deletar":
    condition_value = None
    condition_column = None
    if table == "aviao":
        condition_column = "id"
        condition_value = st.number_input("ID do Avião a ser deletado", min_value=0)
    elif table == "passageiro":
        condition_column = "cpf"
        condition_value = st.text_input("CPF do Passageiro a ser deletado")
    elif table == "funcionario":
        condition_column = "cpf"
        condition_value = st.text_input("CPF do Funcionário a ser deletado")
    elif table == "destinos":
        condition_column = "id"
        condition_value = st.number_input("ID do Destino a ser deletado", min_value=0)
    elif table == "voo":
        condition_column = "id"
        condition_value = st.number_input("ID do Voo a ser deletado", min_value=0)
    elif table == "reserva":
        condition_column = "fk_voo_id"
        condition_value = st.number_input("ID do Voo a ser deletado da reserva", min_value=0)
    if st.button("Deletar"):
        delete_data(table, condition_column, condition_value)

# Atualizar
elif operation == "Atualizar":
    if table == "aviao":
        id = st.number_input("ID do Avião a ser atualizado", min_value=0)
        novo_modelo = st.text_input("Novo Modelo do Avião")
        if st.button("Atualizar"):
            update_data(table, "modelo", novo_modelo, "id", id)
    elif table == "passageiro":
        cpf = st.text_input("CPF do Passageiro a ser atualizado")
        novo_nome = st.text_input("Novo Nome do Passageiro")
        if st.button("Atualizar"):
            update_data(table, "nome", novo_nome, "cpf", cpf)
    elif table == "funcionario":
        cpf = st.text_input("CPF do Funcionário a ser atualizado")
        novo_nome = st.text_input("Novo Nome do Funcionário")
        novo_cargo = st.text_input("Novo Cargo do Funcionário")
        novo_fk_aviao_id = st.number_input("Novo ID do Avião", min_value=0)
        if st.button("Atualizar"):
            update_data(table, "nome", novo_nome, "cpf", cpf)
            update_data(table, "cargo", novo_cargo, "cpf", cpf)
            update_data(table, "fk_aviao_id", novo_fk_aviao_id, "cpf", cpf)
    elif table == "destinos":
        id = st.number_input("ID do Destino a ser atualizado", min_value=0)
        novo_local = st.text_input("Novo Local do Destino")
        if st.button("Atualizar"):
            update_data(table, "local", novo_local, "id", id)
    elif table == "voo":
        id = st.number_input("ID do Voo a ser atualizado", min_value=0)
        novo_fk_destinos_id = st.number_input("Novo ID do Destino", min_value=0)
        novo_fk_aviao_id = st.number_input("Novo ID do Avião", min_value=0)
        if st.button("Atualizar"):
            update_data(table, "fk_destinos_id", novo_fk_destinos_id, "id", id)
            update_data(table, "fk_aviao_id", novo_fk_aviao_id, "id", id)
    elif table == "reserva":
        fk_voo_id = st.number_input("ID do Voo a ser atualizado na reserva", min_value=0)
        novo_fk_passageiro_cpf = st.text_input("Novo CPF do Passageiro")
        if st.button("Atualizar"):
            update_data(table, "fk_passageiro_cpf", novo_fk_passageiro_cpf, "fk_voo_id", fk_voo_id)

# Read
elif operation == 'Read':
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

cursor.close()
conn.close()
