grant select on all tables in schema public to planadmin, planmanager;

grant select, update, insert, delete on plan_data to planadmin, planmanager;

grant select, update, insert, delete on plan_status to planadmin;

grant select, update on plan_status to planmanager;

grant select, update, insert, delete on country_managers to planadmin;

grant select on country_managers to planmanager;

grant select on v_plan_edit to planadmin;

grant select, update on v_plan_edit to planmanager;

grant select on v_plan to planmanager, planadmin;

create user ivan with role planadmin;

create user sophie with role planmanager;

create user kirill with role planmanager;