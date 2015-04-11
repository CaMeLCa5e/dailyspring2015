<?php
// connect to db
$cxn = mysql_connect(
	"dbserver: mysql.students.wd.onepotcooking.com ", 
	"scps",
	"##########",
	"classdb"

) or die("Sorry, we can't connect to the database at the moment");

$query = "SELECT * FROM jmartin_coffees"; 
// $cxn=>query($query);
// $result = $cxn->query($query);
	

$result = $cxn->query($query);	
mysql_error($cxn);

// show results 
while($row = $result->fetch_assoc()) {
	print_r($row);
}


	echo "<article>"
	if(!empty(echo "<h1>" . $row["roast_type"] . "roast</p>"
		))
	echo "<type>"
	echo "<more_stff>"

?>
<!DOCTYPE html>
<html>
<head>
	<title>Coffee notes</title>
</head>
<body>
	<h1>stuff</h1>
	<h2><?php echo $row["brand"]; 
		if(!empty(echo "<h1>" . $row["roast_type"] . "roast</p>"
?>



	</h2>
	<p>more stuff</p>
</body>
</html>

















?>