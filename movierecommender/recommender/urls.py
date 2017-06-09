from django.conf.urls import url
from . import recommendations

urlpatterns=[
url(r'^$',recommendations.recommend,name='recommendations')
]