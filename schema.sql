drop database if exists UniStay;
create database UniStay;
use UniStay;

create table user (
id int auto_increment not null primary key,
username varchar (250) not null,
password varchar (250) not null,
firstName varchar (50) not null,
lastName varchar (50) not null,
email varchar (50) not null
check (email regexp '^.+@.+\..+$'), -- check it is actual email (e.g. sungwoo@qut.edu.au)
phone varchar (10) not null 
check ((char_length(phone) = 10 and phone regexp '^04[0-9]{8}$')), -- check it is actual phone number in Australia (e.g. 0431234567)
avatarUrl varchar (250),
role varchar (20) not null
);

create table university (
id int auto_increment not null primary key,
name varchar (100) not null,
address varchar (250) not null,
logoUrl varchar (250) not null
);

create table property (
id int auto_increment not null primary key,
title varchar (100) not null,
address varchar (250) not null,
description varchar (1000) not null,
propertyType varchar (50) not null,
rentPerWeek int not null,
numBedrooms int not null,
numBathrooms int not null,
livingArea float not null,
availableDate Date not null,
agentId int not null,

foreign key (agentId) references user(id)
);

create table nearby (
propertyId int not null,
universityId int not null,
distance float not null,

primary key (propertyId, universityId),
foreign key (propertyId) references property(id) on delete cascade, 
foreign key (universityId) references university(id) on delete cascade
);

create table propertyAmenity (
propertyId int not null,
amenity varchar (50) not null,

primary key (propertyId, amenity),
foreign key (propertyId) references property(id) on delete cascade
);

create table propertyImage (
propertyId int not null,
url varchar(255) not null,
isPrimary boolean not null default False,

primary key (propertyId, url),
foreign key (propertyId) references property(id) on delete cascade
);

create table propertyDocumentation (
propertyId int not null,
url varchar(255) not null,

primary key (propertyId, url),
foreign key (propertyId) references property(id) on delete cascade
);

create table bookmark (
id int auto_increment not null primary key,
tenantId int not null,
propertyId int not null,
note varchar (1000),
createdAt Date not null,

foreign key (tenantId) references user(id) on delete cascade,
foreign key (propertyId) references property(id) on delete cascade
);

create table enquiry (
senderId int not null,
targetPropertyId int not null,
message varchar (1000) not null,
submittedDate date not null,
status varchar(50) not null,

primary key (senderId, targetPropertyId),
foreign key (senderId) references user(id) on delete cascade,
foreign key (targetPropertyId) references property(id) on delete cascade
);

create table offer ( -- for final submission
senderId int not null,
targetPropertyId int not null,
submittedDate date not null,
status varchar(50) not null,

primary key (senderId, targetPropertyId),
foreign key (senderId) references user(id) on delete cascade,
foreign key (targetPropertyId) references property(id) on delete cascade
); 