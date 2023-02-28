create table Entrenador (
    nlicencia numeric (5),
    nombre_entrenador varchar(30),
    email varchar (50) NOT NULL,
    constraint pk_nlicencia primary key (nlicencia),
    constraint longitud_email CHECK (LENGTH(email) >= 20),
    constraint formato_email CHECK (POSITION ('@' in email) > 0)
);

create table Jugador (
    id_jugador numeric(3),
    nlicencia numeric (5) references Entrenador (nlicencia),
    posicion_ant_camp numeric (4) null,
    coef_elo numeric(3) default 600,
    altura float,
    constraint altura_jugador check (altura >= 1.70 and altura <= 2.10),
    constraint pk_id_jugador primary key (id_jugador)
);

create table Partidas (
    ncorrelativo_partida numeric(4),
    id_jugador numeric(3) references Jugador (id_jugador),
    constraint pk_ncorrelativo_partida primary key (ncorrelativo_partida)
);