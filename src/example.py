from .checker import Checker

template_path   = "example/template.json"
conf_valid_path = "example/config_valid.json"
conf_error_path = "example/config_with_error.json"

checker = Checker(template_path)
error = checker(conf_valid_path)
print(error)
error = checker(conf_error_path)
print(error)