CREATE TABLE estado_agenda_medica (
    id SERIAL PRIMARY KEY,
    descripcion VARCHAR(60) UNIQUE NOT NULL
);

CREATE TABLE especialidades (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(60) UNIQUE NOT NULL
);

CREATE TABLE consultorios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(60) UNIQUE NOT NULL
);

CREATE TABLE horarios (
    id SERIAL PRIMARY KEY,
    dia_semana VARCHAR(15) NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    UNIQUE(dia_semana, hora_inicio, hora_fin)
);

CREATE TABLE personas (
    id SERIAL PRIMARY KEY,
    nombres VARCHAR(70) NOT NULL,
    apellidos VARCHAR(70) NOT NULL,
    cedula_identidad TEXT NOT NULL,
    fecha_nacimiento DATE,
    telefono VARCHAR(15),
    email VARCHAR(70),
    creacion_fecha DATE NOT NULL,
    creacion_hora TIME NOT NULL,
    creacion_usuario INTEGER NOT NULL,
    modificacion_fecha DATE,
    modificacion_hora TIME,
    modificacion_usuario INTEGER
);

CREATE TABLE medicos (
    id SERIAL PRIMARY KEY,
    id_persona INTEGER NOT NULL,
    id_especialidad INTEGER NOT NULL,
    fecha_ingreso DATE NOT NULL,
    FOREIGN KEY(id_persona) REFERENCES personas(id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(id_especialidad) REFERENCES especialidades(id)
    ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    estado BOOLEAN NOT NULL
);

CREATE TABLE agenda_medica (
    id SERIAL PRIMARY KEY,
    id_medico INTEGER NOT NULL,
    id_persona INTEGER NOT NULL,
    id_estado INTEGER NOT NULL,
    id_consultorio INTEGER NOT NULL,
    id_horario INTEGER NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY(id_medico) REFERENCES medicos(id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(id_persona) REFERENCES personas(id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(id_estado) REFERENCES estado_agenda_medica(id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(id_consultorio) REFERENCES consultorios(id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(id_horario) REFERENCES horarios(id)
    ON DELETE RESTRICT ON UPDATE CASCADE
);































INSERT INTO consultorios (nombre) VALUES
('Psicología Infantil'),
('Terapia Familiar'),
('Psicoterapia Individual');

INSERT INTO estado_agenda_medica (descripcion) VALUES
('Pendiente'),
('Confirmada'),
('Cancelada');

INSERT INTO especialidades (nombre) VALUES
('Psicología Clínica'),
('Psicología Educativa'),
('Neuropsicología');

INSERT INTO personas (nombres, apellidos, cedula_identidad, fecha_nacimiento, telefono, email, creacion_fecha, creacion_hora, creacion_usuario) VALUES
('Ana', 'Gómez', '12345678', '1985-06-15', '0981123456', 'ana.gomez@example.com', CURRENT_DATE, CURRENT_TIME, 1),
('Carlos', 'Pérez', '87654321', '1990-08-20', '0981987654', 'carlos.perez@example.com', CURRENT_DATE, CURRENT_TIME, 1),
('María', 'López', '45678912', '1982-01-12', '0981123123', 'maria.lopez@example.com', CURRENT_DATE, CURRENT_TIME, 1);

INSERT INTO medicos (id_persona, id_especialidad, fecha_ingreso) VALUES
(1, 1, '2020-03-15'),
(2, 2, '2021-05-20'),
(3, 3, '2019-11-01');

INSERT INTO horarios (dia_semana, hora_inicio, hora_fin) VALUES
('Lunes', '08:00:00', '12:00:00'),
('Martes', '13:00:00', '17:00:00'),
('Miércoles', '08:00:00', '12:00:00');