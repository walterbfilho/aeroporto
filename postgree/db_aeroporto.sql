-- Criação das tabelas

CREATE TABLE IF NOT EXISTS aviao (
    id SERIAL PRIMARY KEY,
    modelo VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS passageiro (
    cpf VARCHAR(255) PRIMARY KEY UNIQUE,
    nome VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS funcionario (
    cpf VARCHAR(255) PRIMARY KEY UNIQUE,
    nome VARCHAR(255),
    cargo VARCHAR(255),
    fk_aviao_id INTEGER,
    FOREIGN KEY (fk_aviao_id) REFERENCES aviao(id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS destinos (
    id SERIAL PRIMARY KEY,
    local VARCHAR(255) UNIQUE
);

CREATE TABLE IF NOT EXISTS voo (
    id SERIAL PRIMARY KEY,
    fk_destinos_id INTEGER,
    fk_aviao_id INTEGER,
    FOREIGN KEY (fk_destinos_id) REFERENCES destinos(id) ON DELETE RESTRICT,
    FOREIGN KEY (fk_aviao_id) REFERENCES aviao(id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS reserva (
    fk_voo_id INTEGER,
    fk_passageiro_cpf VARCHAR(255),
    PRIMARY KEY (fk_voo_id, fk_passageiro_cpf),
    FOREIGN KEY (fk_voo_id) REFERENCES voo(id) ON DELETE RESTRICT,
    FOREIGN KEY (fk_passageiro_cpf) REFERENCES passageiro(cpf) ON DELETE RESTRICT
);
