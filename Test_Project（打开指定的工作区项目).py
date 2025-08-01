import workspacemanager
import pwktypelib
import util
import os
import subprocess
 
class Test:
    def __init__(self):
        self.polyworks_exe = r"C:\Program Files\InnovMetric\PolyWorks MS 2025\bin\polyworks.exe"
        self.ProjectName = "test"
        self.WorkSpaceName = r"C:\test\test.pwk"
        self.TESTCommand = "FILE OPEN_WORKSPACE"
    def RUN_POLYWORKS(self):
        # 1. 启动PolyWorks
        if not os.path.exists(self.polyworks_exe):
            print("PolyWorks is not installed or the path is incorrect.")
            return
        try:
            subprocess.Popen(self.polyworks_exe)
        except:
            print("Failed to start PolyWorks.")
            return
    def CONNECT_TO_WORKSPACE_MANAGER(self):
        # 2. 连接到WorkspaceManager并打开指定的工作区
        try:
            self.wm = workspacemanager.WorkspaceManagerWrapper()
            self.wm_command_center =self.wm.command_center
            self.wm_command_center.execute_command(self.TESTCommand, self.WorkSpaceName)
        except:
            print("Failed to connect to WorkspaceManager.")
            return
    
    def StartModule(self):
        # 3. 启动模块打开项目
        try:
            self.inspect_command_center = self.wm.start_module("IMInspect", self.ProjectName, self.WorkSpaceName).command_center
            test_command = "MACRO PAUSE"
            self.inspect_command_center.execute_command(test_command,"Message","has been opened the project successfully.")
        except:
            print("Failed to start module.")
            return
      
    

if __name__ == '__main__':
    t = Test()
    t.RUN_POLYWORKS()
    t.CONNECT_TO_WORKSPACE_MANAGER()
    t.StartModule()