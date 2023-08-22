# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, session
from flask_login import LoginManager, login_user, logout_user ,login_required, current_user

from os import urandom
from hashlib import sha256

app = Flask(__name__)
# app.secret_key = urandom(16)

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "/login" # 未ログイン時のリダイレクト先。

@app.route("/")
def index():
    """トップページを表示する。"""

    return render_template("index.html")


# @app.route("/new")
# @login_required
# def new():
#     """投稿ページを表示する。
#     """

#     # 下書きをセッションから復元する。下書きがない場合は空文字を格納する。
#     saved_title = session.get("title") if "title" in session else ""
#     saved_body = session.get("body") if "body" in session else ""

#     return render_template("new.html", saved_title=saved_title, saved_body=saved_body)


# @app.route("/create", methods=["POST"])
# @login_required
# def create():
#     """
#     投稿する。
#     """
#     if request.form["action"] == "draft":
#         # 下書き保存処理だった場合、セッションに格納した上でトップページにリダイレクトする。 
#         session["title"] = request.form["title"]
#         session["body"] = request.form["body"]
#         return redirect("/")

#     title = request.form["title"]
#     body = request.form["body"]

#     # 入力チェック
#     messages = []
#     if title == "":
#         messages.append("タイトルが未入力です")
#     if body == "":
#         messages.append("本文が未入力です")
#     if len(messages) > 0:
#         return render_template("new.html", warning="<br>".join(messages))

#     # 投稿を保存する。
#     post_article(title=title, body=body, user_name=current_user.name)
    
#     # セッションを初期化する。
#     session.pop("title", None)
#     session.pop("body", None)
    
#     return render_template("published.html")

# @app.route("/article/<int:id>")
# def article(id):
#     """記事の詳細ページを表示する。

#     Args:
#         id (str): 記事のID。
#     """
#     # http://localhost:5000/article/1形式のパラメータを取得
#     article = get_article(id)
#     return render_template("article.html", article=article)

# @login_manager.user_loader
# def load_user(user_id):
#     """認証ユーザー情報を再読み込みするための関数。
#     ユーザーインスタンスを返す必要がある。本コードでは都度データベースの検索をしているが、
#     キャッシュに入れた方がパフォーマンスはあがる。

#     Args:
#         user_id (str): ユーザー名。
#     """
#     user = get_user_by_name(user_id)
#     return user
    
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     """GETメソッドの場合、ログインページを表示する。
#     POSTメソッドの場合、認証処理を行う。
#     """
#     if request.method == "GET":
#         return render_template("login.html")

#     name = request.form["name"]
#     password = request.form["password"]
#     # ハッシュ化。
#     password = sha256(password.encode()).hexdigest()
#     user = User(name, password)

#     if search_user(user):
#         # ユーザーが存在した場合、認証してトップページにリダイレクトする。
#         login_user(user)
#         return redirect("/")
#     else:
#         # ユーザーが存在しない場合、ログインページにエラーメッセージを表示する。
#         return render_template("login.html",  user=None, warning="ユーザー名とパスワードが一致しません")


# @app.route("/logout")
# @login_required
# def logout():
#     """ログアウトしてトップページを表示する。
#     """
#     logout_user()
#     return redirect("/")

# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     """GETメソッドの場合、登録ページを表示する。
#     POSTメソッドの場合、登録処理を行う。
#     """
#     if request.method == "GET":
#         return render_template("signup.html")

#     name = request.form["name"]
#     password = request.form["password"]
#     password_confirm = request.form["password-confirm"]

#     # 入力チェック。
#     if name == "" or password == "" or password_confirm == "" :
#         return render_template("signup.html", warning="空欄があります。")
#     if password != password_confirm:
#         return render_template("signup.html", warning="確認用パスワードが一致しません")

#     # ハッシュ化。
#     password = sha256(password.encode()).hexdigest()
#     # ユーザー登録。
#     user = User(name, password)
#     result = register_user(user)
#     if result == False:
#         return render_template("signup.html", warning="すでにアカウントが存在します")

#     # ユーザー登録が成功した場合、ログインした上でリダイレクトする。
#     login_user(user)
#     return redirect("/")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")