import time, os, datetime
def test():
    rs = '';
    for i in range(4):
        body = "jenkkins test demo! git testing: " + str(datetime.datetime.now())
        print(body)
        rs += "<li>" + body + "</li>"
        time.sleep(1)
    with open('report/repoart_demo.html', 'w+') as f:
        temp = '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>report</title>
            </head>
            <body>
                <ul>
        ''' + rs + "</ul></body></html>"
        f.write(temp)
if __name__ == '__main__':
	test()