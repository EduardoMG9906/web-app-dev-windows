SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP TABLE IF EXISTS `pacientes` ;


-- -----------------------------------------------------
-- Table `pacientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pacientes` (
  `id_paciente` INT NOT NULL AUTO_INCREMENT,
  `tipo_id` VARCHAR(45) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `grupo_sanguineo` VARCHAR(45) NOT NULL,
  `genero` VARCHAR(45) NOT NULL,
  `edad` INT NOT NULL,
  `fecha_nacimiento` DATE NOT NULL,
  `direccion` VARCHAR(45) NOT NULL,
  `celular` INT NOT NULL,
  `eps` VARCHAR(45) NOT NULL,
  `serial_hc` INT NOT NULL,
  PRIMARY KEY (`id_paciente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `medicamentos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `medicamentos` (
  `id_medicamento` INT NOT NULL AUTO_INCREMENT,
  `dosis` VARCHAR(45) NOT NULL,
  `via` VARCHAR(45) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `frecuencia_dia` INT NOT NULL,
  `duracion_dias` INT NOT NULL,
  `observaciones` TINYTEXT NULL,
  PRIMARY KEY (`id_medicamento`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

INSERT INTO pacientes (tipo_id, nombre, email, grupo_sanguineo, genero, edad, fecha_nacimiento, direccion, celular, eps, serial_hc)
VALUES
  ('CC', 'Juan Perez', 'juan@email.com', 'O+', 'Masculino', 25, '1998-05-15', 'Calle 123', 123456789, 'EPS_A', 98765),
  ('TI', 'Maria Lopez', 'maria@email.com', 'A-', 'Femenino', 30, '1993-08-20', 'Carrera 456', 987654321, 'EPS_B', 12345),
  ('CC', 'Pedro Ramirez', 'pedro@email.com', 'B+', 'Masculino', 35, '1988-12-10', 'Avenida 789', 555555555, 'EPS_C', 54321),
  ('CC', 'Ana Rodriguez', 'ana@email.com', 'AB+', 'Femenino', 28, '1995-03-03', 'Avenida 987', 111111111, 'EPS_D', 11111),
  ('TI', 'Carlos Gutierrez', 'carlos@email.com', 'O-', 'Masculino', 40, '1982-07-08', 'Calle 246', 222222222, 'EPS_E', 22222),
  ('CC', 'Luisa Hernandez', 'luisa@email.com', 'B-', 'Femenino', 22, '2001-11-25', 'Carrera 789', 333333333, 'EPS_F', 33333),
  ('TI', 'Gabriel Gomez', 'gabriel@email.com', 'A+', 'Masculino', 27, '1996-09-14', 'Avenida 345', 444444444, 'EPS_G', 44444),
  ('CC', 'Sofia Torres', 'sofia@email.com', 'AB-', 'Femenino', 33, '1989-04-18', 'Calle 567', 666666666, 'EPS_H', 66666),
  ('CC', 'Diego Silva', 'diego@email.com', 'O+', 'Masculino', 31, '1992-01-30', 'Carrera 123', 777777777, 'EPS_I', 77777),
  ('TI', 'Laura Perez', 'laura@email.com', 'A-', 'Femenino', 29, '1994-06-22', 'Avenida 678', 888888888, 'EPS_J', 88888);

INSERT INTO medicamentos (dosis, via, nombre, frecuencia_dia, duracion_dias, observaciones)
VALUES
  ('10 mg', 'Oral', 'Paracetamol', 3, 5, 'Tomar con comida'),
  ('25 mg', 'Intravenosa', 'Ibuprofeno', 2, 7, 'Evitar el alcohol'),
  ('50 mg', 'Oral', 'Amoxicilina', 1, 10, 'Completa el tratamiento'),
  ('15 mg', 'Subcutánea', 'Omeprazol', 1, 14, 'Tomar en ayunas'),
  ('30 mg', 'Oral', 'Aspirina', 2, 3, 'Evitar en caso de alergia'),
  ('20 mg', 'Intramuscular', 'Diazepam', 1, 7, 'Evitar la conducción'),
  ('40 mg', 'Oral', 'Loratadina', 1, 5, 'No mezclar con alcohol'),
  ('5 mg', 'Inhalada', 'Salbutamol', 4, 7, 'Usar según necesidad'),
  ('12.5 mg', 'Oral', 'Ciprofloxacina', 2, 10, 'Tomar con abundante agua'),
  ('8 mg', 'Intravenosa', 'Morfina', 3, 2, 'Solo bajo supervisión médica');
