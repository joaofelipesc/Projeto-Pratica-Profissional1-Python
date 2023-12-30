CREATE TABLE ACADEMIA.Clientes(
  Id_Cliente INT PRIMARY KEY NOT NULL,
  Nome VARCHAR(30),
  DataNasc DATE,
  Sexo CHAR(1),
  Telefone VARCHAR(11),
  Email VARCHAR(50),
  Endereco VARCHAR(100)
);
CREATE TABLE ACADEMIA.Professor (
  Id_Professor INT PRIMARY KEY NOT NULL,
  Nome VARCHAR(30),
  Telefone VARCHAR(11),
  Email VARCHAR(30)
);

CREATE TABLE ACADEMIA.Especialidade (
  IdEspecialidade INT PRIMARY KEY NOT NULL,
  Descricao NVARCHAR(20)
);

CREATE TABLE ACADEMIA.ProfessorEspecialidade (
  Id_Professor INT,
  IdEspecialidade INT,
  PRIMARY KEY (Id_Professor, IdEspecialidade),
  FOREIGN KEY (Id_Professor) REFERENCES ACADEMIA.Professor(Id_Professor),
  FOREIGN KEY (IdEspecialidade) REFERENCES ACADEMIA.Especialidade(IdEspecialidade)
);

CREATE TABLE ACADEMIA.Planos(
  Id_Plano INT PRIMARY KEY NOT NULL,
  IdEspecialidade int ,
  Nome VARCHAR(30),
  Descricao VARCHAR(100),
  DuracaoEmMeses INT,
  Valor FLOAT,
  foreign key (IdEspecialidade) references ACADEMIA.Especialidade(IdEspecialidade)
);


CREATE TABLE ACADEMIA.Matricula(
  Id_Matricula INT PRIMARY KEY,
  Id_Cliente INT NOT NULL,
  Id_Plano INT NOT NULL,
  DataInicio DATE NOT NULL,
  DataFim DATE NOT NULL,
  FOREIGN KEY (Id_Cliente) REFERENCES ACADEMIA.Clientes(Id_Cliente),
  FOREIGN KEY (Id_Plano) REFERENCES ACADEMIA.Planos(Id_Plano)
);

INSERT INTO ACADEMIA.Especialidade (IdEspecialidade, Descricao)
VALUES (20, 'Area de Academia');

INSERT INTO ACADEMIA.Especialidade (IdEspecialidade, Descricao)
VALUES (21, 'Dança');

INSERT INTO ACADEMIA.Especialidade (IdEspecialidade, Descricao)
VALUES (22, 'Pilates');

INSERT INTO ACADEMIA.Especialidade (IdEspecialidade, Descricao)
VALUES (23, 'Artes Marciais');


INSERT INTO ACADEMIA.Professor (Id_Professor, Nome, Telefone, Email)
VALUES (101, 'Marcelo Ter', '19988653225', 'marckungfu@gmail.com');
-- Especialidade: Musculação em geral
INSERT INTO ACADEMIA.Professor (Id_Professor, Nome, Telefone, Email)
VALUES (102, 'João Silva', '19998887766', 'joaosilva@gmail.com');

-- Especialidade: Cardiorrespiratório
INSERT INTO ACADEMIA.Professor (Id_Professor, Nome, Telefone, Email)
VALUES (103, 'Maria Santos', '19997776655', 'mariasantos@gmail.com');

-- Especialidade: Pilates
INSERT INTO ACADEMIA.Professor (Id_Professor, Nome, Telefone, Email)
VALUES (104, 'Ana Oliveira', '19996665544', 'anaoliveira@gmail.com');






-- Especialidade: Musculação em geral
INSERT INTO ACADEMIA.Professor (Id_Professor, Nome, Telefone, Email)
VALUES (105, 'Carlos Mendes', '19995554433', 'carlosmendes@gmail.com');

-- Especialidade: Cardiorrespiratório
INSERT INTO ACADEMIA.Professor (Id_Professor, Nome, Telefone, Email)
VALUES (106, 'Laura Ferreira', '19994443322', 'lauraferreira@gmail.com');

-- Especialidade: Pilates
INSERT INTO ACADEMIA.Professor (Id_Professor, Nome, Telefone, Email)
VALUES (107, 'Pedro Almeida', '19993332211', 'pedroalmeida@gmail.com');



-- Especialidade: Artes Marciais
INSERT INTO ACADEMIA.Professor (Id_Professor, Nome, Telefone, Email)
VALUES (108, 'Renato Oliveira', '19992222111', 'renatooliveira@gmail.com');


SELECT P.Id_Professor, P.Nome, E.IdEspecialidade, E.Descricao
FROM ACADEMIA.Professor P
INNER JOIN ACADEMIA.Especialidade E ON P.Id_Professor = E.IdEspecialidade;
SELECT  * from academia.Clientes


drop table academia.Planos
drop table academia.Professor
drop table academia.Especialidade
drop table academia.Matricula
drop table academia.Clientes

select * from ACADEMIA.clientes

select * from ACADEMIA.especialidade
select * from ACADEMIA.professor
 select * from ACADEMIA.ProfessorEspecialidade

 -- Remover a chave estrangeira existente
ALTER TABLE ACADEMIA.Planos
DROP CONSTRAINT FK__Planos__IdEspeci__7226EDCC;

-- Remover a coluna IdEspecialidade
ALTER TABLE ACADEMIA.Planos
DROP COLUMN IdEspecialidade;

-- Criar a tabela de associação
CREATE TABLE ACADEMIA.PlanoEspecialidade (
  Id_Plano INT,
  IdEspecialidade INT,
  PRIMARY KEY (Id_Plano, IdEspecialidade),
  FOREIGN KEY (Id_Plano) REFERENCES ACADEMIA.Planos(Id_Plano),
  FOREIGN KEY (IdEspecialidade) REFERENCES ACADEMIA.Especialidade(IdEspecialidade)
);
select * from ACADEMIA.clientes
delete from ACADEMIA.clientes where id_cliente = 110

select * from ACADEMIA.planos


INSERT INTO ACADEMIA.Matricula (Id_Cliente, Id_Plano, Id_Matricula, DataInicio, DataFim) VALUES (100, 3, 1001, '2023/06/21', '2023/07/21')

delete from academia.matricula where id_matricula = 1001
select * from Academia.matricula
SELECT M.*, C.Nome AS NomeCliente
        FROM ACADEMIA.Matricula AS M
        INNER JOIN ACADEMIA.Clientes AS C ON M.Id_Cliente = C.Id_Cliente