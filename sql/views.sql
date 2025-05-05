-- Vista: transacciones completas
CREATE VIEW vista_transacciones AS
SELECT t.id, t.tipo, t.monto, t.fecha,
       co.numero_cuenta AS cuenta_origen,
       cd.numero_cuenta AS cuenta_destino
FROM transacciones t
LEFT JOIN cuentas co ON t.cuenta_origen_id = co.id
LEFT JOIN cuentas cd ON t.cuenta_destino_id = cd.id;

-- Vista: extracto por cuenta
CREATE VIEW extracto_por_cuenta AS
SELECT 
  t.id,
  t.tipo,
  t.monto,
  t.fecha,
  co.numero_cuenta AS origen,
  cd.numero_cuenta AS destino
FROM transacciones t
LEFT JOIN cuentas co ON t.cuenta_origen_id = co.id
LEFT JOIN cuentas cd ON t.cuenta_destino_id = cd.id;

-- Vista: clientes con sus saldos totales
CREATE VIEW clientes_con_saldos AS
SELECT 
  cl.id,
  cl.nombre,
  cl.apellido,
  cl.dni,
  SUM(c.saldo) AS saldo_total
FROM clientes cl
JOIN cuentas c ON c.cliente_id = cl.id
GROUP BY cl.id;
