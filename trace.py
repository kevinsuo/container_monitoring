import os
import time
import StringIO
import re

conList = []   # container list
totalCPU = 0.0
avgCPU = 0.0
totalmemory = 0.0
avgmemory = 0.0

class Container:
	containerID = ""
        cpu_data                = 0
        mem_usage_data          = 0
        mem_limit_data          = 0
        memoryUtil_data         = 0
        net_receive_data        = 0
        net_send_data           = 0
        block_read_data         = 0
        block_write_data        = 0
	def __init__(self):
		self.containerID = ""
	def print_con(self):
		print(self.containerID)
		print(self.cpu_data)
        	print(self.mem_usage_data)
	        print(self.mem_limit_data)
        	print(self.memoryUtil_data)
	        print(self.net_receive_data)
	        print(self.net_send_data)
	        print(self.block_read_data)
	        print(self.block_write_data)




def function_print_data(str, index):
	global totalCPU
	global totalmemory
        list = str.split( );
#        print(list)

	containerID = list[0]
        cpu = list[2]
        mem_usage = list[3]
        mem_limit = list[5]
        memoryUtil = list[6]
        net_receive = list[7]
        net_send = list[9]
        block_read = list[10]
        block_write = list[12]


	#remove the unit and get the data
        cpu_data                = "".join(re.findall(r"\d+\.?\d*", cpu))
        mem_usage_data          = "".join(re.findall(r"\d+\.?\d*", mem_usage))
        mem_limit_data          = "".join(re.findall(r"\d+\.?\d*", mem_limit))
        memoryUtil_data         = "".join(re.findall(r"\d+\.?\d*", memoryUtil))
        net_receive_data        = "".join(re.findall(r"\d+\.?\d*", net_receive))
        net_send_data           = "".join(re.findall(r"\d+\.?\d*", net_send))
        block_read_data         = "".join(re.findall(r"\d+\.?\d*", block_read))
        block_write_data        = "".join(re.findall(r"\d+\.?\d*", block_write))


#        print(cpu_data)
#        print(mem_usage_data)
#        print(mem_limit_data)
#        print(memoryUtil_data)
#        print(net_receive_data)
#        print(net_send_data)
#        print(block_read_data)
#        print(block_write_data)

	conList[index].containerID = ''.join(containerID)
        conList[index].cpu_data = cpu_data
        conList[index].mem_usage_data = mem_usage_data
        conList[index].mem_limit_data = mem_limit_data
        conList[index].memoryUtil_data = memoryUtil_data
        conList[index].net_receive_data = net_receive_data
        conList[index].net_send_data = net_send_data
        conList[index].block_read_data = block_read_data
        conList[index].block_write_data = block_write_data

	totalCPU += float(cpu_data)
	totalmemory += float(mem_usage_data)


def main():
        global totalCPU
        global totalmemory

	containerID = "c64f8944696b"
	#cmd = "sudo docker stats --no-stream " + containerID + " | sed -n '2p'"
	cmd = "sudo docker stats --no-stream "

	str = os.popen(cmd).read()
	lines = re.split('\n',str)
	numofcon = len(lines)-2   # how many containers we have
	print("We have ", numofcon,  "containers.")

	for i in range(numofcon):
                con = Container()
                conList.append(con)

	while(1):
        	str = os.popen(cmd).read()
		print(str)

		totalCPU = 0.0
		avgCPU = 0.0
		totalmemory = 0.0
		avgmemory = 0.0

		index = 0
		lines = re.split('\n',str)

		numofcon = len(lines)-2   # how many containers we have

		# traverse each line of terminal output
		for line in lines:
			if (index > 0 and index < len(lines)-1):     # does not print the first line and last line (last line is an empty line)
			#	print(index-1)
        		#	print(line)
				function_print_data(line, index-1)
			index+=1


		print(totalCPU, totalmemory)

		avgCPU = totalCPU/numofcon
		avgmemory = totalmemory/numofcon
		print(avgCPU, avgmemory)



		for con in conList:
			if (float(con.cpu_data) > avgCPU):
				print(con.containerID, con.cpu_data)

		time.sleep(30)



# run the main function
if __name__ == "__main__":
    main()
