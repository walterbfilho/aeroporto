USE db;

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
    fk_aviao_id BIGINT UNSIGNED,
    FOREIGN KEY (fk_aviao_id) REFERENCES aviao(id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS destinos (
    id SERIAL PRIMARY KEY,
    local VARCHAR(255) UNIQUE
);

CREATE TABLE IF NOT EXISTS voo (
    id SERIAL PRIMARY KEY,
    fk_destinos_id BIGINT UNSIGNED,
    fk_aviao_id BIGINT UNSIGNED,
    FOREIGN KEY (fk_destinos_id) REFERENCES destinos(id) ON DELETE RESTRICT,
    FOREIGN KEY (fk_aviao_id) REFERENCES aviao(id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS reserva (
    fk_voo_id BIGINT UNSIGNED,
    fk_passageiro_cpf VARCHAR(255),
    PRIMARY KEY (fk_voo_id, fk_passageiro_cpf),
    FOREIGN KEY (fk_voo_id) REFERENCES voo(id) ON DELETE RESTRICT,
    FOREIGN KEY (fk_passageiro_cpf) REFERENCES passageiro(cpf) ON DELETE RESTRICT
);
INSERT INTO aviao (id, modelo) VALUES
(1, 'Boeing 737'),
(2, 'Airbus A320'),
(3, 'Embraer E195'),
(4, 'Boeing 787'),
(5, 'Airbus A380'),
(6, 'Cessna 172');

INSERT INTO passageiro (cpf, nome) VALUES
('12345678900', 'Alice Silva'),
('23456789012', 'Bruno Souza'),
('34567890123', 'Carla Dias'),
('45678901234', 'Daniel Costa'),
('56789012345', 'Eva Martins'),
('67890123456', 'Felipe Lima');

INSERT INTO funcionario (cpf, nome, cargo, fk_aviao_id) VALUES
('78901234567', 'Gabriel Rocha', 'Piloto', 1),
('89012345678', 'Helena Alves', 'Copiloto', 2),
('90123456789', 'Igor Mendes', 'Comissário', 3),
('01234567890', 'Julia Nunes', 'Piloto', 4),
('12345678001', 'Lucas Pereira', 'Comissário', 5),
('23456789023', 'Mariana Ferreira', 'Comissário', 6);

INSERT INTO destinos (id, local) VALUES
(1, 'Nova York'),
(2, 'Paris'),
(3, 'Tóquio'),
(4, 'Londres'),
(5, 'Sydney'),
(6, 'Rio de Janeiro');

INSERT INTO voo (id, fk_destinos_id, fk_aviao_id) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6);

INSERT INTO reserva (fk_voo_id, fk_passageiro_cpf) VALUES
(1, '12345678900'),
(1, '23456789012'),
(2, '34567890123'),
(3, '45678901234'),
(4, '56789012345'),
(5, '67890123456');
