import pandas as pd
from flaskr import db, create_app
from flaskr.models import Insurance

app=create_app()
with app.app_context():
    db.create_all()
    def create_tables():
        s = db.session()
        if len(s.query(Insurance).all()) == 0:
            print('No data in the table detected.')
            print('Initialising the table in database.')
            engine = s.get_bind()
            df = pd.read_csv('flaskr/tables/insurance.csv')
            df.to_sql('insurance',
                      con=engine,
                      if_exists='append',
                      chunksize=1000,
                      index=False)
    create_tables()
# Check if the existing table contain data, if not then initialize with csv insert
