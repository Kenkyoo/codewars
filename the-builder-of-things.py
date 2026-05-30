class Thing(object):
    def __init__(self, name=""):
        self.name = name
        self._boolean_properties = {}
        self._methods = {}
        self._methods_archive = {}
        self._method_archives = {}

    def __getattr__(self, name):
        if name == "is_a":
            return BooleanProxy(self, True)

        if name == "is_not_a":
            return BooleanProxy(self, False)

        if name in ("is_the", "being_the", "and_the"):
            return IsTheProxy(self)

        if name == "can":
            return CanProxy(self)

        if name.startswith("is_a_"):
            return self._boolean_properties.get(name[5:], False)

        if name.startswith("is_not_a_"):
            return not self._boolean_properties.get(name[9:], False)

        if name.startswith("is_"):
            expected_name = name[3:]
            return self.name == expected_name

        if name in self._methods:
            def dynamic_method(*args, **kwargs):
                result = self._methods[name](self, *args, **kwargs)

                archive_name = self._method_archives.get(name)
                if archive_name:
                    self._methods_archive[archive_name].append(result)

                return result

            return dynamic_method

        if name in self._methods_archive:
            return self._methods_archive[name]

        raise AttributeError(
            f"'{type(self).__name__}' object has no attribute '{name}'"
        )

    def has(self, count):
        return HasProxy(self, count)

    def having(self, count):
        return self.has(count)

class ThingList(Thing, tuple):
    def __new__(cls, name, items):
        return super(ThingList, cls).__new__(cls, items)

    def __init__(self, name, items):
        Thing.__init__(self, name)

    def __getattr__(self, name):
        if name.startswith("is_"):
            return self.name == name[3:]
        return Thing.__getattr__(self, name)

    def each(self, callback):
        for item in self:
            callback(item)
        return self

class BooleanProxy(object):
    def __init__(self, thing, value):
        self.thing = thing
        self.value = value

    def __getattr__(self, name):
        self.thing._boolean_properties[name] = self.value
        return self.thing


class IsTheProxy(object):
    def __init__(self, thing):
        self.thing = thing

    def __getattr__(self, name):
        return PropertyAssignerProxy(self.thing, name)


class PropertyAssignerProxy(object):
    def __init__(self, thing, property_name):
        self.thing = thing
        self.property_name = property_name

    def __getattr__(self, value_name):
        setattr(self.thing, self.property_name, value_name)
        return self.thing


class HasProxy(object):
    def __init__(self, thing, count):
        self.thing = thing
        self.count = count

    def __getattr__(self, name):
        if self.count == 1:
            new_thing = Thing(name)
            setattr(self.thing, name, new_thing)
            return new_thing
        else:
            singular_name = name[:-1] if name.endswith('s') else name
            items = [Thing(singular_name) for _ in range(self.count)]
            thing_list = ThingList(name, items)
            setattr(self.thing, name, thing_list)
            return thing_list


class CanProxy(object):
    def __init__(self, thing):
        self.thing = thing

    def __getattr__(self, method_name):
        def register_method(func, archive=None):
            self.thing._methods[method_name] = func

            if archive:
                self.thing._methods_archive[archive] = []
                self.thing._method_archives[method_name] = archive

            return self.thing

        return register_method