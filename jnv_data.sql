-- create table
create table student(
	id integer primary key,
	name text NOT NULL,
	gender varchar(1),
	special varchar(1),
	nickname text,
	friend_id integer references House(id)
);

-- insert in table
insert into student(name,gender,special,friend_id,nickname) values ("Rahul",'M','Y',1,"Rafale");
insert into student(name,gender,special,friend_id,nickname) values ("Mudit",'M','N',2,"Haddi");
insert into student(name,gender,special,friend_id,nickname) values ("Govind",'M','Y',1,"Gobado");
insert into student(name,gender,special,friend_id,nickname) values ("Priya",'F','N',2,NULL);
insert into student(name,gender,special,friend_id,nickname) values ("Sumit",'M','Y',2,NULL);
insert into student(name,gender,special,friend_id,nickname) values ("Atul",'M','Y',2,"Baba");
insert into student(name,gender,special,friend_id,nickname) values ("Avinash",'M','Y',1,"Bora");
insert into student(name,gender,special,friend_id,nickname) values ("Vaishanvi",'F','N',2,NULL);
insert into student(name,gender,special,friend_id,nickname) values ("Umashanker",'M','Y',1,"Umado");
insert into student(name,gender,special,friend_id,nickname) values ("Smriti",'F','N',1,NULL);

-- Updating
update student set name="Rudra" where id=1;

-- Create new table
create table House(
	id integer primary key,
	name text not null,
	house_name text
);

insert into House(name,house_name) values ("Rahul","Udaigiri");
insert into House(name,house_name) values ("Mudit","Nilgiri");
insert into House(name,house_name) values ("Govind","Aravali");
insert into House(name,house_name) values ("Priya","Nilgiri");
insert into House(name,house_name) values ("Sumit","Shivalik");
insert into House(name,house_name) values ("Atul","Nilgiri");
insert into House(name,house_name) values ("Avinash","Aravali");
insert into House(name,house_name) values ("Vaishanvi","Nilgiri");
insert into House(name,house_name) values ("Umashanker","Nilgiri");
insert into House(name,house_name) values ("Smriti","Shivalik");

select s.name,s.gender,f.name from student s,House f where s.friend_id=f.id and f.House_name="Udaigiri";
