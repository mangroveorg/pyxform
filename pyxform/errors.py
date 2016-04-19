class PyXFormError(Exception):
    pass


class ValidationError(PyXFormError):
    pass


class BindError(PyXFormError):

    def __init__(self, field, attribute, message):
        self.field = field
        self.attribute = attribute
        super(BindError, self).__init__(message)
