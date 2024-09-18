class FundsRouter:
    funds_route = {'deposits', 'loan'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.funds_route:
            return 'funds_slave'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.funds_route:
            return 'funds_master'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.funds_route or
            obj2._meta.app_label in self.funds_route
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.funds_route:
            return db == 'funds_master'
        return None