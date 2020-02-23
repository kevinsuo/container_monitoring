import os
import time


containerID = "c64f8944696b"
cmd = "sudo docker stats --no-stream " + containerID + " | sed -n '2p'"


while(1):
        str = os.popen(cmd).read()
        print(str)

        list = str.split( );
        print(list)

        cpu = list[2]
        mem_usage = list[3]
        mem_limit = list[5]
        memoryUtil = list[6]
        net_receive = list[7]
        net_send = list[9]
        block_read = list[10]
        block_write = list[12]


#remove the unit and get the data
        cpu_data                = cpu[:-1]
        mem_usage_data          = mem_usage[:-3]
        mem_limit_data          = mem_limit[:-3]
        memoryUtil_data         = memoryUtil[:-1]
        net_receive_data        = net_receive[:-2]
        net_send_data           = net_send[:-2]
        block_read_data         = block_read[:-1]
        block_write_data        = block_write[:-1]


        print(cpu_data)
        print(mem_usage_data)
        print(mem_limit_data)
        print(memoryUtil_data)
        print(net_receive_data)
        print(net_send_data)
        print(block_read_data)
        print(block_write_data)


        time.sleep(5)

