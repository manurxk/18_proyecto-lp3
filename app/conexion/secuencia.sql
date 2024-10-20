-- Tabla de Países
CREATE TABLE Pais (
    id_pais INT PRIMARY KEY AUTO_INCREMENT,
    nombre_pais VARCHAR(100) NOT NULL
);

-- Tabla de Ciudades
CREATE TABLE Ciudad (
    id_ciudad INT PRIMARY KEY AUTO_INCREMENT,
    nombre_ciudad VARCHAR(100) NOT NULL,
    id_pais INT NOT NULL,
    FOREIGN KEY (id_pais) REFERENCES Pais(id_pais) ON DELETE CASCADE
);

-- Tabla de Nacionalidades
CREATE TABLE Nacionalidad (
    id_nacionalidad INT PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(100) NOT NULL
);

-- Tabla de Estado Civil
CREATE TABLE EstadoCivil (
    id_estado_civil INT PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(50) NOT NULL
);

-- Tabla de Sexos
CREATE TABLE Sexo (
    id_sexo INT PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(50) NOT NULL
);

-- Tabla Persona
CREATE TABLE Persona (
    id_persona INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    telefono VARCHAR(20),
    direccion VARCHAR(255),
    id_ciudad INT,
    id_pais INT,
    id_nacionalidad INT,
    id_estado_civil INT,
    id_sexo INT,
    FOREIGN KEY (id_ciudad) REFERENCES Ciudad(id_ciudad) ON DELETE SET NULL,
    FOREIGN KEY (id_pais) REFERENCES Pais(id_pais) ON DELETE SET NULL,
    FOREIGN KEY (id_nacionalidad) REFERENCES Nacionalidad(id_nacionalidad) ON DELETE SET NULL,
    FOREIGN KEY (id_estado_civil) REFERENCES EstadoCivil(id_estado_civil) ON DELETE SET NULL,
    FOREIGN KEY (id_sexo) REFERENCES Sexo(id_sexo) ON DELETE SET NULL
);

-- Tabla Pacientes
CREATE TABLE Paciente (
    id_paciente INT PRIMARY KEY AUTO_INCREMENT,
    id_persona INT NOT NULL,
    FOREIGN KEY (id_persona) REFERENCES Persona(id_persona) ON DELETE CASCADE
);

-- Tabla de Médicos
CREATE TABLE Medico (
    id_medico INT PRIMARY KEY AUTO_INCREMENT,
    id_persona INT NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100),
    FOREIGN KEY (id_persona) REFERENCES Persona(id_persona) ON DELETE CASCADE
);

-- Tabla de Empleados
CREATE TABLE Empleado (
    id_empleado INT PRIMARY KEY AUTO_INCREMENT,
    id_persona INT NOT NULL,
    cargo VARCHAR(100) NOT NULL,
    fecha_contratacion DATE NOT NULL,
    salario DECIMAL(10, 2),
    FOREIGN KEY (id_persona) REFERENCES Persona(id_persona) ON DELETE CASCADE
);

-- Tabla de Citas
CREATE TABLE Cita (
    id_cita INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT NOT NULL,
    id_medico INT NOT NULL,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    motivo_consulta VARCHAR(255) NOT NULL,
    estado VARCHAR(50),
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente) ON DELETE CASCADE,
    FOREIGN KEY (id_medico) REFERENCES Medico(id_medico) ON DELETE CASCADE
);

-- Tabla de Documentos Relacionados a Ficha Médica del Paciente
CREATE TABLE DocumentoFicha (
    id_documento INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT NOT NULL,
    tipo_documento VARCHAR(100),
    descripcion TEXT,
    archivo LONGBLOB,
    fecha_subida DATE NOT NULL,
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente) ON DELETE CASCADE
);

-- Tabla de Avisos Recordatorios
CREATE TABLE AvisoRecordatorio (
    id_aviso INT PRIMARY KEY AUTO_INCREMENT,
    id_cita INT NOT NULL,
    mensaje TEXT NOT NULL,
    fecha_envio DATE NOT NULL,
    enviado BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_cita) REFERENCES Cita(id_cita) ON DELETE CASCADE
);

-- Tabla para la Gestión de Estados de Cita (Reservación, Confirmación, Anulación)
CREATE TABLE EstadoCita (
    id_estado_cita INT PRIMARY KEY AUTO_INCREMENT,
    id_cita INT NOT NULL,
    estado VARCHAR(50) NOT NULL,
    fecha_actualizacion DATE NOT NULL,
    FOREIGN KEY (id_cita) REFERENCES Cita(id_cita) ON DELETE CASCADE
);
