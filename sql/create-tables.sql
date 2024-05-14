USE aeroporto;

CREATE TABLE IF NOT EXISTS Aviao (
    id INTEGER PRIMARY KEY,
    modelo VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Passageiro (
    cpf VARCHAR(255) PRIMARY KEY UNIQUE,
    Nome VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS  Funcionario (
    cpf VARCHAR(255) PRIMARY KEY UNIQUE,
    Nome VARCHAR(255),
    cargo VARCHAR(255),
    fk_Aviao_id INTEGER,
    FOREIGN KEY (fk_Aviao_id) REFERENCES Aviao (id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS  Destinos (
    id INTEGER PRIMARY KEY,
    local VARCHAR(255),
    UNIQUE (local, id)
);

CREATE TABLE IF NOT EXISTS  Voo (
    id INTEGER PRIMARY KEY UNIQUE,
    fk_Destinos_id INTEGER,
    fk_Aviao_id INTEGER,
    FOREIGN KEY (fk_Destinos_id) REFERENCES Destinos (id) ON DELETE CASCADE,
    FOREIGN KEY (fk_Aviao_id) REFERENCES Aviao (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS  Reserva (
    fk_voo_id INTEGER,
    fk_passageiro_cpf VARCHAR(255),
    FOREIGN KEY (fk_voo_id) REFERENCES Voo (id),
    FOREIGN KEY (fk_passageiro_cpf) REFERENCES Passageiro (cpf)
);
