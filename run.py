from app import create_app
import os

app = create_app()
app.config['SECRET_KEY'] =  os.urandom(32)
if __name__ == "__main__":
    
    app.run(port=1000, debug=True)