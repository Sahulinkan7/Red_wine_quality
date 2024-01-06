import os,sys 

def error_message_details(error_message:str,error_details:sys):
        _, _,exc_tb=error_details.exc_info()
        file_name=exc_tb.tb_frame.f_code.co_filename
        
        error_message=f"""
        Error occurred in python file {file_name},
        line number {exc_tb.tb_lineno},
        the error message is "{str(error_message)}"
        
        """
        return error_message
    
class CustomException(Exception):
    def __init__(self,error_message,error_details):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_details)    
        
    def __str__(self) -> str:
        return self.error_message