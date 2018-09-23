from plotly import tools
import sys
import plotly
import plotly.graph_objs as go
import numpy as np

def draw_graph():
    N=100
    font_size_heading=18
    font_size_threshold=12
    color_SG='#0000FF'
    color_HK='#298A08'
    SG_T3_CPU = np.random.uniform(low=60, high=80, size=12)
    HK_T3_CPU = np.random.uniform(low=50, high=60, size=12)
    SG_T3_MEM = np.random.uniform(low=70, high=90, size=12)
    HK_T3_MEM = np.random.uniform(low=50, high=60, size=12)
    SG_T3_DISK_USED = np.random.uniform(low=60, high=80, size=12)
    HK_T3_DISK_USED = np.random.uniform(low=50, high=60, size=12)
    SG_T3_DISK_OPROV = np.random.uniform(low=20, high=30, size=12)
    HK_T3_DISK_OPROV = np.random.uniform(low=10, high=20, size=12)
    clusters=['cluster A', 'cluster B', 'cluster C', 'cluster D', 'cluster E']
    cluster_dc=['SG','HK','SG','SG','HK']
    cluster_status=['Open','Closed','Open','Closed','Open']
    cluster_status_color=['#58FA58','#DF013A','#58FA58','#DF013A','#58FA58']
    cluster_constrainedby=['Storage','Memory','CPU','Storage','CPU']
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul','Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    trace_table=go.Table(
        columnorder=[1, 2, 3, 4],
        columnwidth=[10, 5, 8, 15],
        domain=dict(x=[0.37,0.63], y=[0,0.4]),
        header=dict(height=40,
                    values=[['Cluster'], ['DC'], ['Status'], ['Constrained By']],
                    line=dict(color=['#000000'])    ,
                    font=dict(color=['rgb(45, 45, 45)'] * 5, size=14),
                    fill=dict(color='#ffffff'),
                    align=['center']*4,
                    ),

        cells = dict(values=[clusters, cluster_dc, cluster_status, cluster_constrainedby],
                    font=dict(color=['rgb(40, 40, 40)'] * 4, size=12),
                    height=30,
                    fill=dict(color=['#ffffff','#ffffff',cluster_status_color,'#ffffff']),
                    line=dict(color=['#000000']))

    )
    #fill = dict(color=['rgb(235, 193, 238)', 'rgba(228, 222, 249, 0.65)']))

    traces = [
        go.Scatter(x=month, y=SG_T3_CPU, name='SG_CPU', mode='lines', line=dict(width=1, color=(color_SG))),
        go.Scatter(x=month, y=HK_T3_CPU, name='HK_CPU', mode='lines', line=dict(width=1, color=(color_HK))),
        go.Scatter(x=month, y=SG_T3_MEM, name='SG_MEM', mode='lines', xaxis='x2', yaxis='y2',line=dict(width=1, color=(color_SG))),
        go.Scatter(x=month, y=HK_T3_MEM, name='HK_MEM', mode='lines', xaxis='x2', yaxis='y2',line=dict(width=1, color=(color_HK))),
        go.Scatter(x=month, y=SG_T3_DISK_USED, name='HK_DISK_USED', xaxis='x3', mode='lines', yaxis='y3',line=dict(width=1, color=(color_SG))),
        go.Scatter(x=month, y=HK_T3_DISK_USED, name='HK_DISK_USED', xaxis='x3', mode='lines', yaxis='y3',line=dict(width=1, color=(color_SG))),
        go.Scatter(x=month, y=SG_T3_DISK_OPROV, name='HK_DISK_OPROV', xaxis='x3', mode='lines', yaxis='y3',line=dict(width=1, color=(color_HK))),
        go.Scatter(x=month, y=HK_T3_DISK_OPROV, name='HK_DISK_OPROV', xaxis='x3', mode='lines', yaxis='y3',line=dict(width=1, color=(color_HK))),
        go.Scatter(x=month, y=np.random.uniform(low=40, high=80, size=12), mode='lines', xaxis='x4', yaxis='y4',line=dict(width=1)),
        #go.Scatter(x=month, y=np.random.uniform(low=30, high=50, size=12), mode='lines', xaxis='x5', yaxis='y5',line=dict(width=1)),
        go.Scatter(x=month, y=np.random.uniform(low=70, high=90, size=12), mode='lines', xaxis='x6', yaxis='y6',line=dict(width=1))
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
            ,
            dict(
                type='line',
                xref='paper',
                yref='paper',
                x0=0.74,
                y0=0.75,
                x1=1,
                y1=0.75,
                line=dict(color='rgb(250,0,0)', width=3, dash='dash')
            )
        ],
        annotations = [
            dict(
                x=-0.04944728761514841,
                y=0.83,
                showarrow=False,
                text='T3',
                textangle=-90,
                font=dict(size=24),
                xref='paper',
                yref='paper'
            ),
            dict(
                x=-0.04944728761514841,
                y=0.17,
                showarrow=False,
                text='T4',
                textangle=-90,
                font=dict(size=24),
                xref='paper',
                yref='paper'
            ),
            dict(
                xref='paper',
                yref='paper',
                x=-0.06,
                y=0.55,
                arrowhead=0,
                showarrow=False,
                xanchor='left',
                yanchor='middle',
                text='Legend : '
            ),
            dict(
                xref='paper',
                yref='paper',
                x=-0.05,
                y=0.52,
                arrowcolor=color_SG,
                arrowhead=0,
                showarrow=True,
                xanchor='left',
                yanchor='middle',
                ax=20,
                ay=0,
                text='SG'
            ),
            dict(
                xref='paper',
                yref='paper',
                x=-0.05,
                y=0.49,
                arrowcolor=color_HK,
                arrowhead=0,
                showarrow=True,
                xanchor='left',
                yanchor='middle',
                ax=20,
                ay=0,
                text='HK'
            ),
            dict(
                xref='paper',
                yref='paper',
                x=0.14444444444444446,
                y=1,
                xanchor='center',
                yanchor='bottom',
                showarrow=False,
                text='',
                font=dict(size=font_size_heading)
            ),
            dict(
                xref='paper',
                yref='paper',
                x=0.5,
                y=1,
                xanchor='center',
                yanchor='bottom',
                showarrow=False,
                text='MEMORY UTILIZATION (%)',
                font=dict(size=font_size_heading)
            ),
            dict(
                xref='paper',
                yref='paper',
                x=0.8555555555555556,
                y=1,
                xanchor='center',
                yanchor='bottom',
                showarrow=False,
                text='STORAGE UTILIZATION (%)',
                font=dict(size=font_size_heading)
            ),
            dict(
                xref='paper',
                yref='paper',
                x=0.14444444444444446,
                y=0.375,
                xanchor='center',
                yanchor='bottom',
                showarrow=False,
                text='',
                font=dict(size=font_size_heading)
            ),
            dict(
                xref='paper',
                yref='paper',
                x=0.5,
                y=0.405,
                xanchor='center',
                yanchor='bottom',
                showarrow=False,
                text='Current Cluster Status',
                font=dict(size=font_size_heading)
            ),
            dict(
                xref='paper',
                yref='paper',
                x=0.8555555555555556,
                y=0.375,
                xanchor='center',
                yanchor='bottom',
                showarrow=False,
                text='',
                font=dict(size=font_size_heading)
            ),
            dict(
                xref='paper',
                yref='paper',
                x=0.14444444444444446,
                y=1,
                xanchor='center',
                yanchor='bottom',
                showarrow=False,
                text='CPU UTILIZATION (%)',
                font=dict(size=font_size_heading)
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
                font=dict(size=font_size_threshold)
            ),
            dict(
                xref='paper',
                yref='paper',
                x=0.63,
                y=0.75,
                xanchor='right',
                yanchor='bottom',
                showarrow=False,
                text='Threshold',
                font=dict(size=font_size_threshold)
            ),
            dict(
                xref='paper',
                yref='paper',
                x=1,
                y=0.75,
                xanchor='right',
                yanchor='bottom',
                showarrow=False,
                text='Threshold_Util',
                font=dict(size=font_size_threshold)
            )
        ],
        showlegend=True,
        xaxis=dict(
            domain=[0, 0.26],
            fixedrange=True,
            showline=True,
            showgrid=True
        ),
        xaxis2=dict(
            domain=[0.37, 0.63],
            showline=True,
            anchor='y2',
            fixedrange=True,

        ),
        xaxis3=dict(
            domain=[0.74, 1],
            showline=True,
            anchor='y3',
            fixedrange=True
        ),
        xaxis4=dict(
            domain=[0, 0.26],
            showline=True,
            anchor='y4',
            fixedrange=True
        ),
        xaxis5=dict(
            domain=[0.37, 0.63],
            showline=True,
            anchor='y5',
            fixedrange=True
        ),
        xaxis6=dict(
            domain=[0.74, 1],
            anchor='y6',
            showline=True,
            fixedrange=True
        ),
        yaxis=dict(
            domain=[0.6, 1],
            anchor='x',
            showline=True,
            range=[0,100],
            fixedrange=True,
            showgrid=True

        ),
        yaxis2=dict(
            domain=[0.6, 1],
            anchor='x2',
            showline=True,
            range = [0, 100],
            fixedrange=True
        ),
        yaxis3=dict(
            domain=[0.6, 1],
            anchor='x3',
            showline=True,
            range = [0, 100],
            fixedrange=True
        ),
        yaxis4=dict(
            domain=[0, 0.4],
            anchor='x4',
            showline=True,
            range = [0, 100],
            fixedrange=True
        ),
        yaxis5=dict(
            domain=[0, 0.4],
            anchor='x5',
            showline=True,
            range = [0, 100],
            fixedrange=True
        ),
        yaxis6=dict(
            domain=[0, 0.4],
            anchor='x6',
            showline=True,
            range = [0, 100],
            fixedrange=True
        )
    )
    config = {'displayModeBar':False, 'showLink':False}
    data = [traces[0], traces[1], traces[2], traces[3], traces[4], traces[5], traces[6], traces[7], traces[8], traces[9],trace_table]
    fig = go.Figure(data=data,layout=layout)
    plotly.offline.plot(fig, output_type='file', config=config)
    #print(code)

sys.stdout = open('subplot_ver2.txt','w')

draw_graph()
