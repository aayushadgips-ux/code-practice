<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Happy Birthday Aayush 🎉</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background: linear-gradient(135deg, #ff9a9e, #fad0c4);
      font-family: Arial, sans-serif;
      overflow: hidden;
    }
    .card {
      background: white;
      padding: 30px;
      border-radius: 20px;
      text-align: center;
      box-shadow: 0 8px 20px rgba(0,0,0,0.2);
      position: relative;
      z-index: 2;
    }
    h1 {
      color: #ff4b5c;
      font-size: 36px;
      margin-bottom: 10px;
    }
    p {
      font-size: 20px;
      color: #444;
      margin-bottom: 20px;
    }
    button {
      background: #ff4b5c;
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: 10px;
      font-size: 16px;
      cursor: pointer;
      transition: 0.3s;
    }
    button:hover {
      background: #ff6b7d;
    }
    .balloon {
      position: absolute;
      bottom: -150px;
      width: 50px;
      height: 70px;
      background: red;
      border-radius: 50% 50% 50% 50%;
      animation: float 8s infinite ease-in;
    }
    .balloon::after {
      content: "";
      position: absolute;
      width: 2px;
      height: 60px;
      background: #555;
      top: 70px;
      left: 50%;
      transform: translateX(-50%);
    }
    @keyframes float {
      0% { transform: translateY(0) scale(1); opacity: 1; }
      100% { transform: translateY(-120vh) scale(1.1); opacity: 0; }
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>🎉 Happy Birthday Aayush 🎉</h1>
    <p>Dear Aayush, wishing you lots of happiness, success, and joy on your special day! You are more than a friend, you are a brother ❤️</p>
    <button onclick="launchBalloons()">Click for Surprise 🎈</button>
  </div>  <script>
    function launchBalloons() {
      for (let i = 0; i < 20; i++) {
        let balloon = document.createElement("div");
        balloon.className = "balloon";
        balloon.style.left = Math.random() * 100 + "vw";
        balloon.style.background = randomColor();
        balloon.style.animationDuration = (5 + Math.random() * 5) + "s";
        document.body.appendChild(balloon);
        setTimeout(() => balloon.remove(), 10000);
      }
    }

    function randomColor() {
      const colors = ["#ff4b5c", "#ffcc29", "#6bcdfd", "#9d65c9", "#4cd137"];
      return colors[Math.floor(Math.random() * colors.length)];
    }
  </script></body>
</html>