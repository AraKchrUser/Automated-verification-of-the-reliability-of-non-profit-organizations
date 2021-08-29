from deeppavlov import build_model, configs

print('1 ---> ')
# download=False если данные скачваться не будут
model = build_model(configs.classifiers.rusentiment_elmo_twitter_cnn, download=False)
print('2 ---> ')
with open('/save_file/sentimental_result.txt', 'w') as f:
    f.write(model(['В Африке воды мало, но она вкусная'])[0])
