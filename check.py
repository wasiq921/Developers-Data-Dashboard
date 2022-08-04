from tkinter import TRUE
from flask import Flask, render_template
from turtle import update
import flask
import dash
import dash_bootstrap_components as dbc
from dash import html, Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
from dash import dcc
import plotly.express as px
import numpy as np
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from torch import layout

server = Flask(__name__)

path = 'D:/Wasiq/Data Studio/'
data_set_path = pd.read_excel(path + 'dataset_paths.xlsx')
colors = {
    'background': '#ededed',
    'text': '#0b1710'
}

# ---------------------------- January Data ----------------------------------------#

jan_avail_data = pd.read_excel(path + 'Jan\Availability - Jan.xlsx')

jan_timesheet_data = pd.read_excel(path + 'Jan\Timesheet Jan.xlsx')

jan_tis_data = pd.read_excel(path + 'Jan\TISReport Jan.xlsx', 'SumReport')

jan_done_data = pd.read_excel(path + 'Jan\DONE Jan.xlsx')


# ---------------------------- February Data ----------------------------------------#

feb_avail_data = pd.read_excel(path + 'Feb\Availability - Feb.xlsx')

feb_timesheet_data = pd.read_excel(path + 'Feb\Timesheet Feb.xlsx')

feb_tis_data = pd.read_excel(path + 'Feb\TISReport Feb.xlsx', 'SumReport')

feb_done_data = pd.read_excel(path + 'Feb\DONE Feb.xlsx')

# ---------------------------- March Data ----------------------------------------#

march_avail_data = pd.read_excel(path + 'March\Availability - March.xlsx')

march_timesheet_data = pd.read_excel(path + 'March\Timesheet March.xlsx')

march_tis_data = pd.read_excel(path + 'March\TISReport March.xlsx', 'SumReport')

march_done_data = pd.read_excel(path + 'March\DONE March.xlsx')

# ---------------------------- April Data ----------------------------------------#

april_avail_data = pd.read_excel(path + 'April\Availability - April.xlsx')

april_timesheet_data = pd.read_excel(path + 'April\Timesheet Apr.xlsx')

april_tis_data = pd.read_excel(path + 'April\TISReport Apr.xlsx', 'SumReport')

april_done_data = pd.read_excel(path + 'April\DONE Apr.xlsx')

# ---------------------------- May Data ----------------------------------------#

may_avail_data = pd.read_excel(path + 'May\Availability - May.xlsx')

may_timesheet_data = pd.read_excel(path + 'May\Timesheet May.xlsx')

may_tis_data = pd.read_excel(path + 'May\TISReport May.xlsx', 'SumReport')


may_done_data = pd.read_excel(path + 'May\DONE May.xlsx')


# ---------------------------- June Data ----------------------------------------#

june_avail_data = pd.read_excel(path + 'June\Availability - June.xlsx')

june_timesheet_data = pd.read_excel(path + 'June\Timesheet June.xlsx')

june_tis_data = pd.read_excel(path + 'June\TISReport June.xlsx', 'SumReport')


june_done_data = pd.read_excel(path + 'June\DONE June.xlsx')

# ---------------------------- July Data ----------------------------------------#

july_avail_data = pd.read_excel(path + 'July\Availability - July.xlsx')

july_timesheet_data = pd.read_excel(path + 'July\Timesheet July.xlsx')

july_tis_data = pd.read_excel(path + 'July\TISReport July.xlsx', 'SumReport')


july_done_data = pd.read_excel(path + 'July\DONE July.xlsx')

# ---------------------------- August Data ----------------------------------------#

august_avail_data = pd.read_excel(path + 'Aug\Availability - Aug.xlsx')

august_timesheet_data = pd.read_excel(path + 'Aug\Timesheet Aug.xlsx')

august_tis_data = pd.read_excel(path + 'Aug\TISReport Aug.xlsx', 'SumReport')


august_done_data = pd.read_excel(path + 'Aug\DONE Aug.xlsx')

# ---------------------------- September Data ----------------------------------------#

sep_avail_data = pd.read_excel(path + 'Sep\Availability - Sep.xlsx')

sep_timesheet_data = pd.read_excel(path + 'Sep\Timesheet Sep.xlsx')

sep_tis_data = pd.read_excel(path + 'Sep\TISReport Sep.xlsx', 'SumReport')


sep_done_data = pd.read_excel(path + 'Sep\DONE Sep.xlsx')

# ---------------------------- October Data ----------------------------------------#

oct_avail_data = pd.read_excel(path + 'Oct\Availability - Oct.xlsx')

oct_timesheet_data = pd.read_excel(path + 'Oct\Timesheet Oct.xlsx')

oct_tis_data = pd.read_excel(path + 'Oct\TISReport Oct.xlsx', 'SumReport')


oct_done_data = pd.read_excel(path + 'Oct\DONE Oct.xlsx')

# ---------------------------- November Data ----------------------------------------#

nov_avail_data = pd.read_excel(path + 'Nov\Availability - Nov.xlsx')

nov_timesheet_data = pd.read_excel(path + 'Nov\Timesheet Nov.xlsx')

nov_tis_data = pd.read_excel(path + 'Nov\TISReport Nov.xlsx', 'SumReport')


nov_done_data = pd.read_excel(path + 'Nov\DONE Nov.xlsx')

# ---------------------------- December Data ----------------------------------------#

dec_avail_data = pd.read_excel(path + 'Dec\Availability - Dec.xlsx')

dec_timesheet_data = pd.read_excel(path + 'Dec\Timesheet Dec.xlsx')

dec_tis_data = pd.read_excel(path + 'Dec\TISReport Dec.xlsx', 'SumReport')


dec_done_data = pd.read_excel(path + 'Dec\DONE Dec.xlsx')




 
mohsin_app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],server = server,url_base_pathname='/mohsin/')
jalil_app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],server = server,url_base_pathname='/jalil/')
angela_app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],server = server,url_base_pathname='/angela/')
narek_app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],server = server,url_base_pathname='/narek/')




@server.route('/')
def home():  # put application's code here
    return render_template('select.html')

app = DispatcherMiddleware(server, {
    '/mohsin': mohsin_app.server,
    '/jalil': jalil_app.server,
    '/angela': angela_app.server,
    '/narek': narek_app.server,
})

@server.route('/mohsin')
def render_mohsin_dashboard():
    return flask.redirect('/mohsin')


@server.route('/jalil')
def render_jalil_dashboard():
    return flask.redirect('/jalil')

@server.route('/angela')
def render_angela_dashboard():
    return flask.redirect('/angela')

@server.route('/narek')
def render_narek_dashboard():
    return flask.redirect('/narek')


