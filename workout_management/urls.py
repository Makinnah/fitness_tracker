from .views import ActivityViewSet, GoalViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')

urlpatterns = [
    path('', include(router.urls)),
]

#Registering the new viewset
router.register(r'goals', GoalViewSet, basename='goal')

#URL Route
from .views import activity_summary

urlpatterns += [
    path('summary/', activity_summary, name='activity-summary'),
]


# 2nd URL Route
from .views import goal_progress

urlpatterns += [
    path('goal-progress/', goal_progress, name='goal-progress'),
]
