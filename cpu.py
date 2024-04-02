from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

def unix_time_millis(dt):
    """Convert datetime object to milliseconds since epoch (Unix time)."""
    epoch = datetime.datetime.utcfromtimestamp(0)
    return int((dt - epoch).total_seconds() * 1000)

def fcfs(processes):
    """
    Implementation of First-Come, First-Served (FCFS) CPU scheduling algorithm.
    """
    processes.sort(key=lambda x: x[1])  # Sort processes based on arrival time
    completion_time = [0] * len(processes)
    waiting_time = [0] * len(processes)
    turnaround_time = [0] * len(processes)
    total_waiting_time = 0
    total_turnaround_time = 0
    current_time = 0
    start_times = []
    gantt_chart_data = []

    # Assuming the simulation starts at a specific datetime, adjust as needed.
    simulation_start = datetime.datetime.now()

    for i, process in enumerate(processes):
        arrival_delay = datetime.timedelta(seconds=process[1])
        burst_duration = datetime.timedelta(seconds=process[2])
        start_time = simulation_start + arrival_delay
        end_time = start_time + burst_duration

        current_time = max(current_time, process[1])
        completion_time[i] = current_time + process[2]
        turnaround_time[i] = completion_time[i] - process[1]
        waiting_time[i] = turnaround_time[i] - process[2]
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]
        start_times.append(start_time)

        gantt_chart_data.append({
            'process_id': process[0],
            'start_time': unix_time_millis(start_time),
            'end_time': unix_time_millis(end_time)
        })
        current_time += process[2]

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)

    return completion_time, waiting_time, turnaround_time, avg_waiting_time, avg_turnaround_time, gantt_chart_data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_processes = int(request.form['num_processes'])
        processes = []

        for i in range(1, num_processes + 1):
            # Assuming arrival and burst times are provided in seconds.
            arrival_time = int(request.form[f'arrival_time_{i}'])
            burst_time = int(request.form[f'burst_time_{i}'])
            processes.append((i, arrival_time, burst_time))

        completion_time, waiting_time, turnaround_time, avg_waiting_time, avg_turnaround_time, gantt_chart_data = fcfs(processes)

        return render_template('result.html', processes=processes,
                               completion_time=completion_time,
                               waiting_time=waiting_time,
                               turnaround_time=turnaround_time,
                               avg_waiting_time=avg_waiting_time,
                               avg_turnaround_time=avg_turnaround_time,
                               gantt_chart_data=gantt_chart_data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
