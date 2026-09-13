from aux_func import *
import matplotlib.pyplot as plt

K = 2


def USV(X):  # Ver diapos 6. Análisis de componentes principales
    ux = X.mean(axis=0)
    Xc = X - ux

    U, s, Vt = np.linalg.svd(Xc, full_matrices=False)
    V = Vt.T
    S = np.diag(s)

    return U, S, V, ux


def proyectar_k(X, mu, V, k):
    Xc = X - mu
    Vk = V[:,:k]

    return Xc @ Vk

def scatter1b(X_test, y_test):
    sanos = []
    enfermos = []
    for i in range(len(X_test)):
        if y_test[i] == 0:
            sanos.append(X_test[i])
        else:
            enfermos.append(X_test[i])

    sanos = np.array(sanos)
    enfermos = np.array(enfermos)

    plt.scatter(sanos[:,0],sanos[:,1],c="blue",label="Pulmones sanos")
    plt.scatter(enfermos[:,0],enfermos[:,1],c="red",label="Pulmones enfermos")
    plt.ylabel("Componente 2")
    plt.xlabel("Componente 1")
    plt.title("Análisis de 2 componentes principales")
    plt.legend()
    plt.show()


def __main__():
    X_train, y_train = get_train_data()
    X_test, y_test = get_test_data()

    # 1.a)-------------SIN PCA-------------------------------------


    lr_model = get_model()

    train(X_train, y_train, lr_model)

    acc = test(X_test, y_test, lr_model)

    print(f"Accuracy antes de aplicar PCA: {acc}")


    # 1.b)----------PROYECCIONES + SCATTER-------------------------


    U, S, V, ux= USV(
        X_train
    )  # Recibimos U, S, V, ux
    X_test_K2 = proyectar_k(X_test, ux, V, 2) # Proyectamos el conjunto de test sobre la matriz de proyeccion
    scatter1b(X_test_K2, y_test)



    # 1.c)----------CON PCA + DISTINTOS K--------------
    ks = []
    accs = []

    for k in range(2,500,10):
        ks.append(k)
        lr_model_k = get_model()
        X_train_k = proyectar_k(X_train, ux, V, k)
        X_test_k = proyectar_k(X_test, ux, V, k)
        train(X_train_k,y_train,lr_model_k)
        acc_k = test(X_test_k,y_test,lr_model_k)
        accs.append(acc_k)

    ks = np.array(ks)
    accs = np.array(accs)

    plt.plot(ks,accs,"ro-")
    plt.title("Accuracy en función del K")
    plt.axhline(acc, c="black",linestyle="--",label="Accuracy sin PCA")
    plt.ylabel("Accuracy")
    plt.xlabel("k")
    plt.legend()
    plt.grid()
    plt.show()
__main__()
