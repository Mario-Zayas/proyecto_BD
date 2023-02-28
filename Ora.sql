CREATE TABLE Entrenador (
   nlicencia NUMBER(5),
   nombre_entrenador VARCHAR2(30),
   email VARCHAR(50) NOT NULL,
   CONSTRAINT longitud_email CHECK (LENGTH(email) >= 20),
   CONSTRAINT formato_email CHECK (INSTR(email, '@') > 0),
   CONSTRAINT pk_nlicencia PRIMARY KEY (nlicencia)
);

create table Jugador (
   id_jugador number(3),
   nlicencia number(5),
   posicion_ant_camp number(4) null,
   coef_elo number(3) default 600,
   altura float,
   constraint altura_jugador check (altura >= 1.70 and altura <= 2.10),
   constraint pk_id_jugador primary key (id_jugador),
   constraint fk_nlicencia foreign key (nlicencia) references Entrenador (nlicencia)
);

create table Partidas (
   ncorrelativo_partida number(4),
   id_jugador number(3) not null,
   constraint pk_ncorrelativo_partida primary key (ncorrelativo_partida),
   constraint fk_id_jugador foreign key (id_jugador) references Jugador (id_jugador),
);