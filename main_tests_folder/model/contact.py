from sys import maxsize

class Contact:

    def __init__(self,name=None, middle_name=None, last_name=None, nickname=None, company=None, address=None, home=None,
                            phone=None, work=None, email=None, id=None):
        self.name = name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home = home
        self.phone = phone
        self.work = work
        self.email = email
        self.id = id


    def __repr__(self):
        return "%s:%s" % (self.id, self.name)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize