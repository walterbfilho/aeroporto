import streamlit as st
import mysql.connector
import pandas as pd
import os

# Função para selecionar dados
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

# Função para inserir dados
def insert_data(table, data):
    conn = mysql.connector.connect(
        user='root',
        password='root',
        host='mysql',
        database='db',
        port="3306"
    )
    cursor = conn.cursor()
    query = f"INSERT INTO {table} VALUES ({', '.join(['%s']*len(data))})"
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
    conn.close()
    st.success(f'Dados inseridos em {table}.')

# Função para deletar dados
def delete_data(table, condition_column, condition_value):
    conn = mysql.connector.connect(
        user='root',
        password='root',
        host='mysql',
        database='db',
        port="3306"
    )
    cursor = conn.cursor()
    query = f"DELETE FROM {table} WHERE {condition_column} = %s"
    cursor.execute(query, (condition_value,))
    conn.commit()
    cursor.close()
    conn.close()
    st.success(f'Dados deletados de {table}.')

# Função para atualizar dados
def update_data(table, set_column, set_value, condition_column, condition_value):
    conn = mysql.connector.connect(
        user='root',
        password='root',
        host='mysql',
        database='db',
        port="3306"
    )
    cursor = conn.cursor()
    query = f"UPDATE {table} SET {set_column} = %s WHERE {condition_column} = %s"
    cursor.execute(query, (set_value, condition_value))
    conn.commit()
    cursor.close()
    conn.close()
    st.success(f'Dados atualizados em {table}.')

# Interface
st.title("Operações no Banco de Dados")
operation = st.sidebar.selectbox("Selecione a operação", ("Inserir", "Deletar", "Atualizar", "Read", "Join Operation"))

if operation != "Join Operation":
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
    if table == "aviao":
        query = f"SELECT * FROM {table}"
        data = select_data(query)
        st.write(f"Dados da tabela {table}:")    
        df = pd.DataFrame(data, columns=["ID", "Modelo"])
    elif table == "passageiro":
        query = f"SELECT * FROM {table}"
        data = select_data(query)
        st.write(f"Dados da tabela {table}:")
        df = pd.DataFrame(data, columns=["CPF", "Nome"])
    elif table == "funcionario":
        query = f"SELECT * FROM {table}"
        data = select_data(query)
        st.write(f"Dados da tabela {table}:")    
        df = pd.DataFrame(data, columns=["CPF", "Nome", "Cargo", "ID do Avião"])
    elif table == "destinos":
        query = f"SELECT * FROM {table}"
        data = select_data(query)
        st.write(f"Dados da tabela {table}:")
        df = pd.DataFrame(data, columns=["ID", "Local"])

    elif table == "voo":
        query = """
        SELECT voo.id AS VooID, destinos.local AS Destino, aviao.modelo AS AviaoModelo
        FROM voo
        JOIN destinos ON voo.fk_destinos_id = destinos.id
        JOIN aviao ON voo.fk_aviao_id = aviao.id
        """
        data = select_data(query)
        st.write(f"Dados da tabela {table}:")
        df = pd.DataFrame(data, columns=["VooID", "Destino", "AviaoModelo"])
    elif table == "reserva":
        query = f"SELECT * FROM {table}"
        data = select_data(query)
        st.write(f"Dados da tabela {table}:")
        df = pd.DataFrame(data, columns=["ID do Voo", "CPF do Passageiro"])
    st.dataframe(df, width=800)

# Join Operation
elif operation == "Join Operation":
    join_option = st.selectbox("Escolha o tipo de join", ["voo_aviao","reserva_passageiro_voo"])
    if join_option == "voo_aviao":
        query = """
        SELECT voo.id AS VooID, destinos.local AS Destino, aviao.modelo AS AviaoModelo
        FROM voo
        JOIN destinos ON voo.fk_destinos_id = destinos.id
        JOIN aviao ON voo.fk_aviao_id = aviao.id
        """
        data = select_data(query)
        df = pd.DataFrame(data, columns=["VooID", "Destino", "AviaoModelo"])
        st.dataframe(df, width=800)
    elif join_option == "reserva_passageiro_voo":
            query = """
            SELECT 
                reserva.fk_voo_id AS VooID, 
                voo.fk_destinos_id AS DestinoID, 
                destinos.local AS Destino, 
                reserva.fk_passageiro_cpf AS PassageiroCPF, 
                passageiro.nome AS PassageiroNome
            FROM 
                reserva
            JOIN 
                voo ON reserva.fk_voo_id = voo.id
            JOIN 
                destinos ON voo.fk_destinos_id = destinos.id
            JOIN 
                passageiro ON reserva.fk_passageiro_cpf = passageiro.cpf;
            """
            data = select_data(query)
            df = pd.DataFrame(data, columns=["VooID", "DestinoID", "Destino", "PassageiroCPF", "PassageiroNome"])
            st.dataframe(df, width=800)