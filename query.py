import sqlite3


def connect(query):
    with sqlite3.connect("animal.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result


def main():
    query_1 = """
        CREATE TABLE colors (
        color_id integer PRIMARY KEY AUTOINCREMENT,
        color varchar(50) 
        )"""
    # print(connect(query_1))

    query_2 = """
        CREATE TABLE animals_color(
        animals_id INTEGER ,
        colors_id INTEGER , 
        FOREIGN KEY (animals_id) REFERENCES animals(id) ,
        FOREIGN KEY (colors_id) REFERENCES colors(id)
        
    )  """
    # print(connect(query_2))

    query_3 = """
    INSERT INTO  colors (color)
    SELECT DISTINCT  color1 AS color
    FROM animals
    """
    #print(connect(query_3))

    query_4 = """
    INSERT INTO colors (color)
    SELECT DISTINCT color2 AS color
    FROM animals
    """
    #print(connect(query_4))

    query_5 = """
    INSERT INTO animals_color (animals_id, colors_id)
    SELECT DISTINCT animals."index", colors.color_id
    FROM colors
             INNER JOIN animals
                        ON colors.color = animals.color1
                        and colors.color = animals.color2
    """
    #print(connect(query_5))

    query_6 = """
    CREATE TABLE animal_types (
        type_id integer PRIMARY KEY AUTOINCREMENT,
        `name` varchar(50)
    )
    """
    # print(connect(query_6))

    query_7 = """
       INSERT INTO animal_types (`name`)
       SELECT DISTINCT animal_type
       FROM animals
       """
    # print(connect(query_7))

    query_8 = """
    CREATE TABLE breeds (
        breed_id integer PRIMARY KEY AUTOINCREMENT,
        breed varchar(50) NOT NULL
    )"""
    # print(connect(query_8))

    query_9 = """
       INSERT INTO breeds (breed)
       SELECT DISTINCT breed
       FROM animals
       """
    # print(connect(query_9))

    query_10 = """
    CREATE TABLE IF NOT EXISTS outcome (
        id integer PRIMARY KEY AUTOINCREMENT,
        outcome_subtype varchar(50),
        outcome_type varchar(50),
        outcome_month integer,
        outcome_year integer 
    )"""
    # print(connect(query_10))

    query_11 = """
    INSERT INTO outcome (outcome_subtype, outcome_type, outcome_month, outcome_year)
    SELECT DISTINCT outcome_subtype,
                    outcome_type,
                    outcome_month,
                    outcome_year
    FROM animals
    """
    # print(connect(query_11))

    query_12 = """
        CREATE TABLE animals_new (
            id integer PRIMARY KEY AUTOINCREMENT,
            `name` varchar(50),
            age_upon_outcome varchar(50),
            animal_id varchar(50),
            date_of_birth date,
            animal_type_id integer,
            breed_id integer,
            color_id integer,
            outcome_id integer,
            FOREIGN KEY (animal_type_id) REFERENCES animal_types(type_id),
            FOREIGN KEY (Color_id) REFERENCES colors(color_id),
            FOREIGN KEY (breed_id) REFERENCES breeds(breed_id),
            FOREIGN KEY (outcome_id) REFERENCES outcome(id)
        )"""
    # print(connect(query_12))
    query_13 = """
        INSERT INTO animals_new (`name`, age_upon_outcome, animal_id, date_of_birth, animal_type_id, breed_id, color_id, outcome_id)
        SELECT
            animals.name, animals.age_upon_outcome, animals.animal_id, animals.date_of_birth,  animal_types.type_id, breeds.breed_id, colors.color_id, outcome.id
        FROM animals
        LEFT JOIN outcome
            ON  outcome.outcome_subtype = animals.outcome_subtype
            AND  outcome.outcome_type = animals.outcome_type
            AND  outcome.outcome_month = animals.outcome_month
            AND  outcome.outcome_year = animals.outcome_year
        JOIN animal_types
            ON animal_types.name = animals.name
        LEFT JOIN colors
            ON animals.color1 = colors.color
            AND animals.color2 = colors.color
        LEFT JOIN breeds
            ON animals.breed = breeds.breed
    """
    # print(connect(query_13))


if __name__ == '__main__':
    main()










