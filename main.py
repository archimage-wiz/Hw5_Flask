from flask import Flask, jsonify, request
from flask.views import MethodView

from models import Advertisements, User, engine, get_session
from validators import AdvValidate, UserValidate
from views.Adv import Adv
from views.UserManage import UsersManage

app = Flask("ad_app")

# MVP :)


app.add_url_rule(
    "/user", view_func=UsersManage.as_view("usr_mana"), methods=["GET", "POST"]
)
app.add_url_rule(
    "/adv", view_func=Adv.as_view("advert"), methods=["GET", "POST", "DELETE"]
)

if __name__ == "__main__":
    print("app run")
    app.run(host="127.0.0.1", port=5000)
