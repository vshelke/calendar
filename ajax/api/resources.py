from tastypie.resources import ModelResource
from ajax.models import Event


class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        allowed_methods = ['get']
