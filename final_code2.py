import random #generating random numbers
import simpy  #used for descrete event simulation
import statistics #statistical calculation and analysis of data
import math #mathematical calculations

# Define a class for queue simulation
class QueueSimulation:       
    def __init__(self, inter_arrival_time_mean, service_time_mean, num_customers):  # Initialize simulation parameters
        self.inter_arrival_time_mean = inter_arrival_time_mean
        self.service_time_mean = service_time_mean
        self.num_customers = num_customers
        self.env = simpy.Environment()   # Create a SimPy environment manages in simulation time and events
        self.arrival_time = []     # List to store arrival times of customers
        self.departure_time = []   # List to store departure times of customers
        self.waiting_time = []     # List to store waiting times of customers
        self.service_time = []     # List to store service times of customers

    def generate_inter_arrival_time(self):  # Generate inter-arrival time using exponential distribution
        return random.expovariate(1.0 / self.inter_arrival_time_mean) 

    def generate_service_time(self):   # Generate service time using exponential distribution
        return random.expovariate(1.0 / self.service_time_mean)

    def customer(self):
        previous_departure_time = 0
        for _ in range(self.num_customers):
            inter_arrival_time = self.generate_inter_arrival_time() # Generate inter-arrival time
            service_time = self.generate_service_time() # Generate service time

            arrival_time = previous_departure_time + inter_arrival_time # Calculate arrival time
            self.arrival_time.append(arrival_time) # Add arrival time to the list
            self.service_time.append(service_time) # Add service time to the list

            yield self.env.timeout(inter_arrival_time) # Wait for inter-arrival timeprocess should wait for the given duration before continuing
            #yield statement is used to pause the execution of the current process until the specified duration has passed
            waiting_time = arrival_time - previous_departure_time # Calculate waiting time
            self.waiting_time.append(waiting_time)  # Add waiting time to the list
            departure_time = arrival_time + waiting_time # Calculate departure time
            self.departure_time.append(departure_time)  # Add departure time to the list

            previous_departure_time = departure_time  # Update previous departure time

    def simulate(self):
        self.env.process(self.customer()) # Start the simulation process
        self.env.run() # Run the simulation

        print("Simulation Summary:") # Print simulation summary
        print("Total Customers Served:", len(self.arrival_time)) # length of this list represents the total number of customers served
        print("Average Waiting Time:", statistics.mean(self.waiting_time)) #calculates the average waiting time
        print("Average Service Time:", statistics.mean(self.service_time)) #calculates the average service time

        mean_waiting_time = statistics.mean(self.waiting_time) 
        mean_service_time = statistics.mean(self.service_time)  # It assigns to the value to the mean of waiting time,service and inter arrival time 
        mean_inter_arrival_time = statistics.mean( [self.inter_arrival_time_mean])
        # Calculate additional metrics
        throughput = 1 / (mean_waiting_time + mean_service_time) #represents the number of customers served per unit of time
        utilization = mean_service_time / mean_inter_arrival_time # measures the degree of resource utilization or occupancy
        mean_number_of_customers = mean_service_time * throughput # average number of customers present in the system over time
        mean_response_time = mean_waiting_time + mean_service_time # average time a customer spends, includes both waiting time and service time
        mean_waiting_time = mean_number_of_customers / throughput # average time a customer spends waiting in the queue before being served

        print("\nAdditional Metrics:")
        print("Throughput:", throughput)
        print("Utilization:", utilization)
        print("Mean Number of Customers:", mean_number_of_customers)
        print("Mean Response Time:", mean_response_time)
        print("Mean Waiting Time:", mean_waiting_time)

      

        print("\nSimulation Details:")
        for i in range(len(self.arrival_time)):
            print(
                "Arrival at {:.2f}, Inter-arrival Time: {:.2f}, Service Time: {:.2f}, Departure at: {:.2f}, "
                "Waiting Time: {:.2f}".format(self.arrival_time[i], self.arrival_time[i] - (self.arrival_time[i - 1] if i > 0 else 0),
                 self.service_time[i], self.departure_time[i], self.waiting_time[i]))
# It calculates the time difference between the current arrival and the previous arrival

# Run multiple simulations
num_simulations = 10 
inter_arrival_time_mean = 0.5
service_time_mean = 0.3
num_customers = 100

simulation_results = []

for i in range(num_simulations):
    print("Simulation", i + 1)
    simulation = QueueSimulation(inter_arrival_time_mean, service_time_mean, num_customers)
    simulation.simulate()
    simulation_results.append(simulation)  # Store the simulation object

print("---------------------------------------")

# Calculate overall statistics from simulation results
waiting_times = []
service_times = []
arrival_times = []
departure_times = []
time_intervals = []

for simulation in simulation_results:
    waiting_times.extend(simulation.waiting_time) # It iterates adds the waiting time to the current list
    service_times.extend(simulation.service_time) # It iterates adds the service time to the current list
    arrival_times.extend(simulation.arrival_time) # It iterates adds the arrival time to the current list
    departure_times.extend(simulation.departure_time) # It iterates adds the departure time to the current list
    time_intervals.extend([arrival_times[i] - arrival_times[i - 1]for i in range(1, len(arrival_times))]) # It iterates adds the arrival time to the current list

# Calculate overall variance, confidence values, and mean time interval
variance_arrival_time = statistics.variance(arrival_times) #variance measures how much the values in a dataset vary from the mean
variance_service_time = statistics.variance(service_times) #it measures the variability of the values in the dataset

arrival_time_confidence = 1.96 * math.sqrt(variance_arrival_time) / math.sqrt(len(arrival_times)) #critical value corresponding to a 95% confidence level
service_time_confidence = 1.96 * math.sqrt(variance_service_time) / math.sqrt(len(service_times)) #critical value corresponding to a 95% confidence level

mean_time_interval = statistics.mean(time_intervals) # It calculates the sum of all values in the list divided by the number of values, providing an estimate of the average time interval between events.

print("Overall Metrics:")
print("Variance of Arrival Time:", variance_arrival_time)
print("Variance of Service Time:", variance_service_time)
print("Confidence Level of Arrival Time:", arrival_time_confidence)
print("Confidence Level of Service Time:", service_time_confidence)
print("Mean Time Interval:", mean_time_interval)
