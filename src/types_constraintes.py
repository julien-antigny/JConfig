TYPES = {"int","float","str","bool","list"}

CONSTRAINTS = {
    "int" :{
        "is_int":    lambda x: type(x) == int,

        "min_inc":   lambda integer, min: integer >= min,
        "min_exc":   lambda integer, min: integer >  min,
        "max_inc":   lambda integer, max: integer >= max,
        "max_exc":   lambda integer, max: integer >  max,

        "value_in":  lambda integer, value_in: integer in value_in,
        "value_out": lambda integer, value_out: not integer in value_out
    },
    "float": {
        "is_float":  lambda x: type(x) == float,

        "min_inc":   lambda integer, min: integer >= min,
        "min_exc":   lambda integer, min: integer >  min,
        "max_inc":   lambda integer, max: integer >= max,
        "max_exc":   lambda integer, max: integer >  max,

        "value_in":  lambda float_, value_in: float_ in value_in,
        "value_out": lambda float_, value_out: not float_ in value_out
    },
    "str": {
        "is_str":    lambda x: type(x) == str,
        "value_in":  lambda string, value_in: string in value_in,
        "value_out": lambda string, value_out: not string in value_out
    },
    "list": {
        "equal_len": lambda list_, len_: len(list_) == len_,
        "min_len"  : lambda list_, min_len: len(list_) >= min_len,

        "min_inc": lambda list_, min: all(x >= min for x in list_),
        "min_exc": lambda list_, min: all(x >  min for x in list_),
        "max_inc": lambda list_, max: all(x <= max for x in list_),
        "max_exc": lambda list_, max: all(x >  max for x in list_)
    }
}


CONSTRAINT_CHECKS = {
    "int" :{
        "min_inc":   lambda min: type(min) in [int, float],
        "min_exc":   lambda min: type(min) in [int, float],
        "max_inc":   lambda max: type(max) in [int, float],
        "max_exc":   lambda max: type(max) in [int, float],
        
        "value_in":  lambda value_in:  all([type(value) == int for value in value_in]),
        "value_out": lambda value_out: all([type(value) == int for value in value_out])
    },
    "float": {
        "min_inc":   lambda min: type(min) in [int, float],
        "min_exc":   lambda min: type(min) in [int, float],
        "max_inc":   lambda max: type(max) in [int, float],
        "max_exc":   lambda max: type(max) in [int, float],

        "value_in":  lambda value_in:  all([type(value) in [int,float] for value in value_in]),
        "value_out": lambda value_out: all([type(value) in [int,float] for value in value_out])
    },
    "str": {
        "value_in":  lambda value_in:  all([type(value) == str for value in value_in]),
        "value_out": lambda value_out: all([type(value) == str for value in value_out])
    },
    "list": {
        "equal_len": lambda len_: type(len_) == int and len_ > 0,
        "min_len"  : lambda min: type(min) == int and min >= 0,

        "min_inc": lambda min: type(min) in [int,float],
        "min_exc": lambda min: type(min) in [int,float],
        "max_inc": lambda max: type(max) in [int,float],
        "max_exc": lambda max: type(max) in [int,float],
    }
}
