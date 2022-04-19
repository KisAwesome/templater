import sys
import os

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <script src="script.js"></script>
</body>
</html>"""


try:
    PROJ_NAME = sys.argv[1]

except:
    PROJ_NAME = 'Project'


if os.path.exists(f'/{PROJ_NAME}'):
    print(f'{PROJ_NAME} already exists in {os.getcwd()}')
    sys.exit()

os.mkdir(PROJ_NAME)

with open(f'{PROJ_NAME}/main.html', 'w') as f:
    f.write(HTML_TEMPLATE)

with open(f'{PROJ_NAME}/script.js', 'w') as f:
    f.write('')

with open(f'{PROJ_NAME}/style.css', 'w') as f:
    f.write('')
