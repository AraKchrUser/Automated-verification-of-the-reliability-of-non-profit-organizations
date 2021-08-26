import pandas as pd
import sklearn


def learning_and_plot_model():
    pass


if __name__ == "__main__":

    # Данные о ссылках на сайтах и о фонде: подборбнее к  mmvvrr
    data = pd.read_csv('data/refer_in_site.csv')

    # Обработка
    data['ИНН'] = data['ИНН'].apply(lambda x: 0 if x == 'nan' else 1)
    data['Благонадежный (да/нет)'] = data['Благонадежный (да/нет)'].map({'да': 1, 'нет': 0})
    data['Маил Добро'] = data['Маил Добро'].apply(lambda x: 0 if x == pd.NaT else 1)
    data['Нужна помощь'] = data['Нужна помощь'].apply(lambda x: 0 if x == pd.NaT else 1)
    data['Нужна помощь Фонд'] = data['Нужна помощь Ссылка'].astype(str).apply(lambda x: 0 if x == 'nan' else float(x))
    df_preprocess = data[['Наименование', 'Город', 'ИНН', 'Благонадежный (да/нет)', 'Маил Добро', 'Нужна помощь',
                         'Нужна помощь Фонд']].copy()

    # Файл docker содержит данные - результаты обраотки новостей, отзывов  т. д.
    news_sentimental = pd.read_csv('../docker/save_file/news_summarization.csv')

    # merge
    # dataset = data.merge(news_sentimental, on='key')
    # learning_and_plot_model(dataset)


