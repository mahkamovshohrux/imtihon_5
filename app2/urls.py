from django.urls import path
from .views import (Listyangilik1,Listyangilik2,Detailyangilik1,
                    Detailyangilik2,Createyangilik1,Createyangilik2,
                    UpdateYangilik1,UpdateYangilik2,DeleteYangilik1,
                    DeleteYangilik2)

urlpatterns = [
    path('all_list1/', Listyangilik1.as_view()),
    path('all_list2/', Listyangilik2.as_view()),
    path('detail1/<int:id_y1>', Detailyangilik1.as_view()),
    path('detail2/<int:id_y2>', Detailyangilik2.as_view()),
    path("creat1/",Createyangilik1.as_view()),
    path("creat2/",Createyangilik2.as_view()),
    path('update1/<int:id_y1>', UpdateYangilik1.as_view()),
    path('update2/<int:id_y2>', UpdateYangilik2.as_view()),
    path('delete1/<int:id_y1>', DeleteYangilik1.as_view()),
    path('delete2/<int:id_y2>', DeleteYangilik2.as_view()),
    ]