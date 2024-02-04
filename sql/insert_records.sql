-- Insert a single author
INSERT INTO authors (name) VALUES ('John Doe');

-- Insert multiple authors in a single statement
INSERT INTO authors (name) VALUES ('Alice Smith'), ('Bob Johnson'), ('Eva Brown');

-- Insert an author and retrieve the auto-generated ID (SQLite specific)
INSERT INTO authors (name) VALUES ('Jane Green');
SELECT last_insert_rowid();