# 1. Import Dash
import dash
from dash import dcc
from dash import html
from dash import Dash
from dash import dash_table
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd
import plotly
import plotly.express as px

import statistics as st
from statistics import mode


# 2. Creat a Dash app instance
app = dash.Dash(
    external_stylesheets=[dbc.themes.LUX],
    name = 'Employee Data'
)

app.title = 'Employee Attrition Data Dashboard Analytics'

# Navbar

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="https://www.google.com/")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Employee Attrition Data Dashboard",
    brand_href="#",
    color="#C00000",
    dark=True,
)

# IMPORT DATA EA

ea = pd.read_csv('HR Employee Attrition.csv')

agecat = []
for i in ea['Age']:
    if i<20:
        agecat.append('< 20')
    elif i>=20:
        if i<30:
            agecat.append('20 - 30')
        elif i>=30:
            if i<40:
                agecat.append('30 - 40')
            elif i>=40:
                if i<50:
                    agecat.append('40 - 50')
                elif i>=50:
                    agecat.append('> 50')

ea['RangeAge']=agecat

alldept = ['All Department']
deptlist = ea['Department'].unique().tolist()
deptopt = alldept + deptlist

# CARD CONTENT

# headcount = [
#     dbc.CardHeader('Headcount', style={"color":"black"}),
#     dbc.CardBody([
#         html.H1(ea.shape[0])
#     ]),
# ]

# ats = [
#     dbc.CardHeader('Attrition', style={"color":"black"}),
#     dbc.CardBody([
#         html.H1(f"{round((((ea[ea['Attrition']=='Yes'].shape[0])/(ea.shape[0]))*100),2)} %")
#     ]),
# ]

# Gender Pie
# genderpie = px.pie(ea,
#         values='EmployeeCount',
#         names='Gender',
#         color_discrete_sequence=['#C00000', '#FF8181'],
#         template='ggplot2',
#         title='by Gender',
#         )

# Position Bar
# position=pd.crosstab(
#         index=ea['JobRole'],
#         columns='Headcount',
#     ).reset_index().sort_values('Headcount', ascending=False)
# barposition = px.bar(
#         position,
#         x='JobRole',
#         y='Headcount',
#         labels={
#             'JobRole':'Position'
#         },
#         template='ggplot2',
#         color_discrete_sequence=['#C00000'],
#         title = 'Headcount by Position',
#     )

# Range Age Bar
# kumur=pd.crosstab(
#         index=ea['RangeAge'],
#         columns='Headcount',
#     ).reset_index().sort_values('RangeAge', ascending=True)
# barage = px.bar(
#         kumur,
#         x='RangeAge',
#         y='Headcount',
#         labels={
#             'RangeAge':'Kelompok Umur'
#         },
#         template='ggplot2',
#         color_discrete_sequence=['#C00000'],
#         title = 'Headcount by Age',
#     )

# Performance Bar
# perf=pd.crosstab(
#         index=ea['PerformanceRating'],
#         columns='Headcount',
#     ).reset_index().sort_values('PerformanceRating', ascending=True)
# barperformance = px.bar(
#         perf,
#         x='PerformanceRating',
#         y='Headcount',
#         labels={
#             'PerformanceRating':'Performance Score'
#         },
#         template='ggplot2',
#         color_discrete_sequence=['#C00000'],
#         title = 'by Performance',
#     )

# Env Satisfaction Bar
# env=pd.crosstab(
#         index=ea['EnvironmentSatisfaction'],
#         columns='Headcount',
#     ).reset_index().sort_values('EnvironmentSatisfaction', ascending=True)
# barenv = px.bar(
#         env,
#         x='EnvironmentSatisfaction',
#         y='Headcount',
#         labels={
#             'EnvironmentSatisfaction':'Satisfaction of Working Environment'
#         },
#         template='ggplot2',
#         color_discrete_sequence=['#C00000'],
#         title = 'by Environment Satisfaction',
#     )

