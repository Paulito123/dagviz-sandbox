import graphviz
from graphviz import nohtml

import json

g = graphviz.Digraph('arg1', filename='arg1.gv')
g.attr(compound='true', ranksep='1')


def vertaal_kleur(status_code):
    if status_code == 0:
        kleur = 'grey'
    elif status_code == 1:
        kleur = 'orange'
    elif status_code == 2:
        kleur = 'green'
    else:
        kleur = 'red'
    return kleur


with open('input/iws_v1.json') as f:
    data = json.load(f)

    if 'job_streams' in data:
        # iterate streams
        for stream_key in data['job_streams'].keys():
            with g.subgraph(name=f'cluster_{stream_key}') as c:
                c.attr(style='filled', color='lightblue', label=stream_key)
                c.node_attr.update(style='filled', color='grey', shape='record', height='.1')
                # iterate jobs
                if 'jobs' in data['job_streams'][stream_key]:
                    edges = []
                    for job_key in data['job_streams'][stream_key]['jobs'].keys():
                        
                        status_code = -1
                        kleur = 'grey'
                        odi_object_name = 'UNKNOWN'
                        if 'jobs' in data and job_key in data['jobs']:
                            if 'status' in data['jobs'][job_key]:
                                status_code = data['jobs'][job_key]['status']
                                kleur = vertaal_kleur(status_code)
                            if 'odi_object_name' in data['jobs'][job_key]:
                                odi_object_name = data['jobs'][job_key]['odi_object_name']
                        
                        c.node(f'struct_{job_key}', '''<
                            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
                                <TR>
                                    <TD bgcolor="''' + kleur + '''" PORT="f0">''' + job_key + '''</TD>
                                </TR>
                                <TR>
                                    <TD PORT="f1">''' + odi_object_name + '''</TD>
                                </TR>
                            </TABLE>>''')
                        
                        if 'preceded_by' in data['job_streams'][stream_key]['jobs'][job_key]:
                            edge = (f"struct_{data['job_streams'][stream_key]['jobs'][job_key]['preceded_by']}", f'struct_{job_key}')
                            edges.append(edge)

                    c.edges(edges)

# g.edge('cluster_jobStream_1', 'cluster_jobStream_2')
# g.edge('struct_job3', 'struct_job4', ltail='cluster_jobStream_1', lhead='cluster_jobStream_2')
g.edge('struct_job5', 'struct_job6', ltail='cluster_jobStream_2', lhead='cluster_jobStream_3')

g.view()
        
        

# s.node('struct1', '''<
# <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
#   <TR>
#     <TD>left</TD>
#     <TD PORT="f1">middle</TD>
#     <TD PORT="f2">right</TD>
#   </TR>
# </TABLE>>''')

# s.node('struct2', '''<
# <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
#   <TR>
#     <TD PORT="f0">one</TD>
#     <TD>two</TD>
#   </TR>
# </TABLE>>''')

# s.node('struct3', '''<
# <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">
#   <TR>
#     <TD ROWSPAN="3">hello<BR/>world</TD>
#     <TD COLSPAN="3">b</TD>
#     <TD ROWSPAN="3">g</TD>
#     <TD ROWSPAN="3" bgcolor="#00CC11">h</TD>
#   </TR>
#   <TR>
#     <TD>c</TD>
#     <TD PORT="here">d</TD>
#     <TD>e</TD>
#   </TR>
#   <TR>
#     <TD COLSPAN="3">f</TD>
#   </TR>
# </TABLE>>''')

# s.edges([('struct1:f1', 'struct2:f0'), ('struct1:f2', 'struct3:here')])

# s.view()