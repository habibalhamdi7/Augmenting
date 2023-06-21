import os
import pandas as pd
import pickle

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer

from django.conf import settings

media = settings.MEDIA_ROOT

class Training:
    def __init__(self):
        csv_file = os.path.join(media, 'genteng1.csv')
        self.data_csv = pd.read_csv(csv_file)
        self.label_encoders = {}
        self.model = None
        self.mlb = None
        self.mlb_file = None
        print("TRAIN HEAD", self.data_csv.head())
        print("SHAPE", self.data_csv.shape)
    
    def summaries_features(self, df):
        # tipe data
        summary = pd.DataFrame(df.dtypes, columns=['dtypes'])
        summary = summary.reset_index()

        # jumlah missing value
        summary['Missing'] = df.isnull().sum().values

        # jumlah unique value
        summary['Unique'] = df.nunique().values
        return summary
    
    def encode_labels(self):
        # membagi label yang mengandung spasi mejadi kata terpisah
        self.data_csv['Jenis'] = self.data_csv['Jenis'].str.split()
        self.data_csv['Pabrik'] = self.data_csv['Pabrik'].str.split()

        # Mengonversi list menjadi string untuk label encoder
        self.data_csv['Jenis'] = self.data_csv['Jenis'].apply(lambda x: ' '.join(map(str, x)))
        self.data_csv['Pabrik'] = self.data_csv['Pabrik'].apply(lambda x: ' '.join(map(str, x)))

        # membuat label encoder untuk kolom yang memerlukan encoding
        self.label_encoders['Jenis'] = LabelEncoder()
        self.label_encoders['Pabrik'] = LabelEncoder()

        # mengubah data menjadi multi-label binarizer
        self.mlb = MultiLabelBinarizer()

        # menerapkan transformasi label encoder dan multi-label binarizer
        # pada data
        for column, le in self.label_encoders.items():
            self.data_csv[column] = le.fit_transform(self.data_csv[column])
        # self.data_csv = self.mlb.fit_transform(
        #     self.data_csv[['Jenis','Pabrik']]
        # )
    
    def transform_data(self):
        # menggabungkan fitur yang sudah diencode
        transformed = pd.concat(
            [self.data_csv['Jenis'],
            self.data_csv['Pabrik']],
            axis=1
        )
        # mengubah data menjadi dataframe dengan fitur yang sesuai
        # transformed = pd.DataFrame(
        #     self.data_csv,
        #     columns=self.mlb.classes_
        # )
        return transformed
    
    def train_model(self):
        # mengambil fitur dan target
        X = self.transform_data()
        y = self.data_csv['Harga']

        # melakukan pelatihan
        self.model = LinearRegression()
        self.model.fit(X, y)
    
    def save_model(self):
        # menyimpan model ke dalam file
        model_path = os.path.join(media, 'model_regression.pk1')
        with open(model_path, 'wb') as file:
            pickle.dump(self.model, file)
        
        # menyimpan label encoder ke dalam file
        encoder_path = os.path.join(media, 'model_label.pk1')
        with open(encoder_path, 'wb') as file:
            pickle.dump(self.label_encoders, file)
    
    def the_datas(self):
        summary = self.summaries_features(self.data_csv)
        print("SUMMARY", summary)
        self.encode_labels()
        self.transform_data()
        self.train_model()
        self.save_model()
        result = {
            'summary': summary,
            'head': self.data_csv.head(),
            'shape': self.data_csv.shape
        }
        return result


class Prediction:
    def __init__(self):
        file = os.path.join(media, 'genteng1.csv')
        self.df = pd.read_csv(file)
        self.model_file = os.path.join(media, 'model_regression.pk1')
        self.label_file = os.path.join(media, 'model_label.pk1')
        self.model = None
        self.label_encoders = {}
    
    def load_model(self):
        with open(self.model_file, 'rb') as file:
            self.model = pickle.load(file)
        
        with open(self.label_file, 'rb') as file:
            self.label_encoders = pickle.load(file)

    def transform_input(self, input_data):
        #mengubah input menjadi angka
        transformed_input = pd.DataFrame(input_data, index=[0])

        # membagi label yang mengandung spasi
        transformed_input['Jenis'] = transformed_input['Jenis'].str.split()
        transformed_input['Pabrik'] = transformed_input['Pabrik'].str.split()

        transformed_input['Jenis'] = transformed_input['Jenis'].apply(lambda x: ' '.join(map(str, x)))
        transformed_input['Pabrik'] = transformed_input['Pabrik'].apply(lambda x: ' '.join(map(str, x)))

        # konversi list menjadi string
        for column, le in self.label_encoders.items():
            # Mengabaikan label yang belum pernah dilihat pada saat pelatihan
            transformed_input[column] = transformed_input[column].apply(
                lambda x: le.transform([x])[0] if x in le.classes_ else -1
            )
        return transformed_input

    def predict_price(self, jenis, pabrik):
        self.load_model()
        print("LABEL ENCODER", self.label_encoders, self.model)

        print("Coef", self.model.coef_)
        print('Intercept', self.model.intercept_)
        # mengubah input jadi angkat
        transform_input = self.transform_input(
            {
                'Jenis': jenis,
                'Pabrik': pabrik
            }
        )

        _prediksi = self.model.predict(transform_input)[0]
        prediksi = f'''
            Prediksi harga genteng jenis {jenis} Pabrik {pabrik} 
            adalah {_prediksi:,.2f}
        '''
        return prediksi