import os

from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ночные огни</title>
    <style>
        /* Определение шрифта */
       @font-face {
            font-family: PixelFont;
            src: url('{{ url_for('static', filename='pixeltimes.ttf') }}');
        }

        body {
            font-family: PixelFont;
  
        }

        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            background-image: url('{{ url_for('static', filename='cyberpunk_bg.jpg') }}');
            background-size: 100% 100%;
            background-repeat: no-repeat;
            background-position: center center;
            background-attachment: fixed;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: PixelFont;
            overflow: hidden;
        }

        .content {
            text-align: center;
            background: rgba(0, 0, 0, 0.5);
            padding: 20px;
            border-radius: 10px;
            animation: fadeIn 2s;
        }

        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }

        .title {
            color: #ffffff;
            font-size: 48px;
            margin-bottom: 20px;
        }

        .subtitle {
            color: #cccccc;
            font-size: 24px;
            margin-bottom: 20px;
        }

            button {
                 position: absolute;
                top: 10px; 
                left: 10px; 
                font-family: PixelFont;
                padding: 10px 20px;
                font-size: 20px;
                cursor: pointer;
                background-color: #ffffff;
                border: 2px solid #000000;
                border-radius: 5px;
                color: #000000;
                transition: background-color 0.3s, color 0.3s, box-shadow 0.3s;
            }

        button:hover {
            background-color: #000000;
            color: #ffffff;
            box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.5);
        }
        html {
            font-family: 'Times New Roman', sans-serif;
            font-size: 26px;
            font-smooth: auto;
            font-weight: bold;
            line-height: 1.5;
            color: white;
        }

        body {
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            height: 100vh;
        }

        div {
            font-size: 200px;
        }

        button:hover {
    background-color: #000000;
    color: #ffffff;
    box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.5);
}

button:hover:before, button:hover:after {
    font-size: 50px;
    position: fixed; 
    content: 'ALLERT';
    top: 30%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 1; 
}

button:hover:before {
    color: rgba(233, 30, 99, 0.8);
    animation: distort1 300ms linear infinite;
}

button:hover:after {
    color: rgba(3, 169, 244, 0.8);
    animation: distort2 300ms linear infinite;
}

@keyframes distort1 {
    0%    { top: 53.5%; left: 51.5%; }
    12.5% { top: 53.5%; left: 52%; }
    25%   { top: 53.5%; left: 52.5%; }
    37.5% { top: 54%; left: 52.5%; }
    50%   { top: 54.5%; left: 52.5%; }
    62.5% { top: 54.5%; left: 52%; }
    75%   { top: 54.5%; left: 51.5%; }
    87.5% { top: 54%; left: 51.5%; }
    100%  { top: 53.5%; left: 51.5%; }
}

@keyframes distort2 {
    0%    { top: 54.5%; left: 52.5%; }
    12.5% { top: 54%; left: 52.5%; }
    25%   { top: 53.5%; left: 52.5%; }
    37.5% { top: 53.5%; left: 52%; }
    50%   { top: 53.5%; left: 51.5%; }
    62.5% { top: 54%; left: 51.5%; }
    75%   { top: 54.5%; left: 51.5%; }
    87.5% { top: 54.5%; left: 52%; }
    100%  { top: 54.5%; left: 52.5%; }
}

    </style>
    <body>
        <div class="data">
            <canvas id="canvas"></canvas>
            <button onclick="handleRedirect()">Перейти</button>
            <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script>
        $(document).ready(function() {
  var canvas = $('#canvas')[0];
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  
  if(canvas.getContext) {
    var ctx = canvas.getContext('2d');
    var w = canvas.width;
    var h = canvas.height;
    ctx.strokeStyle = 'rgba(174,194,224,0.5)';
    ctx.lineWidth = 1;
    ctx.lineCap = 'round';
    
    
    var init = [];
    var maxParts = 1000;
    for(var a = 0; a < maxParts; a++) {
      init.push({
        x: Math.random() * w,
        y: Math.random() * h,
        l: Math.random() * 1,
        xs: -4 + Math.random() * 4 + 2,
        ys: Math.random() * 10 + 10
      })
    }
    
    var particles = [];
    for(var b = 0; b < maxParts; b++) {
      particles[b] = init[b];
    }
    
    function draw() {
      ctx.clearRect(0, 0, w, h);
      for(var c = 0; c < particles.length; c++) {
        var p = particles[c];
        ctx.beginPath();
        ctx.moveTo(p.x, p.y);
        ctx.lineTo(p.x + p.l * p.xs, p.y + p.l * p.ys);
        ctx.stroke();
      }
      move();
    }
    
    function move() {
      for(var b = 0; b < particles.length; b++) {
        var p = particles[b];
        p.x += p.xs;
        p.y += p.ys;
        if(p.x > w || p.y > h) {
          p.x = Math.random() * w;
          p.y = -20;
        }
      }
    }
    
    setInterval(draw, 30);
    
  }
});
            function handleRedirect() {
                const url = "https://netology.ru/";
                window.location.href = "/frame?url=" + encodeURIComponent(url);
            }
        </script>
    </body>
    </html>
    ''')

@app.route('/frame')
def frame():
    url = request.args.get('url')
    if url in ["127.0.0.1", "0.0.0.0"]:
        return f"Флаг: {os.environ.get('FLAG', 'no flag')}"

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Frame</title>
    </head>
    <body style="margin:0; padding:0; overflow:hidden;">
        <iframe src="{{ url }}" frameborder="0" style="overflow:hidden;height:100%;width:100%; position:absolute; top:0; left:0;"></iframe>
    </body>
    </html>
    ''', url=url)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
