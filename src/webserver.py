from flask import Flask, request

from flask_cors import CORS

from functions.funciones import *



def create_app(database):
    
    app = Flask(__name__)
    CORS(app)
    
    # initialising the database
    init_db(database)
    
    
      # ROUTES ADD USERS
    @app.route('/user', methods=['POST'])
    def add_user_route():
            return add_user()
    
    # ROUTES GET USERS
    # routes a_get
    @app.route('/user', methods=['GET'])
    def get_users():
            return users_get()
    
    @app.route("/user/<int:id>", methods=['GET'])
    def get_a_user(id):
        return get_user(id)
    
    # ROUTES DELETE USERS  
    @app.route('/user/<int:id>', methods=['DELETE'])
    def delete_user(id):
          return user_delete(id)
    
   #  ROUTES UPDATE USERS  
    @app.route('/user/<int:id>', methods=['PATCH'])
    def edit_user(id):
        data = request.get_json()
        return user_edit_clientes(id, data)
        
    
    
    
    
    
    
    
  
  
  
  
  
  
  
  
    
    
     # TO EXECUTE THE APPLICATION
    if __name__ == '__main__':
        app.run(debug=True)
    # with app.run we're going to indicate that the app is going to be in development
    return app