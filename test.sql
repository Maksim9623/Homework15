CREATE TABLE colors
(
        color_id integer PRIMARY KEY AUTOINCREMENT,
        color1 varchar(50),
        color2 varchar(50)
);

CREATE TABLE IF NOT EXISTS animals_color
(
        animals_id integer ,
        colors_id integer ,
        FOREIGN KEY (animals_id) REFERENCES animals_new(id) ,
        FOREIGN KEY (colors_id) REFERENCES colors(color_id)
);

INSERT INTO  colors (color1)
SELECT DISTINCT
        color1 AS color1
FROM animals;


INSERT INTO colors (color2)
SELECT DISTINCT color2 AS color2
FROM animals;

INSERT INTO animals_color (animals_id, colors_id)
SELECT DISTINCT animals_new.id, colors.color_id
FROM animals
JOIN colors
ON colors.color2 = animals.color2
LEFT JOIN animals_new
ON animals_new.animal_id = animals.animal_id;

INSERT INTO animals_color (animals_id, colors_id)
SELECT DISTINCT animals_new.id, colors.color_id
FROM animals
JOIN colors
ON colors.color1 = animals.color1
LEFT JOIN animals_new
ON animals_new.animal_id = animals.animal_id;

CREATE TABLE breeds
(
        breed_id integer PRIMARY KEY AUTOINCREMENT,
        breed varchar(50)
);

INSERT INTO breeds (breed)
       SELECT DISTINCT breed
       FROM animals;

CREATE TABLE IF NOT EXISTS animal_types
 (
        type_id integer PRIMARY KEY AUTOINCREMENT,
        name varchar(50)
);

INSERT INTO animal_types (name)
       SELECT DISTINCT animal_type
       FROM animals
LEFT JOIN animal_types
    ON animal_types.type_id = animals.animal_id;

CREATE TABLE outcome
(
        id integer PRIMARY KEY AUTOINCREMENT,
        outcome_subtype varchar(100),
        outcome_type varchar(50),
        outcome_month integer ,
        outcome_year integer
);

INSERT INTO outcome (outcome_subtype, outcome_type, outcome_month, outcome_year)
SELECT DISTINCT outcome_subtype,
                outcome_type,
                outcome_month,
                outcome_year
FROM animals;

CREATE TABLE IF NOT EXISTS animals_new
(
            id integer PRIMARY KEY AUTOINCREMENT,
            age_upon_outcome varchar(50),
            animal_id varchar(50),
            animal_type_id integer,
            `name` varchar(50),
            date_of_birth date,
            breed_id integer,
            outcome_id integer,
            FOREIGN KEY (animal_type_id) REFERENCES animal_types(type_id),
            FOREIGN KEY (breed_id) REFERENCES breeds(breed_id),
            FOREIGN KEY (outcome_id) REFERENCES outcome(id)
);


INSERT INTO animals_new (age_upon_outcome, animal_id, `name`, date_of_birth, breed_id, outcome_id, animal_type_id)

SELECT
     animals.age_upon_outcome, animals.animal_id, animals.name,animals.date_of_birth, breeds.breed_id, outcome.id, animal_types.type_id
FROM animals
JOIN outcome
    ON  outcome.outcome_subtype = animals.outcome_subtype
    AND  outcome.outcome_type = animals.outcome_type
    AND  outcome.outcome_month = animals.outcome_month
    AND  outcome.outcome_year = animals.outcome_year
JOIN animal_types
    ON animal_types.name = animals.animal_type
LEFT JOIN breeds
  ON breeds.breed = animals.breed;


SELECT animals_new.id, animals_new.name, colors.color1, breed, outcome_type
FROM animals_new
JOIN animals_color
ON animals_color.animals_id = animals_new.id
JOIN colors
ON colors.color_id = animals_color.colors_id
JOIN breeds on breeds.breed_id = animals_new.breed_id
JOIN outcome  on outcome.id = animals_new.outcome_id;
--WHERE  animals_new.id = 2  ;