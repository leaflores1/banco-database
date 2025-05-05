-- Ver clientes
SELECT * FROM clientes;

-- Ver transacciones de la cuenta 1
SELECT * FROM extracto_por_cuenta WHERE origen = '0001-000001' OR destino = '0001-000001';