# Job Satisfaction Bar
# jobsat=pd.crosstab(
#         index=ea['JobSatisfaction'],
#         columns='Headcount',
#     ).reset_index().sort_values('JobSatisfaction', ascending=True)
# barjobsat = px.bar(
#         jobsat,
#         x='JobSatisfaction',
#         y='Headcount',
#         labels={
#             'JobSatisfaction':'Job Satisfaction'
#         },
#         template='ggplot2',
#         color_discrete_sequence=['#C00000'],
#         title = 'by Job Satisfaction',
#     )

# Relationship Satisfaction
# relsat=pd.crosstab(
#         index=ea['RelationshipSatisfaction'],
#         columns='Headcount',
#     ).reset_index().sort_values('RelationshipSatisfaction', ascending=True)
# barrelsat = px.bar(
#         relsat,
#         x='RelationshipSatisfaction',
#         y='Headcount',
#         labels={
#             'RelationshipSatisfaction':'Satisfaction of Working Relationship'
#         },
#         template='ggplot2',
#         color_discrete_sequence=['#C00000'],
#         title = 'by Relationship Satisfaction',
#     )

# Extract Data by Attrite Employee Only

ea_attrite=ea[ea['Attrition']=='Yes']

# Correlation Attrition by Distance

# distatt=pd.DataFrame({'Distance':[],
#                      'AttritionRatebyDistance':[]
#                     })
# distlist=[]
# vardist=1
# while vardist<30:
#     distlist.append(vardist)
#     vardist=vardist+1

# distatt['Distance']=distlist

# percent_dist=[]
# for i in distatt['Distance']:
#     percent_dist.append((len(ea_attrite[ea_attrite['DistanceFromHome']==i])/len(ea[ea['DistanceFromHome']==i]))*100)

# distatt['AttritionRatebyDistance']=percent_dist

# scatter_distatt = px.scatter(
#                     distatt,
#                     x = 'Distance',
#                     y = 'AttritionRatebyDistance',
#                     labels={
#                         'AttritionRatebyDistance':'Attrition (Rate per Distance)'
#                     },
#                     color_discrete_sequence=['#C00000'],
#                     trendline='ols',
#                     title='Correlation between Attrition and Office Distance From Home',
#                 )

# Correlation Attrition by Age

# ageatt=pd.DataFrame({'Age':[],
#                      'AttritionRatebyAge':[]
#                     })
# agelist=[]
# varage=18
# while varage<61:
#     agelist.append(varage)
#     varage=varage+1

# ageatt['Age']=agelist

# percent_age=[]
# for i in ageatt['Age']:
#     percent_age.append((len(ea_attrite[ea_attrite['Age']==i])/len(ea[ea['Age']==i]))*100)

# ageatt['AttritionRatebyAge']=percent_age

# scatter_ageatt = px.scatter(
#                     ageatt,
#                     x = 'Age',
#                     y = 'AttritionRatebyAge',
#                     labels={
#                         'AttritionRatebyAge':'Attrition (Rate per Age)'
#                     },
#                     color_discrete_sequence=['#C00000'],
#                     trendline='ols',
#                     title='Correlation between Attrition and Age',
#                 )

# correl = px.scatter(
#     ea,
#     x="YearsAtCompany",
#     y="MonthlyIncome",
#     trendline="ols",
#     color_discrete_sequence=['#C00000'],
#     labels={
#             'YearsAtCompany':'Tenure'
#         },
#     title='Correlation between Tenure and Monthly Income')
# corr = px.get_trendline_results(correl)
# corrresult = corr.px_fit_results.iloc[0].summary()


# LAYOUT

