create table Entrenador (
    nlicencia int (5),
    nombre_entrenador varchar(30),
    email varchar (50) NOT NULL,
    constraint pk_nlicencia primary key (nlicencia),
    constraint longitud_email CHECK (LENGTH(email) >= 20),
    constraint formato_email CHECK (LOCATE ('@', email) > 0)
);

create table Jugador (
    id_jugador int(3),
    nlicencia int (5),
    posicion_ant_camp int (4) null,
    coef_elo int(3) default 600,
    altura float,
    constraint altura_jugador check (altura >= 1.70 and altura <= 2.10),
    constraint pk_id_jugador primary key (id_jugador),
    constraint fk_nlicencia foreign key (nlicencia) references Entrenador (nlicencia)
);

create table Partidas (
    ncorrelativo_partida int(4),
    id_jugador int(3),
    constraint pk_ncorrelativo_partida primary key (ncorrelativo_partida),
    constraint fk_id_jugador foreign key (id_jugador) references Jugador (id_jugador)
);