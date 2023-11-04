-- Editorials
INSERT INTO editorials (name, description) 
VALUES 
('Alianza Editorial', 'Editorial'),
('Tusquets Editores', 'Editorial'),
('Herder', 'Editorial'),
('Planeta', 'Editorial'),
('Plutón ediciones', 'Editorial');


-- Authors
INSERT INTO authors (name, bio)
VALUES
('Viktor Frankl', ''),
('Milan Kundera', ''),
('Haruki Murakami', ''),
('Friedrich Nietzsche', ''),
('Herman Hesse', '');


-- Genres
INSERT INTO genres (name)
VALUES
('Literatura'), 
('Economía'),
('Filosofía'),
('Negocios'),
('Historia'),
('Política'),
('Finanzas'),
('Psicología'),
('Autoayuda'),
('Misterio'),
('Suspense'),
('Thriller'),
('Romance');


-- books
INSERT INTO books 
(name, description, is_active, cover, author_id, editorial_id, genre_id)
VALUES
('El hombre en busca de sentido', '...', true, 'cover', 1, 3, 3),
('Contra el vacío existencial', '...', true, 'cover', 1, 3, 3),
('La insoportable levedad del ser', '...', true, 'cover', 2, 2, 1),
('La inmortalidad', '...', true, 'cover', 2, 2, 1),
('Kafka en la Orilla', '...', true, 'cover', 3, 2, 1),
('Tokyo Blues', '...', true, 'cover', 3, 2, 1),
('El Anticristo', '...', true, 'cover', 4, 5, 1),
('Así habló Zaratustra', '...', true, 'cover', 4, 5, 1),
('El lobo Estepario', '...', true, 'cover', 5, 1, 1),
('Demian', '...', true, 'cover', 5, 1, 1);