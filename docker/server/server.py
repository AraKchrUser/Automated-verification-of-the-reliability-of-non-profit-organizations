# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import pandas as pd

from parserbs import get_info

app = Flask(__name__, static_url_path='')
app.secret_key = "super secret key"


@app.route('/', methods=['POST', 'GET'])
def form_sample():
    # df = pd.read_csv(
    #     '/home/user/src/hackaton_project/Automated-verification-of-the-reliability-of-non-profit-organizations/docker/server/preprocessing_data.csv')
    # df.drop(['ИНН'], axis=1, inplace=True)

    if request.method == 'POST':
        result = request.form
        res = get_info(result.get("NKO_name"))
        print('res: ', res)
        return render_template("result.html", result = result)

        # for k, v in res.items():
        #     res[k] = [v]
        #
        # from sklearn.linear_model import LogisticRegression
        # # df1 = pd.DataFrame(res)
        # # df1['Маил Добро'] = df1['Маил Добро'].apply(lambda x: 0 if x == pd.NaT else 1)
        # # df1['Нужна помощь'] = df['Нужна помощь'].apply(lambda x: 0 if x == pd.NaT else 1)
        # # df1['Нужна помощь Фонд'] = df1['Нужна помощь Ссылка'].astype(str).apply(lambda x: 0 if x == 'nan' else float(x))
        # # df1 = df1[['Наименование', 'Маил Добро', 'Нужна помощь',
        # #            'Нужна помощь Фонд']].copy()
        #
        # # df = pd.concat(df, df1, axis=0)
        # model = LogisticRegression().fit(df.drop(['Благонадежный (да/нет)'], axis=1), df['Благонадежный (да/нет)'])
        # print(model.score(df.drop(['Благонадежный (да/нет)'], axis=1), df['Благонадежный (да/нет)']))
    return render_template('index.html')


def main():
    app.run(port=8080, host='127.0.0.1')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        res = get_info(result.get("NKO_name"))
        print('res: ', res)
        return render_template("result.html", res=res)

if __name__ == '__main__':
    main()
