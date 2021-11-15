import psutil
import os
import time
from datetime import datetime

def exec():
    p = input('Укажите путь к процессу:  ')
    t = input('Укажите интервал обновления данных целым числом: ')
    try:
        proc = psutil.Popen(p)
        monitor(t, proc)
    except:
        print('Выбранно не корректное приложение, попробуйте вновь.')

def monitor(interval, proc):
    try:
        with open(os.path.dirname(os.path.abspath(__file__)) +'/' + proc.name() +" logs.txt", "w+") as f:
            # Прописываем столбы у таблицы
            f.write('Time;Usage percent CPU;Resident Set Size;Virtual Memory Size;Number of file descriptors;' + '\n')
            while proc.status() != 'zombie':
                interval = int(interval)
                # Выводим данные о потреблении ресурсов
                print('Usage percent CPU: ' + str(proc.cpu_percent()) + ' Resident Set Size : ' + str(
                    proc.memory_full_info()[0]) + ' Virtual Memory Size: ' + str(proc.memory_full_info()[1])+\
                      'Number of file descriptors :' + str(proc.num_fds()), '\n')
                # Записываем данные о потреблении ресурсов
                f.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')) + ';' + str(proc.cpu_percent()) + ';' + str(proc.memory_full_info()[0]) + ';' + str(
                    proc.memory_full_info()[1]) +';'+ str(proc.num_fds()) + '\n')
                # Задержка перед следующей проверкой
                time.sleep(interval)
        f.close()
        print('Конец логирования')
    except:
        print('Непредвиденный конец')
        pass
exec()