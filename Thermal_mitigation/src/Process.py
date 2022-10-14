from datetime import datetime
import threading, re
from src import data_signal

class Process(threading.Thread):
    
    def __init__(self, ser, signal: data_signal, duration: int, 
                 thermal_level_dict: dict, thermal_temp_dict : dict ):
        super(Process, self).__init__()
        print('hello')
        self.ser = ser
        self.data = signal
        self.duration = duration
        self.alive = False
        self.stop_thread = False
        self.thermal_level_dict = thermal_level_dict
        self.thermal_level_keys = list(self.thermal_level_dict.keys())
        self.thermal_temp_dict = thermal_temp_dict
        self.current_level = 0
        self.temp_list=[]
        self.cnt = 0
        self.count = 0
        self.init_level = True
        self.pre_expected = 0


    def run(self):

        while not self.stop_thread:
            

                self.output = self.ser.read(64).decode()


                if self.stop_thread == True:
                    
                    self.data.start_after_stoped(True)
                    
                    return 0
                
                
                if 'AT+SETLPM' in self.output:
                    self.output = self.output.split()
                    self.result_list = []
                    print(self.output)
                    for i in range(len(self.output)):
                        if 'AT+SETLPM' in self.output[i]:
                            self.result_list.append(self.output[i])
                            self.result_list.append(self.output[i+1])
                            self.output = '\n'.join(self.result_list)
                            self.data.setlpm_output(self.output)
                            

                elif not self.output:
                    self.gettmu_command()
                    
                    
                else:
                    try:
                        self.output = self.output.split()
                        if len(self.output) == 3:
                            self.count += 1
                            print(self.count,"회 진행")
                            
                            self.current_temp_value = re.sub(r'[^0-9]','', self.output[1])
                            self.current_temp_value = int(self.current_temp_value)
                            print(self.current_temp_value)
                            
                            self.data.gettmu_output(self.output[1], self.gettmu_command_time, self.duration)
                            self.check_current_tpl(self.current_temp_value)

                        else:
                            #print("@@@@@@@@@@@@@@@@@@@@@@@@@리스트 초기와@@@@@@@@@@@@@@@@@@@@@@@@@")
                            self.gettmu_command()
                            
                    except:
                        
                        if self.cnt == self.duration:
                            self.thermal_level_transition()
                        
                        else:
                            #self.output = []
                            #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@뻑@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                            self.gettmu_command()
                        

    def check_current_tpl(self, current_temp_value: int):
        
        print("Current Level : ", self.current_level)
        
        for level in range(1,len(self.thermal_temp_dict)+1):
            #print(self.thermal_temp_dict[level][0])
            if self.thermal_temp_dict[level][0] < current_temp_value < self.thermal_temp_dict[level][1]:
                
                
                self.expected_level = self.thermal_level_keys[level-1]

                
                break
        
        print("Expected_next_level : ",self.expected_level)
        self.check_thermal_level_trasition(self.current_temp_value)

        

            
        
        
                
    def check_thermal_level_trasition(self, current_temp_value : int):

        if self.init_level == True:                                                     #처음 시작 시, Level 설정
            
            self.current_level = self.expected_level
                    
            self.thermal_level_init()
        
        else:                                                                           #초기 Level 설정 다음부터 실행 될 구문
            
                if current_temp_value < self.thermal_temp_dict[self.current_level][0]:  #Level 하한보다 내려갈 경우
                    
                    self.cnt += 1
                    print("Down stream count : ", self.cnt)
                    if self.cnt == self.duration:
                        
                        self.thermal_level_down()

                        
                    else:
                    
                        self.gettmu_command()
                    
                elif self.thermal_temp_dict[self.current_level][1] < current_temp_value: #Level 상한을 넘어갔을 경우
                    
                    self.cnt += 1
                    print("Up stream count : ", self.cnt)
                    
                    if self.cnt == self.duration:
                        
                        self.thermal_level_up()

                        
                    else:
                        
                        self.gettmu_command()
                        
                else:
                    
                    self.cnt = 0
                    self.gettmu_command()
            
            
    def thermal_level_down(self):
        
        self.current_level = self.current_level-1
        level_down = str(self.thermal_level_dict[self.current_level])
        self.ser.write(level_down.encode())
        self.cnt = 0
        
        
    def thermal_level_up(self):
        
        self.current_level = self.current_level+1
        level_up = str(self.thermal_level_dict[self.current_level])
        self.ser.write(level_up.encode())
        self.cnt = 0
        
    def thermal_level_init(self):
        
        
        init_level = str(self.thermal_level_dict[self.current_level])
                
        self.ser.write(init_level.encode())
        self.thermal_level_init = False
        self.cnt = 0
                        
    def gettmu_command(self):
        
        self.gettmu_command_time = datetime.now().replace(microsecond=0)
        self.gettmu="AT+GETTMU=0\r"
        self.ser.write(self.gettmu.encode())

                

