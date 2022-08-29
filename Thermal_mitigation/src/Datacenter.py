from PySide6.QtCore import (QObject, Signal)
from datetime import datetime


class data_signal(QObject):
    
    setlpm_changed = Signal(str)
    gettmu_changed = Signal(list)

    def __init__(self):
        super().__init__()
        
        self.join_data = []
        self.received_data = []
        self.emit_loop = True
        self.emit_time = ''
        self.delay_time = ''       


    def setlpm_output(self, output_data: str):
        
        self.setlpm_changed.emit(output_data)

        
    def gettmu_output(self, output_data: str, gettmu_command_time, interval):
        
        command_time = gettmu_command_time
        command_time = str(command_time)
        
        self.interval = interval
        
        self.received_data.append(output_data)
        self.received_data.append(command_time)
        self.join_data.append(self.received_data)
        self.received_data = []

        
        if self.emit_loop == True:

            self.emit_loop = False
            self.emit_time = datetime.now().replace(microsecond=0)
            emit_data = '\t'.join(self.join_data[0])
            self.gettmu_changed.emit(emit_data)


        
        self.delay_time = gettmu_command_time - self.emit_time
        self.delay_time = self.delay_time.seconds

        if self.delay_time == self.interval:
            
            self.emit_loop = True
            self.join_data = []
        
        elif self.delay_time > self.interval:
            self.emit_loop = True
            self.join_data = []
    
    def start_after_stoped(self, init):
        
        self.join_data = []
        self.emit_loop = init