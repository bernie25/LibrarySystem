import functools
from abc import ABC, abstractmethod

from django.conf import settings
from django.db.models import Model
from django.forms import ModelForm, ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import CreateView


class BaseCreateView(CreateView, ABC):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None
        self.form = None

    @abstractmethod
    def save_model_instance(self) -> Model:
        pass

    def form_valid(self, form: ModelForm):
        self.object = form.save(commit=False)
        self.form = form
        try:
            self.object = self.save_model_instance()
        except (ValidationError, ValueError) as ex:
            form.add_error(None, ex.message)
            return self.render_to_response(self.get_context_data(form=form))
        return HttpResponseRedirect(self.get_success_url())


def auth_required():
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(self, *args, **kwargs):
            if not self.request.user.is_authenticated:
                return redirect('%s?next=%s' % (settings.LOGIN_URL, self.request.path))
            return fn(self, *args, **kwargs)
        return wrapper

    return decorator