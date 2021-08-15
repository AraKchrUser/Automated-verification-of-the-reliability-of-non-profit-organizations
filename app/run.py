from deeppavlov import configs, build_model
from sentimental_interface import Sentimental
import pandas as pd

if __name__ == '__main__':
    sentimental_model = Sentimental(download=False)
    # input_elmo = pd.read_csv('../dataHACK/input_elmo.csv')
    # preprocess = pd.read_csv('../dataHACK/preprocessing_data.csv')
    # print(input_elmo.head())
    # print(preprocess.head())
    #
    # resault = pd.merge(preprocess, input_elmo, how='left', on=['Наименование'])
    # print(resault)
    # resault.to_csv('../dataHACK/best.csv')
    model = pd.read_csv('../dataHACK/best1.csv')
    print(model.head())

    for vec in model.values:
        sentimental_model.sentimental_feedback_prob(vec[-1])

