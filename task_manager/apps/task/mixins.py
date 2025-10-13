from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib import messages

class AuthorRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        task = self.get_object()
        return task.author == self.request.user
    
    def handle_no_permission(self):
        messages.error(self.request, 'Only task author can delete this task')
        return redirect('task_list')