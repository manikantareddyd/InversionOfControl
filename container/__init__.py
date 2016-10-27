class Container:
    def __init__(self):
        # This list will hold the methods being registered
        self.registered_methods = []
        # This list holds corresponding dependency which the method being registered satisfies
        self.registered_methods_names = []

    def add_method(self,module,method_name,dependency_name):
        # if a dependency has already been registered, its a clash
        if dependency_name in self.registered_methods_names:
            print "A method for",dependency_name,"has already been registered as",self.registered_methods[self.registered_methods_names.index(dependency_name)].__name__
            print "Please check for multiple registrations and clashes. Only a single function can be registered for a dependency."
            exit(0)

        # import the module in which the method to be registered is presetn
        m = __import__ (module)
        method = getattr(m,method_name)
        # method is now a complete method. You can probably call is as method(args)
        if type(method).__name__ == 'function':
            self.registered_methods.append(method)
            self.registered_methods_names.append(dependency_name)
        else:
            # if the method is not a function, we don't register
            print "Unknown Type of method",method.__name__
            print "Not understood:",type(method).__name__
            print "Only methods of type 'function' are allowed to be registered"
            exit(0)
    
    def resolve(self,required_class):
        if type(required_class).__name__ == 'classobj':
            # we resolve only classes and return their objects
            dependencies = required_class.__init__.__code__.co_varnames[1:]
        else:
            print "Unknown Type of required_class",required_class.__name__
            print "Not understood:",type(required_class).__name__
            print "Only required_class's of type 'classobj' are allowed to be resolved"
            exit(0)
        
        dependency_methods = []
        for dependency in dependencies:
            if dependency not in self.registered_methods_names:
                print "Dependency,",dependency,", not registered"
                exit(0)
            dependency_methods.append(self.registered_methods[self.registered_methods_names.index(dependency)])
        # An instance of class is being created, with all the dependencies
        required_object = required_class(*dependency_methods)
        return required_object

    def register_from_config(self):
        with open("config.json") as json_file:
            import simplejson as json
            for entry in json.load(json_file):
                self.add_method(module=entry["module"],method_name=entry["method_name"],dependency_name=entry["dependency_name"])