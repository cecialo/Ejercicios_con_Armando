from flask import Flask,render_template

app=Flask(__name__)

heroes_info= {
    'spiderman' :{
        "nombre":"Peter Parker",
        "nacionalidad":"USA",
        "poderes":"Teleraña",
        "fecha":"ENERO 1987",
        "picture":"https://www.tonica.la/__export/1585772919500/sites/debate/img/2020/04/01/spiderman_portada.jpg_423682103.jpg"
} ,
    'superman' :{
        "nombre":"Clar Ken",
        "nacionalidad":"USA",
        "poderes":"Fuerza",
        "fecha":"OCTUBRE 1980",
        "picture":"data:image/jpeg;base64,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"
},
    'chapulin' :{
        "nombre":"Roberto Bolaños",
        "nacionalidad":"Mexico",
        "poderes":"Habilidad",
        "fecha":"OCTUBRE 1975",
        "picture":"https://elcomercio.pe/resizer/XCfMPxToRkeXUi6DEF6dnRysoIM=/1200x1200/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/WPCSYPOK3BFHTOCVQHWMS66FII.jpg"
  }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detalles/<key>')
def detalles(key):
    return render_template('heroe.html',heroe=heroes_info[key])
    

app.run(debug=True,port=8000)