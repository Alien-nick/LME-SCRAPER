<?php

// Basic router function
function route($uri, $script) {
    if ($_SERVER['REQUEST_URI'] === $uri) {
        // Execute the Python script and capture its output
        $output = shell_exec("python3 $script");

        // Decode the output as JSON
        $data = json_decode($output);

        // Return the JSON data
        header('Content-Type: application/json');
        echo json_encode($data);
        exit;
    }
}

// Define your routes
route('/zinc', 'zinc-scraper.py');
route('/copper', 'copper-scraper.py');
route('/aluminum', 'aluminum-scraper.py');
route('/cobalt', 'cobalt-scraper.py');
route('/nickel', 'nickel-scraper.py');
route('/tin', 'tin-scraper.py');
route('/lme', 'lme-scraper.py');
route('/lead', 'lead-scraper.py');

// If no route matches, return a 404 response
header("HTTP/1.0 404 Not Found");
echo json_encode(['error' => 'Not Found']);

?>
