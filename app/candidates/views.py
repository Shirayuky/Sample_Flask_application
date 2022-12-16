from flask import Blueprint, render_template
from dao.candidates_dao import CandidatesDAO
from typing import List

PATH = './data/candidates.json'

# Создаем Блюпринт и DAO
candidates_blueprint = Blueprint('candidates_blueprint',
                                 __name__,
                                 template_folder='templates')
candidates_dao = CandidatesDAO(PATH)


@candidates_blueprint.route('/candidates/')
def page_candidates_all():
    """Вьюшка для всех кандидатов"""
    candidates: List[dict] = candidates_dao.get_all()
    return render_template('candidates_all.html', candidates=candidates)


@candidates_blueprint.route('/candidates/<int:pk>/')
def page_candidate_by_pk(pk):
    """Вьюшка для искомого кандидата"""
    candidate: dict = candidates_dao.get_by_pk(pk)
    return render_template('candidates_id.html', candidate=candidate, pk=pk)
