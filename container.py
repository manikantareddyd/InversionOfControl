class Container:
    def __init__(self):
        self.registered_components = []
        self.registered_components_names = []

    def add_component(self,component):
        self.registered_components.append(component)
        self.registered_components_names.append(component.__name__)
    
    def resolve(self,component):
        print self.registered_components_names
        dependencies = component.__init__.__code__.co_varnames[1:]
        dependency_keys = []
        for dependency in dependencies:
            if dependency not in self.registered_components_names:
                print "Dependency,",dependency,", not found"
                exit(0)
            dependency_keys.append(self.registered_components_names.index(dependency))
        dependency_methods = [self.registered_components[key] for key in dependency_keys]
        return component(*dependency_methods)
        
