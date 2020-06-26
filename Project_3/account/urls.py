from django.urls import path

from .views import UserAccountLoginView, UserAccountLogoutView, UserAccountUpdateView, CreateUserAccountView, \
    LeaderBoard

app_name = 'account'

urlpatterns = [

    path('register/', CreateUserAccountView.as_view(), name='registration'),
    path('login/', UserAccountLoginView.as_view(), name='login'),
    path('logout/', UserAccountLogoutView.as_view(), name='logout'),
    path('profile/', UserAccountUpdateView.as_view(), name='profile'),
    path('leaderboard/', LeaderBoard.as_view(), name='leaderboard'),

]
