# Let's build a simple dash app

# Import necessary dash libraries
import dash
import dash_html_components as html

app = dash.Dash(__name__)
app.layout = html.H1("Hello World")

if __name__ == '__main__':
    app.run_server(debug=True, port=8080, host='0.0.0.0')
