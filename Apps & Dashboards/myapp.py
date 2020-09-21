from bokeh.io import show, curdoc
from bokeh.plotting import figure, ColumnDataSource
from bokeh.layouts import row, column
from bokeh.models.widgets import Tabs, Panel
from bokeh.models import Slider, CheckboxGroup, RadioGroup, Button, CustomJS


#data source
x = [x*0.005 for x in range(0, 200)]
y = x
source = ColumnDataSource(data=dict(x=x, y=y))

#Plots
plot_1 = figure(plot_width=400, plot_height=400)
plot_1.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

plot_2=figure(tools='box_zoom, lasso_select')
plot_2.circle(x=[1,2,3,4,5], y=[2,3,1,1,2])
plot_2.background_fill_color = 'black'

plot_3=figure(tools='box_zoom, lasso_select')
plot_3.circle(x=[1,2,3,4,5], y=[2,3,1,1,2])

#widgets
slider = Slider(start=0.1, end=4, value=1, step=.1, title="power")
button = Button(label='Click')
checkbox = CheckboxGroup(labels=['Kibana', 'Bokeh', 'Streamlit', 'Dash'])
radio = RadioGroup(labels=['Kibana', 'Bokeh', 'Streamlit', 'Dash'])

#Interactivity
callback = CustomJS(args=dict(source=source), code="""
        var data = source.data;
        var f = cb_obj.value
        var x = data['x']
        var y = data['y']
        for (var i = 0; i < x.length; i++) {
            y[i] = Math.pow(x[i], f)
        }
        source.change.emit();
    """)
slider.js_on_change('value', callback)

#Plots zoom-linking
plot_2.x_range=plot_3.x_range
plot_2.y_range=plot_3.y_range

#Tabs
first=Panel(child=row(column(slider, button, checkbox, radio), plot_1), title='first')
second=Panel(child=row(plot_2,plot_3), title='second')
tabs=Tabs(tabs=[first, second])

#App
curdoc().add_root(tabs)
show(tabs)
