"""
Author: Patan Musthakheem
"""

from app import create_app
import os

app = create_app()
app.config['SECRET_KEY'] =  os.urandom(32)
if __name__ == "__main__":
    
    app.run(host='0.0.0.0', port=5000, debug=True)