app.layout = html.Div(children=[
    navbar,

    html.Br(),

    # Component Main Page

    html.Div([

        # ROW 1
        dbc.Row([

            # ROW 1 - COL 1
            dbc.Col(
                [
                    html.Br(),
                    dbc.Card([
                        dbc.CardHeader('Select Country'),
                        dbc.CardBody(
                            dcc.Dropdown(
                                id='choose_dept',
                                options=deptopt,
                                value='All Department',
                            ),
                        ),
                    ]),
                    html.Br(),
                    dbc.Card(id='card_headcount', color='#D9D9D9',),
                    html.Br(),
                    dbc.Card(id='card_ats', color='#D9D9D9',),
                ],
                width=3),

            # ROW 1 - COL 2
            dbc.Col(
                [
                    dcc.Graph(id='plotpie_gender'),
                ],
                width=3),
            
            # ROW 1 - COL 3
            dbc.Col(
                [
                    dcc.Graph(id='plotbar_position'),
                ],
                width=6),
        ]),

        html.Hr(),

        # ROW 2
        dbc.Row([

            # ROW 2 - COL 1
            dbc.Col([
                dcc.Graph(id='plotbar_rangeage')
            ],
            width=6),
            
            # ROW 2 - COL 2
            dbc.Col([
#                html.H1('Analysis by Satisfaction/Performance'),
                dbc.Tabs([
                    # TAB 1: Performance
                    dbc.Tab(
                        dcc.Graph(
                            id='plotbar_performance',
                        ),
                        label='Performance Score'),

                    # TAB 2: Job Satisfaction
                    dbc.Tab(
                        dcc.Graph(
                            id='plotbar_jobsat',
                       ),
                        label='Job Satisfaction'),
                    
                    # TAB 3: Environment Satisfaction
                    dbc.Tab(
                        dcc.Graph(
                            id='plotbar_env',
                        ),
                        label='Working Environment Satisfaction'
                    ),

                    # TAB 4: Relationship Satisfaction
                    dcc.Tab(
                        dcc.Graph(
                            id='plotbar_relsat',
                        ),
                        label='Working Relationship Satisfaction'
                    ),
                ]),
            ],
            width=6),
        ]),

        # ROW 3
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='plotscatter_ageatt',
                ),
            ],
            width=6),
            dbc.Col([
                dcc.Graph(
                    id='plotscatter_distatt',
                ),
            ],
            width=6)
        ])

    ], style={
        'paddingLeft':'30px',
        'paddingRight':'30px',
    }),
])


# CALLBACK FOR ALL PLOT

    # CARD CONTENT HEADCOUNT

@app.callback(
    Output(component_id='card_headcount', component_property='children'),
    Input(component_id='choose_dept', component_property='value')
)
def update_CardHeadcount(dept_name):
    if dept_name == 'All Department':
        ea_card = ea
    else:
        ea_card = ea[ea['Department'] == dept_name]

    headcount = [
        dbc.CardHeader('Headcount', style={"color":"black"}),
        dbc.CardBody([
            html.H1(ea_card.shape[0])
        ]),
    ]
    return headcount


    # CARD CONTENT ATTRITION

@app.callback(
    Output(component_id='card_ats', component_property='children'),
    Input(component_id='choose_dept', component_property='value')
)
def update_CardATS(dept_name):
    if dept_name == 'All Department':
        ea_card = ea
    else:
        ea_card = ea[ea['Department'] == dept_name]

    ats = [
        dbc.CardHeader('Attrition', style={"color":"black"}),
        dbc.CardBody([
            html.H1(f"{round((((ea_card[ea_card['Attrition']=='Yes'].shape[0])/(ea_card.shape[0]))*100),2)} %")
        ]),
    ]
    return ats


    # GENDER PLOT PIE

@app.callback(
    Output(component_id='plotpie_gender', component_property='figure'),
    Input(component_id='choose_dept', component_property='value')
)
def update_PieGender(dept_name):
    if dept_name == 'All Department':
        ea_plot = ea
    else:
        ea_plot = ea[ea['Department'] == dept_name]
    genderpie = px.pie(ea_plot,
            values='EmployeeCount',
            names='Gender',
            color_discrete_sequence=['#C00000', '#FF8181'],
            template='ggplot2',
            title='by Gender',
            )
    return genderpie


    # PLOT BAR POSITION

