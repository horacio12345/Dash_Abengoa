import dash
from dash import dcc, html
import plotly.graph_objs as go
#import os
# Crear la aplicación Dash
app = dash.Dash(__name__)

# Datos para los escenarios
escenarios = ['Escenario 1', 'Escenario 2', 'Escenario 3']
trabajadores_inicial = [12, 8, 5]
tarifa_inicial = [34, 33, 39.5]
trabajadores_objetivo = [15, 12, 8]
tarifa_objetivo = [34, 32, 34]

# Function to calculate percentage difference
def percentage_diff(final, initial):
    return ((final - initial) / initial) * 100

# Gráfico: Escenarios vs Variación de Trabajadores y Tarifas (Inicial)
grafico_variacion_inicial = go.Figure()

# Línea A: Variación del equipo contratado (secuencial)
grafico_variacion_inicial.add_trace(go.Scatter(
    x=escenarios,
    y=trabajadores_inicial,
    mode='lines+markers',
    name='Equipo Contratado',
    line=dict(dash='dash'),
    marker=dict(size=23),
    hovertemplate='<span style="font-size: 16px;">%{text}</span><extra></extra>',
    text=[f"<b>{trabajadores_inicial[0]} trabajadores</b>",
          f"<b>{trabajadores_inicial[1]} trabajadores</b><br>Diferencia: <b>{percentage_diff(trabajadores_inicial[1], trabajadores_inicial[0]):.2f}%</b>",
          f"<b>{trabajadores_inicial[2]} trabajadores</b><br>Diferencia: <b>{percentage_diff(trabajadores_inicial[2], trabajadores_inicial[1]):.2f}%</b><br>Diferencia total: <b>{percentage_diff(trabajadores_inicial[2], trabajadores_inicial[0]):.2f}%</b>"]
))

# Línea B: Variación de la Tarifa (secuencial)
grafico_variacion_inicial.add_trace(go.Scatter(
    x=escenarios,
    y=tarifa_inicial,
    mode='lines+markers',
    name='Tarifa',
    line=dict(dash='dash', color='green'),
    marker=dict(size=23, color='green'),
    hovertemplate='<span style="font-size: 16px;">%{text}</span><extra></extra>',
    text=[f"<b>Tarifa: {tarifa_inicial[0]} €/HH</b>",
          f"<b>Tarifa: {tarifa_inicial[1]} €/HH</b><br>Diferencia: <b>{percentage_diff(tarifa_inicial[1], tarifa_inicial[0]):.2f}%</b>",
          f"<b>Tarifa: {tarifa_inicial[2]} €/HH</b><br>Diferencia: <b>{percentage_diff(tarifa_inicial[2], tarifa_inicial[1]):.2f}%</b><br>Diferencia total: <b>{percentage_diff(tarifa_inicial[2], tarifa_inicial[0]):.2f}%</b>"]
))

# Gráfico 2: Escenarios vs Variación de Trabajadores y Tarifas (Objetivo)
grafico_variacion_objetivo = go.Figure()

# Línea A: Variación del equipo contratado (objetivo)
grafico_variacion_objetivo.add_trace(go.Scatter(
    x=escenarios,
    y=trabajadores_objetivo,
    mode='lines+markers',
    name='Equipo Contratado (Objetivo)',
    line=dict(dash='dash'),
    marker=dict(size=23),
    hovertemplate='<span style="font-size: 16px;">%{text}</span><extra></extra>',
    text=[f"<b>{trabajadores_objetivo[0]} trabajadores</b>",
          f"<b>{trabajadores_objetivo[1]} trabajadores</b><br>Diferencia: <b>{percentage_diff(trabajadores_objetivo[1], trabajadores_objetivo[0]):.2f}%</b>",
          f"<b>{trabajadores_objetivo[2]} trabajadores</b><br>Diferencia: <b>{percentage_diff(trabajadores_objetivo[2], trabajadores_objetivo[1]):.2f}%</b><br>Diferencia total: <b>{percentage_diff(trabajadores_objetivo[2], trabajadores_objetivo[0]):.2f}%</b>"]
))

