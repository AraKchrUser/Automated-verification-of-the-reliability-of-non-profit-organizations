# -*- coding: utf-8 -*-

from flask import Flask, url_for, request, render_template, redirect
app = Flask(__name__, static_url_path='')
app.secret_key = "super secret key"


@app.route('/', methods=['POST', 'GET'])
def form_sample():
    """Форма, где пользователь вводит значения..."""

    if request.method == 'GET':
        # Выводим начальную форму
        pass
        # Пример
        # return render_template('index.html', style_path=url_for('static', filename='css/style.css'),
        #                        text=data.get_text(), question=data.get_question(), answer=data.get_answer(),
        #                        user_name=user_name)
    elif request.method == 'POST':
        # Получаем данные с формы и производим вычисления и отображаем на форме:
        # парсим данные
        # Пропускаем через классификатор -> получаем прогноз
        # рисуем графики : количество отзывов в сети в виде круговых диаграмм и т.д.
        pass
        # Пример
        # if request.form.get('accept'):
        #     pass
        # # Получить ответ на вопрос
        # return render_template('index.html', style_path=url_for('static', filename='css/style.css'),
        #                        text=data.get_text(), question=data.get_question(), answer=data.get_answer(),
        #                        user_name=user_name)
    return render_template('index.html')


def main():
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
