document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('generateForm').addEventListener('click', function() {
        var numProcesses = document.getElementById('num_processes').value;
        var formContainer = document.getElementById('processesForm');
        formContainer.innerHTML = ''; // Clear previous inputs
        for (let i = 1; i <= numProcesses; i++) {
            var htmlContent = `
                <div class="form-group">
                    <label for="arrival_time_${i}">Arrival Time for Process ${i}</label>
                    <input type="number" class="form-control" name="arrival_time_${i}" required>
                    <label for="burst_time_${i}">Burst Time for Process ${i}</label>
                    <input type="number" class="form-control" name="burst_time_${i}" required>
                </div>
            `;
            formContainer.innerHTML += htmlContent;
        }
    });
});
