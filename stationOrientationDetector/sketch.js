// Station orientation detectior via magnetic filed.

let station, sensorN, sensorS;

function setup() {
  createCanvas(windowWidth, windowHeight);
  
  // Station constructors: position, orientation, size.
  let position = createVector(0, 0);
  let orientation = createVector(1, 0);
  let size = windowWidth > windowHeight ? windowWidth * 0.05 : windowHeight * 0.05;
  station = new Station(position, orientation, size);
  
  // Sensor constructors: position, size, detectorCount.
  position = createVector(width / 4, height / 4);
  let sensorCount = 32;
  sensorN = new Sensor(position, size, sensorCount);
  
  position = createVector(-width / 4, -height / 4);
  sensorS = new Sensor(position, size, sensorCount);
  
  // arrow arguments: v1, v2, color, weight.
}

function draw() {
  background(51);
  translate(width / 2, height / 2);
  
  // Random location for the sensors.
  if (frameCount % 100 == 0) {
    let tempX = random(width / 2, -width / 2);
    let tempY = random(height / 2, -height / 2);
    sensorN.changePosition(createVector(tempX, tempY));
    sensorN.update();
    
    tempX = random(width / 2, -width / 2);
    tempY = random(height / 2, -height / 2);
    sensorS.changePosition(createVector(tempX, tempY));
    sensorS.update();
  }
  
  // Rotation for the station.
  let newOrientation = p5.Vector.fromAngle(-frameCount * 0.01);
  station.changeOrientation(newOrientation);
  station.update();
  station.show();
  
  // Show sensors and recieve its approximated vectors.
  sensorN.show();
  let approximationN = sensorN.showFromDetector(station.N, 0);
  sensorS.show();
  let approximationS = sensorS.showFromDetector(station.S, 1);
  
  // Draw approximated orientation vector.
  approximationN.add(sensorN.position);
  approximationS.add(sensorS.position);
  let approximationOrientation = p5.Vector.sub(approximationN, approximationS);
  approximationOrientation.setMag(station.size * 2.5);
  let approximationSN = p5.Vector.add(sensorN.position, approximationOrientation);
  arrow(sensorN.position, approximationSN, color(0, 255, 255), 3);
  
  // Approximated vector from center.
  temp = p5.Vector.add(createVector(0, 0), approximationSN);
  arrow(createVector(0, 0), approximationOrientation, color(0, 255, 255), 3);
}
