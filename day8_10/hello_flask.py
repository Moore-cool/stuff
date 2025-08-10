from flask import Flask
 
app = Flask(__name__) 
 
@app.route('/')
def hello_world():
    return '''<!DOCTYPE html>

<html>
<head>
    <title>My first website!</title>
</head>
<body>
    <script type="text/python">
        print("hello")
    </script>
    <h1>LINKS</h1>
    <a href="https://www.google.com" target=_self title="title takes you to google">
        <p><h1>Google</h1></p>
    </a>

    <a href="https://portal.achieve3000.com/index?lg=%2Fhome" target=_self title="title takes you to A3000">
        <p><h1>A3000</h1></p>
    </a>

    <a href="https://poki.com/zh/g/narrow-one" target=_self title="title takes you to a game">
        <p><h1>Game</h1></p>
    </a>

    <h1>TEST RESULTS</h1>
    <table bgcolor="black" align="center" width="920">
        <tr bgcolor="grey" align="center">
            <th width="120">Grade</th>
            <th width="100">Total</th>
            <th width="100">Chinese</th>
            <th width="100">Maths</th>
            <th width="100">English</th>
            <th width="100">History</th>
            <th width="100">Biology</th>
            <th width="100">Geography</th>
            <th width="100">Morality</th>
        </tr>
        <tr bgcolor="lightgrey" align="center">
            <td>
                First 1S 7th
            </td>
            <td>84th</td>
            <td>76,290th</td>
            <td>95,8th</td>
            <td>87.5,113rd</td>
            <td>49,130th</td>
            <td>45,42nd</td>
            <td>45,97th</td>
            <td>31.5,207th</td>
        </tr>
        <tr bgcolor="lightgrey" align="center">
            <td>
                Second 1S 7th
            </td>
            <td>127th</td>
            <td>87.5,220th</td>
            <td>88,177th</td>
            <td>94.75,14rd</td>
            <td>52,146th</td>
            <td>44,73nd</td>
            <td>40,104th</td>
            <td>37,189th</td>
        </tr>
        <tr bgcolor="lightgrey" align="center">
            <td>
                First 2S 7th</td>
            <td>166th</td>
            <td>82.5,326th</td>
            <td>90,32th</td>
            <td>92.5,23rd</td>
            <td>54,190th</td>
            <td>26,276nd</td>
            <td>32,185th</td>
            <td>35,258th</td>
        </tr>
        <tr bgcolor="lightgrey" align="center">
            <td>
                Second 2S 7th</td>
            <td>215th</td>
            <td>86.5,202th</td>
            <td>96,31th</td>
            <td>87,171st</td>
            <td>57,221st</td>
            <td>35,207th</td>
            <td>26,354th</td>
            <td>27,353th</td>
        </tr>
    </table>
</body>
</html>''' 
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1314) 