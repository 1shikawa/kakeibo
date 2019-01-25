from django.urls import path
from . import views

app_name = 'kakeiboapp'

urlpatterns = [
    # 一覧表示
    path('kakeibo_list/', views.KakeiboListView.as_view(), name='kakeibo_list'),
    # データ登録
    path('kakeibo_create/', views.KakeiboCreateView.as_view(), name='kakeibo_create'),
    path('create_done/', views.create_done, name='create_done'),
    # データ更新
    path('kakeibo_update/<int:pk>/', views.KakeiboUpdateView.as_view(), name='kakeibo_update'),
    path('update_done/', views.update_done, name='update_done'),
    # データ削除
    path('kakeibo_delete/<int:pk>/', views.KakeiboDeleteView.as_view(), name='kakeibo_delete'),
    path('delete_done/', views.delete_done, name='delete_done'),
    # カテゴリ別割合の円グラフ
    path('circle/', views.show_circle_graph, name='kakeibo_circle'),
    # カテゴリ別チャート
    path('line/', views.show_line_grahp, name='kakeibo_line'),
]
