class Station {
  constructor(position, orientation, size) {
    this.position = position;
    this.orientation = orientation;
    this.size = size;
    
    this.orientation.setMag(this.size);
    this.N = p5.Vector.add(this.position, this.orientation);
    let temp = createVector(-this.orientation.x, -this.orientation.y);
    this.S = p5.Vector.add(this.position, temp);
  }
  
  changeOrientation(orientation) {
    this.orientation = orientation;
  }
  
  // Update poles.
  update() {
    this.orientation.setMag(this.size);
    this.N = p5.Vector.add(this.position, this.orientation);
    let temp = createVector(-this.orientation.x, -this.orientation.y);
    this.S = p5.Vector.add(this.position, temp);
  }
  
  show() {
    push();
    stroke(255);
    strokeWeight(3);
    fill(150);
    rectMode(RADIUS);
    rect(this.position.x, this.position.y, this.size * 1.5, this.size * 1.5);
    
    let weight = 2;                  // strokeWeight for arrow.
    let temp = color(255, 0, 0);     // color for arrow.
    arrow(this.position, this.N, temp, weight);    // darwing N.
    
    temp = color(0, 0, 255);
    arrow(this.position, this.S, temp, weight);    // drawing S.
    
    point(this.position.x, this.position.y);       // point middle point.
    pop();
  }
}
