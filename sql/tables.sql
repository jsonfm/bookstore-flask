CREATE TABLE IF NOT EXISTS user_roles (
    id SERIAL NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    role VARCHAR(50) UNIQUE NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS users (
    id SERIAL NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_role_id FOREIGN KEY (role_id) REFERENCES user_roles(id)
);


CREATE TABLE IF NOT EXISTS genres (
    id SERIAL NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    name VARCHAR(255),
    PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS authors (
    id SERIAL NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    name VARCHAR(255),
    bio TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS editorials (
    id SERIAL NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    name VARCHAR(255),
    description TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS books (
    id SERIAL NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    name VARCHAR(255),
    description TEXT,
    cover VARCHAR(1024),
    is_active BOOLEAN,
    genre_id INTEGER,
    author_id INTEGER,
    editorial_id INTEGER,
    PRIMARY KEY (id),
    CONSTRAINT fk_genre_id FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE SET NULL,
    CONSTRAINT fk_author_id FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE SET NULL,
    CONSTRAINT fk_editorial_id FOREIGN KEY (editorial_id) REFERENCES editorials(id) ON DELETE SET NULL
);


CREATE TABLE IF NOT EXISTS prices (
    id SERIAL NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    value FLOAT(4),
    book_id INTEGER,
    PRIMARY KEY (id),
    CONSTRAINT fk_book_id FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE SET NULL
);

