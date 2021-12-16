'''
Author: Rakesh Musale
Date: 2022-16-12 11:15:55
Last Modified by: Rakesh Musale
Last Modified time: 2022-16-12 11:15:14
Title : StopWatch Program.
'''

import time
input("Press enter to start time")
start_time = time.time()
input("Press enter to end time")
end_time = time.time()
elapsed_time = end_time - start_time
print("The time elapsed is : ",elapsed_time)