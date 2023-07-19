Queue System Simulation using SimPy

You are tasked with simulating a queue system to analyze its performance using the SimPy library in Python. The queue system consists of customers arriving at a service center, waiting in a queue, and then being served by a service agent. Your task is to implement the simulation and calculate various performance metrics based on the simulation results.

Code Description:

The provided Python code simulates a queue system using the SimPy library. It includes a QueueSimulation class that represents the simulation. The simulation parameters, such as inter-arrival time mean, service time mean, and the number of customers, are initialized in the constructor.

The generate_inter_arrival_time and generate_service_time methods use the exponential distribution to generate random inter-arrival times and service times, respectively.

The customer method defines the behavior of each customer during the simulation. It generates arrival times, and service times, and calculates waiting times, and departure times for each customer.

The simulation method starts the simulation process using the customer method and runs the simulation. After each simulation, various metrics, such as total customers served, average waiting time, and average service time, are calculated and printed.

Multiple simulations are performed by running the QueueSimulation class with different sets of parameters, and the overall statistics are calculated based on the results.
