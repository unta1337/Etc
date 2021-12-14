class Detector {
  constructor(position, size) {
    this.position = position;
    this.size = size;
  }
  
  // Return distance between detector and pole; determine the direction.
  detect(point) {
    return this.position.dist(point);
  }
  
  show() {
    stroke(255);
    fill(150);
    ellipse(this.position.x, this.position.y, this.size, this.size);
  }
}

class Sensor {
  constructor(position, size, detectorCount) {
    this.position = position;
    this.size = size;
    this.detectorCount = detectorCount;
    
    // Detector constructors: position, size.
    // Declare detectors around the sensor.
    this.detectors = new Array(this.detectorCount);
    for (let i = 0; i < this.detectorCount; i++) {
      let temp = p5.Vector.fromAngle(TWO_PI * (i / this.detectorCount), this.size);
      temp.add(this.position);
      this.detectors[i] = new Detector(temp, this.size * 0.1);
    }
  }
  
  // Update detectors base on changed position.
  update() {
    this.detectors = new Array(this.detectorCount);
    for (let i = 0; i < this.detectorCount; i++) {
      let temp = p5.Vector.fromAngle(TWO_PI * (i / this.detectorCount), this.size);
      temp.add(this.position);
      this.detectors[i] = new Detector(temp, this.size * 0.1);
    }
  }
  
  changePosition(position) {
    this.position = position; 
  }
  
  // Return nearest detector's index.
  detectDetector(point) {    
    let min = Infinity;
    let minIndex = 0;
    
    for (let i = 0; i < this.detectorCount; i++) {
      let temp = this.detectors[i].detect(point);
      if (temp < min) {
        min = temp
        minIndex = i;
      }
    }
    return minIndex;
  }
  
  // Show nearest detector and return centerToDetector vector.
  showFromDetector(point, polarity) {
    let minIndex = this.detectDetector(point);
    let minDetector = this.detectors[minIndex];
    
    // Exact vector.
    arrow(minDetector.position, point, color(255, 255, 255), 2);

    // Calculate approximated vector.
    let angle = TWO_PI * (minIndex / this.detectorCount);
    let distance = this.position.dist(point);
    let orientation = p5.Vector.fromAngle(angle, distance);
    let centerToDetector = p5.Vector.add(this.position, orientation);
    
    // Approximated vector.
    let tempColor = color(255, 0, 0);
    if (polarity)
      tempColor = color(0, 0, 255);
    arrow(this.position, centerToDetector, tempColor, 2);
    
    return orientation;
  }
  
  show() {
    stroke(255);
    strokeWeight(2);
    fill(150);
    ellipse(this.position.x, this.position.y, this.size, this.size);
   
    for (let detector of this.detectors) {
      detector.show(); 
    }
  }
}
