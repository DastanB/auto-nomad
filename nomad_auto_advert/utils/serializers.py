from rest_framework import serializers


class MultiSerializerViewSetMixin(object):
    def get_serializer_class(self):
        """
        Look for serializer class in self.serializer_action_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:

        class MyViewSet(MultiSerializerViewSetMixin, ViewSet):
            serializer_class = MyDefaultSerializer
            serializer_action_classes = {
               'list': MyListSerializer,
               'my_action': MyActionSerializer,
            }

            @action
            def my_action:
                ...

        If there's no entry for that action then just fallback to the regular
        get_serializer_class lookup: self.serializer_class, DefaultSerializer.
        """
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError) as e:
            try:
                return self.serializer_action_classes[self.request.method]
            except KeyError as e:
                if self.request.method == 'PATCH':
                    try:
                        return self.serializer_action_classes['GET']
                    except KeyError:
                        try:
                            return self.serializer_action_classes['list']
                        except KeyError:
                            raise AttributeError
            except AttributeError:
                return super(MultiSerializerViewSetMixin, self).get_serializer_class()


class ChoiceValueDisplayField(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data

    def get_attribute(self, instance):
        try:
            attr = self.source
            display_method = getattr(instance, 'get_%s_display' % attr)

            value = getattr(instance, attr)
            display_value = display_method()

            return {
                'value': value,
                'display': display_value
            }
        except Exception as e:
            print(e)
            return super(ChoiceValueDisplayField, self).get_attribute(instance)
