class Group:

    def __init__(self, name=None, description=None, other=None, id=None):
        self.name = name
        self.description = description
        self.other = other
        self.id = id


    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
