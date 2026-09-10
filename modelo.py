from sklearn.tree import DecisionTreeClassifier, export_text

def entrenar_modelo(X, Y):
    arbol = DecisionTreeClassifier(max_depth=3)
    arbol.fit(X, Y)
    return arbol

def extraer_reglas(arbol, nombres_variables):
    reglas = export_text(arbol, feature_names=nombres_variables)
    return reglas

def predecir(arbol, edad, horas_online, compras_previas):
    entrada = [[edad, horas_online, compras_previas]]
    prediccion = arbol.predict(entrada)[0]
    return prediccion
