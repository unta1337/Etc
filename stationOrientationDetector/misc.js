function arrow(v1, v2, color, weight) {
  let xAxis = createVector(1, 0);
  let temp = p5.Vector.sub(v2, v1);
  let angle = xAxis.angleBetween(temp);
  
  push();
  stroke(color);
  strokeWeight(weight);
  line(v1.x, v1.y, v2.x, v2.y);
  translate(v2.x, v2.y);
  push();
  rotate(angle);
  line(0, 0, -5, -5);
  line(0, 0, -5, 5);
  pop();
  pop();
}
