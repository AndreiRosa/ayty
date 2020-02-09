CREATE DATABASE db_AYTY




---- TABELAS ----


CREATE TABLE call (
	id_call INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	extension CHAR(4),
	nu_ddd CHAR (2) NOT NULL, 
	nu_phone CHAR(9) NOT NULL, -- aceita números no formato NNNNNNNNN 
	dt_start date, 
	dt_answer date, 
	dt_finish date,
	id_extension int FOREIGN KEY REFERENCES extension(id_extension)
)

CREATE TABLE extent_event (
	id_exten_event INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	extension CHAR(4), 
	status VARCHAR (9),
	dt_event date,
	id_extension int FOREIGN KEY REFERENCES extension(id_extension)
)

CREATE TABLE extension (
	id_extension INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
	extension CHAR(4) NOT NULL, 
	nm_extension CHAR(4) NOT NULL, 
	is_active BIT NOT NULL, 
	must_record BIT NOT NULL, 
	number_transfer CHAR(9), 
	was_exported BIT NOT NULL, 
)




---- MÉTODOS ---- 


-- Criar uma chamada (call):
INSERT INTO call (extension, nu_ddd, nu_phone, dt_start, dt_answer, dt_finish, id_extension)
VALUES (extension, nu_ddd, nu_phone, dt_start, dt_answer, dt_finish, id_extension) -- ESSES VALORES SÃO VARIÁVEIS

-- Atualizar a data que ocorreu o evento da chamada:
-- dt_start (quando cria uma chamada) 
UPDATE call
SET dt_start = dt_start -- ESSE VALOR É VARIÁVEL
WHERE id_call = id_call -- ESSE VALOR É VARIÁVEL

-- dt_answer (quando a chamada é atendida) 
UPDATE call
SET dt_answer = dt_answer -- ESSE VALOR É VARIÁVEL
WHERE id_call = id_call -- ESSE VALOR É VARIÁVEL

-- dt_finish (quando a chamada é finalizada) 
UPDATE call
SET dt_finish = dt_finish -- ESSE VALOR É VARIÁVEL
WHERE id_call = id_call -- ESSE VALOR É VARIÁVEL

-- Criar eventos do ramal (exten_event). Status permitidos: ring, in_call, available:
INSERT INTO exten_event (extension, status, dt_event, id_extension)
VALUES (extension, status, dt_event, id_extension) -- ESSES VALORES SÃO VARIÁVEIS

-- Criar um ramal (extension):
INSERT INTO extension (extension, nm_extension, is_active, must_record, number_transfer, was_exported)
VALUES (extension, nm_extension, is_active, must_record, number_transfer, was_exported) -- ESSES VALORES SÃO VARIÁVEIS

-- Atualizar um ramal (extension). Para cada atualização was_exported = 0:
UPDATE extension
SET nm_extension = nm_extension, -- ESSE VALOR É VARIÁVEL
	is_active = is_active, -- ESSE VALOR É VARIÁVEL
	must_record = must_record, -- ESSE VALOR É VARIÁVEL
	number_transfer = number_transfer, -- ESSE VALOR É VARIÁVEL
	was_exported = 0
WHERE id_extension = id_extension -- ESSE VALOR É VARIÁVEL

-- Deletar um ramal (extension):
DELETE FROM extension
WHERE id_extension = id_extension -- ESSE VALOR É VARIÁVEL

-- Consultar um ramal (extension):
SELECT * FROM extension
WHERE id_extension = id_extension -- ESSE VALOR É VARIÁVEL

-- Consultar todas os ramais (extension):
SELECT * FROM extension

-- Consultar a duração total de uma chamada (call):
SELECT dt_answer, dt_finish, DATEDIFF (minute, dt_answer, dt_finish) as call_duration FROM call
WHERE id_call = id_call -- ESSE VALOR É VARIÁVEL

-- Consultar todas as chamadas (call) de um ramal (extension) em uma data especifica:
SELECT * FROM call
WHERE (id_extension LIKE id_extension) AND (dt_start LIKE dt_start) -- ESSES VALORES SÃO VARIÁVEIS  (ACHO QUE A PARTE DA DATA TA ERRADA)

-- Consultar os eventos (exten_event) de um ramal (extension) em uma data especifica:
SELECT * FROM exten_event
WHERE (id_extension LIKE id_extension) AND (dt_event LIKE dt_event) -- ESSES VALORES SÃO VARIÁVEIS


