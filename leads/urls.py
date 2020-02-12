from django.contrib import admin
from django.urls import path,include
from leads.api import LeadViewset
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/leads',LeadViewset,'leads')



urlpatterns = router.urls