from app import mongo

class User(mongo.Model):
    username = mongo.StringProperty(required = True)
    pw_hash = mongo.StringProperty(required = True)
    email = mongo.StringProperty()

    @classmethod
    def by_id(cls, uid):
        return cls.get_by_id(uid)