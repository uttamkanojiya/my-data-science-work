import matplotlib.pyplot as plt
import random

kohil_run = sorted(random.sample(range(300,2500),10))
rohit_run = sorted(random.sample(range(200,2100),10))
sachin_run = sorted(random.sample(range(100,2000),10))
sehwag_run = sorted(random.sample(range(0,1900),10))

years = sorted(random.sample(range(1980,2010),10))

plt.plot(years,kohil_run,label="Virat Kohil Runs",linewidth=1)
plt.plot(years,rohit_run,label="Rohit Sharma Runs",linewidth=1)
plt.plot(years,sachin_run,label="Sachine Tendulkar Runs",linewidth=1)
plt.plot(years,sehwag_run,label="Sehwag Runs",linewidth=1)
plt.xlabel("Years")
plt.ylabel("Runs")
plt.title("Performance Comparsion")
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()