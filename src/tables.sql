CREATE TABLE IF NOT EXISTS ppal_table(
    cod_loc INT,
    id_provincia INT,
    id_departamento INT,
    categoria TEXT,
    provincia TEXT,
    fuente TEXT,
    localidad TEXT,
    nombre TEXT,
    descripcion TEXT,
    monumentos TEXT,
    museos TEXT,
    latitud FLOAT,
    longitud FLOAT,
    artesanias_tipicas TEXT,
    comidas_tipicas TEXT,
    sitios_de_interes TEXT
);
			

CREATE TABLE IF NOT EXISTS transformation_table(
    provincia TEXT,
    categoria TEXT,
    ferias INT,
    comidas_tipicas INT,
    museos INT

);