from flask import Flask, render_template, request, g
import pymysql

app = Flask(__name__)

# Database configuration
DATABASE = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Nivu@2012',
    'db': 'Players',
}

def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(**DATABASE)
    return g.db

@app.teardown_appcontext
def close_db(error):
    if 'db' in g:
        g.db.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/players')
def all_players():
    with get_db().cursor() as cursor:
        cursor.execute("SELECT * FROM male_players")
        players_data = cursor.fetchall()
    return render_template('players.html', players=players_data)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        player_name = request.form['player_name']
        with get_db().cursor() as cursor:
            cursor.execute("SELECT * FROM male_players WHERE Name LIKE %s", (f"%{player_name}%",))
            search_results = cursor.fetchall()
        return render_template('search_results.html', results=search_results)
    return render_template('search.html')

@app.route('/player/<int:player_id>')
def player_details(player_id):
    with get_db().cursor() as cursor:
        cursor.execute("SELECT * FROM male_players WHERE `Order` = %s", (player_id,))
        player_data = cursor.fetchone()
    
    print("Player Data:", player_data)  # Add this line for debugging
    
    return render_template('player_details.html', player=player_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
