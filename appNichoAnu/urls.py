from django.conf.urls import include, url

from . import views, views_node_info1_4, views_edge_info1_2,  \
    views_add_node1_1, views_add_edge1_1, \
    views_del_node1_1, views_del_edge1_1

app_name = "appNichoAnu"

urlpatterns = [

    url(r'^node_info/node_vis_id=(?P<node_vis_id>[^@\s]+)$',
        views_node_info1_4.node_vis_id_info, name="node_vis_id_info"),   
    url(r'^node_info/node_vis_id=(?P<node_vis_id>\S+)@hwidth=(?P<hwidth>\d+)_hheight=(?P<hheight>\d+)_offx=(?P<offx>-?\d+)_offy=(?P<offy>-?\d+)$',
        views_node_info1_4.node_vis_id_info, name="node_vis_id_info"),  
    url(r'^edge_info/(?P<edge_id>\S+)$',
        views_edge_info1_2.edge_info, name="edge_info"),
    url(r'^del_node/(?P<node_vis_id>\S+)$',
        views_del_node1_1.del_node, name="del_node"),
    url(r'^del_edge/(?P<edge_id>\S+)$',
        views_del_edge1_1.del_edge, name="del_edge"),
    url(r'^add_node$',
        views_add_node1_1.add_node, name="add_node"),
    url(r'^add_edge$',
        views_add_edge1_1.add_edge, name="add_edge"),
    url(r'^$', views.index, name="index"),               
    url(r'^info_pub$', views.pub_db_tools, name="pub_db_tools"),  
    url(r'^survey$', views.survey, name="survey"),  
    url(r'^member$', views.member, name="member"),  
    url(r'^material_src$', views.material_src, name="material_src"),      
    url(r'^history$', views.history, name="history"),  
    url(r'^work_record$', views.work_record, name="work_record"), 
    url(r'^blog$', views.blog, name="blog"),  

#     url(r'^node_info/(?P<id>\S+)$',
#         views.node_info, name="node_info"),     
    
]
