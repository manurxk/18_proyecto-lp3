-- Tabla de Persona (base para Paciente, Medico y Empleado)
CREATE TABLE Persona (
    id_persona INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    telefono VARCHAR(20),
    direccion VARCHAR(255)
);

-- Tabla de Pacientes (hereda de Persona)
CREATE TABLE Paciente (
    id_paciente INT PRIMARY KEY AUTO_INCREMENT,
    id_persona INT NOT NULL,
    FOREIGN KEY (id_persona) REFERENCES Persona(id_persona) ON DELETE CASCADE
);

-- Tabla de Médicos (hereda de Persona)
CREATE TABLE Medico (
    id_medico INT PRIMARY KEY AUTO_INCREMENT,
    id_persona INT NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100),
    FOREIGN KEY (id_persona) REFERENCES Persona(id_persona) ON DELETE CASCADE
);

-- Tabla de Empleados (hereda de Persona)
CREATE TABLE Empleado (
    id_empleado INT PRIMARY KEY AUTO_INCREMENT,
    id_persona INT NOT NULL,
    cargo VARCHAR(100) NOT NULL,
    fecha_contratacion DATE NOT NULL,
    salario DECIMAL(10, 2),
    FOREIGN KEY (id_persona) REFERENCES Persona(id_persona) ON DELETE CASCADE
);

-- Tabla de Agenda Médica
CREATE TABLE AgendaMedica (
    id_agenda INT PRIMARY KEY AUTO_INCREMENT,
    id_medico INT NOT NULL,
    fecha_agenda DATE NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    disponible BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_medico) REFERENCES Medico(id_medico) ON DELETE CASCADE
);

-- Tabla de Citas
CREATE TABLE Cita (
    id_cita INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT NOT NULL,
    id_agenda INT NOT NULL,
    estado_cita ENUM('Reservada', 'Confirmada', 'Anulada') NOT NULL,
    motivo_consulta VARCHAR(255),
    fecha_reservacion DATETIME NOT NULL,
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente) ON DELETE CASCADE,
    FOREIGN KEY (id_agenda) REFERENCES AgendaMedica(id_agenda) ON DELETE CASCADE
);

-- Tabla de Avisos Recordatorios
CREATE TABLE AvisoRecordatorio (
    id_aviso INT PRIMARY KEY AUTO_INCREMENT,
    id_cita INT NOT NULL,
    fecha_aviso DATE NOT NULL,
    mensaje_aviso VARCHAR(255) NOT NULL,
    FOREIGN KEY (id_cita) REFERENCES Cita(id_cita) ON DELETE CASCADE
);

-- Tabla de Documentos Médicos
CREATE TABLE DocumentoMedico (
    id_documento INT PRIMARY KEY AUTO_INCREMENT,
    id_paciente INT NOT NULL,
    tipo_documento ENUM('Receta', 'Examen', 'Informe') NOT NULL,
    nombre_archivo VARCHAR(255) NOT NULL,
    fecha_documento DATE NOT NULL,
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente) ON DELETE CASCADE
);
