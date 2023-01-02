import os.path
import re
import sys


def replace_python_executable(file: str, executable: str):
    r = re.compile(rb'#!(.*\.exe)\n\r')
    with open(file, 'rb+') as fp:
        file_bytes = fp.read()
        match = r.search(file_bytes)
        if match:
            old_executable = match.groups()[0]
            new_file_bytes = file_bytes.replace(old_executable, executable.encode())
            fp.write(new_file_bytes)
            print(file, '已修复')
        else:
            print(file, '未搜索到执行文件，修复失败')


if __name__ == '__main__':
    python_path = sys.exec_prefix
    script_path = os.path.join(python_path, 'Scripts')
    print("Python安装目录：", python_path)
    print("Scripts目录：", script_path)
    print("开始修复Script文件")
    with os.scandir(script_path) as it:
        for entry in it:
            if entry.is_file() and entry.name.endswith('.exe'):
                replace_python_executable(entry.path, sys.executable)
