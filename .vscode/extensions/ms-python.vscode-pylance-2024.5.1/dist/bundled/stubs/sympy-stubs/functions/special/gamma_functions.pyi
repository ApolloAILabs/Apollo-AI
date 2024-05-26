from sympy.core.function import Function, UndefinedFunction

def intlike(n) -> bool:
    ...

class gamma(Function):
    unbranched = ...
    _singularities = ...
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, arg) -> type[UndefinedFunction] | None:
        ...
    


class lowergamma(Function):
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, a, x) -> type[UndefinedFunction] | None:
        ...
    


class uppergamma(Function):
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, a, z):
        ...
    


class polygamma(Function):
    @classmethod
    def eval(cls, n, z) -> type[UndefinedFunction] | None:
        ...
    
    def fdiff(self, argindex=...) -> polygamma:
        ...
    


class loggamma(Function):
    @classmethod
    def eval(cls, z) -> type[UndefinedFunction] | None:
        ...
    
    def fdiff(self, argindex=...) -> type[UndefinedFunction]:
        ...
    


class digamma(Function):
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, z) -> type[UndefinedFunction]:
        ...
    


class trigamma(Function):
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, z) -> type[UndefinedFunction]:
        ...
    


class multigamma(Function):
    unbranched = ...
    def fdiff(self, argindex=...):
        ...
    
    @classmethod
    def eval(cls, x, p):
        ...
    


