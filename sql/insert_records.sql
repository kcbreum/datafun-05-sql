-- Insert a single author
INSERT INTO authors (name) VALUES ('S.E. Hinton');

-- Insert multiple authors in a single statement
INSERT INTO authors (name) VALUES ('S.E. Hinton'), ('Sarah J. Maas'), ('Lewis Carroll');

-- Insert an author and retrieve the auto-generated ID (SQLite specific)
INSERT INTO authors (name) VALUES ('Rebecca Yarros');
SELECT last_insert_rowid();