


//loop through each row
while ($row = $result->fetch_assoc()) { 

	$currentDateGMT = gmdate("Y-m-d\TH:i:s\Z", time()); //current date in GMT
	$postDateGMT = gmdate("Y-m-d\TH:i:s\Z", strtotime($row['created'])); //created date in GMT
	$dateDiffInSeconds = strtotime($currentDateGMT) - strtotime($postDateGMT); //difference in seconds between the two dates
	$dateDiffInHours = floor($dateDiffInSeconds / 3600); //difference in hours between the two dates

	//output a paragraph with the info
	print <<<END
 
 <p>
 The current date is {$currentDateGMT} in GMT.<br />
 The post was created at {$postDateGMT} in GMT.<br />
 That's a difference of {$dateDiffInSeconds} minutes, or {$dateDiffInHours} hours. <br />
 </p>
  
END;

}


<?php

$mysqli = new mysqli(	"mysql.students.wd.onepotcooking.com", 
						"scps", 
						"#");
?>


Need to have ID 
Tweet 
Creation_time 
Flag 
