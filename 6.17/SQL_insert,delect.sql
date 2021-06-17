use tip;
select * from tips;
insert into tips (total_bill, tip, sex, smoker, day, time, size)
values (3.07, 1, 'null', 'Yes', 'Sun', 'Dinner', 3),
(3.07, 1, 'null', 'Yes', 'Sun', 'Dinner', 2);  #없는 값은 'null'로 넣으면 그 글자로 생각함
select * from tips where tips.sex='null';
delete from tips where tips.sex='null';
insert into tips (total_bill, tip, sex, smoker, day, time, size)
values (3.07, 1, 'Female', 'Yes', '', 'Dinner', 3),
(3.07, 1, 'Female', 'Yes', '', 'Dinner', 2);  #없는 값은 ''로 넣으면 오류
select * from tips where tips.day='';
delete from tips where tips.day='';
insert into tips (total_bill, tip, sex, smoker, day, time, size)
values (3.07, 1, NULL, 'Yes', 'Sun', 'Dinner', NULL),
(3.07, 1, 'Female', 'Yes', 'Sun', 'Dinner', NULL);  #없는 값은 항상 NULL꼴로 넣기
