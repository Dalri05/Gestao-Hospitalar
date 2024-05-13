CREATE TABLE IF NOT EXISTS pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INT,
    sexo TEXT,
    cpf VARCHAR(14) UNIQUE,
    endereco TEXT,
    telefone VARCHAR(20)
);
