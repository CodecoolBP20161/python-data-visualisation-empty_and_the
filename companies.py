from colors import Colors


class Companies:

    def __init__(self, name, number_of_projects=None, avg_color=None):
        self.name = name
        self.number_of_projects = number_of_projects
        self.avg_color = avg_color

    @staticmethod
    def get_object_from_dictionary(kwargs):
        return Companies(name=kwargs.get('name'), number_of_projects=kwargs.get('number_of_projects'),
                         avg_color=kwargs.get('avg_color'))

    @staticmethod
    def get_companies_object_list(list_of_arguments, list_from_sql):
        for element in list_from_sql:
            element[2] = Colors.get_avg_color(element[2])
        companies_object_list = []
        dict_arguments_sql = {}
        for element in list_from_sql:
            for i in range(len(list_of_arguments)):
                dict_arguments_sql[list_of_arguments[i]] = element[i]
            company = Companies.get_object_from_dictionary(dict_arguments_sql)
            companies_object_list.append(company)
        return companies_object_list
