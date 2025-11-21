import streamlit as st

st.set_page_config(page_title="Sesión 2 | ISIL", layout="centered")

st.title("Segmentación de Clientes por Comportamiento Digital | Timeline")
st.write("Autor: Christian Torres | ISIL")
st.write(
    "Explora cómo ha evolucionado la segmentación y el análisis del comportamiento digital "
    "en marketing, data science y comercio electrónico."
)

# URLs de imágenes en GitHub (modifícalas según tus archivos)
base_url = "https://raw.githubusercontent.com/christlv/timeline_segmentacion/main/"

imagenes = {
   1: base_url + "segmentacion1.png",
   2: base_url + "segmentacion2.png",
   3: base_url + "segmentacion3.png",
   4: base_url + "segmentacion4.png",
   5: base_url + "segmentacion5.png"
}

# Slider
opcion = st.slider(
    "Selecciona un punto del timeline",
    min_value=1,
    max_value=5,
    value=1,
    step=1
)

# Mostrar imagen según slider
st.image(imagenes[opcion], use_container_width=True)

# Información del timeline
if opcion == 1:
    st.info(
        "**2000 – Inicio del análisis web (Web Analytics 1.0)** | "
        "Comienza el uso de métricas básicas como visitas, páginas vistas y tasa de rebote. "
        "Se sientan las bases del análisis de comportamiento digital."
    )

if opcion == 2:
    st.info(
        "**2008 – Evolución hacia Web Analytics 2.0** | "
        "Aparecen métricas orientadas al usuario, segmentación por fuentes, embudos de conversión "
        "y análisis del customer journey."
    )

if opcion == 3:
    st.info(
        "**2015 – Segmentación basada en Machine Learning** | "
        "Se masifica el uso de clustering (K-means, DBSCAN) para segmentar usuarios por comportamiento "
        "como frecuencia, valor, navegación o intención de compra."
    )

if opcion == 4:
    st.info(
        "**2018 – Personalización en tiempo real** | "
        "Plataformas de e-commerce y marketing digital comienzan a personalizar contenido dinámicamente "
        "según el comportamiento histórico y actual del usuario."
    )

if opcion == 5:
    st.info(
        "**2023 – Segmentación avanzada con IA generativa y big data** | "
        "La IA puede analizar interacciones a gran escala, generar perfiles de clientes, predecir comportamientos "
        "y optimizar campañas automáticamente."
    )
