from colors import Colors
from budgets import Budgets


class Projects:

    def __init__(self, name, duedate=None, company_name=None, company_hq=None, main_color=None, manager=None,
                 budget_value=None, budget_currency=None, status=None, maintenance_requested=None):
        self.name = name
        self.duedate = duedate
        self.company_name = company_name
        self.company_hq = company_hq
        self.main_color = Colors(main_color).hex_to_rgb()
        self.manager = manager
        self.budget_value = budget_value
        self.budget_currency = budget_currency
        self.status = status
        self.maintenance_requested = maintenance_requested
        try:
            self.budget_eur = Budgets(budget_value, budget_currency).calculate_budget_eur()
        except:
            self.budget_eur = None

    @staticmethod
    def get_object_from_dictionary(kwargs):
        return Projects(name=kwargs.get('name'), duedate=kwargs.get('duedate'), company_name=kwargs.get('company_name'),
                        company_hq=kwargs.get('company_hq'), main_color=kwargs.get('main_color'),
                        manager=kwargs.get('manager'), budget_value=kwargs.get('budget_value'),
                        budget_currency=kwargs.get('budget_currency'), status=kwargs.get('status'),
                        maintenance_requested=kwargs.get('maintenance_requested'))

    @staticmethod
    def get_projects_object_list(list_of_arguments, list_from_sql):
        projects_object_list = []
        dict_arguments_sql = {}
        for element in list_from_sql:
            for i in range(len(list_of_arguments)):
                dict_arguments_sql[list_of_arguments[i]] = element[i]
            project = Projects.get_object_from_dictionary(dict_arguments_sql)
            projects_object_list.append(project)
        return projects_object_list
