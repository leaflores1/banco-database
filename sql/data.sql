-- Clientes de prueba
INSERT INTO clientes (nombre, apellido, dni, direccion, telefono, email)
VALUES 
('Leandro', 'Flores', '12345678', 'Calle Falsa 123', '2611234567', 'leandro@mail.com');

-- Cuentas de prueba
INSERT INTO cuentas (numero_cuenta, tipo, saldo, cliente_id)
VALUES 
('0001-000001', 'Caja de ahorro', 10000.00, 1),
('0001-000002', 'Caja de ahorro', 5000.00, 1);

-- Transacciones de prueba
INSERT INTO transacciones (tipo, monto, cuenta_origen_id)
VALUES ('Extracción', 2000.00, 1);

INSERT INTO transacciones (tipo, monto, cuenta_origen_id, cuenta_destino_id)
VALUES ('Transferencia', 1000.00, 1, 2);
