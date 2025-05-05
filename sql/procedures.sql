DELIMITER //
CREATE PROCEDURE hacer_extraccion(IN cuenta INT, IN monto DECIMAL(15,2))
BEGIN
  UPDATE cuentas SET saldo = saldo - monto WHERE id = cuenta;
  INSERT INTO transacciones (tipo, monto, cuenta_origen_id)
  VALUES ('Extracción', monto, cuenta);
END;
//
DELIMITER ;
