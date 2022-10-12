from datetime import datetime
import threading, re
from src import data_signal

class Process(threading.Thread):
    
    def __init__(self, ser, signal: data_signal, interval: int, 
                 thermal_max_list: list, thermal_min_list: list, thermal_level_dict : dict ):
        super(Process, self).__init__()
        print('hello')
        self.ser = ser
        self.data = signal
        self.duration = interval
        self.alive = False
        self.stop_thread = False
        #self.auto_set = ''
        self.thermal_max_list = thermal_max_list
        self.thermal_min_list = thermal_min_list
        self.thermal_level_dict = thermal_level_dict
        self.thermal_level_keys = list(self.thermal_level_dict.keys())
        self.pre_level = 0
        self.temp_list=[]
        self.cnt = 0


        

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
                self.current_temp_value = re.sub(r'[^0-9]','', self.output[1])
                self.current_temp_value = int(self.current_temp_value)

                self.data.gettmu_output(self.output[1], self.gettmu_command_time, self.duration)
                
                self.check_current_tpl(self.current_temp_value)
                self.gettmu_command
                


    
    def check_current_tpl(self, current_temp_value: int):

        print("self.pre_level1 : ", self.pre_level)
        for threshold in range(len(self.thermal_max_list)):
            
            if self.thermal_max_list[threshold] < current_temp_value:
                
                self.current_level = int(self.thermal_level_keys[threshold+1])
            
                print("self.expected_current_level1 : ", self.current_level)
                
            
            
            elif self.thermal_min_list[threshold] > current_temp_value:
                
                self.current_level = int(self.thermal_level_keys[threshold])
                print("self.expected_current_level2 : ", self.current_level)

                break
            
        
                
        if self.pre_level == 0:
            self.pre_level = self.current_level
            print("self.pre_level2 : ", self.pre_level)
            self.thermal_level_trasition(current_temp_value)
            
        else : 
            self.thermal_level_trasition(current_temp_value)
            
        
        
                
    def thermal_level_trasition(self, current_temp_value : int):
        
        for threshold in range(len(self.thermal_max_list)):
            
            if self.thermal_min_list[threshold] < current_temp_value and current_temp_value <= self.thermal_max_list[threshold]: # 94 < 93
                
                self.pre_level = self.current_level
            
            
            elif self.thermal_min_list[threshold] > current_temp_value or current_temp_value >= self.thermal_max_list[threshold]:
            
            
                if self.pre_level == self.current_level:
                    
                    self.cnt = 0
                    print("self.cnt : ", self.cnt)
                    
                    
                
                elif self.pre_level != self.current_level:
                    
                    self.cnt += 1
                    print("+=count self.cnt : ", self.cnt)
                    
                    if self.cnt == self.duration:
                        
                        self.pre_level = self.current_level
                        level_transition = str(self.thermal_level_dict[self.current_level])
                    
                        self.ser.write(level_transition.encode())
                    break
                        
    def gettmu_command(self):

        self.gettmu_command_time = datetime.now().replace(microsecond=0)
        self.gettmu="AT+GETTMU=0\r"
        self.ser.write(self.gettmu.encode())
                        
            
            # elif self.thermal_max_list[threshold] <= current_temp_value:
            
            #     if self.pre_level == self.current_level:
                    
            #         self.cnt = 0
                    
                
            #     elif self.pre_level != self.current_level:
                    
            #         self.cnt += 1
            #         print("self.cnt : ", self.cnt)
            #         if self.cnt == 5:
                        
            #             self.pre_level = self.current_level
                        
            # else:
                
            #     pass
            
            

            # elif self.thermal_max_list[threshold] < current_temp_value and current_temp_value <= self.thermal_max_list[threshold+1]:
        
                
                
            #     self.current_level = self.thermal_level_dict[threshold]
        # if self.pre_value == 0:
        #     self.pre_value = current_temp_value
        #     print("not self.pre_value")
        
        # elif self.pre_value < current_temp_value:
        #     print("self.pre_value < current_temp_value -> self.upstream()")
        #     self.pre_value = current_temp_value
        #     self.upstream(current_temp_value)
        
        # elif self.pre_value > current_temp_value:
        #     self.downstream(current_temp_value)
        
        # else:
        #     #self.pre_value = current_temp_value
        #     print("여기오면 안돼")
                
                
    # def downstream(self, current_temp_value):
    #     for threshold in range(len(self.upstream_keys)):

    #         if self.upstream_keys[threshold] < current_temp_value and current_temp_value <= self.upstream_keys[threshold+1]:
                
    #             #print("self.thermal_table_upstream[%d] >= current_temp_value" %threshold)
                
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


                
    
    # def upstream(self, current_temp_value):
    #     for threshold in range(len(self.upstream_keys)):

    #         if self.upstream_keys[threshold] < current_temp_value and current_temp_value <= self.upstream_keys[threshold+1]:
                
    #             #print("self.thermal_table_upstream[%d] >= current_temp_value" %threshold)
                
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
                        

                

