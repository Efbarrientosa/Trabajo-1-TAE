import numpy as np
import pandas as pd
import csv
import lzma
import dill as pickle
import streamlit as st

df = pd.read_csv('grupo0pub.csv', encoding="utf-8")
df1 = pd.read_csv('grupo1pub.csv', encoding="utf-8")
df2 = pd.read_csv('grupo2pub.csv', encoding="utf-8")
df6 = pd.read_csv('grupo3pub.csv', encoding="utf-8")
df3=pd.read_csv('grupo0priv.csv', encoding="utf-8")
df4=pd.read_csv('grupo1priv.csv', encoding="utf-8")
df5=pd.read_csv('grupo2priv.csv', encoding="utf-8")
df7 = pd.read_csv('grupo3priv.csv', encoding="utf-8")
def main():
    st.title("Agrupamiento de Universidades")
    tipo=st.radio("Ingrese el tipo de Universidad",("Publica","Privada"))

    if tipo=="Publica":
        st.title("Instituciones de educacion superior de caracter publico")
        st.text("")
        st.text("El primer grupo cuenta con 482 instituciones, cuenta con las unicas instituciones con educacion a distancia, una tasa de admicion promedio de 67%, un promedio de precio para garantizar estadia de 13648 dolares , la mayoria de instituciones alcanzaron el grado mas alto de certificacion y un costo promedio de matricula de 6200 dolares.")
        st.dataframe(df)
        st.text("")
        st.text("El segundo grupo cuenta con 67 instituciones, no cuenta con instituciones con educacion a distancia, una tasa de admicion promedio de 68%, un promedio de precio para garantizar estadia de 13292 dolares , la mayoria de instituciones cuentan con el grado mas bajo ( y el resto sin certificacion) y un costo promedio de matricula de 7448 dolares.")
        st.dataframe(df1)
        st.text("")
        st.text("El tercer grupo cuenta con 75 instituciones, no cuenta con instituciones con educacion a distancia, una tasa de admicion promedio de 67%, un promedio de precio para garantizar estadia de 11836 dolares , la mayoria de instituciones alcanzaron el segundo grado mas alto de certificacion y un costo promedio de matricula de 5336 dolares.")
        st.dataframe(df2)
        st.text("")
        st.text("El cuarto grupo cuenta con 46 instituciones, no cuenta con instituciones con educacion a distancia, una tasa de admicion promedio de 72%, un promedio de precio para garantizar estadia de 7694 dolares , la mayoria de instituciones alcanzaron el grado intermedio de certificacion y un costo promedio de matricula de 2614 dolares.")
        st.dataframe(df6)


        st.title("Recomendacion")

        st.text("")
        st.text("a continuacion se le preguntara por una caracteristica y el sistema intentara escoger las mejores opciones de instituciones dependiendo la caracteristica")
        st.text("")
        st.text("para educacion a distancia buscara al azar en dataframes donde sea posible encontrarlas")
        st.text("")
        st.text("para concepto de matricula buscara al azar en dataframes donde sea mas bajo el concepto de matricula")
        st.text("")
        st.text("para tasa de admision buscara al azar en dataframes donde las tasa de admision sea mas alta")
        st.text("")
        st.text("para mayor grado de certificacion buscara al azar en dataframes donde esten instituciones que hayan alcanzado el maximo grado de certificacion")
        st.text("")
        st.text("estas opciones se refrescan en el dataframe asi que no siempre son iguales")
        opcion = st.radio("Escoja la caracteristica mas importante que desea: ",
                          ("Educacion a distancia", "Concepto por matricula", "Tasa de admision",
                           "Mayor grado obtenido"))
        if opcion=="Educacion a distancia":
            datax=df.loc[df['DISTANCEONLY'] == 1]
            st.dataframe(datax)
        elif opcion=="Concepto por matricula":
            datax = df6.sample(n=10, replace=True)
            st.dataframe(datax)
        elif opcion=="Tasa de admision":
            datax = df6.sample(n=10, replace=True)
            st.dataframe(datax)
        elif opcion=="Mayor grado obtenido":
            datax = df.sample(n=10, replace=True)
            st.dataframe(datax)

    else:
        st.title("Instituciones de educacion superior de caracter privado")

        st.text("")
        st.text("El primer grupo cuenta con 113 instituciones, no cuenta con instituciones con educacion a distancia, una tasa de admicion promedio de 79%, un promedio de precio para garantizar estadia de 18779 dolares ,la mayoria de instituciones cuentan con el grado mas bajo ( y el resto sin certificacion) y un costo promedio de matricula de 10124 dolares.")
        st.dataframe(df3)
        st.text("")
        st.text("El segundo grupo cuenta con 862 instituciones, cuenta con algunas instituciones con educacion a distancia, una tasa de admicion promedio de 64%, un promedio de precio para garantizar estadia de 22163 dolares , la mayoria de instituciones alcanzaron el grado mas alto de certificacion y un costo promedio de matricula de 15798 dolares.")
        st.dataframe(df4)
        st.text("")
        st.text("El tercer grupo cuenta con 425 instituciones, cuenta con algunas instituciones con educacion a distancia, una tasa de admicion promedio de 70%, un promedio de precio para garantizar estadia de 20732 dolares , la mayoria de instituciones alcanzaron el segundo grado mas alto de certificacion y un costo promedio de matricula de 16158 dolares.")
        st.dataframe(df5)
        st.text("")
        st.text("El cuarto grupo cuenta con 177 instituciones, cuenta con algunas instituciones con educacion a distancia, una tasa de admicion promedio de 81%, un promedio de precio para garantizar estadia de 21149 dolares , la mayoria de instituciones alcanzaron el grado intermedio de certificacion y un costo promedio de matricula de 14831 dolares.")
        st.dataframe(df7)

        st.title("Recomendacion")
        st.text(
            "a continuacion se le preguntara por una caracteristica y el sistema intentara escoger las mejores opciones de instituciones dependiendo la caracteristica")
        st.text("")
        st.text("para educacion a distancia buscara en dataframes donde sea posible encontrarlas")
        st.text("")
        st.text("para concepto de matricula buscara al azar en dataframes donde sea mas bajo el concepto de matricula")
        st.text("")
        st.text("para tasa de admision buscara al azar en dataframes donde las tasa de admision sea mas alta")
        st.text("")
        st.text(
            "para mayor grado de certificacion buscara al azar en dataframes donde esten instituciones que hayan alcanzado el maximo grado de certificacion")
        st.text("")
        st.text("estas opciones se refrescan en el dataframe asi que no siempre son iguales")

        opcion = st.radio("Escoja la caracteristica mas importante que desea: ",
                          ("Educacion a distancia","Concepto por matricula","Tasa de admision", "Mayor grado obtenido"))
        if opcion=="Educacion a distancia":
            datax=df7.loc[df7['DISTANCEONLY'] == 1]
            st.dataframe(datax)
        elif opcion=="Concepto por matricula":
            datax = df3.sample(n=10, replace=True)
            st.dataframe(datax)
        elif opcion=="Tasa de admision":
            datax = df7.sample(n=10, replace=True)
            st.dataframe(datax)
        elif opcion=="Mayor grado obtenido":
            datax = df4.sample(n=10, replace=True)
            st.dataframe(datax)

if __name__=="__main__":
   main()