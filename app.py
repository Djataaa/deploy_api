import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model_2.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)

    if prediction==0:
        hasil = "Lulus"
    elif prediction==1:
        hasil = "Tidak Lulus"
    else: hasil="error"

    # UTS = float_features[0]
    # tugasonline = float_features[1]
    # quizonline = float_features[2]

    # # Membuat list nama tugas dan nilai
    # assignments = ['UTS', 'Tugas Online', 'Quiz Online']
    # scores = [UTS, tugasonline, quizonline]

    # # Membuat DataFrame dari list
    # data_df = pd.DataFrame({'Assignment': assignments, 'Nilai': scores})

    # # Membuat bar plot menggunakan Seaborn
    # plt.figure()
    # sns.barplot(x='Assignment', y='Nilai', data=data_df)

    # # Memberikan label pada sumbu x
    # plt.xlabel('Atribut')

    # # Memberikan label pada sumbu y
    # plt.ylabel('Nilai')

    # # Menampilkan prediksi hasil
    # plt.title("Prediksi: " + hasil)

    # # Menyimpan plot sebagai file gambar
    # # Simpan di folder 'static'
    # image_path = 'static/images/plot.png'
    # plt.savefig(image_path)

    #return render_template('index.html', prediction_text="Mahasiswa/i diprediksi akan {}".format(hasil),image_path=image_path)

    return render_template("index.html", prediction_text = "Mahasiswa/i diprediksi akan {}".format(hasil))

if __name__ == "__main__":
    flask_app.run(host="localhost", port=5000, debug=True)