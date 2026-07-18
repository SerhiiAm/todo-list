from django.views import generic
from .models import Task, Tag


class IndexView(generic.TemplateView):
    template_name = "tasks/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["tasks_list"] = Task.objects.all()

        context["num_tags"] = Tag.objects.count()
        context["num_tasks"] = Task.objects.count()

        num_visits = self.request.session.get("num_visits", 0) + 1
        self.request.session["num_visits"] = num_visits
        context["num_visits"] = num_visits

        return context
