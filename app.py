import math
import streamlit as st

st.title("Calculadora y Simulador Solar Residencial ☀️")

# Menú principal como selección
opcion = st.selectbox(
    "¿Qué operación deseas realizar?",
    (
        "Calcular paneles necesarios para un hogar",
        "Simular energía de un sistema residencial",
    ),
)

if opcion == "Calcular paneles necesarios para un hogar":
  # Valor por defecto realista para el consumo de una casa (ej: 4000W de energía a cubrir)
  nivel_energia = st.number_input(
      "Ingrese la cantidad de energía a satisfacer en el hogar (watts):",
      min_value=0.0,
      value=4000.0,
      step=500.0,  # Saltos de 500 en 500 watts
  )

  tipo_panel = st.selectbox(
      "Seleccione el modelo de panel:",
      (
          "Modelo Res. Standard: 450W",
          "Modelo Res. Alta Potencia: 500W",
      ),
  )

  produccion_panel = 450 if "450W" in tipo_panel else 500

  if st.button("Calcular Paneles"):
    if nivel_energia > 0:
      cantidad_necesaria = math.ceil(nivel_energia / produccion_panel)
      st.success(
          f"🏠 Para cubrir los **{nivel_energia} W** de tu hogar, necesitas un"
          f" mínimo de **{cantidad_necesaria} paneles**."
      )
    else:
      st.error("Por favor ingrese un valor mayor a 0.")

else:
  # Valor por defecto realista: un techo con 8 paneles solares
  cantidad_panel = st.number_input(
      "Ingrese la cantidad de paneles instalados en el hogar:",
      min_value=0,
      value=8,
      step=1,  # De 1 en 1 panel
  )
  produccion_panel = st.number_input(
      "Potencia promedio generada por cada panel (watts):",
      min_value=0.0,
      value=450.0,
      step=50.0,
  )

  if st.button("Simular Producción"):
    produccion_total = produccion_panel * cantidad_panel
    st.success(
        f"⚡ Con tus {cantidad_panel} paneles, el sistema de tu hogar generará"
        f" un total de: **{produccion_total:,.0f} watts** de potencia."
    )