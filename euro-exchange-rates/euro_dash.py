# to data manipulation
import pandas as pd
import numpy as np
# to the plots
from bokeh.plotting import figure, show
from bokeh.models import DatetimeTickFormatter
# to create the app
import streamlit as st

# reading the data
euro = pd.read_csv('https://raw.githubusercontent.com/nathpignaton/guided_projects/main/euro-exchange-rates/euro_data.csv')

# converting the Time column to datetime
euro['Time'] = pd.to_datetime(euro['Time'])

# creating the function to plot the clean line graphs
def clean_lineplot(x, y, fig, color='blue', linew=2):
    g = fig
    g.line(x, y, line_color=color, line_width=linew)

    # changing the background
    g.background_fill_color = 'gray'
    g.background_fill_alpha = 0.05

    # configurating the grid lines
    g.xgrid.grid_line_color = 'white'
    g.ygrid.grid_line_color = 'white'

    # removing the outline
    g.outline_line_color = None

    # making the borders the same as the background
    g.border_fill_color = 'gray'
    g.border_fill_alpha = 0.05

    # changing the labels of the x axis to datetime format
    g.xaxis[0].formatter = DatetimeTickFormatter()

    # making the axis colors gray so it won't hold to much atention
    g.xaxis.axis_line_color = None
    g.xaxis.major_label_text_color = 'gray'
    g.xaxis.major_label_text_alpha = 0.8

    # removing y tick labels
    g.yaxis.axis_line_color = None
    g.yaxis.major_label_text_color = 'gray'
    g.yaxis.major_label_text_alpha = 0.8

    # removing the ticks
    g.xaxis.minor_tick_line_color = None
    g.xaxis.major_tick_line_color = None
    g.yaxis.minor_tick_line_color = None
    g.yaxis.major_tick_line_color = None

    # toggling bar autohide
    g.toolbar.autohide = True

    return g

# creating a function to compare the two lineplots in the same graph, in the clean lineplot configurations
def comparison_lineplot(x, y1, y2, fig):
    g = fig
    g = clean_lineplot(x, y1, color='blue', linew=2, fig=fig)
    g = clean_lineplot(x, y2, color='green', linew=2, fig=fig)
    return g

# creating the main graph for us dollar
g1 = figure(title='Euro x US Dollar Exchange Rates', plot_width=300, plot_height=300)
g1 = clean_lineplot(euro['Time'], euro['rm_dollar'], color='blue', linew=2, fig=g1)

# creating the main graph for br Real
g2 = figure(title='Euro x BR Real Exchange Rates', plot_width=300, plot_height=300)
g2 = clean_lineplot(euro['Time'], euro['rm_real'], color='green', fig=g2)

# creating the comparison lineplot
g3 = figure(title='Comparison Euro Exchanges between US Dollar and BR Real', plot_width=1350, plot_height=300)
g3 = comparison_lineplot(euro['Time'], euro['rm_dollar'], euro['rm_real'], fig=g3)

# configurating the appl
st.set_page_config(layout='wide')

# creating a title
st.title('Euro Exchange Rates Between US Dollar and BR Real')
# st.bokeh_chart(g1, use_container_width=False)
# st.bokeh_chart(g2, use_container_width=False)
# st.bokeh_chart(g3, use_container_width=False)

# button configurations
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

# checkbox configurations
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')


# radio button configuration
genre = st.radio("What's your favorite movie genre", ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy")

# selectbox
option = st.selectbox("How would you like to be contacted?", ("E-mail", "Home phone", "Mobile phone"))
st.write("You selected:", option)
















# st.bokeh_chart(g3, use_container_width=True)
