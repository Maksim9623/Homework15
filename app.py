from flask import Flask, jsonify
from query import connect

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def db_connect(query):
    # функция для подключения к БД
    query_ = connect(query)
    return query_


def get_all_data(item_id):
    # функция по запросу к таблице animals_new
    query = f"""
    SELECT animals_new.id, animals_new.name, colors.color, breed, outcome_type
    FROM animals_new
    JOIN animals_color
    ON animals_color.animals_id = animals_new.id
    JOIN colors
    ON colors.color_id = animals_color.colors_id
    JOIN breeds ON breeds.breed_id = animals_new.breed_id
    JOIN outcome  ON outcome.id = animals_new.outcome_id
    WHERE animals_new.id = {item_id}
            """
    response = db_connect(query)
    return response


@app.route('/<itemid>/')
def data_index(itemid):
    # Вьшка и функция по поиску в Б/Д
    animal = get_all_data(itemid)
    return jsonify(animal)


if __name__ == '__main__':
    app.run(debug=False)
