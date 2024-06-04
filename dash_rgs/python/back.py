from flask import Flask
from flask_cors import CORS, cross_origin
from flask_caching import Cache
from graphis import *
import pandas as pd
import sqlite3

con = sqlite3.connect("../server/data_base.db", check_same_thread=False)

# dados_brutos = "../public/data/%s"
# df = pd.read_csv(dados_brutos%"analise_ada_rhguaiba_municipios_10052024.csv", encoding="latin1")

app = Flask(__name__)

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_mapping(config)


cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app, config={'CACHE_TYPE': 'SimpleCache'})
cors = CORS(app)
cache = Cache(app)



@app.route('/')
@cross_origin()
@cache.cached()
def home():
    return [x for x in range(1,6)]



@app.route('/graphis1')
@cross_origin()
@cache.cached()
def b():
    df = pd.read_sql("select * from analise_ada_municipios", con=con)
    return plot1(df)

@app.route('/graphis2')
@cross_origin()
@cache.cached()
def c():
    df = pd.read_sql("select * from analise_ada_municipios", con=con)
    return plot2(df)

@app.route('/graphis3')
@cross_origin()
@cache.cached()
def d():
    df = pd.read_sql("select * from analise_ada_municipios", con=con)
    return plot3(df)


@app.route('/graphis4')
@cross_origin()
@cache.cached()
def f():
    df = pd.read_sql("select * from analise_ada_municipios", con=con)
    return plot4(df)

@app.route('/graphis5')
@cross_origin()
@cache.cached()
def g():
    df = pd.read_sql("select * from analise_ada_municipios", con=con)
    return plot5(df)
    

if __name__ == '__main__':
    app.run(debug=True)