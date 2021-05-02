



from app import create_app

# Method to protect dash views/routes
def protect_dashviews(dashapp):
    for view_func in dashapp.server.view_functions:
        if view_func.startswith(dashapp.url_base_pathname):
            dashapp.server.view_functions[view_func] = login_required(dashapp.server.view_functions[view_func])

# Create Flask server app
server = create_app()

# =============================
# Dash app
# =============================

# Create dash app passing our server
dashapp = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/')
protect_dashviews(dashapp)

# Push an application context so we can use Flask's 'current_app'
with server.app_context():
    #  Layout definition
    dashapp.layout = html.Div([
    # ...   
    ])

    # Callback
    @dashapp.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
    def update_graph(selected_dropdown_value):

server = create_app()