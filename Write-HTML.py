#write-html.py

f= open('invoice.html','w')

message = """
<html>
    <head>
    <?php
    $file = 'invnum.txt'; // the name of the text file (must be writeable by the server)
    $invnumber = file_get_contents ($file); // read file data and store as variable
    ?>
    </head>
    <style>
    table {
        display: table;
        border-collapse: collapse;
        border-spacing: 2px;
        border-color: Black;
    }
    table, th, td {
        border: 1px solid black;
        vertical-align: top;
        text-align: left;
    }
    </style>
    <body>
    <img src="https://i.imgur.com/BEX6Cin.png">
    <br>
        <strong><p align="left"> Invoice: <?php
$invnum = file_get_contents('invnum.txt);
echo $invnum;
?>
</p></strong>
        <strong><p align="left">Date: <SCRIPT LANGUAGE="Javascript">
<!-- 

// Array of day names
var dayNames = new Array("Sunday","Monday","Tuesday","Wednesday",
				"Thursday","Friday","Saturday");

// Array of month Names
var monthNames = new Array(
"January","February","March","April","May","June","July",
"August","September","October","November","December");

var now = new Date();
document.write(now.getDate() + " " + monthNames [now.getMonth()] + " " + now.getFullYear())

// -->
</SCRIPT>
        </p></strong>
        <br>
        <strong>Provider Details:</strong>
        <p>Jane M Clark</p>
        <p>Provider No: 4239236L</p>
        <br>
        <p>ReAct Physiotherapy</p>
        <p>229b Old South Road,</p>
        <p>Old Reynella, SA 5161</p>
        <br>
        <p>ABN: 42 181 849 819</p>
        <table>
            <tr>
                <th>AGED CARE FACILITY</th>
                <th>SERVICES PROVIDED</th>
            </tr>
            <tr>
                <td>The Vales Aged Care Facility 60/66 <br>
                States Road, Morphett Vale SA 5162, <br>
                Australia</td>
                <td>Physiotherapy</td>
            </tr>
        </table>
        <br>
        <br>
        <table>
            <tr>
                <th>Date Fortnight Ending</th>
                <th>Service Description</th>
                <th>Hours</th>
                <th>Fee per hour</th>
                <th>Total</th>
            </tr>
            <tr>
                <td><SCRIPT LANGUAGE="Javascript">
<!-- 

// Array of day names
var dayNames = new Array("Sunday","Monday","Tuesday","Wednesday",
				"Thursday","Friday","Saturday");

// Array of month Names
var monthNames = new Array(
"January","February","March","April","May","June","July",
"August","September","October","November","December");

var now = new Date();
document.write(now.getDate() + " " + monthNames [now.getMonth()] + " " + now.getFullYear())

// -->
</SCRIPT></td>
                <td>General physiotherapy and pain management</td>
                <td>8</td>
                <td>59.18</td>
                <td>473.44</td>
            </tr>
        </table>
        <br>
        <strong><p>Payment: $473.44</p></strong>
        <br>
        <strong><p>EFT Payment Details:</strong></p>
        <strong><p>Bank:</strong> Beyond Bank</p>
        <strong><p>Account Name:</strong> Mrs Jane M Clark</p>
        <strong><p>BSB:</strong> 325-185</p>
        <strong><p>Account Number:</strong> 03373600</p>
        <img src="https://i.imgur.com/B6l2vlG.png">
    </body>
</html>"""

f.write(message)
f.close()