document.addEventListener('DOMContentLoaded', function() {

    document.getElementById('generateForm').addEventListener('click', function() {
        var numProcesses = document.getElementById('num_processes').value;
        var formContainer = document.getElementById('processesForm');
        formContainer.innerHTML = ''; // Clear previous inputs

        // Create a div for the heading
        var headingDiv = document.createElement('div');
        headingDiv.innerHTML = '<h4 id="input_heading1">Enter the Arrival and Burst Time of the processes</h4>';
        formContainer.appendChild(headingDiv);

        for (let i = 1; i <= numProcesses; i++) {
            var htmlContent = `
                <div class="input-group">
                    <span class="input-group-text">Process ${i}</span>
                    <input type="number" class="form-control" name="arrival_time_${i}" placeholder="Arrival Time" required>
                    <input type="number" class="form-control" name="burst_time_${i}" placeholder="Burst Time" required>
                </div>
            `;
            formContainer.innerHTML += htmlContent;
        }
    });
});
