import json
from copy import deepcopy
from .types_constraintes import *

class Checker:
    def __init__(self):
        self.template = None
        self.config   = None


    def __load_json_file(self, json_file):
        with open(json_file, mode = "r", encoding = "utf8") as f:
            data = json.load(f)

        return data
    

    def load_template(self, template_path):
        self.template = self.__load_json_file(template_path)

        # Check template
        error = []
        self.__check_template(deepcopy(self.template), [], error)

        return error


    def __check_template(self, template, root, error, last_key = None):
        """
        Recursive function
        """
        if last_key != None:
            root.append(last_key)

        # Break point
        if template == {}:
            return
        
        for key in template:
            if "type" in template[key]:
                # Check type
                type_ = template[key].pop("type")

                if not type_ in TYPES:
                    error.append({"error_type": "unknown type", "parameter": key, "root": root})
                    return

                # Check constraints
                for constraint in template[key]:
                    if not constraint in CONSTRAINTS[type_]:
                        error.append({"error_type": "unknown constraint", "parameter": key, "unknown constrait": constraint, "root": root})
                        return
            else:
                self.__check_template(template[key], root.copy(), error, key)


    def check_config(self, config_path):
        self.config = self.__load_json_file(config_path)

        # Check template
        error = []
        self.__check_config(self.config, [], error)

        return error

    
    def __check_config(self, config, root, error, last_key = None):
        """
        Recursive function
        """
        if last_key != None:
            root.append(last_key)

        # Break point
        if config == {}:
            return

        for key in config:
            type_ = type(config[key])

            if type_ != dict:
                # Check constraints
                template_tmp = self.template

                for section in root:
                    if not section in template_tmp:
                        error.append({"error_type": "unknown section", "section": section, "root": root})
                        return
                    
                    template_tmp = template_tmp[section]

                # Check type
                if not CONSTRAINTS["is_same_type"](type_, MATCH_TYPES[template_tmp[key]["type"]]):
                    error.append({"error_type": "parameter's type is not correct",
                                  "expected_type": MATCH_TYPES[template_tmp[key]["type"]], 
                                  "actual type": type_,
                                  "root": root})
                    return

                type_ =  template_tmp[key].pop("type")
                for constraint in template_tmp[key]:
                    if not CONSTRAINTS[type_][constraint](config[key], template_tmp[key][constraint]):
                        error.append({"error_type": "constraint not respected",
                                  "parameter": key, 
                                  "parameter value": config[key],
                                  "constraint": constraint,
                                  "constraint value": template_tmp[key][constraint],
                                  "root": root})
                        return
            else:
                self.__check_config(config[key], root.copy(), error, key)