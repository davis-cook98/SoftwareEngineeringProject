from .middlewares import login_required
from flask import Flask, json, g, request
from Services import Service as
from Schemas import UserSchema, ArticleSchema
from flask_cors import flask_cors

app = Flask(__name__)
CORS(app)

@app.route("/kudos", methods=["GET"])
@login_required
def index():
 return json_response(Kudo(g.user).find_all_kudos())


@app.route("/kudos", methods=["POST"])
@login_required
def create():
   article_repo = ArticleSchema().load(json.loads(request.data))

   if article_repo.errors:
     return json_response({'error': article_repo.errors}, 422)

   kudo = Kudo(g.user).create_kudo_for(article_repo)
   return json_response(kudo)

   @app.route("/kudos", methods=["POST"])
   @login_required
   def create():
      user_repo = UserSchema().load(json.loads(request.data))

      if user_repo.errors:
        return json_response({'error': user_repo.errors}, 422)

      kudo = Kudo(g.user).create_kudo_for(article_repo)
      return json_response(kudo)


@app.route("/kudo/<int:repo_id>", methods=["GET"])
@login_required
def show(repo_id):
 kudo = Kudo(g.user).find_kudo(repo_id)

 if kudo:
   return json_response(kudo)
 else:
   return json_response({'error': 'kudo not found'}, 404)


@app.route("/kudo/<int:repo_id>", methods=["PUT"])
@login_required
def update(repo_id):
   article_repo = ArticleSchema().load(json.loads(request.data))

   if article_repo.errors:
     return json_response({'error': article_repo.errors}, 422)

   kudo_service = Kudo(g.user)
   if kudo_service.update_kudo_with(repo_id, article_repo):
     return json_response(article_repo.data)
   else:
     return json_response({'error': 'kudo not found'}, 404)

     @app.route("/kudo/<int:repo_id>", methods=["PUT"])
     @login_required
     def update(repo_id):
        user_repo = UserSchema().load(json.loads(request.data))

        if user_repo.errors:
          return json_response({'error': user_repo.errors}, 422)

        kudo_service = Kudo(g.user)
        if kudo_service.update_kudo_with(repo_id, user_repo):
          return json_response(user_repo.data)
        else:
          return json_response({'error': 'kudo not found'}, 404)


@app.route("/kudo/<int:repo_id>", methods=["DELETE"])
@login_required
def delete(repo_id):
 kudo_service = Kudo(g.user)
 if kudo_service.delete_kudo_for(repo_id):
   return json_response({})
 else:
   return json_response({'error': 'kudo not found'}, 404)


def json_response(payload, status=200):
 return (json.dumps(payload), status, {'content-type': 'application/json'})
