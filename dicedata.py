import plotly.figure_factory as ff
import statistics
import random
student_result=[]
for i in range(0,1000):
    performance1=random.randint(1,6)
    performance2=random.randint(1,6)
    student_result.append(performance1+performance2)
mean=sum(student_result)/len(student_result)
std_deviation=statistics.stdev(student_result)

median=statistics.median(student_result)
mode=statistics.mode(student_result)
first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)
#print(std_deviation)
fig=ff.create_distplot([student_result],["Result"],show_hist=False)
fig.show()
list_of_data_within_1_std_deviation=[result for result in student_result if result>
                                first_std_deviation_start and result< first_std_deviation_end]
list_of_data_within_2_std_deviation=[result for result in student_result if result>
                                second_std_deviation_start and result< second_std_deviation_end ]
list_of_data_within_3_std_deviation=[result for result in student_result if result>
                                third_std_deviation_start and result< third_std_deviation_end ]
print("mean of this data is {}",format(mean))           
print("median of this data is {}",format(median))  
print("mode of this data is {}",format(mode)) 
print("standard deviation of this data is {}",format(std_deviation))         
print("{}% of data lies with 1 standard deviation",format(len(list_of_data_within_1_std_deviation)*100.0/len(student_result)))
print("{}% of data lies with 2 standard deviation",format(len(list_of_data_within_2_std_deviation)*100.0/len(student_result)))
print("{}% of data lies with 3 standard deviation",format(len(list_of_data_within_3_std_deviation)*100.0/len(student_result)))