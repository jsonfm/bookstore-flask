-- authors
SELECT * FROM authors;


-- BOOKS

-- obtain books
SELECT 
    A.name, B.name as author, C.name as genre, D.name as editorials
FROM 
    books AS A
INNER JOIN
    authors AS B
ON 
    A.author_id = B.id
INNER JOIN
    genres as C
ON
    A.genre_id = C.id
INNER JOIN
    editorials as D
ON
    A.editorial_id = D.id
;