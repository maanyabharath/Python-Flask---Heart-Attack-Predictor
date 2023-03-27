create database dbms;
use dbms;
create table doctor(dr_username varchar(20) unique, dr_name varchar(30), dr_pass varchar(15));

insert into doctor values("DoctorRakesh","Rakesh Raj","p1");
insert into doctor values("DoctorParthiv","Parthiv Yagnesh","p2");
insert into doctor values("DoctorHashim","Hashim Faisal","p3");
insert into doctor values("DoctorBadhri","Badhri KV","p4");
insert into doctor values("DoctorAnjana","Anjana Anand","p5");
insert into doctor values("DoctorMohit","Mohit Avva","p6");
insert into doctor values("DoctorAkshat","Akshat Kaimal","p7");
insert into doctor values("DoctorRaj","Rajsekar Balaji","p8");
insert into doctor values("DoctorRam","Ram Lakshmi","p9");
insert into doctor values("DoctorPravalika","Pravalika Arunkumar","p10");
insert into doctor values("DoctorRahul","Rahul M","p11");
insert into doctor values("DoctorRohan","Rohan Suresh","p12");
insert into doctor values("DoctorShashank","Shashank Kannan","p13");
s
select * from doctor;
