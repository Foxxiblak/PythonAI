from flask import Flask
from views.routes import main

from db import engine, SessionLocal
from models.db import Base
from seed.init_db import seed_data

app = Flask(__name__)
app.register_blueprint(main)

def init():
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as session:
        seed_data(session)

if __name__ == '__main__':
    init()
    app.run(debug=True)