from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Configuration de la base de données
db_host = 'clem-maud.postgres.database.azure.com'
db_port = '5432'
db_name = 'wtf'
db_user = 'clemaud'
db_password = 'greta@2023'

# Route de l'API
@app.route('/test')
def get_insee_dept():
    # Connexion à la base de données
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    cursor = conn.cursor()

    # Exécution de la requête SQL
    query = "SELECT * FROM departements"
    cursor.execute(query)
    results = cursor.fetchall()

    # Fermeture de la connexion à la base de données
    cursor.close()
    conn.close()

    # Conversion des résultats en format JSON
    data = []
    for result in results:
        dep, cheflieu, Cheflieu, ncc, nccenr = result
        data.append({'dep': dep, 'cheflieu': cheflieu, 'Cheflieu': Cheflieu, 'ncc': ncc, 'nccenr': nccenr})

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
