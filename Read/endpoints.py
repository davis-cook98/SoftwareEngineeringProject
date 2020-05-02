from .middlewares import login_required
from flask import Flask, json, g, request
from .Schemas import UserSchema, ArticleSchema
from .ReadMongo import ReadConnect as Read
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def test():
  return json_response(Read(g.user).findAllArticles)


@app.route("/kudos", methods=["GET"])
@login_required
def index():
 return json_response(Kudo(g.user).find_all_kudos())

@app.route("/kudo/<int:repo_id>", methods=["GET"])
@login_required
def show(repo_id):
 kudo = Kudo(g.user).find_kudo(repo_id)

 if kudo:
   return json_response(kudo)
 else:
   return json_response({'error': 'kudo not found'}, 404)

def json_response(payload, status=200):
 return (json.dumps(payload), status, {'content-type': 'application/json'})
