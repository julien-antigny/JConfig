from os.path import exists
from .utils import load_json_file
from .types_constraintes import *

class Checker:
    def __init__(self, template):
        self.template = None
        self.config   = None

        self.template_param = None
        self.config_param   = None

        # Load template
        self.load_template(template)


    def load_template(self, template):
        # Load template
        self.template = load_json_file(template)

        # We get the parameters from template
        self.template_param = dict()
        self.__get_parameters_from_template(self.template)
        print("Parameters from template found : ", " / ".join(list(self.template_param.keys())))

        # Check template parameters
        if not self.__check_parameters_template():
            print("=> template file is not valid")
            self.template_param = None
            return

    
    def check_config(self, config):
        if self.template_param == None:
            print("There is not template loaded")
            return 1

        if type(config) != str or not exists(config):
            print("Configuration file is not valid")
            return 1
        
        # Load config
        self.config = load_json_file(config)

        # We get the parameters from configuration
        self.config_param = dict()
        self.__get_parameters_from_config(self.config)
        print("Parameters from configuration found : ", " / ".join(list(self.config_param.keys())))

        # Check configuration
        if not self.__check_parameters_config():
            print("=> Configuration file is not valid")
            return False
        
        return True
    

    def __get_parameters_from_template(self, template):
        """
        Get paramaters from template (recursive function).
        """
        # Break point
        if template == {}:
            return
        
        for key in template.keys():
            if "type" in template[key]:
                self.template_param.update({key: template[key]})
            else:
                self.__get_parameters_from_template(template[key])


    def __get_parameters_from_config(self, config):
        """
        Get parameters from configuration (recursive function)

        Args:
            config (dict): Dictionnary of configuration file.
        """
         # Break point
        if config == {}:
            return

        for key in config.keys():
            if key in self.template_param:
                self.config_param.update({key: config[key]})
            else:
                self.__get_parameters_from_config(config[key])


    def __check_parameters_template(self):
        """
        Check if parameters from template are valid.

        Returns:
            bool: True if parameters are valid else False.
        """
        for parameter in self.template_param.keys():
            if not self.__check_parameter(self.template_param[parameter]):
                print(f"=> {parameter} parameter is not valid")
                return False

        return True

    
    def __check_parameters_config(self):
        """
        Check if parameters from configuration file are valid.

        Returns:
            bool: True if configuration is valid else False.
        """
        for key in self.config_param.keys():
            # We get the parameter type
            type_ = self.template_param[key]["type"]

            for constraints in self.template_param[key]:
                if constraints in ["type", "default"]:
                    continue

                if not CONSTRAINTS[type_][constraints](self.config_param[key], self.template_param[key][constraints]):
                    print(f"The {constraints} constraint on {key} parameter is not respected")
                    return False

        return True


    def __check_parameter(self, parameter):
        """
        Check if parameter is valid.

        Args:
            parameter (dict): Type, constraints and default value (optional) of parameter.

        Returns:
            bool: True if parameter is valid else False.
        """
        # We get the type of parameter
        type_ = parameter["type"]

        # We check the constraints
        for key in parameter.keys():
            if key == "type":
                if not parameter["type"] in TYPES:
                    print("Type of parameter is not valid")
                    return False
                continue

            if key == "default":
                continue

            if not key in CONSTRAINTS[type_]:
                print(f"The {key} constraint is not valid")
                return False

            if not CONSTRAINT_CHECKS[type_][key](parameter[key]):
                print("Value of constraint is not correct")
                return False

        return True
