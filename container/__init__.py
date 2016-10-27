class Container:
    def __init__(self):
        self.registered_components = []
        self.registered_components_names = []

    def add_component(self,module,component_name,dependency_name):
        m = __import__ (module)
        component = getattr(m,component_name)
        if type(component).__name__ == 'function':
            self.registered_components.append(component)
            self.registered_components_names.append(dependency_name)
        else:
            print "Unknown Type of Component",component.__name__
            print "Not understood:",type(component).__name__
            print "Only components of type 'function' are allowed to be registered"
            exit(0)
        
    
    def resolve(self,component):
        if type(component).__name__ == 'classobj':
            dependencies = component.__init__.__code__.co_varnames[1:]
        else:
            print "Unknown Type of Component",component.__name__
            print "Not understood:",type(component).__name__
            print "Only components of type 'classobj' are allowed to be resolved"
            exit(0)
        dependency_keys = []
        for dependency in dependencies:
            if dependency not in self.registered_components_names:
                print "Dependency,",dependency,", not registered"
                exit(0)
            dependency_keys.append(self.registered_components_names.index(dependency))
        dependency_methods = [self.registered_components[key] for key in dependency_keys]
        return component(*dependency_methods)

    def register_from_config(self):
        with open("config.json") as json_file:
            import simplejson as json
            for entry in json.load(json_file):
                self.add_component(module=entry["module"],component_name=entry["component_name"],dependency_name=entry["dependency_name"])