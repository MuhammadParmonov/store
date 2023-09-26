from django.urls import path

from .views import index_view, product_view, profil_page, buyurtma_page, category_page

urlpatterns = [
    path('', index_view, name='index_view'),
    path('products/', product_view, name='product_view'),
    path('profile/', profil_page, name='profil_view'),
    path('buyurtmalar/', buyurtma_page, name='buyurtma_view'),
    path('category/<int:cat_id>', category_page, name='category-page')
]