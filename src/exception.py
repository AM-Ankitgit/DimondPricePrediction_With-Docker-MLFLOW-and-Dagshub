import os
import sys


class CustomException(Exception):

    def __init__(self,error_message:str,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        self.line_number = exc_tb.tb_lineno
        self.filename    = exc_tb.tb_frame.f_code.co_filename
        self.error_message_in_details = "error occurred in script [{0}] in lineno [{1}] error message [{2}]".format(self.filename,self.line_number,str(self.error_message))

    def __str__(self):
        return self.error_message_in_details
