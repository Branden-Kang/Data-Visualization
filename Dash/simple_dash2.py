# Let's build a simple dash app

# Import necessary dash libraries
import dash
import dash_html_components as html

app = dash.Dash(__name__)
app.layout = html.Div(
[
    html.Button('create random number',
               id='button1',
               style={'display':'block', 'background-color':'#aabbcc'}
               ),

    html.Label('...',
               id='label1',
               style={'display':'inline-block','margin':'10'}
              )
]
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8080, host='0.0.0.0')
