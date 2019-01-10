from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Category, Kakeibo
from .forms import KakeiboForm
from django.urls import reverse_lazy
from django.db.models import Sum


class KakeiboListView(ListView):
    model = Kakeibo
    template_name = 'kakeiboapp/kakeibo_list.html'

    # 家計簿テーブルの全データを取得するメソッドを定義
    def queryset(self):
        return Kakeibo.objects.all()


class KakeiboCreateView(CreateView):
    model = Kakeibo
    form_class = KakeiboForm
    success_url = reverse_lazy('kakeiboapp:create_done')


def create_done(request):
    return render(request, 'kakeiboapp/create_done.html')


class KakeiboUpdateView(UpdateView):
    model = Kakeibo
    form_class = KakeiboForm
    success_url = reverse_lazy('kakeiboapp:update_done')


def update_done(request):
    return render(request, 'kakeiboapp/update_done.html')


class KakeiboDeleteView(DeleteView):
    model = Kakeibo
    success_url = reverse_lazy('kakeiboapp:delete_done')
    # テンプレートは内部的に、[モデル名]_confirom_delete.html 使用


def delete_done(request):
    return render(request, 'kakeiboapp/delete_done.html')


def show_circle_graph(request):
    # 全データ取得
    kakeibo_data = Kakeibo.objects.all()

    # 全ての金額の合計を求める
    total = 0
    for item in kakeibo_data:
        total += item.money

    category_list = []
    # 全カテゴリ名をテーブルから取得する。
    category_data = Category.objects.all()
    # ループ処理でカテゴリ名のリストを作成する。
    for item in category_data:
        category_list.append(item.category_name)

    # カテゴリ毎の合計金額を求める
    category_dict = {}
    for i, item in enumerate(category_list):
        category_total = Kakeibo.objects.filter(category__category_name=category_list[i]) \
            .aggregate(sum=Sum('money'))['sum']
        # カテゴリ毎の割合を求める
        if category_total != None:
            ratio = int((category_total / total) * 100)
            category_dict[item] = ratio
        else:
            ratio = 0
            category_dict[item] = ratio

    return render(request, 'kakeiboapp/kakeibo_circle.html', {
        'category_dict': category_dict,
    })
