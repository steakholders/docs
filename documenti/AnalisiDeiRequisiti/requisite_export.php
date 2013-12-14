<?php

$host = "ec2-54-225-101-18.compute-1.amazonaws.com";
$database = "d93tdenfffgafv";
$user = "celknguofrtklt";
$port = 5432;
$password = "Qho2ERigotE3KJ829RTg3jsmXe";

$connessione = "host=$host port=$port dbname=$database user=$user password=$password";

$db = pg_connect($connessione);

if (!$db) {
	print "Errore di connessione al database!";	
	return;
}

$title = array();
$desc = array();
$rif = array();

$query = "select id, title, description from requisites order by title desc";

$arr = pg_fetch_all(pg_query($db,$query));

for ($i=0; $i<count($arr); $i++) {
	$aux = $arr[$i];
	array_push($title,$aux["title"]);
	array_push($desc,$aux["description"]);
	$query = "select use_case_id from requisites_use_cases where requisite_id = " . $aux["id"];
	$fonti = pg_fetch_all(pg_query($db,$query));
	$string = "";
	if (!empty($fonti)) {
		for ($j=0; $j<count($fonti); $j++) {
			$query = "select title from use_cases where id = " . $fonti[$j]["use_case_id"];
			$f = pg_fetch_row(pg_query($db,$query));
			$string .= $f[0] . "\\";	
		} 
	}
	array_push($rif,$string);
}

print "\begin{tabular}{ l | c | r }<br/>";
for ($i=0; $i<count($title); $i++) {
	print "$title[$i] & $desc[$i] & $rif[$i] \\\<br/>";

}
print "\end{tabular}";
?>
