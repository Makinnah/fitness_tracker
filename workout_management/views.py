from rest_framework import viewsets
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework.permissions import IsAuthenticated

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#The Viewset
from .models import Goal
from .serializers import GoalSerializer

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#Summary View
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from datetime import date
from .models import Activity

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def activity_summary(request):
    start = request.query_params.get('start_date', str(date.today()))
    end = request.query_params.get('end_date', str(date.today()))

    activities = Activity.objects.filter(user=request.user, date__range=[start, end])
    summary = activities.aggregate(
        total_distance=Sum('distance'),
        total_duration=Sum('duration'),
        total_calories=Sum('calories_burned')
    )

    return Response({
        "start_date": start,
        "end_date": end,
        "summary": summary
    })
#Goal Comparison View
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def goal_progress(request):
    start = request.query_params.get('start_date', str(date.today()))
    end = request.query_params.get('end_date', str(date.today()))

    goals = Goal.objects.filter(user=request.user, start_date__lte=end, end_date__gte=start)
    activities = Activity.objects.filter(user=request.user, date__range=[start, end])

    progress = activities.aggregate(
        total_distance=Sum('distance'),
        total_duration=Sum('duration'),
        total_calories=Sum('calories_burned')
    )

    results = []
    for goal in goals:
        achieved = False
        actual = None
        if goal.goal_type == 'distance':
            actual = progress['total_distance'] or 0
            achieved = actual >= goal.target_value
        elif goal.goal_type == 'duration':
            actual = progress['total_duration'] or 0
            achieved = actual >= goal.target_value
        elif goal.goal_type == 'calories':
            actual = progress['total_calories'] or 0
            achieved = actual >= goal.target_value

        results.append({
            "goal_type": goal.goal_type,
            "target": goal.target_value,
            "actual": actual,
            "achieved": achieved,
            "start_date": str(goal.start_date),
            "end_date": str(goal.end_date)
        })

    return Response({"progress": results})
