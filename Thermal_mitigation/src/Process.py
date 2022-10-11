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
        self.pre_value = 0
        self.pre_level = 0
        

    def run(self):

        while not self.stop_thread:
            print('hi read')
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

                self.data.gettmu_output(self.output[1], self.gettmu_command_time, self.duration)
                
                self.check_current_tpl(self.temp_value)
                self.gettmu_command
                


    
    def check_current_tpl(self, temp_value: int):
        self.upstream_keys = self.thermal_table_upstream.keys()
        self.upstream_keys = list(self.upstream_keys)

        
        self.downstream_keys = self.thermal_table_downstream.keys()
        self.downstream_keys = list(self.thermal_table_downstream)

        print("pre temp",self.pre_value)
        

        if self.pre_value == 0:
            self.pre_value = temp_value
            print("not self.pre_value")
        
        elif self.pre_value < temp_value:
            print("self.pre_value < temp_value -> self.upstream()")
            self.pre_value = temp_value
            self.upstream(temp_value)
        
        # elif self.pre_value > temp_value:
        #     self.downstream(temp_value)
        
        else:
            #self.pre_value = temp_value
            print("여기오면 안돼")
                
                
    # def downstream(self, temp_value):
    #     for threshold in range(len(self.upstream_keys)):

    #         if self.upstream_keys[threshold] < temp_value and temp_value <= self.upstream_keys[threshold+1]:
                
    #             #print("self.thermal_table_upstream[%d] >= temp_value" %threshold)
                
    #             self.current_level = self.upstream_keys[threshold+1]
    #             print("self.current_level", self.current_level)

    #             if self.pre_level == 0:
                    
    #                 #print("not self.pre_level")
                    
    #                 self.pre_level = self.current_level 
    #                 print("Pre_level", self.pre_level)
                
    #             elif self.pre_level < self.current_level:
                    
    #                 print("self.pre_level<self.current_level")
                    
    #                 self.cnt = self.cnt + 1
    #                 print("self.cnt",self.cnt)
    #                 self.pre_level = self.current_level 
                    
                    
    #                 if self.cnt == self.duration:
                        
    #                     print("self.cnt == self.duration")
                        
    #                     change_level = str(self.thermal_table_upstream[self.current_level])
    #                     print("ser.write")
    #                     self.ser.write(change_level.encode())
                        
    #             else :
    #                 print("self.cnt")
    #                 self.cnt = 0


                
    
    def upstream(self, temp_value):
        for threshold in range(len(self.upstream_keys)):

            if self.upstream_keys[threshold] < temp_value and temp_value <= self.upstream_keys[threshold+1]:
                
                #print("self.thermal_table_upstream[%d] >= temp_value" %threshold)
                
                self.current_level = self.upstream_keys[threshold+1]
                print("self.current_level", self.current_level)

                if self.pre_level == 0:
                    
                    #print("not self.pre_level")
                    
                    self.pre_level = self.current_level 
                    print("Pre_level", self.pre_level)
                
                elif self.pre_level < self.current_level:
                    
                    print("self.pre_level<self.current_level")
                    
                    self.cnt = self.cnt + 1
                    print("self.cnt",self.cnt)
                    self.pre_level = self.current_level 
                    
                    
                    if self.cnt == self.duration:
                        
                        print("self.cnt == self.duration")
                        
                        change_level = str(self.thermal_table_upstream[self.current_level])
                        print("ser.write")
                        self.ser.write(change_level.encode())
                        
                else :
                    print("self.cnt")
                    self.cnt = 0
                        

                
    def gettmu_command(self):

        self.gettmu_command_time = datetime.now().replace(microsecond=0)
        self.gettmu="AT+GETTMU=0\r"
        self.ser.write(self.gettmu.encode())
