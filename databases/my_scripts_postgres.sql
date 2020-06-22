CREATE TABLE courses (
	name		varchar(255),
  	body		text,
  	created_at	timestamp
);
CREATE TABLE users (
	first_name	varchar(255),
  	email		varchar(255),
  	manager		boolean
);
CREATE TABLE course_members (
	user_id		integer,
  	course_id	integer,
  	created_at	timestamp
);
INSERT INTO courses (name, slug, lessons_count, body)
    VALUES ('basics of programming', 'basics', 10, 'this is theory');

INSERT INTO courses (name, slug) VALUES ('Bash', 'bash');
INSERT INTO courses (name, slug) VALUES
  ('Bash', 'bash'), ('PHP', 'php'), ('Ruby', 'ruby');
  INSERT INTO courses VALUES ('linux', 'linux', 3, 'something about linux');

UPDATE courses SET body = 'updated' WHERE slug = 'bash';

UPDATE courses SET body = 'updated!', name = 'Bash' WHERE slug = 'bash';

UPDATE courses SET body = 'oops';

-- compare
UPDATE courses SET name = 'new name' WHERE lessons_count > 3;

UPDATE courses SET name = 'another new name' WHERE lessons_count < 2;

-- И
UPDATE courses SET name = 'new name'
  WHERE slug = 'bash' AND lessons_count > 3;

-- ИЛИ
UPDATE courses SET name = 'another new name'
  WHERE lessons_count < 2 OR lessons_count > 8;

UPDATE courses SET name = 'another new name'
  WHERE (lessons_count < 2 AND lessons_count > 8) OR slug = 'linux';

-- DELETE

DELETE FROM courses WHERE slug = 'bash';

-- truncate - clear all table
TRUNCATE courses;

DELETE FROM users WHERE first_name = 'Sansa';
INSERT INTO users VALUES ('Arya', 'arya@winter.com');
UPDATE users SET manager = true WHERE email = 'tirion@got.com';

-- SELECT

SELECT * FROM users WHERE birthday < '2018-10-21';

SELECT * FROM users LIMIT 3;


SELECT * FROM users ORDER BY birthday;


SELECT * FROM users ORDER BY birthday DESC;

-- Порядок следования частей `WHERE`, `ORDER BY` и `LIMIT` в SQL запросе фиксирован.
SELECT username, created_at FROM users WHERE birthday < '2018-10-21' ORDER BY birthday DESC LIMIT 2;

--Для удобства, длинные запросы разбивают на строчки:

SELECT username, created_at FROM users
  WHERE birthday < '2018-10-21'
  ORDER BY birthday DESC
  LIMIT 2;

SELECT * FROM users 
    WHERE birthday > '1999-10-23'
    ORDER BY first_name ASC
    LIMIT 3;







