class AuthRouter:
    auth_route = {'account', 'auth', 'contenttypes', 'sessions', 'admin', 'utils'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.auth_route:
            return 'default_slave'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.auth_route:
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.auth_route or
            obj2._meta.app_label in self.auth_route
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.auth_route:
            return db == 'default'
        return None


# class UtilsRouter:
#
#     utils_route = {'utils', }
#
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.utils_route:
#             return 'utility_slave'
#         return None
#
#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.utils_route:
#             return 'utility_master'
#         return None
#
#     def allow_relation(self, obj1, obj2, **hints):
#         if (
#             obj1._meta.app_label in self.utils_route or
#             obj2._meta.app_label in self.utils_route
#         ):
#            return True
#         return None
#
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.utils_route:
#             return db == 'utility_master'
#         return None