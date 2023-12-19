CREATE DATABASE IF NOT EXISTS library;

USE library;

CREATE TABLE pelicula(
	pel_id INT NOT NULL AUTO_INCREMENT, 
    pel_titulo VARCHAR(30) NOT NULL, 
    pel_genero VARCHAR(30) NOT NULL,
    pel_clas ENUM('A', 'AA', 'B', 'B15', 'C', 'D') NOT NULL,
    pel_duracion INT NOT NULL COMMENT 'La duracion se da en minutos',
    pel_director VARCHAR(40) NOT NULL,
    pel_fecha_estreno DATE NOT NULL,  
    PRIMARY KEY (pel_id),
    INDEX (pel_titulo),
    INDEX(pel_genero),
    INDEX (pel_clas),
    UNIQUE(pel_titulo, pel_fecha_estreno)
);

CREATE TABLE actor(
	act_id INT NOT NULL AUTO_INCREMENT,
    act_nombre VARCHAR(50) NOT NULL,
    act_nombre_real VARCHAR(50),
    act_fecha_nac DATE,
    act_genero ENUM('M', 'H', 'Otro') NOT NULL,
    act_pais_nac VARCHAR(40),
    PRIMARY KEY(act_id),
    INDEX(act_nombre),
    INDEX(act_pais_nac),
    UNIQUE(act_nombre_real, act_fecha_nac)
);

CREATE TABLE elenco(
	ele_pel_id INT NOT NULL,
    ele_act_id INT NOT NULL,
    ele_personaje VARCHAR(40) NOT NULL,
    ele_salario DECIMAL(15,2) NOT NULL COMMENT 'Salario en USD',
    ele_papel ENUM('protagonico', 'soporte', 'extra') NOT NULL,
    PRIMARY KEY (ele_pel_id, ele_act_id),
    CONSTRAINT fk_pelicula_elenco
		FOREIGN KEY (ele_pel_id)
        REFERENCES pelicula(pel_id)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
	CONSTRAINT fk_actor_elenco
		FOREIGN KEY(ele_act_id)
        REFERENCES actor(act_id)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT
);

INSERT INTO pelicula( pel_titulo, pel_genero, pel_clas, pel_duracion, pel_director, pel_fecha_estreno)
	VALUES( 'Ciudades de Papel', 'Drama', 'B','145', 'Edward Muller', '2019-08-01'),  
			('Yo antes de ti', 'Drama','A' ,'160', 'Michael J', '2019-01-19'),
			('El hoyo', 'Drama','C', '138', 'Alfonso Perez', '2019-01-10'),  
            ('A dos metros de ti', 'Drama','B', '167', 'Armando Ramos', '2021-08-10'),
            ('Bajo Cero', 'Accion','C', '170', 'Fabiola R', '2002-03-14'), 
            ('John Wick', 'Accion','B', '130', 'Polo Ruiz', '2012-08-01'),
            ('Spiderman', 'Accion','B', '180', 'Edward Muller', '2011-06-16'),
            ('¿Que le pasó a lunes?', 'Accion','B', '167', 'Edward Muller',  '2013-11-28'),
            ('La mascara', 'Fantasia','C', '150', 'Angel Lopez',  '2014-07-10'),
            ('Paul', 'Fantasia','C', '160', 'Demetrio Rodriguez', '2015-10-10'),
            ('Lucy', 'Fantasia','D', '125', 'Paola Oros',  '2016-11-16'), 
            ('Volver al futuro', 'Fantasia','B', '155', 'Amanda Miguel', '2017-10-10'),
            ('La casa de los abuelos', 'Terror','B', '170', 'Edward Muller', '2019-08-01'),  
            ('Masacre en Texas', 'Terror','C', '190', 'Edgar Torres',  '2022-10-10'),
             ('La noche del demonio', 'Terror','B', '165', 'Francia C',  '2010-07-29'),
             ('Veronica', 'Terror','D', '140', 'Sandra Polo',  '2020-08-10');

INSERT INTO actor( act_nombre, act_nombre_real,act_fecha_nac, act_genero, act_pais_nac)
	VALUES ('Salma Hayek','Salma Valgarma Hayek','1966-09-02','M', 'Mexico'),
    ('Eugenio Derbez','Eugenio Gonzalez Derbez','1961-09-02','H',  'Mexico'),
    ('Diego Luna','Diego Luna Alexander','1979-12-29', 'H','Mexico'),
    ('Robert Downey Jr','Robert Downey Jr','1965-04-04', 'H', 'Estados Unidos'),
     ('Chris Evans','Christoper Robert Evans','1981-06-13', 'H', 'Estados Unidos'),
      ('Adam Sandler','Adam Richard Sandler','1966-09-09', 'H','Estados Unidos'),
       ('Tom Holland','Thomas Stanley Holland','1996-06-01', 'H', 'Reino Unido'),
        ('Andrew Garfield','Andrew Rusell Garfield','1983-08-20', 'H', 'Reino Unido'),
         ('Ciaran Madden','Ciaran Madden','1942-12-27','H', 'Reino Unido');

INSERT INTO actor( act_nombre, act_nombre_real,act_fecha_nac, act_genero, act_pais_nac)
	VALUES ('Eiza Gonzalez','Eiza González Reyna','1990-01-30','M', 'Mexico');
    

INSERT INTO elenco (ele_pel_id, ele_act_id, ele_personaje, ele_salario, ele_papel)
VALUES (1 , 3, 'Uriel Zair', '1330050', 'Soporte'),
(2 , 4, 'Emilio Martinez', '2500000', 'Extra'),
(3, 5, 'Ximena Medel Gallardo', '13020000', 'Protagonico'),
(3, 7, 'Pancha Francisca', '24632000', 'Protagonico'),
(1, 8, 'Emiliano Flores', '2500000', 'Protagonico'),
(3, 2, 'Anatomi', '13004340', 'Protagonico'),
(4, 1, 'Adelita Martinez', '2500000', 'Extra'),
(1, 2, 'Jose Luis', '12344000', 'Soporte'),
(3, 4, 'Roberto Carlos', '2500000', 'Extra'),
(2, 9, 'Jason Ramirez', '5300000', 'Extra'),
(1, 7, 'Sierra Villasenor', '2500000', 'Extra'),
(2, 6, 'Benito Martinez', '1304000', 'Extra'),
(7, 2, 'Miguel Angel', '2500000', 'Extra'),
(2, 1, 'Matias', '1300001', 'Extra'),
(9, 3, 'Santiago', '22000080', 'Extra'),
(5, 6, 'Leonardo', '9800000', 'Extra'),
(3, 1, 'Emiliano', '1500000', 'Extra'),
(8, 3, 'Hector', '1500500', 'Extra'),
(4, 6, 'Emiliano Flores', '2500000', 'Extra'),
(6, 9, 'Diego', '1320200', 'Extra'),
(8, 2, 'Sebastian', '7500000', 'Extra'),
(8, 1, 'Camila', '1300090', 'Extra'),
(3, 8, 'Maria Fernanda', '1500000', 'Extra'),
(5, 2, 'Maria Jose', '1300040', 'Extra'),
(5, 1, 'Renata', '2300000', 'Extra'),
(9, 5, 'Victoria', '1300050', 'Extra'),
(5, 5, 'Sofia', '2500200', 'Extra'),
(2, 2, 'Valentina', '1300001', 'Extra'),
(1, 1, 'Maria Fernanda', '2503000', 'Extra'),
(4, 4, 'Valeria', '1100000', 'Extra'),
(4, 3, 'Mateo', '3500000', 'Extra');