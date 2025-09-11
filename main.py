from app import create_app
import os
from dotenv import load_dotenv

load_dotenv()

app=create_app()

#course content
@app.route("/")
def home():
    return "My API is working"
    
if __name__=="__main__":
    
    app.run(debug=True)