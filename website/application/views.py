from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from .models import CdKeys, G2A, InstantGaming
from .extensions import db


bp = Blueprint("view", __name__, static_folder="static", template_folder="templates")

@bp.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

        game_name = request.form.get('Search')
        cd_games = CdKeys.query.filter(CdKeys.name.contains(game_name)).first()
        g2a_games = G2A.query.filter(G2A.name.contains(game_name)).first()
        i_games = InstantGaming.query.filter(InstantGaming.name.contains(game_name)).first()

        if len(game_name) < 4:
            pass
        else:
            return render_template("games.html", cd_games=cd_games, i_games=i_games,  g2a_games=g2a_games)
        
    return render_template("index.html")


