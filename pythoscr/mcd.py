
from flask import Flask, render_template,request


app = Flask(__name__)
app.config['SECRET_KEY'] ='DSADASDASDAS'
app.debug = True
def is_hex(s):
    try:
        int(s, 16)
    except ValueError:
        return "NO hex value given"
    return len(s) % 2 == 0

@app.route("/", methods=['POST','GET'])
def mov():
    if request.method == 'POST':
        ax = request.form.get('ax')
        bx = request.form.get('bx')
        cx = request.form.get('cx')
        dx = request.form.get('dx')
        mov_z = request.form.get('z')
        mov_do = request.form.get('do')
        print("fdsf")
        print(request.form.get('exchange'))
        if request.form.get('exchange') =="exchange":
            if mov_z == "ax":
                
                if mov_do == "ax":
                    return render_template("tes.html",ax=ax,bx=bx,cx=cx,dx=dx)
                
                elif mov_do == "bx":
                    return render_template("tes.html",ax=bx,bx=ax,cx=cx,dx=dx)
                elif mov_do == "cx":
                    return render_template("tes.html",ax=cx,bx=bx,cx=ax,dx=dx)
                elif mov_do == "dx":
                    return render_template("tes.html",ax=dx,bx=bx,cx=cx,dx=ax)
            
            elif mov_z == "bx":
                
                if mov_do == "ax":
                    return render_template("tes.html",ax=bx,bx=ax,cx=cx,dx=dx)
                
                elif mov_do == "bx":
                    return render_template("tes.html",ax=ax,bx=bx,cx=cx,dx=dx)
                elif mov_do == "cx":
                    return render_template("tes.html",ax=ax,bx=cx,cx=bx,dx=dx)
                elif mov_do == "dx":
                    return render_template("tes.html",ax=ax,bx=dx,cx=cx,dx=bx)

            elif mov_z == "cx":
                
                if mov_do == "ax":
                    return render_template("tes.html",ax=cx,bx=bx,cx=ax,dx=dx)
                
                elif mov_do == "bx":
                    return render_template("tes.html",ax=ax,bx=cx,cx=bx,dx=dx)
                elif mov_do == "cx":
                    return render_template("tes.html",ax=ax,bx=bx,cx=cx,dx=dx)
                elif mov_do == "dx":
                    return render_template("tes.html",ax=ax,bx=bx,cx=dx,dx=cx)

            elif mov_z == "dx":
                
                if mov_do == "ax":
                    return render_template("tes.html",ax=dx,bx=bx,cx=cx,dx=ax)
                
                elif mov_do == "bx":
                    return render_template("tes.html",ax=ax,bx=dx,cx=cx,dx=bx)
                elif mov_do == "cx":
                    return render_template("tes.html",ax=ax,bx=bx,cx=dx,dx=cx)
                elif mov_do == "dx":
                    return render_template("tes.html",ax=ax,bx=bx,cx=cx,dx=dx)

        if request.form.get('mov') =="mov":
            if mov_z == "ax":
                
                if mov_do == "ax":
                    return render_template("tes.html",ax=ax,bx=bx,cx=cx,dx=dx)
                
                elif mov_do == "bx":
                    return render_template("tes.html",ax=ax,bx=ax,cx=cx,dx=dx)
                elif mov_do == "cx":
                    return render_template("tes.html",ax=ax,bx=bx,cx=ax,dx=dx)
                elif mov_do == "dx":
                    return render_template("tes.html",ax=ax,bx=bx,cx=cx,dx=ax)
            
            elif mov_z == "bx":
                
                if mov_do == "ax":
                    return render_template("tes.html",ax=bx,bx=bx,cx=cx,dx=dx)
                
                elif mov_do == "bx":
                    return render_template("tes.html",ax=ax,bx=bx,cx=cx,dx=dx)
                elif mov_do == "cx":
                    return render_template("tes.html",ax=ax,bx=bx,cx=bx,dx=dx)
                elif mov_do == "dx":
                    return render_template("tes.html",ax=ax,bx=bx,cx=cx,dx=bx)

            elif mov_z == "cx":
                
                if mov_do == "ax":
                    return render_template("tes.html",ax=cx,bx=bx,cx=cx,dx=dx)
                
                elif mov_do == "bx":
                    return render_template("tes.html",ax=ax,bx=cx,cx=cx,dx=dx)
                elif mov_do == "cx":
                    return render_template("tes.html",ax=ax,bx=bx,cx=cx,dx=dx)
                elif mov_do == "dx":
                    return render_template("tes.html",ax=ax,bx=bx,cx=cx,dx=cx)

            elif mov_z == "dx":
                
                if mov_do == "ax":
                    return render_template("tes.html",ax=dx,bx=bx,cx=cx,dx=dx)
                
                elif mov_do == "bx":
                    return render_template("tes.html",ax=ax,bx=dx,cx=cx,dx=dx)
                elif mov_do == "cx":
                    return render_template("tes.html",ax=ax,bx=bx,cx=dx,dx=dx)
                elif mov_do == "dx":
                    return render_template("tes.html",ax=ax,bx=bx,cx=cx,dx=dx)
                
                


    return render_template("tes.html",ax="21E4",bx="1DE5",cx="14DF",dx="0C8C")




if __name__ == "__main__":
    app.run()