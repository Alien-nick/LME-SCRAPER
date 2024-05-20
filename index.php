<?php

// Execute the Python script and capture its output
$output = shell_exec("python3 zinc.py");

// Decode the output as JSON
$data = json_decode($output);

// Return the JSON data
header('Content-Type: application/json');
echo json_encode($data);

?>
