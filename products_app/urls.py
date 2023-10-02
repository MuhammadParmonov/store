from django.urls import path

from .views import product_view, profil_page, buyurtma_page, category_page

app_name = 'products' 

urlpatterns = [
    path('products/', product_view, name='product_view'),
    path('profile/', profil_page, name='profil_view'),
    path('buyurtmalar/', buyurtma_page, name='buyurtma_view'),
    path('category/<int:cat_id>', category_page, name='category-page')
]