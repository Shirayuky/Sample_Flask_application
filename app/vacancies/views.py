from flask import Blueprint, render_template
from dao.vacancies_dao import VacanciesDAO
from typing import List

PATH = './data/vacancies.json'

vacancies_blueprint = Blueprint('vacancies_blueprint',
                                __name__,
                                template_folder='templates')
vacancies_dao = VacanciesDAO(PATH)


@vacancies_blueprint.route('/vacancies')
def page_vacancies():
    vacancies: List[dict] = vacancies_dao.get_all()
    return render_template('vacancies_all.html', vacancies=vacancies)


@vacancies_blueprint.route('/vacancies/<int:pk>/')
def page_vacancy_by_pk(pk):
    vacancy = vacancies_dao.get_by_pk(pk)
    return render_template('vacancies_id.html', vacancy=vacancy, pk=pk)
