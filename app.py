import pandas as pd
import plotly.express as px
import streamlit as st

# ==========================
# Configuración de la página
# ==========================

st.set_page_config(
    page_title="Dashboard de Vehículos",
    layout="wide"
)

# ==========================
# Leer datos
# ==========================

car_data = pd.read_csv("vehicles_us.csv")

# ==========================
# Encabezado
# ==========================

st.title("🚗 Dashboard de Vehículos Usados")

st.markdown("""
Bienvenido al panel interactivo del conjunto de datos **Vehicles US**.

En esta aplicación podrás explorar los anuncios de venta de vehículos mediante gráficos interactivos desarrollados con **Plotly** y **Streamlit**.
""")

st.divider()

# ==========================
# Métricas
# ==========================

col1, col2, col3 = st.columns(3)

col1.metric("Vehículos", len(car_data))
col2.metric("Precio promedio", f"${car_data['price'].mean():,.0f}")
col3.metric("Kilometraje promedio", f"{car_data['odometer'].mean():,.0f}")

st.divider()

# ==========================
# Vista previa
# ==========================

st.subheader("Vista previa del conjunto de datos")

st.dataframe(car_data)

st.divider()

# ==========================
# Filtro
# ==========================

vehicle_type = st.selectbox(
    "Seleccione el tipo de vehículo",
    sorted(car_data["type"].unique())
)

filtered_data = car_data[car_data["type"] == vehicle_type]

# ==========================
# Histograma
# ==========================

if st.checkbox("Mostrar Histograma"):

    fig = px.histogram(
        filtered_data,
        x="odometer",
        nbins=40,
        title=f"Distribución del odómetro ({vehicle_type})"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==========================
# Dispersión
# ==========================

if st.checkbox("Mostrar Gráfico de Dispersión"):

    fig = px.scatter(
        filtered_data,
        x="odometer",
        y="price",
        color="condition",
        title=f"Precio vs Odómetro ({vehicle_type})"
    )

    st.plotly_chart(fig, use_container_width=True)
