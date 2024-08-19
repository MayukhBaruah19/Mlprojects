import sys
import logging

def error_massage_Details(error,error_details:sys):
    file_name=exc.tb.tb_frame.f_code.co_filename
    _,_,exe_tb=error_details.exc_info()
    error_massage="Error occured i python script name [{0}] error massage [{2}]".format(
    file_name.exc_tb.tb.lineno,str(error)
    )    
    return error_massage  
    

class CustomException(Exception) :
    def __init__(self,error_massage,error_details:sys) :
        super().__init__(error_massage)  
        self.error_massage=error_massage_Details(error_massage,error_details=error_details)

    def __str__(self):
        return self.error_massage


           

