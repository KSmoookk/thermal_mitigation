from datetime import datetime
import threading, re
from src import data_signal

class Process(threading.Thread):
    
    def __init__(self, ser, signal: data_signal, interval: int, thermal_table_upstream: dict, thermal_table_downstream: dict):
        super(Process, self).__init__()

        self.ser = ser
        self.data = signal
        self.duration = interval
        self.alive = False
        self.stop_thread = False
        #self.temp_range_dict()
        self.auto_set = ''
        self.thermal_table_upstream = thermal_table_upstream
        self.thermal_table_downstream = thermal_table_downstream
        self.temp_list=[]
        #self.temp_list_index_cnt = 5/self.interval
        self.cnt = 0
        

    def run(self):

        while not self.stop_thread:
            #print('hi read')
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
                #print('else output')
                #self.pre_value = self.temp_value
                #print("prevalue:",self.pre_value)
                self.output = self.output.split()
                self.temp_value = re.sub(r'[^0-9]','', self.output[1])
                self.temp_value = int(self.temp_value)
                self.data.gettmu_output(self.output[1], self.gettmu_command_time, self.duration)
                
                print(self.temp_value)
                self.temp_list.append(self.temp_value)

                self.gettmu_command
                


    
    def check_current_tpl(self, temp_value):
        self.upstream_keys = self.thermal_table_upstream.keys()
        self.upstream_keys = list(self.upstream_keys)
        
        self.downstream_keys = self.thermal_table_downstream.keys()
        self.downstream_keys = list(self.thermal_table_downstream)
        

        if not pre_value or pre_value == temp_value:
            pre_value = temp_value
        
        elif pre_value < temp_value:
            self.upstream(temp_value)
        
        # elif pre_value > temp_value:
        #     self.downstream(temp_value)
                

                
    
    def upstream(self, temp_value):
        for threshold in range(len(self.upstream_keys)):
            
            if self.thermal_table_upstream[threshold] >= temp_value:
                
                self.current_level = self.thermal_table_upstream[threshold]
                
                if not self.pre_level:
                    
                    self.pre_level = self.thermal_table_upstream[threshold]
                
                elif self.pre_level < self.current_level:
                    
                    self.cnt += 1
                    self.pre_level = self.thermal_table_upstream[threshold]
                    
                    if self.cnt == self.duration:
                        
                        self.ser.write(self.thermal_table_upstream[threshold].encode())
                
                else :
                    self.cnt = 0
                        
                        
    # def downstream(self, temp_value):
    #     for threshold in range(len(self.downstream_keys)):
            
    #         if self.thermal_table_upstream[threshold] >= temp_value:
                
    #             self.current_level = self.thermal_table_upstream[threshold]
                
    #             if not self.pre_level:
                    
    #                 self.pre_level = self.thermal_table_upstream[threshold]
                
    #             elif self.pre_level < self.current_level:
                    
    #                 self.cnt += 1
    #                 self.pre_level = self.thermal_table_upstream[threshold]
                    
    #                 if self.cnt == self.duration:
                        
    #                     self.ser.write(self.thermal_table_upstream[threshold].encode())
            
            
            
            # elif self.thermal_table_upstream[threshold] < temp_value and temp_value <= self.thermal_table_upstream[threshold+1]:
                
            #     self.current_level = self.upstream_keys[threshold]
                
            # else 
                
             
                
    
    
    
                
    def gettmu_command(self):

        self.gettmu_command_time = datetime.now().replace(microsecond=0)
        self.gettmu="AT+GETTMU=0\r"
        self.ser.write(self.gettmu.encode())
        # temp_keys = self.temp_dict.keys()
        # temp_keys = list(temp_keys)
        
    #     self.level1_key = temp_keys[0]
    #     self.level2_key = temp_keys[1]
    #     self.level3_key = temp_keys[2]
    #     self.level4_key = temp_keys[3]
    #     self.level5_key = temp_keys[4]
        
    # def upstream(self):
        
        
        
        
        
    # def downstream(self):
        
        


        
        
        #print(temp_keys_level1[0])
        # print(temp_keys)
        # print(type(temp_keys))
        
        

    # def temp_range_dict(self):
        
    #             self.temp_dict = {
            
    #         #label              #path
    #         35                :'AT+SETLPM=1,1,256\r',
    #         36                :'AT+SETLPM=0,1,128\r',
    #         37                :'AT+SETLPM=0,1,1\r',
    #         38                :'AT+SETLPM=1,1,64\r',
    #         39                :'AT+SETLPM=0,1,16\r',
    #         40                :'AT+SETLPM=1,1,32\r'
    #     }
                
                
                
    # def auto_set_temp(self):
        
    #             if self.temp_value >= 40:
    #                 if self.auto_set != self.temp_dict.get(40):
    #                     self.auto_set = self.temp_dict.get(40)
    #                     self.ser.write(self.auto_set.encode())

    #                 else:
                        
    #                     self.gettmu_command()
                        
    #             elif self.temp_value >= 39 and self.temp_value < 40:
    #                 if self.auto_set != self.temp_dict.get(39):
    #                     self.auto_set = self.temp_dict.get(39)
    #                     self.ser.write(self.auto_set.encode())
    #                 else:
                        
    #                     self.gettmu_command()
                        
    #             elif self.temp_value >= 38 and self.temp_value < 39:
    #                 if self.auto_set != self.temp_dict.get(38):
    #                     self.auto_set = self.temp_dict.get(38)
    #                     self.ser.write(self.auto_set.encode())
    #                 else:
    #                     self.gettmu_command()
                        
    #             elif self.temp_value >= 37 and self.temp_value < 38:
    #                 if self.auto_set != self.temp_dict.get(37):
    #                     self.auto_set = self.temp_dict.get(37)
    #                     self.ser.write(self.auto_set.encode())
    #                 else:
                        
    #                     self.gettmu_command()
                        
    #             elif self.temp_value >= 36 and self.temp_value < 37:
    #                 if self.auto_set != self.temp_dict.get(36):
    #                     self.auto_set = self.temp_dict.get(36)
    #                     self.ser.write(self.auto_set.encode())
    #                 else:
                        
    #                     self.gettmu_command()
                        
    #             elif self.temp_value >= 35 and self.temp_value < 36:
    #                 if self.auto_set != self.temp_dict.get(35):
    #                     self.auto_set = self.temp_dict.get(35)
    #                     self.ser.write(self.auto_set.encode())
    #                 else:
                        
    #                     self.gettmu_command()
                
                