def mohsin_layout(a):
    jan_sp1 = jan_done_data[jan_done_data['User'].str.contains('Mohsin')]
    jan_sp1 = jan_sp1[jan_sp1['StoryPoints'] == 1]

    jan_sp2 = jan_done_data[jan_done_data['User'].str.contains('Mohsin')]
    jan_sp2 = jan_sp2[jan_sp2['StoryPoints'] == 2]


    jan_sp3 = jan_done_data[jan_done_data['User'].str.contains('Mohsin')]
    jan_sp3 = jan_sp3[jan_sp3['StoryPoints'] == 3]

    jan_sp5 = jan_done_data[jan_done_data['User'].str.contains('Mohsin')]
    jan_sp5 = jan_sp5[jan_sp5['StoryPoints'] == 5]

    jan_sp8 = jan_done_data[jan_done_data['User'].str.contains('Mohsin')]
    jan_sp8 = jan_sp8[jan_sp8['StoryPoints'] == 8]

    feb_sp1 = feb_done_data[feb_done_data['User'].str.contains('Mohsin')]
    feb_sp1 = feb_sp1[feb_sp1['StoryPoints'] == 1]

    feb_sp2 = feb_done_data[feb_done_data['User'].str.contains('Mohsin')]
    feb_sp2 = feb_sp2[feb_sp2['StoryPoints'] == 2]


    feb_sp3 = feb_done_data[feb_done_data['User'].str.contains('Mohsin')]
    feb_sp3 = feb_sp3[feb_sp3['StoryPoints'] == 3]

    feb_sp5 = feb_done_data[feb_done_data['User'].str.contains('Mohsin')]
    feb_sp5 = feb_sp5[feb_sp5['StoryPoints'] == 5]

    feb_sp8 = feb_done_data[feb_done_data['User'].str.contains('Mohsin')]
    feb_sp8 = feb_sp8[feb_sp8['StoryPoints'] == 8]


    march_sp1 = march_done_data[march_done_data['User'].str.contains('Mohsin')]
    march_sp1 = march_sp1[march_sp1['StoryPoints'] == 1]

    march_sp2 = march_done_data[march_done_data['User'].str.contains('Mohsin')]
    march_sp2 = march_sp2[march_sp2['StoryPoints'] == 2]


    march_sp3 = march_done_data[march_done_data['User'].str.contains('Mohsin')]
    march_sp3 = march_sp3[march_sp3['StoryPoints'] == 3]

    march_sp5 = march_done_data[march_done_data['User'].str.contains('Mohsin')]
    march_sp5 = march_sp5[march_sp5['StoryPoints'] == 5]

    march_sp8 = march_done_data[march_done_data['User'].str.contains('Mohsin')]
    march_sp8 = march_sp8[march_sp8['StoryPoints'] == 8]


    april_sp1 = april_done_data[april_done_data['User'].str.contains('Mohsin')]
    april_sp1 = april_sp1[april_sp1['StoryPoints'] == 1]

    april_sp2 = april_done_data[april_done_data['User'].str.contains('Mohsin')]
    april_sp2 = april_sp2[april_sp2['StoryPoints'] == 2]


    april_sp3 = april_done_data[april_done_data['User'].str.contains('Mohsin')]
    april_sp3 = april_sp3[april_sp3['StoryPoints'] == 3]

    april_sp5 = april_done_data[april_done_data['User'].str.contains('Mohsin')]
    april_sp5 = april_sp5[april_sp5['StoryPoints'] == 5]

    april_sp8 = april_done_data[april_done_data['User'].str.contains('Mohsin')]
    april_sp8 = april_sp8[april_sp8['StoryPoints'] == 8]

    may_sp1 = may_done_data[may_done_data['User'].str.contains('Mohsin')]
    may_sp1 = may_sp1[may_sp1['StoryPoints'] == 1]

    may_sp2 = may_done_data[may_done_data['User'].str.contains('Mohsin')]
    may_sp2 = may_sp2[may_sp2['StoryPoints'] == 2]


    may_sp3 = may_done_data[may_done_data['User'].str.contains('Mohsin')]
    may_sp3 = may_sp3[may_sp3['StoryPoints'] == 3]

    may_sp5 = may_done_data[may_done_data['User'].str.contains('Mohsin')]
    may_sp5 = may_sp5[may_sp5['StoryPoints'] == 5]

    may_sp8 = may_done_data[may_done_data['User'].str.contains('Mohsin')]
    may_sp8 = may_sp8[may_sp8['StoryPoints'] == 8]
    
    june_sp1 = june_done_data[june_done_data['User'].str.contains('Mohsin')]
    june_sp1 = june_sp1[june_sp1['StoryPoints'] == 1]
    
    june_sp2 = june_done_data[june_done_data['User'].str.contains('Mohsin')]
    june_sp2 = june_sp2[june_sp2['StoryPoints'] == 2]


    june_sp3 = june_done_data[june_done_data['User'].str.contains('Mohsin')]
    june_sp3 = june_sp3[june_sp3['StoryPoints'] == 3]

    june_sp5 = june_done_data[june_done_data['User'].str.contains('Mohsin')]
    june_sp5 = june_sp5[june_sp5['StoryPoints'] == 5]

    june_sp8 = june_done_data[june_done_data['User'].str.contains('Mohsin')]
    june_sp8 = june_sp8[june_sp8['StoryPoints'] == 8]
    
    july_sp1 = july_done_data[july_done_data['User'].str.contains('Mohsin')]
    july_sp1 = july_sp1[july_sp1['StoryPoints'] == 1]
    
    july_sp2 = july_done_data[july_done_data['User'].str.contains('Mohsin')]
    july_sp2 = july_sp2[july_sp2['StoryPoints'] == 2]


    july_sp3 = july_done_data[july_done_data['User'].str.contains('Mohsin')]
    july_sp3 = july_sp3[july_sp3['StoryPoints'] == 3]

    july_sp5 = july_done_data[july_done_data['User'].str.contains('Mohsin')]
    july_sp5 = july_sp5[july_sp5['StoryPoints'] == 5]

    july_sp8 = july_done_data[july_done_data['User'].str.contains('Mohsin')]
    july_sp8 = july_sp8[july_sp8['StoryPoints'] == 8]

    august_sp1 = august_done_data[august_done_data['User'].str.contains('Mohsin')]
    august_sp1 = august_sp1[august_sp1['StoryPoints'] == 1]
    
    august_sp2 = august_done_data[august_done_data['User'].str.contains('Mohsin')]
    august_sp2 = august_sp2[august_sp2['StoryPoints'] == 2]


    august_sp3 = august_done_data[august_done_data['User'].str.contains('Mohsin')]
    august_sp3 = august_sp3[august_sp3['StoryPoints'] == 3]

    august_sp5 = august_done_data[august_done_data['User'].str.contains('Mohsin')]
    august_sp5 = august_sp5[august_sp5['StoryPoints'] == 5]

    august_sp8 = august_done_data[august_done_data['User'].str.contains('Mohsin')]
    august_sp8 = august_sp8[august_sp8['StoryPoints'] == 8]

    sep_sp1 = sep_done_data[sep_done_data['User'].str.contains('Mohsin')]
    sep_sp1 = sep_sp1[sep_sp1['StoryPoints'] == 1]
    
    sep_sp2 = sep_done_data[sep_done_data['User'].str.contains('Mohsin')]
    sep_sp2 = sep_sp2[sep_sp2['StoryPoints'] == 2]


    sep_sp3 = sep_done_data[sep_done_data['User'].str.contains('Mohsin')]
    sep_sp3 = sep_sp3[sep_sp3['StoryPoints'] == 3]

    sep_sp5 = sep_done_data[sep_done_data['User'].str.contains('Mohsin')]
    sep_sp5 = sep_sp5[sep_sp5['StoryPoints'] == 5]

    sep_sp8 = sep_done_data[sep_done_data['User'].str.contains('Mohsin')]
    sep_sp8 = sep_sp8[sep_sp8['StoryPoints'] == 8]


    oct_sp1 = oct_done_data[oct_done_data['User'].str.contains('Mohsin')]
    oct_sp1 = oct_sp1[oct_sp1['StoryPoints'] == 1]
    
    oct_sp2 = oct_done_data[oct_done_data['User'].str.contains('Mohsin')]
    oct_sp2 = oct_sp2[oct_sp2['StoryPoints'] == 2]


    oct_sp3 = oct_done_data[oct_done_data['User'].str.contains('Mohsin')]
    oct_sp3 = oct_sp3[oct_sp3['StoryPoints'] == 3]

    oct_sp5 = oct_done_data[oct_done_data['User'].str.contains('Mohsin')]
    oct_sp5 = oct_sp5[oct_sp5['StoryPoints'] == 5]

    oct_sp8 = oct_done_data[oct_done_data['User'].str.contains('Mohsin')]
    oct_sp8 = oct_sp8[oct_sp8['StoryPoints'] == 8]

    nov_sp1 = nov_done_data[nov_done_data['User'].str.contains('Mohsin')]
    nov_sp1 = nov_sp1[nov_sp1['StoryPoints'] == 1]
    
    nov_sp2 = nov_done_data[nov_done_data['User'].str.contains('Mohsin')]
    nov_sp2 = nov_sp2[nov_sp2['StoryPoints'] == 2]


    nov_sp3 = nov_done_data[nov_done_data['User'].str.contains('Mohsin')]
    nov_sp3 = nov_sp3[nov_sp3['StoryPoints'] == 3]

    nov_sp5 = nov_done_data[nov_done_data['User'].str.contains('Mohsin')]
    nov_sp5 = nov_sp5[nov_sp5['StoryPoints'] == 5]

    nov_sp8 = nov_done_data[nov_done_data['User'].str.contains('Mohsin')]
    nov_sp8 = nov_sp8[nov_sp8['StoryPoints'] == 8]

    dec_sp1 = dec_done_data[dec_done_data['User'].str.contains('Mohsin')]
    dec_sp1 = dec_sp1[dec_sp1['StoryPoints'] == 1]
    
    dec_sp2 = dec_done_data[dec_done_data['User'].str.contains('Mohsin')]
    dec_sp2 = dec_sp2[dec_sp2['StoryPoints'] == 2]


    dec_sp3 = dec_done_data[dec_done_data['User'].str.contains('Mohsin')]
    dec_sp3 = dec_sp3[dec_sp3['StoryPoints'] == 3]

    dec_sp5 = dec_done_data[dec_done_data['User'].str.contains('Mohsin')]
    dec_sp5 = dec_sp5[dec_sp5['StoryPoints'] == 5]

    dec_sp8 = dec_done_data[dec_done_data['User'].str.contains('Mohsin')]
    dec_sp8 = dec_sp8[dec_sp8['StoryPoints'] == 8]
    
    jan_intime_loggedtime = (jan_tis_data['Abdul Mohsin - In Progress']/jan_timesheet_data[jan_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100

    feb_intime_loggedtime = (feb_tis_data['Abdul Mohsin - In Progress']/feb_timesheet_data[feb_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100
   
    march_intime_loggedtime = (march_tis_data['Abdul Mohsin - In Progress']/march_timesheet_data[march_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100

    april_intime_loggedtime = (april_tis_data['Abdul Mohsin - In Progress']/april_timesheet_data[april_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100

    may_intime_loggedtime = (may_tis_data['Mohsin - In Progress']/may_timesheet_data[may_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100

    june_intime_loggedtime = (june_tis_data['Mohsin - In Progress']/june_timesheet_data[june_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100

    july_intime_loggedtime = (july_tis_data['Mohsin - In Progress']/july_timesheet_data[july_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100
    
    august_intime_loggedtime = (august_tis_data['Mohsin - In Progress']/august_timesheet_data[august_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100

    sep_intime_loggedtime = (sep_tis_data['Mohsin - In Progress']/sep_timesheet_data[sep_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100

    oct_intime_loggedtime = (oct_tis_data['Mohsin - In Progress']/oct_timesheet_data[oct_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100

    nov_intime_loggedtime = (nov_tis_data['Mohsin - In Progress']/nov_timesheet_data[nov_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100
    
    dec_intime_loggedtime = (dec_tis_data['Mohsin - In Progress']/dec_timesheet_data[dec_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100

    graph_colors = {
        'background': 'transparent',
    }

    avail_logg_diff = ["{:.2f}".format((jan_avail_data['Availability'][a]/jan_timesheet_data[jan_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100),
    "{:.2f}".format((feb_avail_data['Availability'][a]/feb_timesheet_data[feb_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100),
    "{:.2f}".format((march_avail_data['Availability'][a]/march_timesheet_data[march_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100),
    "{:.2f}".format((april_avail_data['Availability'][a]/april_timesheet_data[april_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100),
    "{:.2f}".format((may_avail_data['Availability'][a]/may_timesheet_data[may_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100),
    "{:.2f}".format((june_avail_data['Availability'][a]/june_timesheet_data[june_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100),
    "{:.2f}".format((july_avail_data['Availability'][a]/july_timesheet_data[july_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100),
    "{:.2f}".format((august_avail_data['Availability'][a]/august_timesheet_data[august_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100),
    "{:.2f}".format((sep_avail_data['Availability'][a]/sep_timesheet_data[sep_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100),
    "{:.2f}".format((oct_avail_data['Availability'][a]/oct_timesheet_data[oct_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100),
    "{:.2f}".format((nov_avail_data['Availability'][a]/nov_timesheet_data[nov_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100),
    "{:.2f}".format((dec_avail_data['Availability'][a]/dec_timesheet_data[dec_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100)]
    
    months = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    in_time_logg_time = ["{:.2f}".format(float(jan_intime_loggedtime)), 
    "{:.2f}".format(float(feb_intime_loggedtime)), 
    "{:.2f}".format(float(march_intime_loggedtime)), 
    "{:.2f}".format(float(april_intime_loggedtime)), 
    "{:.2f}".format(float(may_intime_loggedtime)), 
    "{:.2f}".format(float(june_intime_loggedtime)), 
    "{:.2f}".format(float(july_intime_loggedtime)), 
    "{:.2f}".format(float(august_intime_loggedtime)), 
    "{:.2f}".format(float(sep_intime_loggedtime)), 
    "{:.2f}".format(float(oct_intime_loggedtime)), 
    "{:.2f}".format(float(nov_intime_loggedtime)), 
    "{:.2f}".format(float(dec_intime_loggedtime))] 




    layout = html.Div(style = {'background-color' : 'darkgray', 'width' : '100%'}, children=[
                dbc.Row([
                    # dbc.Col([dbc.Button(
                    #     "Button1", id="april-button", n_clicks=0, color="dark", style={"width": "100%"})]),
                    # dbc.Col([dbc.Button(
                    #     "Button2", id="may-button", n_clicks=0, color="dark", style={"width": "100%"})]),
                    # dbc.Col([dbc.Button(
                    #     "Button3", id="june-button", n_clicks=0, color="dark", style={"width": "100%"})]),
                ]),

    # dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    # dbc.Col([
    #     html.Div([
    # dbc.Button(children  = april_avail_data['User'][0], id="mohsin-button", n_clicks =0, style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #     dbc.Button(children  = april_avail_data['User'][1], id = "baghdasaryan-button", n_clicks = 0,style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #         dbc.Button(children  = april_avail_data['User'][2], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #             dbc.Button(children  = april_avail_data['User'][3], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #             dbc.Button(children  = april_avail_data['User'][4], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #             #    dbc.Button(children  = april_avail_data['User'][0], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    # html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    # ], )
    # ]
    # )
    # ]),
    # html.Br(),
    # html.Br(),
    dbc.Collapse([
    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    html.H1(children  = april_avail_data['User'][a], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),
    # html.Br(),
    # html.Br(),
    html.Div(style = {'margin-left': '45px', 'background-color': 'white',      'width' : '1250px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '20px', 'margin-left' : '30px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability (hours per month)', style={'margin-left' : '20px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ])
    ,
    dbc.Row([ dbc.Col([
        html.Div(style = {'margin-top' : '10px', 'margin-left' : '15px','width':'100%'}, children=[
            html.Span(children= jan_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '40px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= feb_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= march_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= april_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= may_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= june_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children=  july_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= august_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= sep_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= oct_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= nov_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= dec_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            
        ])
    ])]),
        dbc.Row([dbc.Col([
        html.Div(style = {'margin-top' : '10px', 'margin-left' : '15px'}, children=[
            html.Span(children= 'Jan', style={'display' : 'inline-block', 'margin-left' : '40px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Feb', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Mar', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Apr', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'May', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Jun', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Jul', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Aug', style={'display' : 'inline-block', 'margin-left' : '40px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Sep', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Oct', style={'display' : 'inline-block', 'margin-left' : '20px','margin-right' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Nov', style={'display' : 'inline-block', 'margin-left' : '20px','margin-right' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Dec', style={'display' : 'inline-block', 'margin-left' : '20px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            
        ])
    ]),


    ])
    ]
    ),

    html.Br(),
    html.Br(),



    dbc.Row(style= {'width' : '1200px', 'margin-left': '70px'},
    children = [
        dbc.Col(style = {'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'AVAILABILITY  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = avail_logg_diff, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
        dbc.Col(style = {'margin-left' : '20px', 'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'IN STATUS TIME  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = in_time_logg_time, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
    ]),
    html.Br(),


    dbc.Row(style= {'width' : '1200px', 'margin-left': '70px'},
    children = [
        dbc.Col(style = {'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = april_avail_data['User'][a], style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    html.P(children = 'Works with ?????? on our web-platform and is located in ????? with timezone ???', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    html.P(children = 'Other Descriptive Text', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'})
    ])
        ]),
        dbc.Col(style = {'margin-left' : '20px', 'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = '1 STORYPOINT  vs LOGGED TIME(weighted average, hours)', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = in_time_logg_time, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
    ]),
    html.Br(),


    dbc.Row(style= {'width' : '1200px', 'margin-left': '70px'},
    children = [
        dbc.Col(style = {'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'AVAILABILITY  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = avail_logg_diff, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
        dbc.Col(style = {'margin-left' : '20px', 'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'IN STATUS TIME  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = in_time_logg_time, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1200px', 'margin-left': '70px'},
    children = [
        dbc.Col(style = {'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'AVAILABILITY  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = avail_logg_diff, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
        dbc.Col(style = {'margin-left' : '20px', 'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'IN STATUS TIME  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = in_time_logg_time, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
    ]),

    html.Br(),
    html.Br(),

                html.Div(children=[
                        dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'January', id="jan-button", n_clicks =0, style={'border': '0px','background-color':'transparent','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = jan_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = jan_timesheet_data[jan_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(jan_tis_data['Abdul Mohsin - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((jan_avail_data['Availability'][a]/jan_timesheet_data[jan_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),

    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(jan_intime_loggedtime)) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),


    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(jan_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(jan_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(jan_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(jan_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(jan_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="jan-collapse", is_open=False),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
        dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'February', id="feb-button", n_clicks =0, style={'border': '0px','background-color':'transparent','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = feb_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = feb_timesheet_data[feb_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(feb_tis_data['Abdul Mohsin - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((feb_avail_data['Availability'][a]/feb_timesheet_data[feb_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),

    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  ="{:.2f}".format(float(feb_intime_loggedtime)) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),


    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(feb_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(feb_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(feb_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(feb_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(feb_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="feb-collapse", is_open=False),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'March', id="march-button", n_clicks =0, style={'border': '0px','background-color':'transparent','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = march_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = march_timesheet_data[march_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(march_tis_data['Abdul Mohsin - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((march_avail_data['Availability'][a]/march_timesheet_data[march_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),

    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(march_intime_loggedtime)) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(march_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(march_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(march_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(march_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(march_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="march-collapse", is_open=False),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'April', id="april-button", n_clicks =0, style={'border': '0px','background-color':'transparent','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = april_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = april_timesheet_data[april_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(april_tis_data['Abdul Mohsin - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((april_avail_data['Availability'][a]/april_timesheet_data[april_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),

    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(april_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(april_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(april_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(april_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(april_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(april_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="april-collapse", is_open=False),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'May', id = 'may-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = may_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = may_timesheet_data[may_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(may_tis_data['Mohsin - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((may_avail_data['Availability'][a]/may_timesheet_data[may_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(may_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(may_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(may_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(may_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(may_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(may_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="may-collapse", is_open=False),
                        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'June', id = 'june-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = june_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = june_timesheet_data[june_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(june_tis_data['Mohsin - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((june_avail_data['Availability'][a]/june_timesheet_data[june_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(june_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(june_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(june_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(june_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(june_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(june_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="june-collapse", is_open=False),
    html.Br(),
    html.Br(),

                        dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'July', id = 'july-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = july_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = july_timesheet_data[july_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(july_tis_data['Mohsin - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((july_avail_data['Availability'][a]/july_timesheet_data[july_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(july_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(july_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(july_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(july_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(july_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(july_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="july-collapse", is_open=False),
                        html.Br(),
    html.Br(),

                        dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'August', id = 'august-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = august_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = august_timesheet_data[august_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(august_tis_data['Mohsin - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((august_avail_data['Availability'][a]/august_timesheet_data[august_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(august_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(august_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(august_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(august_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(august_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(august_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="august-collapse", is_open=False),

                    
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'September', id = 'sep-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = sep_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = sep_timesheet_data[sep_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(sep_tis_data['Mohsin - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((sep_avail_data['Availability'][a]/sep_timesheet_data[sep_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(sep_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(sep_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(sep_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(sep_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(sep_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(sep_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="sep-collapse", is_open=False),
                            
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'October', id = 'oct-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = oct_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = oct_timesheet_data[oct_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(oct_tis_data['Mohsin - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((oct_avail_data['Availability'][a]/oct_timesheet_data[oct_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(oct_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(oct_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(oct_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(oct_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(oct_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(oct_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="oct-collapse", is_open=False),
           
                    
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'November', id = 'nov-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = nov_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = nov_timesheet_data[nov_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(nov_tis_data['Mohsin - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((nov_avail_data['Availability'][a]/nov_timesheet_data[nov_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(nov_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(nov_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(nov_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(nov_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(nov_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(nov_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="nov-collapse", is_open=False),
                        
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'December', id = 'dec-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = dec_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = dec_timesheet_data[dec_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(dec_tis_data['Mohsin - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((dec_avail_data['Availability'][a]/dec_timesheet_data[dec_timesheet_data['User'].str.contains('Mohsin')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(dec_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(dec_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(dec_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(dec_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(dec_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(dec_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="dec-collapse", is_open=False),

                ]),
                dcc.Interval(
                    id='interval-component',
                    interval=1000, # in milliseconds
                    n_intervals=1,
                    max_intervals = 2, 
                    disabled = True
                )
                ], id = "mohsin-collapse", is_open = True),
                
    ])

    @mohsin_app.callback(
            [
                
                Output("jan-collapse", "is_open"),
                Output("feb-collapse", "is_open"),
                Output("march-collapse", "is_open"),
            Output("april-collapse", "is_open"),
            Output("may-collapse", "is_open"),
            Output("june-collapse", "is_open"),
            Output("july-collapse", "is_open"),
            Output("august-collapse", "is_open"),
            Output("sep-collapse", "is_open"),
            Output("oct-collapse", "is_open"),
            Output("nov-collapse", "is_open"),
            Output("dec-collapse", "is_open"),
        
            ],
            [
            
                Input("jan-button", "n_clicks"),
            Input("feb-button", "n_clicks"),
            Input("march-button", "n_clicks"),
            Input("april-button", "n_clicks"),
            Input("may-button", "n_clicks"),
            Input("june-button", "n_clicks"),
            Input("july-button", "n_clicks"),
            Input("august-button", "n_clicks"),
            Input("sep-button", "n_clicks"),
            Input("oct-button", "n_clicks"),
            Input("nov-button", "n_clicks"),
            Input("dec-button", "n_clicks"),
        
            ],
        )
    def toggle_collapses(button_one, button_two, button_three, button_four, button_five, button_six, button_seven, button_eight,
    button_nine, button_ten, button_eleven, button_twelve):
            ctx = dash.callback_context

            if not ctx.triggered:
                raise PreventUpdate
            else:
                button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            
            
            if button_id == 'jan-button':
                print(april_sp1['StoryPoints'])
                return True, False, False, False, False, False, False, False, False, False, False, False
            elif button_id == 'feb-button':
                return False, True, False, False, False, False, False, False, False, False, False, False
            elif button_id == 'march-button':
                return False, False, True, False, False, False, False, False, False, False, False, False
            elif button_id == 'april-button':
                return False, False, False, True, False, False, False, False, False, False, False, False
            elif button_id == 'may-button':
                return False, False, False, False, True, False, False, False, False, False, False, False
            elif button_id == 'june-button':
                return False, False, False, False, False, True, False, False, False, False, False, False
            elif button_id == 'july-button':
                return False, False, False, False, False, False, True, False, False, False, False, False
            elif button_id == 'august-button':
                return False, False, False, False, False, False, False, True, False, False, False, False
            elif button_id == 'sep-button':
                return False, False, False, False, False, False, False, False, True, False, False, False
            elif button_id == 'oct-button':
                return False, False, False, False, False, False, False, False, False, True, False, False
            elif button_id == 'nov-button':
                return False, False, False, False, False, False, False, False, False, False, True, False
            elif button_id == 'dec-button':
                return False, False, False, False, False, False, False, False, False, False, False, True
            else:
                raise ValueError(f'Unexpected ID: {button_id}')
    return layout


def jalil_layout(a):
    jan_sp1 = jan_done_data[jan_done_data['User'].str.contains('Abdul Jalil')]
    jan_sp1 = jan_sp1[jan_sp1['StoryPoints'] == 1]

    jan_sp2 = jan_done_data[jan_done_data['User'].str.contains('Abdul Jalil')]
    jan_sp2 = jan_sp2[jan_sp2['StoryPoints'] == 2]


    jan_sp3 = jan_done_data[jan_done_data['User'].str.contains('Abdul Jalil')]
    jan_sp3 = jan_sp3[jan_sp3['StoryPoints'] == 3]

    jan_sp5 = jan_done_data[jan_done_data['User'].str.contains('Abdul Jalil')]
    jan_sp5 = jan_sp5[jan_sp5['StoryPoints'] == 5]

    jan_sp8 = jan_done_data[jan_done_data['User'].str.contains('Abdul Jalil')]
    jan_sp8 = jan_sp8[jan_sp8['StoryPoints'] == 8]

    feb_sp1 = feb_done_data[feb_done_data['User'].str.contains('Abdul Jalil')]
    feb_sp1 = feb_sp1[feb_sp1['StoryPoints'] == 1]

    feb_sp2 = feb_done_data[feb_done_data['User'].str.contains('Abdul Jalil')]
    feb_sp2 = feb_sp2[feb_sp2['StoryPoints'] == 2]


    feb_sp3 = feb_done_data[feb_done_data['User'].str.contains('Abdul Jalil')]
    feb_sp3 = feb_sp3[feb_sp3['StoryPoints'] == 3]

    feb_sp5 = feb_done_data[feb_done_data['User'].str.contains('Abdul Jalil')]
    feb_sp5 = feb_sp5[feb_sp5['StoryPoints'] == 5]

    feb_sp8 = feb_done_data[feb_done_data['User'].str.contains('Abdul Jalil')]
    feb_sp8 = feb_sp8[feb_sp8['StoryPoints'] == 8]


    march_sp1 = march_done_data[march_done_data['User'].str.contains('Abdul Jalil')]
    march_sp1 = march_sp1[march_sp1['StoryPoints'] == 1]

    march_sp2 = march_done_data[march_done_data['User'].str.contains('Abdul Jalil')]
    march_sp2 = march_sp2[march_sp2['StoryPoints'] == 2]


    march_sp3 = march_done_data[march_done_data['User'].str.contains('Abdul Jalil')]
    march_sp3 = march_sp3[march_sp3['StoryPoints'] == 3]

    march_sp5 = march_done_data[march_done_data['User'].str.contains('Abdul Jalil')]
    march_sp5 = march_sp5[march_sp5['StoryPoints'] == 5]

    march_sp8 = march_done_data[march_done_data['User'].str.contains('Abdul Jalil')]
    march_sp8 = march_sp8[march_sp8['StoryPoints'] == 8]


    april_sp1 = april_done_data[april_done_data['User'].str.contains('Abdul Jalil')]
    april_sp1 = april_sp1[april_sp1['StoryPoints'] == 1]

    april_sp2 = april_done_data[april_done_data['User'].str.contains('Abdul Jalil')]
    april_sp2 = april_sp2[april_sp2['StoryPoints'] == 2]


    april_sp3 = april_done_data[april_done_data['User'].str.contains('Abdul Jalil')]
    april_sp3 = april_sp3[april_sp3['StoryPoints'] == 3]

    april_sp5 = april_done_data[april_done_data['User'].str.contains('Abdul Jalil')]
    april_sp5 = april_sp5[april_sp5['StoryPoints'] == 5]

    april_sp8 = april_done_data[april_done_data['User'].str.contains('Abdul Jalil')]
    april_sp8 = april_sp8[april_sp8['StoryPoints'] == 8]

    may_sp1 = may_done_data[may_done_data['User'].str.contains('Abdul Jalil')]
    may_sp1 = may_sp1[may_sp1['StoryPoints'] == 1]

    may_sp2 = may_done_data[may_done_data['User'].str.contains('Abdul Jalil')]
    may_sp2 = may_sp2[may_sp2['StoryPoints'] == 2]


    may_sp3 = may_done_data[may_done_data['User'].str.contains('Abdul Jalil')]
    may_sp3 = may_sp3[may_sp3['StoryPoints'] == 3]

    may_sp5 = may_done_data[may_done_data['User'].str.contains('Abdul Jalil')]
    may_sp5 = may_sp5[may_sp5['StoryPoints'] == 5]

    may_sp8 = may_done_data[may_done_data['User'].str.contains('Abdul Jalil')]
    may_sp8 = may_sp8[may_sp8['StoryPoints'] == 8]
    
    june_sp1 = june_done_data[june_done_data['User'].str.contains('Abdul Jalil')]
    june_sp1 = june_sp1[june_sp1['StoryPoints'] == 1]
    
    june_sp2 = june_done_data[june_done_data['User'].str.contains('Abdul Jalil')]
    june_sp2 = june_sp2[june_sp2['StoryPoints'] == 2]


    june_sp3 = june_done_data[june_done_data['User'].str.contains('Abdul Jalil')]
    june_sp3 = june_sp3[june_sp3['StoryPoints'] == 3]

    june_sp5 = june_done_data[june_done_data['User'].str.contains('Abdul Jalil')]
    june_sp5 = june_sp5[june_sp5['StoryPoints'] == 5]

    june_sp8 = june_done_data[june_done_data['User'].str.contains('Abdul Jalil')]
    june_sp8 = june_sp8[june_sp8['StoryPoints'] == 8]
    
    july_sp1 = july_done_data[july_done_data['User'].str.contains('Abdul Jalil')]
    july_sp1 = july_sp1[july_sp1['StoryPoints'] == 1]
    
    july_sp2 = july_done_data[july_done_data['User'].str.contains('Abdul Jalil')]
    july_sp2 = july_sp2[july_sp2['StoryPoints'] == 2]


    july_sp3 = july_done_data[july_done_data['User'].str.contains('Abdul Jalil')]
    july_sp3 = july_sp3[july_sp3['StoryPoints'] == 3]

    july_sp5 = july_done_data[july_done_data['User'].str.contains('Abdul Jalil')]
    july_sp5 = july_sp5[july_sp5['StoryPoints'] == 5]

    july_sp8 = july_done_data[july_done_data['User'].str.contains('Abdul Jalil')]
    july_sp8 = july_sp8[july_sp8['StoryPoints'] == 8]

    august_sp1 = august_done_data[august_done_data['User'].str.contains('Abdul Jalil')]
    august_sp1 = august_sp1[august_sp1['StoryPoints'] == 1]
    
    august_sp2 = august_done_data[august_done_data['User'].str.contains('Abdul Jalil')]
    august_sp2 = august_sp2[august_sp2['StoryPoints'] == 2]


    august_sp3 = august_done_data[august_done_data['User'].str.contains('Abdul Jalil')]
    august_sp3 = august_sp3[august_sp3['StoryPoints'] == 3]

    august_sp5 = august_done_data[august_done_data['User'].str.contains('Abdul Jalil')]
    august_sp5 = august_sp5[august_sp5['StoryPoints'] == 5]

    august_sp8 = august_done_data[august_done_data['User'].str.contains('Abdul Jalil')]
    august_sp8 = august_sp8[august_sp8['StoryPoints'] == 8]

    sep_sp1 = sep_done_data[sep_done_data['User'].str.contains('Abdul Jalil')]
    sep_sp1 = sep_sp1[sep_sp1['StoryPoints'] == 1]
    
    sep_sp2 = sep_done_data[sep_done_data['User'].str.contains('Abdul Jalil')]
    sep_sp2 = sep_sp2[sep_sp2['StoryPoints'] == 2]


    sep_sp3 = sep_done_data[sep_done_data['User'].str.contains('Abdul Jalil')]
    sep_sp3 = sep_sp3[sep_sp3['StoryPoints'] == 3]

    sep_sp5 = sep_done_data[sep_done_data['User'].str.contains('Abdul Jalil')]
    sep_sp5 = sep_sp5[sep_sp5['StoryPoints'] == 5]

    sep_sp8 = sep_done_data[sep_done_data['User'].str.contains('Abdul Jalil')]
    sep_sp8 = sep_sp8[sep_sp8['StoryPoints'] == 8]


    oct_sp1 = oct_done_data[oct_done_data['User'].str.contains('Abdul Jalil')]
    oct_sp1 = oct_sp1[oct_sp1['StoryPoints'] == 1]
    
    oct_sp2 = oct_done_data[oct_done_data['User'].str.contains('Abdul Jalil')]
    oct_sp2 = oct_sp2[oct_sp2['StoryPoints'] == 2]


    oct_sp3 = oct_done_data[oct_done_data['User'].str.contains('Abdul Jalil')]
    oct_sp3 = oct_sp3[oct_sp3['StoryPoints'] == 3]

    oct_sp5 = oct_done_data[oct_done_data['User'].str.contains('Abdul Jalil')]
    oct_sp5 = oct_sp5[oct_sp5['StoryPoints'] == 5]

    oct_sp8 = oct_done_data[oct_done_data['User'].str.contains('Abdul Jalil')]
    oct_sp8 = oct_sp8[oct_sp8['StoryPoints'] == 8]

    nov_sp1 = nov_done_data[nov_done_data['User'].str.contains('Abdul Jalil')]
    nov_sp1 = nov_sp1[nov_sp1['StoryPoints'] == 1]
    
    nov_sp2 = nov_done_data[nov_done_data['User'].str.contains('Abdul Jalil')]
    nov_sp2 = nov_sp2[nov_sp2['StoryPoints'] == 2]


    nov_sp3 = nov_done_data[nov_done_data['User'].str.contains('Abdul Jalil')]
    nov_sp3 = nov_sp3[nov_sp3['StoryPoints'] == 3]

    nov_sp5 = nov_done_data[nov_done_data['User'].str.contains('Abdul Jalil')]
    nov_sp5 = nov_sp5[nov_sp5['StoryPoints'] == 5]

    nov_sp8 = nov_done_data[nov_done_data['User'].str.contains('Abdul Jalil')]
    nov_sp8 = nov_sp8[nov_sp8['StoryPoints'] == 8]

    dec_sp1 = dec_done_data[dec_done_data['User'].str.contains('Abdul Jalil')]
    dec_sp1 = dec_sp1[dec_sp1['StoryPoints'] == 1]
    
    dec_sp2 = dec_done_data[dec_done_data['User'].str.contains('Abdul Jalil')]
    dec_sp2 = dec_sp2[dec_sp2['StoryPoints'] == 2]


    dec_sp3 = dec_done_data[dec_done_data['User'].str.contains('Abdul Jalil')]
    dec_sp3 = dec_sp3[dec_sp3['StoryPoints'] == 3]

    dec_sp5 = dec_done_data[dec_done_data['User'].str.contains('Abdul Jalil')]
    dec_sp5 = dec_sp5[dec_sp5['StoryPoints'] == 5]

    dec_sp8 = dec_done_data[dec_done_data['User'].str.contains('Abdul Jalil')]
    dec_sp8 = dec_sp8[dec_sp8['StoryPoints'] == 8]
    
    jan_intime_loggedtime = (jan_tis_data['Abdul Jalil - In Progress']/jan_timesheet_data[jan_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100

    feb_intime_loggedtime = (feb_tis_data['Abdul Jalil - In Progress']/feb_timesheet_data[feb_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100
   
    march_intime_loggedtime = (march_tis_data['Abdul Jalil - In Progress']/march_timesheet_data[march_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100

    april_intime_loggedtime = (april_tis_data['Abdul Jalil - In Progress']/april_timesheet_data[april_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100

    may_intime_loggedtime = (may_tis_data['Abdul Jalil - In Progress']/may_timesheet_data[may_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100

    june_intime_loggedtime = (june_tis_data['Abdul Jalil - In Progress']/june_timesheet_data[june_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100

    july_intime_loggedtime = (july_tis_data['Abdul Jalil - In Progress']/july_timesheet_data[july_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100
    
    august_intime_loggedtime = (august_tis_data['Abdul Jalil - In Progress']/august_timesheet_data[august_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100

    sep_intime_loggedtime = (sep_tis_data['Abdul Jalil - In Progress']/sep_timesheet_data[sep_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100

    oct_intime_loggedtime = (oct_tis_data['Abdul Jalil - In Progress']/oct_timesheet_data[oct_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100

    nov_intime_loggedtime = (nov_tis_data['Abdul Jalil - In Progress']/nov_timesheet_data[nov_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100
    
    dec_intime_loggedtime = (dec_tis_data['Abdul Jalil - In Progress']/dec_timesheet_data[dec_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100

    graph_colors = {
        'background': 'transparent',
    }

    avail_logg_diff = ["{:.2f}".format((jan_avail_data['Availability'][a]/jan_timesheet_data[jan_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100),
    "{:.2f}".format((feb_avail_data['Availability'][a]/feb_timesheet_data[feb_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100),
    "{:.2f}".format((march_avail_data['Availability'][a]/march_timesheet_data[march_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100),
    "{:.2f}".format((april_avail_data['Availability'][a]/april_timesheet_data[april_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100),
    "{:.2f}".format((may_avail_data['Availability'][a]/may_timesheet_data[may_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100),
    "{:.2f}".format((june_avail_data['Availability'][a]/june_timesheet_data[june_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100),
    "{:.2f}".format((july_avail_data['Availability'][a]/july_timesheet_data[july_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100),
    "{:.2f}".format((august_avail_data['Availability'][a]/august_timesheet_data[august_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100),
    "{:.2f}".format((sep_avail_data['Availability'][a]/sep_timesheet_data[sep_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100),
    "{:.2f}".format((oct_avail_data['Availability'][a]/oct_timesheet_data[oct_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100),
    "{:.2f}".format((nov_avail_data['Availability'][a]/nov_timesheet_data[nov_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100),
    "{:.2f}".format((dec_avail_data['Availability'][a]/dec_timesheet_data[dec_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100)]
    
    months = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    in_time_logg_time = ["{:.2f}".format(float(jan_intime_loggedtime)), 
    "{:.2f}".format(float(feb_intime_loggedtime)), 
    "{:.2f}".format(float(march_intime_loggedtime)), 
    "{:.2f}".format(float(april_intime_loggedtime)), 
    "{:.2f}".format(float(may_intime_loggedtime)), 
    "{:.2f}".format(float(june_intime_loggedtime)), 
    "{:.2f}".format(float(july_intime_loggedtime)), 
    "{:.2f}".format(float(august_intime_loggedtime)), 
    "{:.2f}".format(float(sep_intime_loggedtime)), 
    "{:.2f}".format(float(oct_intime_loggedtime)), 
    "{:.2f}".format(float(nov_intime_loggedtime)), 
    "{:.2f}".format(float(dec_intime_loggedtime))] 




    layout = html.Div(style = {'background-color' : 'darkgray', 'width' : '100%'}, children=[
                dbc.Row([
                    # dbc.Col([dbc.Button(
                    #     "Button1", id="april-button", n_clicks=0, color="dark", style={"width": "100%"})]),
                    # dbc.Col([dbc.Button(
                    #     "Button2", id="may-button", n_clicks=0, color="dark", style={"width": "100%"})]),
                    # dbc.Col([dbc.Button(
                    #     "Button3", id="june-button", n_clicks=0, color="dark", style={"width": "100%"})]),
                ]),

    # dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    # dbc.Col([
    #     html.Div([
    # dbc.Button(children  = april_avail_data['User'][0], id="Abdul Jalil-button", n_clicks =0, style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #     dbc.Button(children  = april_avail_data['User'][1], id = "baghdasaryan-button", n_clicks = 0,style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #         dbc.Button(children  = april_avail_data['User'][2], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #             dbc.Button(children  = april_avail_data['User'][3], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #             dbc.Button(children  = april_avail_data['User'][4], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #             #    dbc.Button(children  = april_avail_data['User'][0], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    # html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    # ], )
    # ]
    # )
    # ]),
    # html.Br(),
    # html.Br(),
    dbc.Collapse([
    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    html.H1(children  = april_avail_data['User'][a], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),
    # html.Br(),
    # html.Br(),
    html.Div(style = {'margin-left': '45px', 'background-color': 'white',      'width' : '1250px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '20px', 'margin-left' : '30px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability (hours per month)', style={'margin-left' : '20px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ])
    ,
    dbc.Row([ dbc.Col([
        html.Div(style = {'margin-top' : '10px', 'margin-left' : '15px','width':'100%'}, children=[
            html.Span(children= jan_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '40px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= feb_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= march_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= april_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= may_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= june_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children=  july_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= august_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= sep_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= oct_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= nov_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= dec_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            
        ])
    ])]),
        dbc.Row([dbc.Col([
        html.Div(style = {'margin-top' : '10px', 'margin-left' : '15px'}, children=[
            html.Span(children= 'Jan', style={'display' : 'inline-block', 'margin-left' : '40px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Feb', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Mar', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Apr', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'May', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Jun', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Jul', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Aug', style={'display' : 'inline-block', 'margin-left' : '40px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Sep', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Oct', style={'display' : 'inline-block', 'margin-left' : '20px','margin-right' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Nov', style={'display' : 'inline-block', 'margin-left' : '20px','margin-right' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Dec', style={'display' : 'inline-block', 'margin-left' : '20px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            
        ])
    ]),


    ])
    ]
    ),

    html.Br(),
    html.Br(),


    dbc.Row(style= {'width' : '1200px', 'margin-left': '70px'},
    children = [
        dbc.Col(style = {'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'AVAILABILITY  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = avail_logg_diff, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
        dbc.Col(style = {'margin-left' : '20px', 'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'IN STATUS TIME  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = in_time_logg_time, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
    ]),
    html.Br(),


    dbc.Row(style= {'width' : '1200px', 'margin-left': '70px'},
    children = [
        dbc.Col(style = {'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = april_avail_data['User'][a], style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    html.P(children = 'Works with ?????? on our web-platform and is located in ????? with timezone ???', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    html.P(children = 'Other Descriptive Text', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'})
    ])
        ]),
        dbc.Col(style = {'margin-left' : '20px', 'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = '1 STORYPOINT  vs LOGGED TIME(weighted average, hours)', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = in_time_logg_time, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
    ]),
    html.Br(),


    dbc.Row(style= {'width' : '1200px', 'margin-left': '70px'},
    children = [
        dbc.Col(style = {'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'AVAILABILITY  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = avail_logg_diff, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
        dbc.Col(style = {'margin-left' : '20px', 'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'IN STATUS TIME  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = in_time_logg_time, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1200px', 'margin-left': '70px'},
    children = [
        dbc.Col(style = {'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'AVAILABILITY  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = avail_logg_diff, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
        dbc.Col(style = {'margin-left' : '20px', 'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'IN STATUS TIME  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = in_time_logg_time, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
    ]),

    html.Br(),
    html.Br(),


                html.Div(children=[
                        dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'January', id="jan-button", n_clicks =0, style={'border': '0px','background-color':'transparent','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = jan_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = jan_timesheet_data[jan_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(jan_tis_data['Abdul Jalil - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((jan_avail_data['Availability'][a]/jan_timesheet_data[jan_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),

    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(jan_intime_loggedtime)) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),


    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(jan_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(jan_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(jan_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(jan_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(jan_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="jan-collapse", is_open=False),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
        dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'February', id="feb-button", n_clicks =0, style={'border': '0px','background-color':'transparent','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = feb_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = feb_timesheet_data[feb_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(feb_tis_data['Abdul Jalil - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((feb_avail_data['Availability'][a]/feb_timesheet_data[feb_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),

    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  ="{:.2f}".format(float(feb_intime_loggedtime)) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),


    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(feb_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(feb_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(feb_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(feb_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(feb_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="feb-collapse", is_open=False),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'March', id="march-button", n_clicks =0, style={'border': '0px','background-color':'transparent','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = march_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = march_timesheet_data[march_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(march_tis_data['Abdul Jalil - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((march_avail_data['Availability'][a]/march_timesheet_data[march_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),

    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(march_intime_loggedtime)) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(march_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(march_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(march_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(march_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(march_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="march-collapse", is_open=False),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'April', id="april-button", n_clicks =0, style={'border': '0px','background-color':'transparent','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = april_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = april_timesheet_data[april_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(april_tis_data['Abdul Jalil - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((april_avail_data['Availability'][a]/april_timesheet_data[april_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),

    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(april_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(april_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(april_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(april_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(april_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(april_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="april-collapse", is_open=False),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'May', id = 'may-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = may_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = may_timesheet_data[may_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(may_tis_data['Abdul Jalil - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((may_avail_data['Availability'][a]/may_timesheet_data[may_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(may_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(may_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(may_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(may_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(may_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(may_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="may-collapse", is_open=False),
                        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'June', id = 'june-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = june_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = june_timesheet_data[june_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(june_tis_data['Abdul Jalil - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((june_avail_data['Availability'][a]/june_timesheet_data[june_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(june_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(june_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(june_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(june_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(june_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(june_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="june-collapse", is_open=False),
    html.Br(),
    html.Br(),

                        dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'July', id = 'july-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = july_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = july_timesheet_data[july_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(july_tis_data['Abdul Jalil - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((july_avail_data['Availability'][a]/july_timesheet_data[july_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(july_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(july_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(july_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(july_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(july_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(july_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="july-collapse", is_open=False),
                        html.Br(),
    html.Br(),

                        dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'August', id = 'august-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = august_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = august_timesheet_data[august_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(august_tis_data['Abdul Jalil - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((august_avail_data['Availability'][a]/august_timesheet_data[august_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(august_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(august_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(august_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(august_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(august_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(august_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="august-collapse", is_open=False),

                    
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'September', id = 'sep-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = sep_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = sep_timesheet_data[sep_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(sep_tis_data['Abdul Jalil - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((sep_avail_data['Availability'][a]/sep_timesheet_data[sep_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(sep_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(sep_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(sep_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(sep_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(sep_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(sep_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="sep-collapse", is_open=False),
                            
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'October', id = 'oct-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = oct_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = oct_timesheet_data[oct_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(oct_tis_data['Abdul Jalil - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((oct_avail_data['Availability'][a]/oct_timesheet_data[oct_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(oct_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(oct_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(oct_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(oct_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(oct_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(oct_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="oct-collapse", is_open=False),
           
                    
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'November', id = 'nov-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = nov_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = nov_timesheet_data[nov_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(nov_tis_data['Abdul Jalil - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((nov_avail_data['Availability'][a]/nov_timesheet_data[nov_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(nov_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(nov_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(nov_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(nov_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(nov_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(nov_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="nov-collapse", is_open=False),
                        
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'December', id = 'dec-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = dec_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = dec_timesheet_data[dec_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(dec_tis_data['Abdul Jalil - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((dec_avail_data['Availability'][a]/dec_timesheet_data[dec_timesheet_data['User'].str.contains('Abdul Jalil')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(dec_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(dec_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(dec_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(dec_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(dec_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(dec_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="dec-collapse", is_open=False),

                ]),
                dcc.Interval(
                    id='interval-component',
                    interval=1000, # in milliseconds
                    n_intervals=1,
                    max_intervals = 2, 
                    disabled = True
                )
                ], id = "mohsin-collapse", is_open = True),
                
    ])

    @jalil_app.callback(
            [
                
                Output("jan-collapse", "is_open"),
                Output("feb-collapse", "is_open"),
                Output("march-collapse", "is_open"),
            Output("april-collapse", "is_open"),
            Output("may-collapse", "is_open"),
            Output("june-collapse", "is_open"),
            Output("july-collapse", "is_open"),
            Output("august-collapse", "is_open"),
            Output("sep-collapse", "is_open"),
            Output("oct-collapse", "is_open"),
            Output("nov-collapse", "is_open"),
            Output("dec-collapse", "is_open"),
        
            ],
            [
            
                Input("jan-button", "n_clicks"),
            Input("feb-button", "n_clicks"),
            Input("march-button", "n_clicks"),
            Input("april-button", "n_clicks"),
            Input("may-button", "n_clicks"),
            Input("june-button", "n_clicks"),
            Input("july-button", "n_clicks"),
            Input("august-button", "n_clicks"),
            Input("sep-button", "n_clicks"),
            Input("oct-button", "n_clicks"),
            Input("nov-button", "n_clicks"),
            Input("dec-button", "n_clicks"),
        
            ],
        )
    def toggle_collapses(button_one, button_two, button_three, button_four, button_five, button_six, button_seven, button_eight,
    button_nine, button_ten, button_eleven, button_twelve):
            ctx = dash.callback_context

            if not ctx.triggered:
                raise PreventUpdate
            else:
                button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            
            
            if button_id == 'jan-button':
                print(april_sp1['StoryPoints'])
                return True, False, False, False, False, False, False, False, False, False, False, False
            elif button_id == 'feb-button':
                return False, True, False, False, False, False, False, False, False, False, False, False
            elif button_id == 'march-button':
                return False, False, True, False, False, False, False, False, False, False, False, False
            elif button_id == 'april-button':
                return False, False, False, True, False, False, False, False, False, False, False, False
            elif button_id == 'may-button':
                return False, False, False, False, True, False, False, False, False, False, False, False
            elif button_id == 'june-button':
                return False, False, False, False, False, True, False, False, False, False, False, False
            elif button_id == 'july-button':
                return False, False, False, False, False, False, True, False, False, False, False, False
            elif button_id == 'august-button':
                return False, False, False, False, False, False, False, True, False, False, False, False
            elif button_id == 'sep-button':
                return False, False, False, False, False, False, False, False, True, False, False, False
            elif button_id == 'oct-button':
                return False, False, False, False, False, False, False, False, False, True, False, False
            elif button_id == 'nov-button':
                return False, False, False, False, False, False, False, False, False, False, True, False
            elif button_id == 'dec-button':
                return False, False, False, False, False, False, False, False, False, False, False, True
            else:
                raise ValueError(f'Unexpected ID: {button_id}')
    return layout


def angela_layout(a):
    jan_sp1 = jan_done_data[jan_done_data['User'].str.contains('Angela Avetisyan')]
    jan_sp1 = jan_sp1[jan_sp1['StoryPoints'] == 1]

    jan_sp2 = jan_done_data[jan_done_data['User'].str.contains('Angela Avetisyan')]
    jan_sp2 = jan_sp2[jan_sp2['StoryPoints'] == 2]


    jan_sp3 = jan_done_data[jan_done_data['User'].str.contains('Angela Avetisyan')]
    jan_sp3 = jan_sp3[jan_sp3['StoryPoints'] == 3]

    jan_sp5 = jan_done_data[jan_done_data['User'].str.contains('Angela Avetisyan')]
    jan_sp5 = jan_sp5[jan_sp5['StoryPoints'] == 5]

    jan_sp8 = jan_done_data[jan_done_data['User'].str.contains('Angela Avetisyan')]
    jan_sp8 = jan_sp8[jan_sp8['StoryPoints'] == 8]

    feb_sp1 = feb_done_data[feb_done_data['User'].str.contains('Angela Avetisyan')]
    feb_sp1 = feb_sp1[feb_sp1['StoryPoints'] == 1]

    feb_sp2 = feb_done_data[feb_done_data['User'].str.contains('Angela Avetisyan')]
    feb_sp2 = feb_sp2[feb_sp2['StoryPoints'] == 2]


    feb_sp3 = feb_done_data[feb_done_data['User'].str.contains('Angela Avetisyan')]
    feb_sp3 = feb_sp3[feb_sp3['StoryPoints'] == 3]

    feb_sp5 = feb_done_data[feb_done_data['User'].str.contains('Angela Avetisyan')]
    feb_sp5 = feb_sp5[feb_sp5['StoryPoints'] == 5]

    feb_sp8 = feb_done_data[feb_done_data['User'].str.contains('Angela Avetisyan')]
    feb_sp8 = feb_sp8[feb_sp8['StoryPoints'] == 8]


    march_sp1 = march_done_data[march_done_data['User'].str.contains('Angela Avetisyan')]
    march_sp1 = march_sp1[march_sp1['StoryPoints'] == 1]

    march_sp2 = march_done_data[march_done_data['User'].str.contains('Angela Avetisyan')]
    march_sp2 = march_sp2[march_sp2['StoryPoints'] == 2]


    march_sp3 = march_done_data[march_done_data['User'].str.contains('Angela Avetisyan')]
    march_sp3 = march_sp3[march_sp3['StoryPoints'] == 3]

    march_sp5 = march_done_data[march_done_data['User'].str.contains('Angela Avetisyan')]
    march_sp5 = march_sp5[march_sp5['StoryPoints'] == 5]

    march_sp8 = march_done_data[march_done_data['User'].str.contains('Angela Avetisyan')]
    march_sp8 = march_sp8[march_sp8['StoryPoints'] == 8]


    april_sp1 = april_done_data[april_done_data['User'].str.contains('Angela Avetisyan')]
    april_sp1 = april_sp1[april_sp1['StoryPoints'] == 1]

    april_sp2 = april_done_data[april_done_data['User'].str.contains('Angela Avetisyan')]
    april_sp2 = april_sp2[april_sp2['StoryPoints'] == 2]


    april_sp3 = april_done_data[april_done_data['User'].str.contains('Angela Avetisyan')]
    april_sp3 = april_sp3[april_sp3['StoryPoints'] == 3]

    april_sp5 = april_done_data[april_done_data['User'].str.contains('Angela Avetisyan')]
    april_sp5 = april_sp5[april_sp5['StoryPoints'] == 5]

    april_sp8 = april_done_data[april_done_data['User'].str.contains('Angela Avetisyan')]
    april_sp8 = april_sp8[april_sp8['StoryPoints'] == 8]

    may_sp1 = may_done_data[may_done_data['User'].str.contains('Angela Avetisyan')]
    may_sp1 = may_sp1[may_sp1['StoryPoints'] == 1]

    may_sp2 = may_done_data[may_done_data['User'].str.contains('Angela Avetisyan')]
    may_sp2 = may_sp2[may_sp2['StoryPoints'] == 2]


    may_sp3 = may_done_data[may_done_data['User'].str.contains('Angela Avetisyan')]
    may_sp3 = may_sp3[may_sp3['StoryPoints'] == 3]

    may_sp5 = may_done_data[may_done_data['User'].str.contains('Angela Avetisyan')]
    may_sp5 = may_sp5[may_sp5['StoryPoints'] == 5]

    may_sp8 = may_done_data[may_done_data['User'].str.contains('Angela Avetisyan')]
    may_sp8 = may_sp8[may_sp8['StoryPoints'] == 8]
    
    june_sp1 = june_done_data[june_done_data['User'].str.contains('Angela Avetisyan')]
    june_sp1 = june_sp1[june_sp1['StoryPoints'] == 1]
    
    june_sp2 = june_done_data[june_done_data['User'].str.contains('Angela Avetisyan')]
    june_sp2 = june_sp2[june_sp2['StoryPoints'] == 2]


    june_sp3 = june_done_data[june_done_data['User'].str.contains('Angela Avetisyan')]
    june_sp3 = june_sp3[june_sp3['StoryPoints'] == 3]

    june_sp5 = june_done_data[june_done_data['User'].str.contains('Angela Avetisyan')]
    june_sp5 = june_sp5[june_sp5['StoryPoints'] == 5]

    june_sp8 = june_done_data[june_done_data['User'].str.contains('Angela Avetisyan')]
    june_sp8 = june_sp8[june_sp8['StoryPoints'] == 8]
    
    july_sp1 = july_done_data[july_done_data['User'].str.contains('Angela Avetisyan')]
    july_sp1 = july_sp1[july_sp1['StoryPoints'] == 1]
    
    july_sp2 = july_done_data[july_done_data['User'].str.contains('Angela Avetisyan')]
    july_sp2 = july_sp2[july_sp2['StoryPoints'] == 2]


    july_sp3 = july_done_data[july_done_data['User'].str.contains('Angela Avetisyan')]
    july_sp3 = july_sp3[july_sp3['StoryPoints'] == 3]

    july_sp5 = july_done_data[july_done_data['User'].str.contains('Angela Avetisyan')]
    july_sp5 = july_sp5[july_sp5['StoryPoints'] == 5]

    july_sp8 = july_done_data[july_done_data['User'].str.contains('Angela Avetisyan')]
    july_sp8 = july_sp8[july_sp8['StoryPoints'] == 8]

    august_sp1 = august_done_data[august_done_data['User'].str.contains('Angela Avetisyan')]
    august_sp1 = august_sp1[august_sp1['StoryPoints'] == 1]
    
    august_sp2 = august_done_data[august_done_data['User'].str.contains('Angela Avetisyan')]
    august_sp2 = august_sp2[august_sp2['StoryPoints'] == 2]


    august_sp3 = august_done_data[august_done_data['User'].str.contains('Angela Avetisyan')]
    august_sp3 = august_sp3[august_sp3['StoryPoints'] == 3]

    august_sp5 = august_done_data[august_done_data['User'].str.contains('Angela Avetisyan')]
    august_sp5 = august_sp5[august_sp5['StoryPoints'] == 5]

    august_sp8 = august_done_data[august_done_data['User'].str.contains('Angela Avetisyan')]
    august_sp8 = august_sp8[august_sp8['StoryPoints'] == 8]

    sep_sp1 = sep_done_data[sep_done_data['User'].str.contains('Angela Avetisyan')]
    sep_sp1 = sep_sp1[sep_sp1['StoryPoints'] == 1]
    
    sep_sp2 = sep_done_data[sep_done_data['User'].str.contains('Angela Avetisyan')]
    sep_sp2 = sep_sp2[sep_sp2['StoryPoints'] == 2]


    sep_sp3 = sep_done_data[sep_done_data['User'].str.contains('Angela Avetisyan')]
    sep_sp3 = sep_sp3[sep_sp3['StoryPoints'] == 3]

    sep_sp5 = sep_done_data[sep_done_data['User'].str.contains('Angela Avetisyan')]
    sep_sp5 = sep_sp5[sep_sp5['StoryPoints'] == 5]

    sep_sp8 = sep_done_data[sep_done_data['User'].str.contains('Angela Avetisyan')]
    sep_sp8 = sep_sp8[sep_sp8['StoryPoints'] == 8]


    oct_sp1 = oct_done_data[oct_done_data['User'].str.contains('Angela Avetisyan')]
    oct_sp1 = oct_sp1[oct_sp1['StoryPoints'] == 1]
    
    oct_sp2 = oct_done_data[oct_done_data['User'].str.contains('Angela Avetisyan')]
    oct_sp2 = oct_sp2[oct_sp2['StoryPoints'] == 2]


    oct_sp3 = oct_done_data[oct_done_data['User'].str.contains('Angela Avetisyan')]
    oct_sp3 = oct_sp3[oct_sp3['StoryPoints'] == 3]

    oct_sp5 = oct_done_data[oct_done_data['User'].str.contains('Angela Avetisyan')]
    oct_sp5 = oct_sp5[oct_sp5['StoryPoints'] == 5]

    oct_sp8 = oct_done_data[oct_done_data['User'].str.contains('Angela Avetisyan')]
    oct_sp8 = oct_sp8[oct_sp8['StoryPoints'] == 8]

    nov_sp1 = nov_done_data[nov_done_data['User'].str.contains('Angela Avetisyan')]
    nov_sp1 = nov_sp1[nov_sp1['StoryPoints'] == 1]
    
    nov_sp2 = nov_done_data[nov_done_data['User'].str.contains('Angela Avetisyan')]
    nov_sp2 = nov_sp2[nov_sp2['StoryPoints'] == 2]


    nov_sp3 = nov_done_data[nov_done_data['User'].str.contains('Angela Avetisyan')]
    nov_sp3 = nov_sp3[nov_sp3['StoryPoints'] == 3]

    nov_sp5 = nov_done_data[nov_done_data['User'].str.contains('Angela Avetisyan')]
    nov_sp5 = nov_sp5[nov_sp5['StoryPoints'] == 5]

    nov_sp8 = nov_done_data[nov_done_data['User'].str.contains('Angela Avetisyan')]
    nov_sp8 = nov_sp8[nov_sp8['StoryPoints'] == 8]

    dec_sp1 = dec_done_data[dec_done_data['User'].str.contains('Angela Avetisyan')]
    dec_sp1 = dec_sp1[dec_sp1['StoryPoints'] == 1]
    
    dec_sp2 = dec_done_data[dec_done_data['User'].str.contains('Angela Avetisyan')]
    dec_sp2 = dec_sp2[dec_sp2['StoryPoints'] == 2]


    dec_sp3 = dec_done_data[dec_done_data['User'].str.contains('Angela Avetisyan')]
    dec_sp3 = dec_sp3[dec_sp3['StoryPoints'] == 3]

    dec_sp5 = dec_done_data[dec_done_data['User'].str.contains('Angela Avetisyan')]
    dec_sp5 = dec_sp5[dec_sp5['StoryPoints'] == 5]

    dec_sp8 = dec_done_data[dec_done_data['User'].str.contains('Angela Avetisyan')]
    dec_sp8 = dec_sp8[dec_sp8['StoryPoints'] == 8]
    
    jan_intime_loggedtime = (jan_tis_data['Angela Avetisyan - In Progress']/jan_timesheet_data[jan_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100

    feb_intime_loggedtime = (feb_tis_data['Angela Avetisyan - In Progress']/feb_timesheet_data[feb_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100
   
    march_intime_loggedtime = (march_tis_data['Angela Avetisyan - In Progress']/march_timesheet_data[march_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100

    april_intime_loggedtime = (april_tis_data['Angela Avetisyan - In Progress']/april_timesheet_data[april_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100

    may_intime_loggedtime = (may_tis_data['Angela Avetisyan - In Progress']/may_timesheet_data[may_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100

    june_intime_loggedtime = (june_tis_data['Angela Avetisyan - In Progress']/june_timesheet_data[june_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100

    july_intime_loggedtime = (july_tis_data['Angela Avetisyan - In Progress']/july_timesheet_data[july_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100
    
    august_intime_loggedtime = (august_tis_data['Angela Avetisyan - In Progress']/august_timesheet_data[august_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100

    sep_intime_loggedtime = (sep_tis_data['Angela Avetisyan - In Progress']/sep_timesheet_data[sep_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100

    oct_intime_loggedtime = (oct_tis_data['Angela Avetisyan - In Progress']/oct_timesheet_data[oct_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100

    nov_intime_loggedtime = (nov_tis_data['Angela Avetisyan - In Progress']/nov_timesheet_data[nov_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100
    
    dec_intime_loggedtime = (dec_tis_data['Angela Avetisyan - In Progress']/dec_timesheet_data[dec_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100

    graph_colors = {
        'background': 'transparent',
    }

    avail_logg_diff = ["{:.2f}".format((jan_avail_data['Availability'][a]/jan_timesheet_data[jan_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((feb_avail_data['Availability'][a]/feb_timesheet_data[feb_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((march_avail_data['Availability'][a]/march_timesheet_data[march_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((april_avail_data['Availability'][a]/april_timesheet_data[april_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((may_avail_data['Availability'][a]/may_timesheet_data[may_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((june_avail_data['Availability'][a]/june_timesheet_data[june_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((july_avail_data['Availability'][a]/july_timesheet_data[july_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((august_avail_data['Availability'][a]/august_timesheet_data[august_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((sep_avail_data['Availability'][a]/sep_timesheet_data[sep_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((oct_avail_data['Availability'][a]/oct_timesheet_data[oct_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((nov_avail_data['Availability'][a]/nov_timesheet_data[nov_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((dec_avail_data['Availability'][a]/dec_timesheet_data[dec_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100)]
    
    months = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    in_time_logg_time = ["{:.2f}".format(float(jan_intime_loggedtime)), 
    "{:.2f}".format(float(feb_intime_loggedtime)), 
    "{:.2f}".format(float(march_intime_loggedtime)), 
    "{:.2f}".format(float(april_intime_loggedtime)), 
    "{:.2f}".format(float(may_intime_loggedtime)), 
    "{:.2f}".format(float(june_intime_loggedtime)), 
    "{:.2f}".format(float(july_intime_loggedtime)), 
    "{:.2f}".format(float(august_intime_loggedtime)), 
    "{:.2f}".format(float(sep_intime_loggedtime)), 
    "{:.2f}".format(float(oct_intime_loggedtime)), 
    "{:.2f}".format(float(nov_intime_loggedtime)), 
    "{:.2f}".format(float(dec_intime_loggedtime))] 



    layout = html.Div(style = {'background-color' : 'darkgray', 'width' : '100%'}, children=[
                dbc.Row([
                    # dbc.Col([dbc.Button(
                    #     "Button1", id="april-button", n_clicks=0, color="dark", style={"width": "100%"})]),
                    # dbc.Col([dbc.Button(
                    #     "Button2", id="may-button", n_clicks=0, color="dark", style={"width": "100%"})]),
                    # dbc.Col([dbc.Button(
                    #     "Button3", id="june-button", n_clicks=0, color="dark", style={"width": "100%"})]),
                ]),

    # dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    # dbc.Col([
    #     html.Div([
    # dbc.Button(children  = april_avail_data['User'][0], id="Angela Avetisyan-button", n_clicks =0, style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #     dbc.Button(children  = april_avail_data['User'][1], id = "baghdasaryan-button", n_clicks = 0,style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #         dbc.Button(children  = april_avail_data['User'][2], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #             dbc.Button(children  = april_avail_data['User'][3], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #             dbc.Button(children  = april_avail_data['User'][4], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #             #    dbc.Button(children  = april_avail_data['User'][0], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    # html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    # ], )
    # ]
    # )
    # ]),
    # html.Br(),
    # html.Br(),
    dbc.Collapse([
    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    html.H1(children  = april_avail_data['User'][a], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),
    # html.Br(),
    # html.Br(),
    html.Div(style = {'margin-left': '45px', 'background-color': 'white',      'width' : '1250px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '20px', 'margin-left' : '30px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability (hours per month)', style={'margin-left' : '20px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ])
    ,
    dbc.Row([ dbc.Col([
        html.Div(style = {'margin-top' : '10px', 'margin-left' : '15px','width':'100%'}, children=[
            html.Span(children= jan_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '40px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= feb_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= march_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= april_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= may_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= june_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children=  july_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= august_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= sep_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= oct_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= nov_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= dec_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            
        ])
    ])]),
        dbc.Row([dbc.Col([
        html.Div(style = {'margin-top' : '10px', 'margin-left' : '15px'}, children=[
            html.Span(children= 'Jan', style={'display' : 'inline-block', 'margin-left' : '40px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Feb', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Mar', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Apr', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'May', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Jun', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Jul', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Aug', style={'display' : 'inline-block', 'margin-left' : '40px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Sep', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Oct', style={'display' : 'inline-block', 'margin-left' : '20px','margin-right' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Nov', style={'display' : 'inline-block', 'margin-left' : '20px','margin-right' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Dec', style={'display' : 'inline-block', 'margin-left' : '20px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            
        ])
    ]),


    ])
    ]
    ),

    html.Br(),
    html.Br(),



    dbc.Row(style= {'width' : '1200px', 'margin-left': '70px'},
    children = [
        dbc.Col(style = {'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'AVAILABILITY  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = avail_logg_diff, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
        dbc.Col(style = {'margin-left' : '20px', 'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'IN STATUS TIME  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = in_time_logg_time, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
    ]),
    html.Br(),


    dbc.Row(style= {'width' : '1200px', 'margin-left': '70px'},
    children = [
        dbc.Col(style = {'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = april_avail_data['User'][a], style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    html.P(children = 'Works with ?????? on our web-platform and is located in ????? with timezone ???', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    html.P(children = 'Other Descriptive Text', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'})
    ])
        ]),
        dbc.Col(style = {'margin-left' : '20px', 'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = '1 STORYPOINT  vs LOGGED TIME(weighted average, hours)', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = in_time_logg_time, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
    ]),
    html.Br(),


    dbc.Row(style= {'width' : '1200px', 'margin-left': '70px'},
    children = [
        dbc.Col(style = {'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'AVAILABILITY  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = avail_logg_diff, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
        dbc.Col(style = {'margin-left' : '20px', 'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'IN STATUS TIME  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = in_time_logg_time, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1200px', 'margin-left': '70px'},
    children = [
        dbc.Col(style = {'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'AVAILABILITY  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = avail_logg_diff, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
        dbc.Col(style = {'margin-left' : '20px', 'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'IN STATUS TIME  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = in_time_logg_time, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
    ]),

    html.Br(),
    html.Br(),


                html.Div(children=[
                        dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'January', id="jan-button", n_clicks =0, style={'border': '0px','background-color':'transparent','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = jan_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = jan_timesheet_data[jan_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(jan_tis_data['Angela Avetisyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((jan_avail_data['Availability'][a]/jan_timesheet_data[jan_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),

    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(jan_intime_loggedtime)) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),


    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(jan_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(jan_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(jan_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(jan_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(jan_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="jan-collapse", is_open=False),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
        dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'February', id="feb-button", n_clicks =0, style={'border': '0px','background-color':'transparent','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = feb_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = feb_timesheet_data[feb_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(feb_tis_data['Angela Avetisyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((feb_avail_data['Availability'][a]/feb_timesheet_data[feb_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),

    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  ="{:.2f}".format(float(feb_intime_loggedtime)) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),


    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(feb_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(feb_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(feb_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(feb_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(feb_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="feb-collapse", is_open=False),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'March', id="march-button", n_clicks =0, style={'border': '0px','background-color':'transparent','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = march_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = march_timesheet_data[march_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(march_tis_data['Angela Avetisyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((march_avail_data['Availability'][a]/march_timesheet_data[march_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),

    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(march_intime_loggedtime)) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(march_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(march_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(march_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(march_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(march_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="march-collapse", is_open=False),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'April', id="april-button", n_clicks =0, style={'border': '0px','background-color':'transparent','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = april_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = april_timesheet_data[april_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(april_tis_data['Angela Avetisyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((april_avail_data['Availability'][a]/april_timesheet_data[april_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),

    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(april_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(april_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(april_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(april_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(april_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(april_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="april-collapse", is_open=False),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'May', id = 'may-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = may_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = may_timesheet_data[may_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(may_tis_data['Angela Avetisyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((may_avail_data['Availability'][a]/may_timesheet_data[may_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(may_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(may_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(may_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(may_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(may_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(may_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="may-collapse", is_open=False),
                        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'June', id = 'june-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = june_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = june_timesheet_data[june_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(june_tis_data['Angela Avetisyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((june_avail_data['Availability'][a]/june_timesheet_data[june_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(june_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(june_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(june_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(june_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(june_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(june_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="june-collapse", is_open=False),
    html.Br(),
    html.Br(),

                        dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'July', id = 'july-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = july_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = july_timesheet_data[july_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(july_tis_data['Angela Avetisyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((july_avail_data['Availability'][a]/july_timesheet_data[july_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(july_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(july_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(july_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(july_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(july_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(july_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="july-collapse", is_open=False),
                        html.Br(),
    html.Br(),

                        dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'August', id = 'august-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = august_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = august_timesheet_data[august_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(august_tis_data['Angela Avetisyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((august_avail_data['Availability'][a]/august_timesheet_data[august_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(august_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(august_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(august_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(august_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(august_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(august_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="august-collapse", is_open=False),

                    
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'September', id = 'sep-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = sep_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = sep_timesheet_data[sep_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(sep_tis_data['Angela Avetisyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((sep_avail_data['Availability'][a]/sep_timesheet_data[sep_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(sep_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(sep_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(sep_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(sep_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(sep_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(sep_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="sep-collapse", is_open=False),
                            
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'October', id = 'oct-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = oct_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = oct_timesheet_data[oct_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(oct_tis_data['Angela Avetisyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((oct_avail_data['Availability'][a]/oct_timesheet_data[oct_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(oct_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(oct_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(oct_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(oct_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(oct_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(oct_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="oct-collapse", is_open=False),
           
                    
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'November', id = 'nov-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = nov_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = nov_timesheet_data[nov_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(nov_tis_data['Angela Avetisyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((nov_avail_data['Availability'][a]/nov_timesheet_data[nov_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(nov_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(nov_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(nov_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(nov_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(nov_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(nov_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="nov-collapse", is_open=False),
                        
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'December', id = 'dec-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = dec_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = dec_timesheet_data[dec_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(dec_tis_data['Angela Avetisyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((dec_avail_data['Availability'][a]/dec_timesheet_data[dec_timesheet_data['User'].str.contains('Angela Avetisyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(dec_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(dec_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(dec_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(dec_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(dec_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(dec_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="dec-collapse", is_open=False),

                ]),
                dcc.Interval(
                    id='interval-component',
                    interval=1000, # in milliseconds
                    n_intervals=1,
                    max_intervals = 2, 
                    disabled = True
                )
                ], id = "mohsin-collapse", is_open = True),
                
    ])

    @angela_app.callback(
            [
                
                Output("jan-collapse", "is_open"),
                Output("feb-collapse", "is_open"),
                Output("march-collapse", "is_open"),
            Output("april-collapse", "is_open"),
            Output("may-collapse", "is_open"),
            Output("june-collapse", "is_open"),
            Output("july-collapse", "is_open"),
            Output("august-collapse", "is_open"),
            Output("sep-collapse", "is_open"),
            Output("oct-collapse", "is_open"),
            Output("nov-collapse", "is_open"),
            Output("dec-collapse", "is_open"),
        
            ],
            [
            
                Input("jan-button", "n_clicks"),
            Input("feb-button", "n_clicks"),
            Input("march-button", "n_clicks"),
            Input("april-button", "n_clicks"),
            Input("may-button", "n_clicks"),
            Input("june-button", "n_clicks"),
            Input("july-button", "n_clicks"),
            Input("august-button", "n_clicks"),
            Input("sep-button", "n_clicks"),
            Input("oct-button", "n_clicks"),
            Input("nov-button", "n_clicks"),
            Input("dec-button", "n_clicks"),
        
            ],
        )
    def toggle_collapses(button_one, button_two, button_three, button_four, button_five, button_six, button_seven, button_eight,
    button_nine, button_ten, button_eleven, button_twelve):
            ctx = dash.callback_context

            if not ctx.triggered:
                raise PreventUpdate
            else:
                button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            
            
            if button_id == 'jan-button':
                print(april_sp1['StoryPoints'])
                return True, False, False, False, False, False, False, False, False, False, False, False
            elif button_id == 'feb-button':
                return False, True, False, False, False, False, False, False, False, False, False, False
            elif button_id == 'march-button':
                return False, False, True, False, False, False, False, False, False, False, False, False
            elif button_id == 'april-button':
                return False, False, False, True, False, False, False, False, False, False, False, False
            elif button_id == 'may-button':
                return False, False, False, False, True, False, False, False, False, False, False, False
            elif button_id == 'june-button':
                return False, False, False, False, False, True, False, False, False, False, False, False
            elif button_id == 'july-button':
                return False, False, False, False, False, False, True, False, False, False, False, False
            elif button_id == 'august-button':
                return False, False, False, False, False, False, False, True, False, False, False, False
            elif button_id == 'sep-button':
                return False, False, False, False, False, False, False, False, True, False, False, False
            elif button_id == 'oct-button':
                return False, False, False, False, False, False, False, False, False, True, False, False
            elif button_id == 'nov-button':
                return False, False, False, False, False, False, False, False, False, False, True, False
            elif button_id == 'dec-button':
                return False, False, False, False, False, False, False, False, False, False, False, True
            else:
                raise ValueError(f'Unexpected ID: {button_id}')
    return layout


def narek_layout(a):
    jan_sp1 = jan_done_data[jan_done_data['User'].str.contains('Narek Poghosyan')]
    jan_sp1 = jan_sp1[jan_sp1['StoryPoints'] == 1]

    jan_sp2 = jan_done_data[jan_done_data['User'].str.contains('Narek Poghosyan')]
    jan_sp2 = jan_sp2[jan_sp2['StoryPoints'] == 2]


    jan_sp3 = jan_done_data[jan_done_data['User'].str.contains('Narek Poghosyan')]
    jan_sp3 = jan_sp3[jan_sp3['StoryPoints'] == 3]

    jan_sp5 = jan_done_data[jan_done_data['User'].str.contains('Narek Poghosyan')]
    jan_sp5 = jan_sp5[jan_sp5['StoryPoints'] == 5]

    jan_sp8 = jan_done_data[jan_done_data['User'].str.contains('Narek Poghosyan')]
    jan_sp8 = jan_sp8[jan_sp8['StoryPoints'] == 8]

    feb_sp1 = feb_done_data[feb_done_data['User'].str.contains('Narek Poghosyan')]
    feb_sp1 = feb_sp1[feb_sp1['StoryPoints'] == 1]

    feb_sp2 = feb_done_data[feb_done_data['User'].str.contains('Narek Poghosyan')]
    feb_sp2 = feb_sp2[feb_sp2['StoryPoints'] == 2]


    feb_sp3 = feb_done_data[feb_done_data['User'].str.contains('Narek Poghosyan')]
    feb_sp3 = feb_sp3[feb_sp3['StoryPoints'] == 3]

    feb_sp5 = feb_done_data[feb_done_data['User'].str.contains('Narek Poghosyan')]
    feb_sp5 = feb_sp5[feb_sp5['StoryPoints'] == 5]

    feb_sp8 = feb_done_data[feb_done_data['User'].str.contains('Narek Poghosyan')]
    feb_sp8 = feb_sp8[feb_sp8['StoryPoints'] == 8]


    march_sp1 = march_done_data[march_done_data['User'].str.contains('Narek Poghosyan')]
    march_sp1 = march_sp1[march_sp1['StoryPoints'] == 1]

    march_sp2 = march_done_data[march_done_data['User'].str.contains('Narek Poghosyan')]
    march_sp2 = march_sp2[march_sp2['StoryPoints'] == 2]


    march_sp3 = march_done_data[march_done_data['User'].str.contains('Narek Poghosyan')]
    march_sp3 = march_sp3[march_sp3['StoryPoints'] == 3]

    march_sp5 = march_done_data[march_done_data['User'].str.contains('Narek Poghosyan')]
    march_sp5 = march_sp5[march_sp5['StoryPoints'] == 5]

    march_sp8 = march_done_data[march_done_data['User'].str.contains('Narek Poghosyan')]
    march_sp8 = march_sp8[march_sp8['StoryPoints'] == 8]


    april_sp1 = april_done_data[april_done_data['User'].str.contains('Narek Poghosyan')]
    april_sp1 = april_sp1[april_sp1['StoryPoints'] == 1]

    april_sp2 = april_done_data[april_done_data['User'].str.contains('Narek Poghosyan')]
    april_sp2 = april_sp2[april_sp2['StoryPoints'] == 2]


    april_sp3 = april_done_data[april_done_data['User'].str.contains('Narek Poghosyan')]
    april_sp3 = april_sp3[april_sp3['StoryPoints'] == 3]

    april_sp5 = april_done_data[april_done_data['User'].str.contains('Narek Poghosyan')]
    april_sp5 = april_sp5[april_sp5['StoryPoints'] == 5]

    april_sp8 = april_done_data[april_done_data['User'].str.contains('Narek Poghosyan')]
    april_sp8 = april_sp8[april_sp8['StoryPoints'] == 8]

    may_sp1 = may_done_data[may_done_data['User'].str.contains('Narek Poghosyan')]
    may_sp1 = may_sp1[may_sp1['StoryPoints'] == 1]

    may_sp2 = may_done_data[may_done_data['User'].str.contains('Narek Poghosyan')]
    may_sp2 = may_sp2[may_sp2['StoryPoints'] == 2]


    may_sp3 = may_done_data[may_done_data['User'].str.contains('Narek Poghosyan')]
    may_sp3 = may_sp3[may_sp3['StoryPoints'] == 3]

    may_sp5 = may_done_data[may_done_data['User'].str.contains('Narek Poghosyan')]
    may_sp5 = may_sp5[may_sp5['StoryPoints'] == 5]

    may_sp8 = may_done_data[may_done_data['User'].str.contains('Narek Poghosyan')]
    may_sp8 = may_sp8[may_sp8['StoryPoints'] == 8]
    
    june_sp1 = june_done_data[june_done_data['User'].str.contains('Narek Poghosyan')]
    june_sp1 = june_sp1[june_sp1['StoryPoints'] == 1]
    
    june_sp2 = june_done_data[june_done_data['User'].str.contains('Narek Poghosyan')]
    june_sp2 = june_sp2[june_sp2['StoryPoints'] == 2]


    june_sp3 = june_done_data[june_done_data['User'].str.contains('Narek Poghosyan')]
    june_sp3 = june_sp3[june_sp3['StoryPoints'] == 3]

    june_sp5 = june_done_data[june_done_data['User'].str.contains('Narek Poghosyan')]
    june_sp5 = june_sp5[june_sp5['StoryPoints'] == 5]

    june_sp8 = june_done_data[june_done_data['User'].str.contains('Narek Poghosyan')]
    june_sp8 = june_sp8[june_sp8['StoryPoints'] == 8]
    
    july_sp1 = july_done_data[july_done_data['User'].str.contains('Narek Poghosyan')]
    july_sp1 = july_sp1[july_sp1['StoryPoints'] == 1]
    
    july_sp2 = july_done_data[july_done_data['User'].str.contains('Narek Poghosyan')]
    july_sp2 = july_sp2[july_sp2['StoryPoints'] == 2]


    july_sp3 = july_done_data[july_done_data['User'].str.contains('Narek Poghosyan')]
    july_sp3 = july_sp3[july_sp3['StoryPoints'] == 3]

    july_sp5 = july_done_data[july_done_data['User'].str.contains('Narek Poghosyan')]
    july_sp5 = july_sp5[july_sp5['StoryPoints'] == 5]

    july_sp8 = july_done_data[july_done_data['User'].str.contains('Narek Poghosyan')]
    july_sp8 = july_sp8[july_sp8['StoryPoints'] == 8]

    august_sp1 = august_done_data[august_done_data['User'].str.contains('Narek Poghosyan')]
    august_sp1 = august_sp1[august_sp1['StoryPoints'] == 1]
    
    august_sp2 = august_done_data[august_done_data['User'].str.contains('Narek Poghosyan')]
    august_sp2 = august_sp2[august_sp2['StoryPoints'] == 2]


    august_sp3 = august_done_data[august_done_data['User'].str.contains('Narek Poghosyan')]
    august_sp3 = august_sp3[august_sp3['StoryPoints'] == 3]

    august_sp5 = august_done_data[august_done_data['User'].str.contains('Narek Poghosyan')]
    august_sp5 = august_sp5[august_sp5['StoryPoints'] == 5]

    august_sp8 = august_done_data[august_done_data['User'].str.contains('Narek Poghosyan')]
    august_sp8 = august_sp8[august_sp8['StoryPoints'] == 8]

    sep_sp1 = sep_done_data[sep_done_data['User'].str.contains('Narek Poghosyan')]
    sep_sp1 = sep_sp1[sep_sp1['StoryPoints'] == 1]
    
    sep_sp2 = sep_done_data[sep_done_data['User'].str.contains('Narek Poghosyan')]
    sep_sp2 = sep_sp2[sep_sp2['StoryPoints'] == 2]


    sep_sp3 = sep_done_data[sep_done_data['User'].str.contains('Narek Poghosyan')]
    sep_sp3 = sep_sp3[sep_sp3['StoryPoints'] == 3]

    sep_sp5 = sep_done_data[sep_done_data['User'].str.contains('Narek Poghosyan')]
    sep_sp5 = sep_sp5[sep_sp5['StoryPoints'] == 5]

    sep_sp8 = sep_done_data[sep_done_data['User'].str.contains('Narek Poghosyan')]
    sep_sp8 = sep_sp8[sep_sp8['StoryPoints'] == 8]


    oct_sp1 = oct_done_data[oct_done_data['User'].str.contains('Narek Poghosyan')]
    oct_sp1 = oct_sp1[oct_sp1['StoryPoints'] == 1]
    
    oct_sp2 = oct_done_data[oct_done_data['User'].str.contains('Narek Poghosyan')]
    oct_sp2 = oct_sp2[oct_sp2['StoryPoints'] == 2]


    oct_sp3 = oct_done_data[oct_done_data['User'].str.contains('Narek Poghosyan')]
    oct_sp3 = oct_sp3[oct_sp3['StoryPoints'] == 3]

    oct_sp5 = oct_done_data[oct_done_data['User'].str.contains('Narek Poghosyan')]
    oct_sp5 = oct_sp5[oct_sp5['StoryPoints'] == 5]

    oct_sp8 = oct_done_data[oct_done_data['User'].str.contains('Narek Poghosyan')]
    oct_sp8 = oct_sp8[oct_sp8['StoryPoints'] == 8]

    nov_sp1 = nov_done_data[nov_done_data['User'].str.contains('Narek Poghosyan')]
    nov_sp1 = nov_sp1[nov_sp1['StoryPoints'] == 1]
    
    nov_sp2 = nov_done_data[nov_done_data['User'].str.contains('Narek Poghosyan')]
    nov_sp2 = nov_sp2[nov_sp2['StoryPoints'] == 2]


    nov_sp3 = nov_done_data[nov_done_data['User'].str.contains('Narek Poghosyan')]
    nov_sp3 = nov_sp3[nov_sp3['StoryPoints'] == 3]

    nov_sp5 = nov_done_data[nov_done_data['User'].str.contains('Narek Poghosyan')]
    nov_sp5 = nov_sp5[nov_sp5['StoryPoints'] == 5]

    nov_sp8 = nov_done_data[nov_done_data['User'].str.contains('Narek Poghosyan')]
    nov_sp8 = nov_sp8[nov_sp8['StoryPoints'] == 8]

    dec_sp1 = dec_done_data[dec_done_data['User'].str.contains('Narek Poghosyan')]
    dec_sp1 = dec_sp1[dec_sp1['StoryPoints'] == 1]
    
    dec_sp2 = dec_done_data[dec_done_data['User'].str.contains('Narek Poghosyan')]
    dec_sp2 = dec_sp2[dec_sp2['StoryPoints'] == 2]


    dec_sp3 = dec_done_data[dec_done_data['User'].str.contains('Narek Poghosyan')]
    dec_sp3 = dec_sp3[dec_sp3['StoryPoints'] == 3]

    dec_sp5 = dec_done_data[dec_done_data['User'].str.contains('Narek Poghosyan')]
    dec_sp5 = dec_sp5[dec_sp5['StoryPoints'] == 5]

    dec_sp8 = dec_done_data[dec_done_data['User'].str.contains('Narek Poghosyan')]
    dec_sp8 = dec_sp8[dec_sp8['StoryPoints'] == 8]
    
    jan_intime_loggedtime = (jan_tis_data['Narek Poghosyan - In Progress']/jan_timesheet_data[jan_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100

    feb_intime_loggedtime = (feb_tis_data['Narek Poghosyan - In Progress']/feb_timesheet_data[feb_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100
   
    march_intime_loggedtime = (march_tis_data['Narek Poghosyan - In Progress']/march_timesheet_data[march_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100

    april_intime_loggedtime = (april_tis_data['Narek Poghosyan - In Progress']/april_timesheet_data[april_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100

    may_intime_loggedtime = (may_tis_data['Narek Poghosyan - In Progress']/may_timesheet_data[may_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100

    june_intime_loggedtime = (june_tis_data['Narek Poghosyan - In Progress']/june_timesheet_data[june_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100

    july_intime_loggedtime = (july_tis_data['Narek Poghosyan - In Progress']/july_timesheet_data[july_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100
    
    august_intime_loggedtime = (august_tis_data['Narek Poghosyan - In Progress']/august_timesheet_data[august_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100

    sep_intime_loggedtime = (sep_tis_data['Narek Poghosyan - In Progress']/sep_timesheet_data[sep_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100

    oct_intime_loggedtime = (oct_tis_data['Narek Poghosyan - In Progress']/oct_timesheet_data[oct_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100

    nov_intime_loggedtime = (nov_tis_data['Narek Poghosyan - In Progress']/nov_timesheet_data[nov_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100
    
    dec_intime_loggedtime = (dec_tis_data['Narek Poghosyan - In Progress']/dec_timesheet_data[dec_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100

    graph_colors = {
        'background': 'transparent',
    }

    avail_logg_diff = ["{:.2f}".format((jan_avail_data['Availability'][a]/jan_timesheet_data[jan_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((feb_avail_data['Availability'][a]/feb_timesheet_data[feb_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((march_avail_data['Availability'][a]/march_timesheet_data[march_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((april_avail_data['Availability'][a]/april_timesheet_data[april_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((may_avail_data['Availability'][a]/may_timesheet_data[may_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((june_avail_data['Availability'][a]/june_timesheet_data[june_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((july_avail_data['Availability'][a]/july_timesheet_data[july_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((august_avail_data['Availability'][a]/august_timesheet_data[august_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((sep_avail_data['Availability'][a]/sep_timesheet_data[sep_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((oct_avail_data['Availability'][a]/oct_timesheet_data[oct_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((nov_avail_data['Availability'][a]/nov_timesheet_data[nov_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100),
    "{:.2f}".format((dec_avail_data['Availability'][a]/dec_timesheet_data[dec_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100)]
    
    months = ['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    in_time_logg_time = ["{:.2f}".format(float(jan_intime_loggedtime)), 
    "{:.2f}".format(float(feb_intime_loggedtime)), 
    "{:.2f}".format(float(march_intime_loggedtime)), 
    "{:.2f}".format(float(april_intime_loggedtime)), 
    "{:.2f}".format(float(may_intime_loggedtime)), 
    "{:.2f}".format(float(june_intime_loggedtime)), 
    "{:.2f}".format(float(july_intime_loggedtime)), 
    "{:.2f}".format(float(august_intime_loggedtime)), 
    "{:.2f}".format(float(sep_intime_loggedtime)), 
    "{:.2f}".format(float(oct_intime_loggedtime)), 
    "{:.2f}".format(float(nov_intime_loggedtime)), 
    "{:.2f}".format(float(dec_intime_loggedtime))] 

    # print(in_time_logg_time)

    layout = html.Div(style = {'background-color' : 'darkgray', 'width' : '100%'}, children=[
                dbc.Row([
                    # dbc.Col([dbc.Button(
                    #     "Button1", id="april-button", n_clicks=0, color="dark", style={"width": "100%"})]),
                    # dbc.Col([dbc.Button(
                    #     "Button2", id="may-button", n_clicks=0, color="dark", style={"width": "100%"})]),
                    # dbc.Col([dbc.Button(
                    #     "Button3", id="june-button", n_clicks=0, color="dark", style={"width": "100%"})]),
                ]),

    # dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    # dbc.Col([
    #     html.Div([
    # dbc.Button(children  = april_avail_data['User'][0], id="Narek Poghosyan-button", n_clicks =0, style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #     dbc.Button(children  = april_avail_data['User'][1], id = "baghdasaryan-button", n_clicks = 0,style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #         dbc.Button(children  = april_avail_data['User'][2], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #             dbc.Button(children  = april_avail_data['User'][3], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #             dbc.Button(children  = april_avail_data['User'][4], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    #             #    dbc.Button(children  = april_avail_data['User'][0], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '120%'}),
    # html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    # ], )
    # ]
    # )
    # ]),
    # html.Br(),
    # html.Br(),
    dbc.Collapse([
    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    html.H1(children  = april_avail_data['User'][a], style={'margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),
    # html.Br(),
    # html.Br(),
    html.Div(style = {'margin-left': '45px', 'background-color': 'white',      'width' : '1250px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '20px', 'margin-left' : '30px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability (hours per month)', style={'margin-left' : '20px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ])
    ,
    dbc.Row([ dbc.Col([
        html.Div(style = {'margin-top' : '10px', 'margin-left' : '15px','width':'100%'}, children=[
            html.Span(children= jan_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '40px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= feb_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= march_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= april_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= may_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= june_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children=  july_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= august_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= sep_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= oct_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= nov_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= dec_avail_data['Availability'][a], style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            
        ])
    ])]),
        dbc.Row([dbc.Col([
        html.Div(style = {'margin-top' : '10px', 'margin-left' : '15px'}, children=[
            html.Span(children= 'Jan', style={'display' : 'inline-block', 'margin-left' : '40px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Feb', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Mar', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Apr', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'May', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Jun', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Jul', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Aug', style={'display' : 'inline-block', 'margin-left' : '40px','margin-right' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Sep', style={'display' : 'inline-block', 'margin-left' : '30px','margin-right' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Oct', style={'display' : 'inline-block', 'margin-left' : '20px','margin-right' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Nov', style={'display' : 'inline-block', 'margin-left' : '20px','margin-right' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            html.Span(children= 'Dec', style={'display' : 'inline-block', 'margin-left' : '20px','margin-right' : '40px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '150%'}),
            
        ])
    ]),


    ])
    ]
    ),

    html.Br(),
    html.Br(),


    dbc.Row(style= {'width' : '1200px', 'margin-left': '70px'},
    children = [
        dbc.Col(style = {'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'AVAILABILITY  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = avail_logg_diff, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
        dbc.Col(style = {'margin-left' : '20px', 'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'IN STATUS TIME  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = in_time_logg_time, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
    ]),
    html.Br(),


    dbc.Row(style= {'width' : '1200px', 'margin-left': '70px'},
    children = [
        dbc.Col(style = {'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = april_avail_data['User'][a], style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    html.P(children = 'Works with ?????? on our web-platform and is located in ????? with timezone ???', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    html.P(children = 'Other Descriptive Text', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'})
    ])
        ]),
        dbc.Col(style = {'margin-left' : '20px', 'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = '1 STORYPOINT  vs LOGGED TIME(weighted average, hours)', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = in_time_logg_time, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
    ]),
    html.Br(),


    dbc.Row(style= {'width' : '1200px', 'margin-left': '70px'},
    children = [
        dbc.Col(style = {'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'AVAILABILITY  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = avail_logg_diff, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
        dbc.Col(style = {'margin-left' : '20px', 'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'IN STATUS TIME  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = in_time_logg_time, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1200px', 'margin-left': '70px'},
    children = [
        dbc.Col(style = {'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'AVAILABILITY  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = avail_logg_diff, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
        dbc.Col(style = {'margin-left' : '20px', 'background-color': 'white', 'width' : '600px', 'height' : '500px','display': 'inline-block'}, children =[
            html.Div( children =[
    html.H4(children = 'IN STATUS TIME  vs LOGGED TIME DIFFERENCE', style={'margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure= px.scatter(x = months, y = in_time_logg_time, 
        labels={
                        'x' : ' ',
                        'y' : ' ',
                    }),
                style ={'height' : '450px', 'width' : '550px'}),
    ])
        ]),
    ]),

    html.Br(),
    html.Br(),


                html.Div(children=[
                        dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'January', id="jan-button", n_clicks =0, style={'border': '0px','background-color':'transparent','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = jan_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = jan_timesheet_data[jan_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(jan_tis_data['Narek Poghosyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((jan_avail_data['Availability'][a]/jan_timesheet_data[jan_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),

    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(jan_intime_loggedtime)) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),


    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(jan_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(jan_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(jan_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(jan_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(jan_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="jan-collapse", is_open=False),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
        dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'February', id="feb-button", n_clicks =0, style={'border': '0px','background-color':'transparent','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = feb_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = feb_timesheet_data[feb_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(feb_tis_data['Narek Poghosyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((feb_avail_data['Availability'][a]/feb_timesheet_data[feb_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),

    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  ="{:.2f}".format(float(feb_intime_loggedtime)) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),


    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(feb_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(feb_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(feb_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(feb_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(feb_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="feb-collapse", is_open=False),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'March', id="march-button", n_clicks =0, style={'border': '0px','background-color':'transparent','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = march_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = march_timesheet_data[march_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(march_tis_data['Narek Poghosyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((march_avail_data['Availability'][a]/march_timesheet_data[march_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),

    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(march_intime_loggedtime)) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(march_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(march_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(march_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(march_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(march_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="march-collapse", is_open=False),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'April', id="april-button", n_clicks =0, style={'border': '0px','background-color':'transparent','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = april_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = april_timesheet_data[april_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(april_tis_data['Narek Poghosyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((april_avail_data['Availability'][a]/april_timesheet_data[april_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),

    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(april_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(april_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(april_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(april_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(april_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(april_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="april-collapse", is_open=False),
        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'May', id = 'may-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = may_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = may_timesheet_data[may_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(may_tis_data['Narek Poghosyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((may_avail_data['Availability'][a]/may_timesheet_data[may_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(may_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(may_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(may_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(may_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(may_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(may_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    ], id="may-collapse", is_open=False),
                        html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'June', id = 'june-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = june_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = june_timesheet_data[june_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(june_tis_data['Narek Poghosyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((june_avail_data['Availability'][a]/june_timesheet_data[june_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(june_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(june_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(june_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(june_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(june_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(june_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="june-collapse", is_open=False),
    html.Br(),
    html.Br(),

                        dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'July', id = 'july-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = july_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = july_timesheet_data[july_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(july_tis_data['Narek Poghosyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((july_avail_data['Availability'][a]/july_timesheet_data[july_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(july_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(july_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(july_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(july_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(july_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(july_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="july-collapse", is_open=False),
                        html.Br(),
    html.Br(),

                        dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'August', id = 'august-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = august_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = august_timesheet_data[august_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(august_tis_data['Narek Poghosyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((august_avail_data['Availability'][a]/august_timesheet_data[august_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(august_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(august_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(august_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(august_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(august_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(august_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="august-collapse", is_open=False),

                    
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'September', id = 'sep-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = sep_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = sep_timesheet_data[sep_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(sep_tis_data['Narek Poghosyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((sep_avail_data['Availability'][a]/sep_timesheet_data[sep_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(sep_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(sep_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(sep_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(sep_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(sep_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(sep_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="sep-collapse", is_open=False),
                            
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'October', id = 'oct-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = oct_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = oct_timesheet_data[oct_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(oct_tis_data['Narek Poghosyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((oct_avail_data['Availability'][a]/oct_timesheet_data[oct_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(oct_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(oct_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(oct_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(oct_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(oct_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(oct_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="oct-collapse", is_open=False),
           
                    
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'November', id = 'nov-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = nov_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = nov_timesheet_data[nov_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(nov_tis_data['Narek Poghosyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((nov_avail_data['Availability'][a]/nov_timesheet_data[nov_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(nov_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(nov_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(nov_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(nov_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(nov_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(nov_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="nov-collapse", is_open=False),
                        
    html.Br(),
    html.Br(),

    dbc.Row(style = {'background-color': 'lightblue', 'width' : '100.85%',  'margin-top': ' -20px', 'height' : '120px'},children=[
    dbc.Col([
        html.Div([
    dbc.Button(children  = 'December', id = 'dec-button',style={'background-color':'transparent', 'border':'0px','margin-left' : '30px','color':'black','display':'inline-block', 'font-family': ' Arial', 'margin-top': '25px', 'font-weight' : 'bold', 'font-size': '300%'}),
    html.H1( children = '2022', style={'display':'inline-block','margin-right' : '50px', 'color':'black', 'float': 'right', 'font-family': ' Arial', 'margin-top': '40px', 'font-weight' : 'bold', 'font-size': '300%'}),
    ], )
    ]
    )
    ]),

    html.Br(),
    html.Br(),

    dbc.Collapse([
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '55px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'Availability', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = dec_avail_data['Availability'][a], style={'margin-top' : '-20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '400%'}),
    html.H1(children  = 'Hours', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    html.H1(children  = 'this month', style={'margin-top': '-10px','margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),
    ], )
    ]
    )
    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'LOGGED TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = dec_timesheet_data[dec_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum(), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '170px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '23px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = 'IN TIME', style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '125%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = np.round(dec_tis_data['Narek Poghosyan - In Progress'], decimals=2), style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'AVAILABILITY vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format((dec_avail_data['Availability'][a]/dec_timesheet_data[dec_timesheet_data['User'].str.contains('Narek Poghosyan')]['BillableHours'].sum())*100) + '%', style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Div(style = {'margin-top':'-10px','display': 'inline-block','margin-left': '30px', 'background-color': 'white',      'width' : '298px', 'height' : '200px'}, children = [
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = ['% DIFFERENCE -', html.Br(),  'IN TIME vs LOGGED TIME'], style={'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '100%'}),

    ], )
    ]
    )
    ]),
    dbc.Row(style = { },children=[
    dbc.Col([
        html.Div(style = {'margin-top': '10px', 'margin-left' : '5px', 'width':'100%'}, children=[
    html.H1(children  = "{:.2f}".format(float(dec_intime_loggedtime)) + '%',  style={'margin-top' : '20px', 'margin-left' : '10px','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '150%'}),

    ], )
    ]
    ),

    ])
    ]),
    html.Br(),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [    
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '1',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('1h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '1h',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure =
        px.scatter(dec_sp1, x = 'BillableHours', y = 'AC Changes', 
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },),
        style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',},
        ),
    ])
        ]),
    ]),
    html.Br(),

    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '2',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('2',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    #    html.H1(children = '3.5h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
    dcc.Graph( figure = px.scatter(dec_sp2, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '3',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('10h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(dec_sp3, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '5',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('1',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(dec_sp5, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
        html.Br(),
    dbc.Row(style= {'width' : '1272px', 'margin-left': '11px','height' : '620px'},
    children = [
        dbc.Col(style = {'margin-left': '45px','background-color': 'white',      'width' : '650px', 'height' : '600px','display': 'inline-block'}, children =[
            html.Div( children =[
        html.H1(children = '8',style={'display':'inline-block','margin-left' : '30px','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '50px'}),
    html.H4(children = 'STORYPOINT', style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'font-weight' : 'bold', 'font-size' : '120%'}),
        html.H4(children = ['Tickets Arriving at Done this Month: ',html.H1('0',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'})], style={'float':'right','display':'inline-block','margin-left' : '20px','color':'black', 'font-family': ' Arial', 'margin-top': '10px', 'font-weight' : 'bold', 'font-size' : '120%'}),
        # html.H1(children = '0',style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'}),
        html.Br(),
        html.H4(children = ['Weighted average of logged time this month: ',html.H1('2h',style={'display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '4px', 'font-weight' : 'bold','font-size': '40px'} )], style={'float':'right','display':'inline-block','color':'black', 'font-family': ' Arial', 'margin-top': '-18px', 'margin-right': '-375px', 'font-weight' : 'bold', 'font-size' : '120%'}),
    dcc.Graph( figure = px.scatter(dec_sp8, x = 'BillableHours', y = 'AC Changes',
        labels={
                        'BillableHours' : "Billable Hours",
                        'AC Changes' : "AC Changes",
                    },) ,
            # 'layout': {
            #     'plot_bgcolor': graph_colors['background'],
            #     'paper_bgcolor': graph_colors['background'],},
        

                style ={'margin-top':'28px','margin-left' : '20px','height' : '500px',}),
    ])
        ]),
    ]),
                    
                    ], id="dec-collapse", is_open=False),

                ]),
                dcc.Interval(
                    id='interval-component',
                    interval=1000, # in milliseconds
                    n_intervals=1,
                    max_intervals = 2, 
                    disabled = True
                )
                ], id = "mohsin-collapse", is_open = True),
                
    ])

    @narek_app.callback(
            [
                
                Output("jan-collapse", "is_open"),
                Output("feb-collapse", "is_open"),
                Output("march-collapse", "is_open"),
            Output("april-collapse", "is_open"),
            Output("may-collapse", "is_open"),
            Output("june-collapse", "is_open"),
            Output("july-collapse", "is_open"),
            Output("august-collapse", "is_open"),
            Output("sep-collapse", "is_open"),
            Output("oct-collapse", "is_open"),
            Output("nov-collapse", "is_open"),
            Output("dec-collapse", "is_open"),
        
            ],
            [
            
                Input("jan-button", "n_clicks"),
            Input("feb-button", "n_clicks"),
            Input("march-button", "n_clicks"),
            Input("april-button", "n_clicks"),
            Input("may-button", "n_clicks"),
            Input("june-button", "n_clicks"),
            Input("july-button", "n_clicks"),
            Input("august-button", "n_clicks"),
            Input("sep-button", "n_clicks"),
            Input("oct-button", "n_clicks"),
            Input("nov-button", "n_clicks"),
            Input("dec-button", "n_clicks"),
        
            ],
        )
    def toggle_collapses(button_one, button_two, button_three, button_four, button_five, button_six, button_seven, button_eight,
    button_nine, button_ten, button_eleven, button_twelve):
            ctx = dash.callback_context

            if not ctx.triggered:
                raise PreventUpdate
            else:
                button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            
            
            if button_id == 'jan-button':
                print(april_sp1['StoryPoints'])
                return True, False, False, False, False, False, False, False, False, False, False, False
            elif button_id == 'feb-button':
                return False, True, False, False, False, False, False, False, False, False, False, False
            elif button_id == 'march-button':
                return False, False, True, False, False, False, False, False, False, False, False, False
            elif button_id == 'april-button':
                return False, False, False, True, False, False, False, False, False, False, False, False
            elif button_id == 'may-button':
                return False, False, False, False, True, False, False, False, False, False, False, False
            elif button_id == 'june-button':
                return False, False, False, False, False, True, False, False, False, False, False, False
            elif button_id == 'july-button':
                return False, False, False, False, False, False, True, False, False, False, False, False
            elif button_id == 'august-button':
                return False, False, False, False, False, False, False, True, False, False, False, False
            elif button_id == 'sep-button':
                return False, False, False, False, False, False, False, False, True, False, False, False
            elif button_id == 'oct-button':
                return False, False, False, False, False, False, False, False, False, True, False, False
            elif button_id == 'nov-button':
                return False, False, False, False, False, False, False, False, False, False, True, False
            elif button_id == 'dec-button':
                return False, False, False, False, False, False, False, False, False, False, False, True
            else:
                raise ValueError(f'Unexpected ID: {button_id}')
    return layout



mohsin_app.layout = mohsin_layout(0)
jalil_app.layout = jalil_layout(2)
angela_app.layout = angela_layout(3)
narek_app.layout = narek_layout(4)

if __name__ == '__main__':
    server.run()