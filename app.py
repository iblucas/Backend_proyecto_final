from src.webserver import create_app
import src.database as db

app = create_app(db.conectdb())
app.run(debug =True)

