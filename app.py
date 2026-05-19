# AWS Configuration
   AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
   AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

from flask import Flask
   
   app = Flask(__name__)
   
   @app.route('/')
   def hello():
       return "Hello, DevSecOps Pipeline!"
   
   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)