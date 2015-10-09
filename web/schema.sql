
drop database if exists owesome;
create database owesome;
use owesome;

create table Users(
	`id` varchar(50) not null,
	primary key(`id`));