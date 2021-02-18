import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render

from products.forms import PurchaseForm
from products.models import Product, Purchase
# Create your views here.
import matplotlib.pyplot as plt
import seaborn as sns
from products.utils import get_salesman_from_id, get_simple_plot, get_image


def sales_dist_view(request):
    df = pd.DataFrame(Purchase.objects.all().values())
    # print(df)
    df['salesman_id'] = df['salesman_id'].apply(get_salesman_from_id)
    df.rename({'salesman_id': 'salesman'}, axis=1, inplace=True)
    df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
    # print(df)
    plt.switch_backend('Agg')
    plt.xticks(rotation=45)
    sns.barplot(x='date', y='total_price', hue='salesman', data=df)
    plt.tight_layout()
    graph = get_image()

    context = {
        'graph': graph,
    }

    return render(request, 'products/sales.html', context)


def chart_select_view(request):
    graph = None
    error_message = None
    df = None
    price = None

    try:
        product_df = pd.DataFrame(Product.objects.all().values())
        purchase_df = pd.DataFrame(Purchase.objects.all().values())
        product_df['product_id'] = product_df['id']

        if purchase_df.shape[0] > 0:
            df = pd.merge(purchase_df, product_df, on='product_id').drop(['id_y', 'date_y'], axis=1).rename(
                {'id_x': 'id', 'date_x': 'date'}, axis=1)
            price = df['price']
            if request.method == 'POST':
                chart_type = request.POST.get('sales')
                date_from = request.POST['date_from']
                date_to = request.POST['date_to']

                df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))

                df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
                if chart_type != '':
                    if date_from != '' and date_to != '':
                        df = df[(df['date'] > date_from) & (df['date'] < date_to)]
                        df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
                    # function to get a graph
                    graph = get_simple_plot(chart_type, x=df2['date'], y=df2['total_price'], data=df)
                else:
                    error_message = 'Please select chart type'

        else:
            error_message = 'No record in database'

    except:
        product_df = None,
        purchase_df = None
        error_message = 'No record in database'

    context = {
        'error_message': error_message,
        'products': product_df.to_html(),
        'purchase': purchase_df.to_html(),
        'df': df.to_html(),
        'graph': graph,
        'price': price,
    }
    return render(request, 'products/main.html', context)


def add_purchase_view(request):
    form = PurchaseForm(request.POST or None)
    added_message = None

    if form.is_valid():
        obj = form.save(commit=False)
        obj.salesman = request.user
        obj.save()

        form = PurchaseForm()
        added_message = 'The purchase has been added'

    context = {
        'form': form,
        'added_message': added_message,
    }
    return render(request, 'products/add.html', context)
