#The most common algorithm for finding LCM 
def LCM(period_1, period_2):
	#initialise variables 
	greater_value = 0
	lcm = 0
	#determine greater value (or whether period_1 == period_2) 
	if period_1 > period_2:      
		greater_value = period_1  
	else:  
		greater_value = period_2 
	#repeat until break
	while(True):  
		#if the greater_value is divisible by both arguments... 
		if((greater_value % period_1 == 0) and (greater_value % period_2 == 0)):  
			lcm = greater_value #assign lcm as the greater value and return LCM
			break
		greater_value += 1 #ifn, greater_value++ && check for LCM, until found
	return lcm  
def utilization_factor(task_set):	
	#initialise variables
	utilization_factor = 0
	icf = 0
	for task in task_set:
		icf+=1
		if task[0] <= 0: #control flow
			return "In task number %d -- improper value of period" % icf 
		utilization_factor += task[2]/task[0] #WCET/Relative Period
	return round(utilization_factor,5)
def hyper_period(task_set):
	#initialise variables
	operational_array = []
	icf = 0
	#for each task in task_set...
	for task in task_set:
		icf +=1
		if task[0] == 0: #check if period == 0
			return "In task number %d -- improper value of period" % icf
		operational_array.append(task[0]) 
		#if period == 0, add task to array of periods 
	#initialise current lowest common multiple
	CURR_LCM = operational_array[0]
	for i in range(len(operational_array)):
			CURR_LCM = LCM(CURR_LCM, operational_array[i]) 
			#call LCM function, passing previous LCM, and the next period value
			#store the result in the current lowest common multiple variable
	return CURR_LCM #return LCM of a task set == hyperperiod
def main():
	#to add tasks to the list, simply add another nested list of size at least 3,
	#bearing in mind the order of notions
	#t_set stands for "task set", and it is an list of nested lists, of length 4, where 
	#array[x][0] == Period
	#array[x][1] == Deadline
	#array[x][2] == Worst case computation time
	#array[x][3] == Fixed priority

	t_set = [[10,4,2,1],[5,3,1,2],[20,10,4,3]]

	print(hyper_period(t_set))
	print(utilization_factor(t_set))

if __name__ == '__main__':
	main()