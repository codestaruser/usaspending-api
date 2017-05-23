import random

# Simple router to randomly choose between reading from the source or read replicas


class ReadReplicaRouter(object):

    def db_for_read(self, model, **hints):
        if (model.__name__ == 'RequestCatalog'):
            return 'db_req_catalog'
        return random.choice(['db_r1', 'db_r2'])

    def db_for_write(self, model, **hints):
        if (model.__name__ == 'RequestCatalog'):
            return 'db_req_catalog'
        return 'db_source'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'requestcatalog' and db == 'db_req_catalog':
            return True
        if model_name != 'requestcatalog' and db == 'db_source':
            return True
        return False
