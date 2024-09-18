class TransactionRouter:
    transaction_route = {'transaction'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.transaction_route:
            return 'transaction_slave'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.transaction_route:
            return 'transaction_master'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.transaction_route or
            obj2._meta.app_label in self.transaction_route
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.transaction_route:
            return db == 'transaction_master'
        return None