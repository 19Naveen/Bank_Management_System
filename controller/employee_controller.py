from dao.employee_dao import EmployeeDao
from models.employee import Employee
from service.session_state import SessionState

class EmployeeController:
    def __init__(self, EmployeeDAO: EmployeeDao, Session_state: SessionState):
        self.employee_dao = EmployeeDAO
        self.session_state = Session_state

    def authenticate(self, email: str, password: str) -> bool:
        res = self.employee_dao.authenticate(email, password)
        if res:
            self.session_state.set_current_user(res[0])
            return True
        else:
            return False
    
    def employee_details(self) -> Employee:
        return Employee(*self.employee_dao.get_employee_details(self.session_state.get_current_user()))
