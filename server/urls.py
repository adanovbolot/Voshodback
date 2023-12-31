from django.urls import path
from . import views


urlpatterns = [
    path('api/v1/user/create/', views.EvotorUsersCreate.as_view()),
    path('installation/event/', views.EvotorUsersDelete.as_view()),
    path('user/verify/', views.EvotorUsersAuth.as_view()),
    path('api/v1/user/token/', views.EvotorTokenCreate.as_view()),
    path('evotor/operators/', views.EvotorOperatorView.as_view()),
    path('shops/', views.ShopsCreateOrUpdateView.as_view()),
    path('shops/inventories/search/', views.ShopsView.as_view()),
    path('terminals/inventories/search/', views.TerminalView.as_view()),
    path('product/inventories/search/', views.ProductView.as_view()),
    path('product/create/inventories/', views.ProductCreate.as_view()),
    path('api/v2/receipts/', views.ReceiptView.as_view()),
    path('api/v1/inventories/employees', views.TerminalUserCreatePutView.as_view()),
    path('api/v1/inventories/devices', views.TerminalCreatePutView.as_view()),
    path('api/v1/inventories/stores', views.AddressCreatePutView.as_view()),
    path('product/create/', views.ProductCategoryList.as_view()),
    # path('test/', views.ProductCategoryList.as_view()),
    path('product/list/create/', views.ProductCreateView.as_view()),
    path('product/category/get/', views.ProductListView.as_view()),
]