# Línea B: Variación de la Tarifa (objetivo)
grafico_variacion_objetivo.add_trace(go.Scatter(
    x=escenarios,
    y=tarifa_objetivo,
    mode='lines+markers',
    name='Tarifa (Objetivo)',
    line=dict(dash='dash', color='green'),
    marker=dict(size=23, color='green'),
    hovertemplate='<span style="font-size: 16px;">%{text}</span><extra></extra>',
    text=[f"<b>Tarifa: {tarifa_objetivo[0]} €/HH</b>",
          f"<b>Tarifa: {tarifa_objetivo[1]} €/HH</b><br>Diferencia: <b>{percentage_diff(tarifa_objetivo[1], tarifa_objetivo[0]):.2f}%</b>",
          f"<b>Tarifa: {tarifa_objetivo[2]} €/HH</b><br>Diferencia: <b>{percentage_diff(tarifa_objetivo[2], tarifa_objetivo[1]):.2f}%</b><br>Diferencia total: <b>{percentage_diff(tarifa_objetivo[2], tarifa_objetivo[0]):.2f}%</b>"]
))

# Calculate the overall min and max for both graphs
all_y_values = trabajadores_inicial + tarifa_inicial + trabajadores_objetivo + tarifa_objetivo
y_min = min(all_y_values)
y_max = max(all_y_values)

# Add some padding to the range
y_range = [y_min - 5, y_max + 5]

# Set consistent graph dimensions and y-axis range
graph_height = 550  # You can adjust this value as needed
graph_width = 1450   # You can adjust this value as needed

# Definir el estilo del fondo negro y texto blanco
layout_style = dict(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white', size=16),  # Aumentamos el tamaño de la fuente
    margin=dict(t=100, b=100, l=100, r=100)  # Aumentamos todos los márgenes
)

# Actualizar el diseño de los gráficos
grafico_variacion_inicial.update_layout(
    title=dict(
        text='<i>Equipo a Contratarse y Tarifa  - Escenario Inicial</i>',
        font=dict(
            size=24,  # Tamaño de fuente más grande para el título
            color='#D1EDFB' # Color azul suave
        ),
        y=0.95  # Mover el título un poco hacia arriba
    ),
    xaxis=dict(
        title=dict(
            text='Escenarios',
            font=dict(size=18),
            standoff=20
        ),
        tickfont={'size': 14},  # Cambiamos el tamaño de la fuente de las etiquetas del eje X
        tickangle=0
    ),
    yaxis=dict(
        title=dict(
            text='Nº de Trabajadores vs Tarifas',
            font=dict(size=18),
            standoff=20
        ),
        tickfont=dict(size=14),
        range=y_range
    ),
    hovermode='closest',
    height=graph_height,
    width=graph_width,
    **layout_style
)

grafico_variacion_objetivo.update_layout(
    title=dict(
        text='<i>Equipo a Contratarse y Tarifa - Escenario Buscado</i>',
        font=dict(
            size=24,  # Tamaño de fuente más grande para el título
            color='#D9F2D0'  # Color verde suave
        ),
        y=0.95  # Mover el título un poco hacia arriba
    ),
    xaxis=dict(
        title=dict(
            text='Escenarios',
            font=dict(size=18),
            standoff=20
        ),
        tickfont={'size': 14},  # Cambiamos el tamaño de la fuente de las etiquetas del eje X
        tickangle=0
    ),
    yaxis=dict(
        title=dict(
            text='Nº de Trabajadores vs Tarifas',
            font=dict(size=18),
            standoff=20
        ),
        tickfont=dict(size=14),
        range=y_range
    ),
    hovermode='closest',
    height=graph_height,
    width=graph_width,
    **layout_style
)

# Definir el layout de la aplicación con estilo de fondo negro y texto blanco
app.layout = html.Div(children=[
    html.H1(children='Comparación de Variaciones en Equipo a Contratarse y Tarifas', 
            style={'color': 'yellow', 'textAlign': 'center', 'fontSize': '32px', 'marginBottom': '40px'}),

    dcc.Graph(
        id='grafico-variacion-inicial',
        figure=grafico_variacion_inicial,
        style={'height': f'{graph_height}px', 'width': '100%', 'marginBottom': '60px'}  # Añadimos margen inferior
    ),
    
    dcc.Graph(
        id='grafico-variacion-objetivo',
        figure=grafico_variacion_objetivo,
        style={'height': f'{graph_height}px', 'width': '100%'}
    )
], style={
    'backgroundColor': 'black',
    'color': 'white',
    'minHeight': '100vh',
    'padding': '40px'  # Aumentamos el padding general
})

# Definir estilos globales para la página
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            body {
                margin: 0;
                background-color: black;
                color: white;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Definir la carpeta de salida
#output_dir = 'graficos'

# Exportar gráficos interactivos como HTML en la carpeta 'graficos'
#grafico_variacion_inicial.write_html(os.path.join(output_dir, 'grafico_variacion_inicial.html'))
#grafico_variacion_objetivo.write_html(os.path.join(output_dir, 'grafico_variacion_objetivo.html'))


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)