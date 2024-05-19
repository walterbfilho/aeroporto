use db;

CREATE TABLE IF NOT EXISTS aviao (
    id INTEGER PRIMARY KEY,
    modelo VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS passageiro (
    cpf VARCHAR(255) PRIMARY KEY UNIQUE,
    Nome VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS funcionario (
    cpf VARCHAR(255) PRIMARY KEY UNIQUE,
    Nome VARCHAR(255),
    cargo VARCHAR(255),
    fk_Aviao_id INTEGER,
    FOREIGN KEY (fk_Aviao_id) REFERENCES aviao (id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS destinos (
    id INTEGER PRIMARY KEY,
    local VARCHAR(255),
    UNIQUE (local, id)
);

CREATE TABLE IF NOT EXISTS voo (
    id INTEGER PRIMARY KEY UNIQUE,
    fk_Destinos_id INTEGER,
    fk_Aviao_id INTEGER,
    FOREIGN KEY (fk_Destinos_id) REFERENCES destinos (id) ON DELETE CASCADE,
    FOREIGN KEY (fk_Aviao_id) REFERENCES aviao (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS reserva (
    fk_voo_id INTEGER,
    fk_passageiro_cpf VARCHAR(255),
    FOREIGN KEY (fk_voo_id) REFERENCES voo (id),
    FOREIGN KEY (fk_passageiro_cpf) REFERENCES passageiro (cpf)
);