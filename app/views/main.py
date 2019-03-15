# -*- coding: utf-8 -*-
import json
from flask import Blueprint, render_template,jsonify,request
from app.models import *
# from app.extensions import db
# from sqlalchemy import *
from app.utils import *

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('/main/index.html')

@main.route('/posts', methods=['GET', 'POST'])
def create_posts():

    url = request.form.get('news_url')
    text = request.form.get('news_text')
    if url:
        res = crawl_and_cut(url)
        return res
    elif text:
        res = text_cut(text)
        return res

