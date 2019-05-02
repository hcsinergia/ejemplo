create database if not exists dbpyqt4;
use dbpyqt4;
create table if not exists Person(Per_Dni varchar(08) not null,
	Per_Names varchar(50) not null,
	Per_Surname varchar(50) not null,
	Per_Date Date not null,
	primary key(Per_Dni));
