from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.pagination import HabitPaginator
from habits.serializer import HabitSerializer
from users.permissions import IsModer, IsOwner


class HabitViewSet(ModelViewSet):
    """ViewSet для управления привычками"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [
        AllowAny,
    ]

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.User = self.request.user
        habit.save()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (~IsModer,)
        elif self.action in ["update", "retrieve"]:
            self.permission_classes = (IsModer | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (~IsModer | IsOwner,)
        return super().get_permissions()

class PublicHabitListAPIView(ListAPIView):
    """ViewSet списка публичных привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_published=True)
    pagination_class = HabitPaginator