@app.callback(
    Output(component_id='plotbar_position', component_property='figure'),
    Input(component_id='choose_dept', component_property='value')
)
def update_BarPosition(dept_name):
    if dept_name == 'All Department':
        ea_plot = ea
    else:
        ea_plot = ea[ea['Department'] == dept_name]
    position=pd.crosstab(
            index=ea_plot['JobRole'],
            columns='Headcount',
        ).reset_index().sort_values('Headcount', ascending=False)
    barposition = px.bar(
            position,
            x='JobRole',
            y='Headcount',
            labels={
                'JobRole':'Position'
            },
            template='ggplot2',
            color_discrete_sequence=['#C00000'],
            title = 'Headcount by Position',
        )
    return barposition


    # PLOT BAR RANGE AGE

@app.callback(
    Output(component_id='plotbar_rangeage', component_property='figure'),
    Input(component_id='choose_dept', component_property='value')
)
def update_BarRangeAge(dept_name):
    if dept_name == 'All Department':
        ea_plot = ea
    else:
        ea_plot = ea[ea['Department'] == dept_name]
    kumur=pd.crosstab(
            index=ea_plot['RangeAge'],
            columns='Headcount',
        ).reset_index().sort_values('RangeAge', ascending=True)
    barage = px.bar(
            kumur,
            x='RangeAge',
            y='Headcount',
            labels={
                'RangeAge':'Range Age'
            },
            template='ggplot2',
            color_discrete_sequence=['#C00000'],
            title = 'Headcount by Age',
        )
    return barage


    # PLOT BAR PERFORMANCE

@app.callback(
    Output(component_id='plotbar_performance', component_property='figure'),
    Input(component_id='choose_dept', component_property='value')
)
def update_BarPerformance(dept_name):
    if dept_name == 'All Department':
        ea_plot = ea
    else:
        ea_plot = ea[ea['Department'] == dept_name]
    perf=pd.crosstab(
            index=ea_plot['PerformanceRating'],
            columns='Headcount',
        ).reset_index().sort_values('PerformanceRating', ascending=True)
    barperformance = px.bar(
            perf,
            x='PerformanceRating',
            y='Headcount',
            labels={
                'PerformanceRating':'Performance Score'
            },
            template='ggplot2',
            color_discrete_sequence=['#C00000'],
            title = 'by Performance',
        )
    return barperformance


    # PLOT BAR JOB SATISFACTION

@app.callback(
    Output(component_id='plotbar_jobsat', component_property='figure'),
    Input(component_id='choose_dept', component_property='value')
)
def update_BarJobSat(dept_name):
    if dept_name == 'All Department':
        ea_plot = ea
    else:
        ea_plot = ea[ea['Department'] == dept_name]
    jobsat=pd.crosstab(
            index=ea_plot['JobSatisfaction'],
            columns='Headcount',
        ).reset_index().sort_values('JobSatisfaction', ascending=True)
    barjobsat = px.bar(
            jobsat,
            x='JobSatisfaction',
            y='Headcount',
            labels={
                'JobSatisfaction':'Job Satisfaction'
            },
            template='ggplot2',
            color_discrete_sequence=['#C00000'],
            title = 'by Job Satisfaction',
        )
    return barjobsat


    # PLOT BAR ENVIRONMENT SATISFACTION

@app.callback(
    Output(component_id='plotbar_env', component_property='figure'),
    Input(component_id='choose_dept', component_property='value')
)
def update_BarEnvSat(dept_name):
    if dept_name == 'All Department':
        ea_plot = ea
    else:
        ea_plot = ea[ea['Department'] == dept_name]
    env=pd.crosstab(
            index=ea_plot['EnvironmentSatisfaction'],
            columns='Headcount',
        ).reset_index().sort_values('EnvironmentSatisfaction', ascending=True)
    barenv = px.bar(
            env,
            x='EnvironmentSatisfaction',
            y='Headcount',
            labels={
                'EnvironmentSatisfaction':'Working Environment Satisfaction'
            },
            template='ggplot2',
            color_discrete_sequence=['#C00000'],
            title = 'by Environment Satisfaction',
        )
    return barenv


    # PLOT BAR RELATIONSHIP SATISFACTION

