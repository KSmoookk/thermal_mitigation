from datetime import datetime
import threading, re
from src import data_signal

class Process(threading.Thread):
    
    def __init__(self, ser, signal: data_signal, interval : int):
        super(Process, self).__init__()

        self.ser = ser
        self.data = signal
        self.interval = interval
        self.alive = False
        self.stop_thread = False
        self.temp_range_dict()
        self.auto_set = ''
        
    def run(self):
        
        while not self.stop_thread:
            
            self.output = self.ser.read(64).decode()


            if self.stop_thread == True:
                self.data.start_after_stoped(True)
                return 0
            
            
            if 'AT+SETLPM' in self.output:
                self.output = self.output.split()
                self.result_list = []
                
                for i in range(len(self.output)):
                    if 'AT+SETLPM' in self.output[i]:
                        self.result_list.append(self.output[i])
                        self.result_list.append(self.output[i+1])
                        self.output = '\n'.join(self.result_list)
                        self.data.setlpm_output(self.output)
                        

            elif not self.output:
                
                self.gettmu_command()
                
                
            else:

                self.output = self.output.split()
                self.temp_value = re.sub(r'[^0-9]','', self.output[1])
                self.temp_value = int(self.temp_value)
                self.data.gettmu_output(self.output[1], self.gettmu_command_time, self.interval)
                self.auto_set_temp()

                
                
    def gettmu_command(self):
        self.gettmu_command_time = datetime.now().replace(microsecond=0)
        self.gettmu="AT+GETTMU=0\r"
        self.ser.write(self.gettmu.encode())
        
        
        
    def temp_range_dict(self):
        
                self.temp_dict = {
            
            #label              #path
            35                :'AT+SETLPM=1,1,256\r',
            36                :'AT+SETLPM=0,1,128\r',
            37                :'AT+SETLPM=0,1,1\r',
            38                :'AT+SETLPM=1,1,64\r',
            39                :'AT+SETLPM=0,1,16\r',
            40                :'AT+SETLPM=1,1,32\r'
        }
                
                
                
    def auto_set_temp(self):
        
                if self.temp_value >= 40:
                    if self.auto_set != self.temp_dict.get(40):
                        self.auto_set = self.temp_dict.get(40)
                        self.ser.write(self.auto_set.encode())

                    else:
                        
                        self.gettmu_command()
                        
                elif self.temp_value >= 39 and self.temp_value < 40:
                    if self.auto_set != self.temp_dict.get(39):
                        self.auto_set = self.temp_dict.get(39)
                        self.ser.write(self.auto_set.encode())
                    else:
                        
                        self.gettmu_command()
                        
                elif self.temp_value >= 38 and self.temp_value < 39:
                    if self.auto_set != self.temp_dict.get(38):
                        self.auto_set = self.temp_dict.get(38)
                        self.ser.write(self.auto_set.encode())
                    else:
                        self.gettmu_command()
                        
                elif self.temp_value >= 37 and self.temp_value < 38:
                    if self.auto_set != self.temp_dict.get(37):
                        self.auto_set = self.temp_dict.get(37)
                        self.ser.write(self.auto_set.encode())
                    else:
                        
                        self.gettmu_command()
                        
                elif self.temp_value >= 36 and self.temp_value < 37:
                    if self.auto_set != self.temp_dict.get(36):
                        self.auto_set = self.temp_dict.get(36)
                        self.ser.write(self.auto_set.encode())
                    else:
                        
                        self.gettmu_command()
                        
                elif self.temp_value >= 35 and self.temp_value < 36:
                    if self.auto_set != self.temp_dict.get(35):
                        self.auto_set = self.temp_dict.get(35)
                        self.ser.write(self.auto_set.encode())
                    else:
                        
                        self.gettmu_command()
                
                