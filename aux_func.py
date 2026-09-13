import numpy as np
import pandas as pd
import os
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from PIL import Image


def get_model(): # Función para recibir un modelo de regresion logaritmica
    lr_model = LogisticRegression(max_iter=2000)
    return lr_model


def train(X_train, y_train, lr_model): # Función para entrenar
    # Entrenamiento del modelo
    lr_model.fit(X_train, y_train)


def test(X_test, y_test, lr_model): # Función para testear
    y_pred = lr_model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    return acc


def get_train_data( # Data para entrenamiento con parametros por default
    ruta_train="./dataset_tp1/train/", ruta_train_labels="dataset_tp1/train_labels.csv"
):
    X_train = []
    for archivo in sorted(os.listdir(ruta_train)):
        if archivo.endswith(".png"):
            ruta_imagen = ruta_train + archivo
            imagen = Image.open(ruta_imagen)
            imagen_array = np.array(imagen).flatten()
            X_train.append(imagen_array)

    X_train = np.array(X_train)

    train_labels = pd.read_csv(ruta_train_labels)
    y_train = train_labels["clase"].to_numpy()

    return X_train, y_train


def get_test_data( # Data para tests con parámetros x default
    ruta_test="./dataset_tp1/test/", ruta_test_labels="dataset_tp1/test_labels.csv"
):
    # Validación del modelo
    X_test = []
    for archivo in sorted(os.listdir(ruta_test)):
        if archivo.endswith(".png"):
            ruta_imagen = ruta_test + archivo
            imagen = Image.open(ruta_imagen)
            imagen_array = np.array(imagen).flatten()
            X_test.append(imagen_array)
    X_test = np.array(X_test)

    test_labels = pd.read_csv(ruta_test_labels)
    y_test = test_labels["clase"].to_numpy()
    return X_test, y_test


