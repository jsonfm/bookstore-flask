-- roles
INSERT INTO user_roles (role)
VALUES 
("ADMIN"),
("USER"),
("SUPPORT"),
("API");

-- users
-- secreto12: $2b$12$NBCYrq1EzQHEMzzhGW223OUVGQ10.P1Y4WD/pXq67hsFmllZepLMu
INSERT INTO users (email, password, role_id)
VALUES 
("test1@gmail.com", "$2b$12$NBCYrq1EzQHEMzzhGW223OUVGQ10.P1Y4WD/pXq67hsFmllZepLMu", 1),
("test2@gmail.com", "$2b$12$NBCYrq1EzQHEMzzhGW223OUVGQ10.P1Y4WD/pXq67hsFmllZepLMu", 1),
("test3@gmail.com", "$2b$12$NBCYrq1EzQHEMzzhGW223OUVGQ10.P1Y4WD/pXq67hsFmllZepLMu", 2),
("test4@gmail.com", "$2b$12$NBCYrq1EzQHEMzzhGW223OUVGQ10.P1Y4WD/pXq67hsFmllZepLMu", 3),
("test5@gmail.com", "$2b$12$NBCYrq1EzQHEMzzhGW223OUVGQ10.P1Y4WD/pXq67hsFmllZepLMu", 4),


INSERT INTO profiles (first_name, last_name, user_id)
VALUES
("Profile 1111", "Test", 1),
("Profile 2222", "Test", 2),
("Profile 3333", "Test", 3),
("Profile 4444", "Test", 4),
("Profile 5555", "Test", 5);