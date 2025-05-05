CREATE DATABASE IF NOT EXISTS banco;
USE banco;

-- Clientes
CREATE TABLE clientes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100),
  apellido VARCHAR(100),
  dni VARCHAR(20) UNIQUE,
  direccion VARCHAR(200),
  telefono VARCHAR(20),
  email VARCHAR(100)
);

-- Cuentas
CREATE TABLE cuentas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  numero_cuenta VARCHAR(20) UNIQUE,
  tipo ENUM('Caja de ahorro', 'Cuenta corriente'),
  saldo DECIMAL(15,2) DEFAULT 0.00,
  cliente_id INT,
  FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- Transacciones
CREATE TABLE transacciones (
  id INT AUTO_INCREMENT PRIMARY KEY,
  tipo ENUM('Depósito', 'Extracción', 'Transferencia'),
  monto DECIMAL(15,2),
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
  cuenta_origen_id INT,
  cuenta_destino_id INT,
  FOREIGN KEY (cuenta_origen_id) REFERENCES cuentas(id),
  FOREIGN KEY (cuenta_destino_id) REFERENCES cuentas(id)
);
