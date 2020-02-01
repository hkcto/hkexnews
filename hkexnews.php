<?php
$url = "https://www1.hkexnews.hk/search/titlesearch.xhtml?lang=en";
 
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query(array("lang"=>"en", "category"=>"0", "market"=>"SEHK", "searchType"=>"-1", "t1code"=>"-2", "t2Gcode"=>"-2", "t2code"=>"-2", "stockId"=>"1000016998", "from"=>"19990401", "to"=>"20191230", "MB-Daterange"=>"0", "title"=>""))); 
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 0);
$output = curl_exec($ch); 
curl_close($ch);
 
//echo $output;

$re = '<table(.|\n)*<\/table>';
$isMatched = preg_match($re, $output, $matches);

// Print the entire match result
var_dump($isMatched, $matches);
// echo $matches;

?>