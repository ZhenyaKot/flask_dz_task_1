# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base_dz.html')


@app.route('/cloth/')
def cloth():
    return render_template('cloth_index.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes_index.html')


@app.route('/jacket/')
def jacket():
    return render_template('jacket_index.html')


if __name__ == '__main__':
    app.run()
