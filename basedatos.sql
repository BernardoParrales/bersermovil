-- Active: 1712879366114@@localhost@3306@master_python
CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE numeros_telefonos(
    id_numero int(25) auto_increment not null,
    persona_id int(25),
    saldo_id int(25),
    numero_telefono varchar(10),
    estado varchar(10),
    CONSTRAINT pk_numeros_telefonos PRIMARY KEY(id_numero),
    CONSTRAINT uq_numero UNIQUE(numero_telefono)
)ENGINE=InnoDb;

CREATE TABLE personas(
    id_persona  int(25) auto_increment not null,
    nombre      varchar(100),
    apellido   varchar(255),
    cedula VARCHAR(10),
    CONSTRAINT pk_personas PRIMARY KEY(id_persona),
    CONSTRAINT uq_cedula  UNIQUE(cedula)
)ENGINE=InnoDb;

CREATE TABLE saldos(
    id_saldo int(25) auto_increment not null,
    saldo_dolares float unsigned,
    saldo_megas int unsigned,
    CONSTRAINT pk_saldos PRIMARY KEY(id_saldo)
)ENGINE=InnoDb;

CREATE TABLE paquetes(
    id_paquete INT(25) AUTO_INCREMENT NOT NULL,
    costo FLOAT UNSIGNED NOT NULL,
    descripcion VARCHAR(200) NOT NULL,
    saldo_megas FLOAT UNSIGNED NOT NULL,
    dias INT(3) UNSIGNED NOT NULL,
    CONSTRAINT pk_paquetes PRIMARY KEY(id_paquete)
)ENGINE=InnoDb;

CREATE TABLE bancos(
    id_banco INT(25) AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    CONSTRAINT pk_bancos PRIMARY KEY(id_banco)
)ENGINE=InnoDb;

CREATE TABLE cuentas_bancarias(
    id INT(25) AUTO_INCREMENT NOT NULL,
    persona_id INT(25) NOT NULL,
    banco_id INT(25) NOT NULL,
    saldo FLOAT UNSIGNED,
    CONSTRAINT pk_cuentas_bancarias PRIMARY KEY(id),
    CONSTRAINT fk_personas FOREIGN KEY(persona_id) REFERENCES personas(id_persona),
    CONSTRAINT fk_bancos FOREIGN KEY(banco_id) REFERENCES bancos(id_banco)
)ENGINE=InnoDb;
