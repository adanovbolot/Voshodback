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
    path('api/v1/inventories/employees', views.TerminalUserUpdateView.as_view()),
]
