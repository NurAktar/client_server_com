<?php
error_reporting(E_ERROR | E_PARSE);
try {
$id = $_GET['id'];

// Connect to SQLite database
$db = new SQLite3('database.db');

// Query database
$query = "SELECT * FROM students WHERE id = $id";
$result = $db->query($query);

// Display result
$row = $result->fetchArray(SQLITE3_ASSOC);
if ($row) {
    echo "Name: " . $row['name'] . "<br>";
    echo "Percentage: " . $row['percentage'] . "<br>";
    echo "Locality: " . $row['locality'] . "<br>";
    echo "Roll No: " . $row['roll_no'] . "<br>";
} else {
    echo "Student not found";
}

// Close database connection
$db->close();
} catch (\Throwable) {
    echo "Something is wrong!";
}

?>
