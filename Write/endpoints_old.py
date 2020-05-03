from .middlewares import login_required
from flask import Flask, json, g, request
from .Schemas import UserSchema, ArticleSchema
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/kudos", methods=["POST"])
@login_required
def createArticle():
   article_repo = ArticleSchema().load(json.loads(request.data))

   if article_repo.errors:
     return json_response({'error': article_repo.errors}, 422)

   kudo = Kudo(g.user).create_kudo_for(article_repo)
   return json_response(kudo)

   @app.route("/kudos", methods=["POST"])
   @login_required
   def createUser():
      user_repo = UserSchema().load(json.loads(request.data))

      if user_repo.errors:
        return json_response({'error': user_repo.errors}, 422)

      kudo = Kudo(g.user).create_kudo_for(article_repo)
      return json_response(kudo)


@app.route("/kudo/<int:repo_id>", methods=["PUT"])
@login_required
def updateArticle(repo_id):
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
     def updateUser(repo_id):
        user_repo = UserSchema().load(json.loads(request.data))

        if user_repo.errors:
          return json_response({'error': user_repo.errors}, 422)

        kudo_service = Kudo(g.user)
        if kudo_service.update_kudo_with(repo_id, user_repo):
          return json_response(user_repo.data)
        else:
          return json_response({'error': 'kudo not found'}, 404)


def json_response(payload, status=200):
 return (json.dumps(payload), status, {'content-type': 'application/json'})
