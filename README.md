# flask-plotly-dash

Flask app which uses:
- the application factory pattern and blueprints
- a database to manage users (sqlite with Flask-SQLAlchemy and -        Flask-Migrate)
- authentication (Flask-Login)
pip3
.envrc 

export FLASK_APP=dashapp
export FLASK_ENV=development
export DATABASE_URL=sqlite:///$PWD/app.db
export SECRET_KEY=1234this_is_it_qwerty

run: source .envrc

```
pip3 install virualenv 
virtualenv env
source env/bin/activate


pip install -r requirements.txt
flask db init
flask db migrate -m 'init'
flask db upgrade
flask run

```


### Still to do 
- bootstrap frontend
- page navigations
- multipage graphs
- 