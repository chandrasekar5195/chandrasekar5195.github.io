from plotly import tools
import sys
import plotly
import plotly.graph_objs as go
import numpy as np

def draw_graph():
    N=100
    SG_Mem=np.random.uniform(low=40, high=80, size=100)
    HK_Mem=(np.random.randn(N) + 2) + 20
    x=np.linspace(0, 1, N)
    traces=[
    go.Scatter(x=np.linspace(0, 1, N), y=SG_Mem, name='SG_Mem', line=dict(width=1)),
    go.Scatter(x=np.linspace(0, 1, N), y=(np.random.randn(N)+2)+20, xaxis='x2', yaxis='y2',line=dict(width=1)),
    go.Scatter(x=np.linspace(0, 1, N), y=np.random.uniform(low=40, high=80, size=100), xaxis='x3', yaxis='y3',line=dict(width=1)),
    go.Scatter(x=np.linspace(0, 1, N), y=(np.random.randn(N)+2)+50, xaxis='x4', yaxis='y4', line=dict(width=1)),
    go.Scatter(x=np.linspace(0, 1, N), y=(np.random.randn(N)+2)+20, xaxis='x5', yaxis='y5', line=dict(width=1)),
    go.Scatter(x=np.linspace(0, 1, N), y=np.random.uniform(low=40, high=80, size=100), xaxis='x6', yaxis='y6', line=dict(width=1)),
    go.Scatter(x=np.linspace(0, 1, N), y=HK_Mem, line=dict(width=1))
             ]
    layout = go.Layout(
        title='APAC IaaS Dashboard',
        autosize=True,
        shapes = [
            dict(
                type='line',
                xref='paper',
                yref='paper',
                x0=0,
                y0=0.75,
                x1=0.26,
                y1=0.75,
                line=dict(color='rgb(250,0,0)', width=3, dash='dash')
            ),
            dict(
                type='line',
                xref='paper',
                yref='paper',
                x0=0.37,
                y0=0.75,
                x1=0.63,
                y1=0.75,
                line=dict(color='rgb(250,0,0)', width=3, dash='dash')
            )
        ],
        annotations = [
            dict(
                xref='paper',
                yref='paper',
                x=0.14444444444444446,
                y=1,
                xanchor='center',
                yanchor='bottom',
                showarrow=False,
                text='CPU',
                font=dict(size=14)
            ),
            dict(
                xref='paper',
                yref='paper',
                x=0.5,
                y=1,
                xanchor='center',
                yanchor='bottom',
                showarrow=False,
                text='MEMORY',
                font=dict(size=14)
            ),
            dict(
                xref='paper',
                yref='paper',
                x=0.8555555555555556,
                y=1,
                xanchor='center',
                yanchor='bottom',
                showarrow=False,
                text='STORAGE',
                font=dict(size=14)
            ),
            dict(
                xref='paper',
                yref='paper',
                x=0.14444444444444446,
                y=0.375,
                xanchor='center',
                yanchor='bottom',
                showarrow=False,
                text='CPU',
                font=dict(size=14)
            ),
            dict(
                xref='paper',
                yref='paper',
                x=0.5,
                y=0.375,
                xanchor='center',
                yanchor='bottom',
                showarrow=False,
                text='MEMORY',
                font=dict(size=14)
            ),
            dict(
                xref='paper',
                yref='paper',
                x=0.8555555555555556,
                y=0.375,
                xanchor='center',
                yanchor='bottom',
                showarrow=False,
                text='STORAGE',
                font=dict(size=14)
            ),
            dict(
                xref='paper',
                yref='paper',
                x=0.14444444444444446,
                y=1,
                xanchor='center',
                yanchor='bottom',
                showarrow=False,
                text='CPU',
                font=dict(size=14)
            ),
            dict(
                xref='paper',
                yref='paper',
                x=0.26,
                y=0.75,
                xanchor='right',
                yanchor='bottom',
                showarrow=False,
                text='Threshold',
                font=dict(size=12)
            ),
            dict(
                xref='x',
                yref='y',
                xanchor='left',
                yanchor='middle',
                showarrow=False,
                text='SG',
                x=1,
                y=SG_Mem[99]
            ),
            dict(
                xref='x',
                yref='y',
                xanchor='left',
                yanchor='middle',
                showarrow=False,
                text='HK',
                x=1,
                y=HK_Mem[99]
            )
        ],
        showlegend=False,
        xaxis=dict(
            domain=[0, 0.26],
            fixedrange=True
        ),
        xaxis2=dict(
            domain=[0.37, 0.63],
            anchor='y2',
            fixedrange=True,

        ),
        xaxis3=dict(
            domain=[0.74, 1],
            anchor='y3',
            fixedrange=True
        ),
        xaxis4=dict(
            domain=[0, 0.26],
            anchor='y4',
            fixedrange=True
        ),
        xaxis5=dict(
            domain=[0.37, 0.63],
            anchor='y5',
            fixedrange=True
        ),
        xaxis6=dict(
            domain=[0.74, 1],
            anchor='y6',
            fixedrange=True
        ),
        yaxis=dict(
            domain=[0.6, 1],
            range=[0,100],
            fixedrange=True,
        ),
        yaxis2=dict(
            domain=[0.6, 1],
            anchor='x2',
            range = [0, 100],
            fixedrange=True
        ),
        yaxis3=dict(
            domain=[0.6, 1],
            anchor='x3',
            range = [0, 100],
            fixedrange=True
        ),
        yaxis4=dict(
            domain=[0, 0.4],
            anchor='x4',
            range = [0, 100],
            fixedrange=True
        ),
        yaxis5=dict(
            domain=[0, 0.4],
            anchor='x5',
            range = [0, 100],
            fixedrange=True
        ),
        yaxis6=dict(
            domain=[0, 0.4],
            anchor='x6',
            range = [0, 100],
            fixedrange=True
        )
    )
    config = {'displayModeBar':False,
              'showLink':False}
    data = [traces[0], traces[1], traces[2], traces[3], traces[4], traces[5], traces[6]]
    fig = go.Figure(data=data,layout=layout)
    plotly.offline.plot(fig, output_type='file', config=config)
    #print(code)

sys.stdout = open('subplot_ver2.txt','w')

draw_graph()
