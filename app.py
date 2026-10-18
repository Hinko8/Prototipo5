import math
import streamlit as st

st.title("Calculadora y Simulador Solar ☀️")

opcion = st.selectbox(
    "¿Qué operación deseas realizar?",
    (
        "Calcular paneles necesarios",
        "Simular energía producida",
    ),
)

if opcion == "Calcular paneles necesarios":
  nivel_energia = st.number_input(
      "Ingrese la cantidad de energía a satisfacer (watts):",
      min_value=0.0,
      value=1000.0,
      step=100.0,  
  )

  tipo_panel = st.selectbox(
      "Seleccione el modelo de panel:", ("Modelo 1: 450W", "Modelo 2: 500W")
  )

  produccion_panel = 450 if "450W" in tipo_panel else 500

  if st.button("Calcular"):
    if nivel_energia > 0:
      cantidad_necesaria = math.ceil(nivel_energia / produccion_panel)
      st.success(
          f"Se necesitan al menos **{cantidad_necesaria} paneles** para"
          f" satisfacer {nivel_energia} W."
      )
    else:
      st.error("Por favor ingrese un valor mayor a 0.")

else:
  cantidad_panel = st.number_input(
      "Ingrese la cantidad de paneles a disposición:",
      min_value=0,
      value=4,
      step=1,
  )
  produccion_panel = st.number_input(
      "Energía generada por cada panel (watts):",
      min_value=0.0,
      value=450.0,
      step=50.0,
  )

  if st.button("Simular"):
    produccion_total = produccion_panel * cantidad_panel
    st.success(
        f"La cantidad total de energía generada es de: **{produccion_total} watts**"
    )