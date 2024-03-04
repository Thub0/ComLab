from flask import Flask

app = Flask (__name__)

@app.route('/<opt>/<float:a>/<float:b>')
def cul(opt,a,b):
    ans = None
    if opt == 'add':
        ans = a + b
    elif opt == 'sub':
        ans = a - b
    elif opt == 'mul':
        ans = a * b
    elif opt == 'div':
        if b != 0:
            ans = a/b
        else:
            return 'div by 0'
    
    return f'ans:{ans}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
