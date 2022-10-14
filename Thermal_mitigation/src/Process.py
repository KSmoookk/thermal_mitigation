from datetime import datetime
import threading, re
from src import data_signal

class Process(threading.Thread):
    
    def __init__(self, ser, signal: data_signal, duration: int, 
                 thermal_level_dict: dict, thermal_temp_dict : dict ):
        super(Process, self).__init__()
        print('thread init')
        self.ser = ser
        self.data = signal
        self.duration = duration
        self.alive = False
        self.stop_thread = False
        self.thermal_level_dict = thermal_level_dict
        self.thermal_level_keys = list(self.thermal_level_dict.keys())
        self.thermal_temp_dict = thermal_temp_dict
        self.current_level = 1
        self.temp_list=[]
        self.cnt = 0
        self.count = 0
        self.init_level = True


    def run(self):

        while not self.stop_thread:
            

                self.output = self.ser.read(64).decode()                                    #1초마다 계속 Serial read 진행


                if self.stop_thread == True:
                    
                    self.data.start_after_stoped(True)
                    
                    return 0
                
                
                if 'AT+SETLPM' in self.output:                                              #output에 AT_SETLPM에 대한 응답이 있으면
                    self.output = self.output.split()                                       #output을 잘라, List로 저장
                    self.result_list = []
                    print(self.output)
                    for i in range(len(self.output)):                                       #list길이 만큼 for문 진행
                        if 'AT+SETLPM' in self.output[i]:
                            self.result_list.append(self.output[i])                         #output[i] = AT+SETLPM=0,x,x을 result_list에 append
                            self.result_list.append(self.output[i+1])                       #output[i+1] = 'OK'를 result_list에 append
                            self.output = '\n'.join(self.result_list)                       #result_list 줄바꿈해서 Join
                            self.data.setlpm_output(self.output)                            #Datacenter에 전달
                            

                elif not self.output:
                    self.gettmu_command()                                                   #초기 output에 아무 응답이 없을 때, 한 번 사용됨
                    
                    
                else:

                        self.output = self.output.split()                                   #AT+GETTMU=0을 보냈을 때 돌아오는 response를 잘라, output에 저장
                        if len(self.output) == 3:                                           #자르면 3개가 나오지만, 타이밍 오류로 가끔 5개가 될 때가 있어서 3개가 아닐 시, 재명령 진행
                            self.count += 1
                            print('===========================================')
                            print(self.count,"회 진행")
                            
                            self.current_temp_value = re.sub(r'[^0-9]','', self.output[1])  #output[1] = HighestTMU=36 에서 숫자만 slice
                            self.current_temp_value = int(self.current_temp_value)
                            print(self.current_temp_value)
                            
                            self.data.gettmu_output(self.output[1], self.gettmu_command_time) #GETTMU에 대한 response를 Datacenter에 전달
                            self.check_current_tpl(self.current_temp_value)                                  #slice된 온도값을 이용해 Level 지정

                        else:
                            self.gettmu_command()
                            

                        

    def check_current_tpl(self, current_temp_value: int):                                #받아온 온도가 속하는 범위의 예상 Level 지정
        
        print("Current Level : ", self.current_level)
        
        for level in range(1,len(self.thermal_temp_dict)+1):

            if self.thermal_temp_dict[level][0] < current_temp_value < self.thermal_temp_dict[level][1]:
                
                
                self.expected_level = self.thermal_level_keys[level-1]                   # 예상하는 Level로 지정
                print('expected Level in for function : ', self.expected_level)
                break
        
        self.check_thermal_level_transition(self.current_temp_value)                    

        

            
        
        
                
    def check_thermal_level_transition(self, current_temp_value : int):                 #Level을 바꾸는지 Check하는 함수

        if self.init_level == True:                                                     #처음 시작 시, Level 설정
            
            self.current_level = self.expected_level
                    
            self.thermal_level_init()
                                                                                        #초기 Level 설정 다음부터 실행 될 구문
            
        elif self.current_level != self.expected_level:                                 #예상 Level과 현재 Level이 다를 때, 현재 Level에서 다시 한 번 체크
                    
            if self.thermal_temp_dict[self.current_level][0] < current_temp_value < self.thermal_temp_dict[self.current_level][1]:
                        
                self.expected_level = self.current_level                                #다시 한 번 체크하여 Level변동이 없어야 한다면, 예상 Level에 현재 Level을 넣어준다
                
            print("Expected_next_level after rechecked : ",self.expected_level)
            self.thermal_transition(current_temp_value)
        
        else:                                                                           
            
            self.thermal_transition(current_temp_value)
        

    def thermal_transition(self, current_temp_value):                                   #Level을 변경할 때, 사용되는 함수                                                      
            
                if current_temp_value <= self.thermal_temp_dict[self.current_level][0]:  #현재 Level의 하한보다 내려갈 경우 카운트, Duration과 같아 질 경우 Level transition
                    
                    self.cnt += 1
                    print("Down stream count : ", self.cnt)
                    if self.cnt == self.duration:
                        
                        self.thermal_level_down()

                        
                    else:
                    
                        self.gettmu_command()
                    
                elif self.thermal_temp_dict[self.current_level][1] <= current_temp_value: #Level 상한을 넘어갔을 경우 카운트, Duration과 같아 질 경우 Level transition
                    
                    self.cnt += 1
                    print("Up stream count : ", self.cnt)
                    
                    if self.cnt == self.duration:
                        
                        self.thermal_level_up()

                        
                    else:                                                                  #카운트가 되면 다시 온도 값 읽어오기 command
                        
                        self.gettmu_command()
                        
                else:                                                                      #카운트 도중에 다시 현재 Level의 온도 범위 내로 들어오면 카운트 초기화
                    
                    self.cnt = 0
                    self.gettmu_command()
            
            
    def thermal_level_down(self):                                                          #Level Down, Level dict에서 하위의 Level 키값을 가져와 Command 진행
        
        self.current_level = self.current_level-1
        level_down = str(self.thermal_level_dict[self.current_level])
        self.ser.write(level_down.encode())
        self.cnt = 0
        
        
    def thermal_level_up(self):                                                            #Level Up, Level dict에서 상위의 Level 키값을 가져와 Command 진행
        
        self.current_level = self.current_level+1
        level_up = str(self.thermal_level_dict[self.current_level])
        self.ser.write(level_up.encode())
        self.cnt = 0
        
    def thermal_level_init(self):                                                          #초기 Level 설정
        
        
        init_level = str(self.thermal_level_dict[self.current_level])
                
        self.ser.write(init_level.encode())
        self.init_level = False
        self.cnt = 0
                        
    def gettmu_command(self):                                                              #AT+GETTMU=0 Command
        
        self.gettmu_command_time = datetime.now().replace(microsecond=0)
        self.gettmu="AT+GETTMU=0\r"
        self.ser.write(self.gettmu.encode())

                