@app.callback(
    Output(component_id='plotbar_relsat', component_property='figure'),
    Input(component_id='choose_dept', component_property='value')
)
def update_BarRelSat(dept_name):
    if dept_name == 'All Department':
        ea_plot = ea
    else:
        ea_plot = ea[ea['Department'] == dept_name]
    relsat=pd.crosstab(
            index=ea_plot['RelationshipSatisfaction'],
            columns='Headcount',
        ).reset_index().sort_values('RelationshipSatisfaction', ascending=True)
    barrelsat = px.bar(
            relsat,
            x='RelationshipSatisfaction',
            y='Headcount',
            labels={
                'RelationshipSatisfaction':'Working Relationship Satisfaction'
            },
            template='ggplot2',
            color_discrete_sequence=['#C00000'],
            title = 'by Relationship Satisfaction',
        )
    return barrelsat


    # PLOT SCATTER CORRELATION AGE AND ATTRITION (YES ONLY)

@app.callback(
    Output(component_id='plotscatter_ageatt', component_property='figure'),
    Input(component_id='choose_dept', component_property='value')
)
def update_ScatterAgeAtt(dept_name):
    if dept_name == 'All Department':
        ea_plot = ea
        ea_plot_a = ea_attrite
    else:
        ea_plot = ea[ea['Department'] == dept_name]
        ea_plot_a = ea_attrite[ea_attrite['Department'] == dept_name]
    ageatt=pd.DataFrame({'Age':[],
                        'AttritionRatebyAge':[]
                        })
    agelist=[]
    varage=18
    while varage<61:
        agelist.append(varage)
        varage=varage+1

    ageatt['Age']=agelist

    percent_age=[]
    for i in ageatt['Age']:
        percent_age.append((len(ea_plot_a[ea_plot_a['Age']==i])/len(ea_plot[ea_plot['Age']==i]))*100)

    ageatt['AttritionRatebyAge']=percent_age

    scatter_ageatt = px.scatter(
                        ageatt,
                        x = 'Age',
                        y = 'AttritionRatebyAge',
                        labels={
                            'AttritionRatebyAge':'Attrition (Rate per Age)'
                        },
                        color_discrete_sequence=['#C00000'],
                        trendline='ols',
                        title='Correlation between Attrition and Age',
                    )
    return scatter_ageatt


    # PLOT SCATTER CORRELATION OFFICE DISTANCE FROM HOME AND ATTRITION (YES ONLY)

@app.callback(
    Output(component_id='plotscatter_distatt', component_property='figure'),
    Input(component_id='choose_dept', component_property='value')
)
def update_ScatterDistAtt(dept_name):
    if dept_name == 'All Department':
        ea_plot = ea
        ea_plot_a = ea_attrite
    else:
        ea_plot = ea[ea['Department'] == dept_name]
        ea_plot_a = ea_attrite[ea_attrite['Department'] == dept_name]
    distatt=pd.DataFrame({'Distance':[],
                        'AttritionRatebyDistance':[]
                        })
    distlist=[]
    vardist=1
    while vardist<30:
        distlist.append(vardist)
        vardist=vardist+1

    distatt['Distance']=distlist

    percent_dist=[]
    for i in distatt['Distance']:
        percent_dist.append((len(ea_plot_a[ea_plot_a['DistanceFromHome']==i])/len(ea_plot[ea_plot['DistanceFromHome']==i]))*100)

    distatt['AttritionRatebyDistance']=percent_dist

    scatter_distatt = px.scatter(
                        distatt,
                        x = 'Distance',
                        y = 'AttritionRatebyDistance',
                        labels={
                            'AttritionRatebyDistance':'Attrition (Rate per Distance)'
                        },
                        color_discrete_sequence=['#C00000'],
                        trendline='ols',
                        title='Correlation between Attrition and Office Distance From Home',
                    )
    return scatter_distatt


# 3. Start the Dash server
if __name__ == "__main__":
    app.run_server()
