from flask import Flask, request
   import os
   
   app = Flask(__name__)
   
   # Intentional vulnerabilities for demo purposes
   API_KEY = "sk-test-1234567890abcdefghijklmnopqrstuvwxyz"
   
   @app.route('/')
   def hello():
       return "Hello, DevSecOps Pipeline!"
   
   @app.route('/search')
   def search():
       # SQL Injection vulnerability
       query = request.args.get('q')
       result = os.system(f"echo {query}")  # Command injection
       return f"Search results for: {query}"
   
   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000, debug=True)