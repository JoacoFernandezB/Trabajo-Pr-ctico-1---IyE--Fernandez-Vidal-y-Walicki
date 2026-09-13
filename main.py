from ejer1_func import *

K = 2


def __main__():
    X_train, y_train = get_train_data()
    X_test, y_test = get_test_data()

    #----------SIN PCA--------------
    
    lr_model = get_model()

    train(X_train, y_train, lr_model)

    acc = test(X_test, y_test, lr_model)

    print(f"Accuracy antes de aplicar PCA: {acc}")

    #----------CON PCA--------------
    
    lr_model_PCA = get_model()

    X_train_PCA, Vk = USV(X_train, K) # Recibimos X_train_PCA (conjunto de train con PCA) y recibimos Vk matriz de proyección
    train(X_train_PCA, y_train, lr_model_PCA)

    X_test_PCA = (X_test - X_test.mean(axis=0)) @ Vk #Proyectamos el conjunto de test sobre la matriz de proyeccion

    acc_PCA = test(X_test_PCA, y_test, lr_model_PCA)

    print(f"Accuracy después de aplicar PCA (k={K}): {acc_PCA}")


__main__()
