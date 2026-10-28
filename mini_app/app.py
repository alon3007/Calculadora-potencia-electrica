import streamlit as st
from backend import calcular_potencia

st.title("Calculadora de Potencia electrica")

voltaje = st.number_input("Ingrese el voltaje (V):", min_value=0.0, value=220.0)
corriente = st.number_input("Ingrese la corriente (A):", min_value=0.0, value=5.0)


if st.button("Calcular Potencia"):
    potencia = calcular_potencia(voltaje, corriente)
    st.success(f"La potencia eléctrica es: {potencia} W")