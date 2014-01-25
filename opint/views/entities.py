from flask import Blueprint, render_template, request

from grano.service import search_entities
from grano.lib.pager import Pager
from grano.model import Entity


entities = Blueprint('entities', __name__, static_folder='../static', template_folder='../templates')


@entities.route('/entities')
def search():
    searcher = search_entities(request.args)
    pager = Pager(searcher)
    return render_template('search.html', searcher=searcher, pager=pager)

@entities.route('/entities/<id>')
def view(id):
    entity = Entity.by_id(id)
    return render_template('entity.html', entity=entity)