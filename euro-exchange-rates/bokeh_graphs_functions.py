import pandas as pd
import matplotlib.pyplot as plt
from bokeh.plotting import figure, show
from bokeh.models import DatetimeTickFormatter

# lineplot function
def clean_lineplot(x, y, fig, color='blue', linew=2):
    """
    it plots clean lineplots with bokeh, but the figure has to be specified before its usage.
    x - information that goes in the x axis
    y - information that goes in the y axis
    color - optional, default is blue, can be any color in the hex
    linew - line width, default is 2, can be any other linewidth when specified
    """
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
    
