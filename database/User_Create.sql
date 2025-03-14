--CREATE USER AND ROLE
CREATE USER Naveen;
CREATE ROLE management_system_role;

--GRANT ACCESS TO DATABASE
GRANT ALL PRIVILEGES ON management_system.* TO 'management_system_role'@'%';
GRANT management_system_role to Naveen;