from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<div style=\"text-align: center;\"><h1> Hello from Mohans Cloud Tech </h1> <p> Welcome to GCP DevOps Projects </p>     <p></P></div>'

if __name__ == "__main__":
   app.run(debug=True)