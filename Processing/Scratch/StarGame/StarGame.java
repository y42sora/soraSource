import processing.core.*; 
import processing.xml.*; 

import java.applet.*; 
import java.awt.Dimension; 
import java.awt.Frame; 
import java.awt.event.MouseEvent; 
import java.awt.event.KeyEvent; 
import java.awt.event.FocusEvent; 
import java.awt.Image; 
import java.io.*; 
import java.net.*; 
import java.text.*; 
import java.util.*; 
import java.util.zip.*; 
import java.util.regex.*; 

public class StarGame extends PApplet {

// \u91cd\u529b\u306e\u5927\u304d\u3055\u3000\u9069\u5f53
float gravity = 0.098f;

// \u661f\u304c\u6c38\u9060\u306b\u751f\u304d\u7d9a\u3051\u308b\u306e\u3092\u56de\u907f
static final int TIMELIMIT = 10000;

// \u6700\u9ad8\u901f\u5ea6 \u4f4e\u3059\u304e\u308b\u3068\u91cd\u529b\u3092\u632f\u308a\u5207\u308c\u306a\u3044
static final int MAXSPEED = 20;

/*
 * \u8907\u6570\u4e09\u89d2\u5f62\u3092\u8868\u793a\u3059\u308b\u30af\u30e9\u30b9
 * \u661f\u306f\u4e09\u89d2\u5f62\u306e\u96c6\u307e\u308a\u3067\u63cf\u753b\u3067\u304d\u308b
 */
class TriangleDrawing {
  /*
   * \u4e94\u8292\u661f\u306f10\u500b\u306e\u70b9\u304b\u3089\u306a\u308b
   */
  float px[] = new float[10];
  float py[] = new float[10];

  /*
   * \u661f\u306e\u5927\u304d\u3055\u3092\u6307\u5b9a\u3057\u3066\u4e94\u8292\u661f\u3092\u66f8\u304f
   */
  TriangleDrawing(int r) {
    setT( r);
  }
  
  /*
   * \u4e94\u8292\u661f\u306f\u5f62\u306f\u6c7a\u307e\u3063\u3066\u3044\u308b\u306e\u3067\u3001\u9577\u3055\u3092\u3069\u3046\u5909\u5316\u3055\u305b\u308b\u304b\u3060\u3051
   */
  public void setT(int r) {
    float rad = 36.0f;

    for (int i=0; i<10; i++) {
      if (i % 2 == 0) {
        px[i] = sin(radians(rad*i))  *r;
        py[i] = cos(radians(rad*i))  *r;
      }
      else {
        px[i] = sin(radians(rad*i))  *r/3.0f;
        py[i] = cos(radians(rad*i))  *r/3.0f;
      }
    }
  }

  /*
   * \u6307\u5b9a\u3055\u308c\u305f\u5ea7\u6a19(x,y)\u306brad\u3060\u3051\u56de\u8ee2\u3055\u305b\u3066col\u8272\u3067\u63cf\u753b\u3059\u308b
   * \u4e94\u8292\u661f\u306f\u4e2d\u5fc3\u70b9\u3068\u92ed\u89d2\u306e\u70b9\u3068\u920d\u89d2\u306e\u70b9\u3067\u4f5c\u3089\u308c\u308b10\u500b\u306e3\u89d2\u5f62\u3067\u63cf\u753b\u3067\u304d\u308b
   */
  public void drawStar(float x, float y, float rad, int col) {
    translate(x, y);
    rotate(rad);

    fill(col);

    for (int i=1; i<10; i++)
      triangle(0, 0, px[i-1], py[i-1], px[i], py[i]);
    triangle(0, 0, px[0], py[0], px[9], py[9]);

    rotate(-rad);
    translate(-x, -y);
  }
}


/*
 * \u4e00\u500b\u4e00\u500b\u306e\u30d1\u30fc\u30c6\u30a3\u30af\u30eb\u7ba1\u7406\u3059\u308b
 */
class Particle {
  float x, y;
  float vx, vy;

  int col;
  
  // \u751f\u5b58\u6642\u9593
  int count;

  int r;  
  
  // \u521d\u671f\u56de\u8ee2\u89d2\u3068\u56de\u8ee2\u901f\u5ea6
  float rad, radSpeed;
  TriangleDrawing triangles[];

  /*
   * \u30d1\u30fc\u30c6\u30a3\u30af\u30eb\u306e\u73fe\u5728\u4f4d\u7f6e\u3068\u79fb\u52d5\u30d9\u30af\u30c8\u30eb\u3001\u661f\u306e\u5927\u304d\u3055\u3068\u304a\u3088\u3073\u661f\u306e\u30c7\u30fc\u30bf\u3092\u3068\u308b
   * \u661f\u306e\u5f62\u306f\u307f\u3093\u306a\u540c\u3058\u306a\u306e\u3067\u5927\u304d\u3055\u4e8b\u306b\u5f62\u3092\u8a08\u7b97\u3057\u305f\u914d\u5217\u3092\u4f7f\u3044\u3001\u305d\u308c\u3092\u4f7f\u3044\u56de\u3059
   */
  Particle(float nx, float ny, float nvx, float nvy, float r, TriangleDrawing triangles[] ) {
    x = nx;
    y = ny;
    vx = nvx;
    vy = nvy;
    col = color(0, 0, 0);

    this.radSpeed = random(0, 10);
    this.count = 0;
    this.r = (int)r;
    this.rad = random(0, 360);  
    this.triangles = triangles;
  }

  /*
   * \u518d\u5ea6\u521d\u671f\u5316\u3059\u308b
   */
  public void setInit(float x, float y, float vx, float vy) {
    this.x = x;
    this.y = y;
    this.vx = vx;
    this.vy = vy;
  }

  public void setColor(int newcol) {
    col = newcol;
  }

  public void draw() {
    rad = (rad+radSpeed) % 360.0f;
    // \u3053\u306e\u30d1\u30fc\u30c6\u30a3\u30af\u30eb\u306e\u5927\u304d\u3055\u306e\u661f\u3092\u63cf\u753b\u3059\u308b
    triangles[r].drawStar(x, y, radians(rad), col);
  }

  /*
   * \u6307\u5b9a\u3055\u308c\u305f\u91cd\u529b\u70b9\u306e\u91cd\u529b\u3092\u8003\u616e\u3057\u3066\u3001\u6b21\u306e\u79fb\u52d5\u30d9\u30af\u30c8\u30eb\u3092\u8a08\u7b97\u3059\u308b
   * \u91cd\u529b\u70b9\u304c\u4e00\u3064\u3068\u306f\u9650\u3089\u306a\u3044\u306e\u3067\u3001\u5b9f\u969b\u306b\u79fb\u52d5\u3059\u308b\u306e\u306f\u5225\u306e\u6240
   */
  public void setMoving(float gx, float gy) {
    float dx = x - gx;
    float dy = y - gy;
    float l = sqrt(dx * dx + dy * dy);
    if (l > 0.0001f) {
      dx = dx / (l * l * l) * 1000;
      dy = dy / (l * l * l) * 1000;
      vx -= dx;
      vy -= dy;

      if (MAXSPEED < vx)
        vx = MAXSPEED;
      if (MAXSPEED < vy)
        vy = MAXSPEED;
      if (vx < -MAXSPEED)
        vx = -MAXSPEED;
      if (vy < -MAXSPEED)
        vy = -MAXSPEED;
    }
  }

  /*
   * \u79fb\u52d5\u3055\u305b\u308b
   */
  public void move() {
    count++;
    vy += gravity;
    x += vx;
    y += vy;
  }

  /*
   * \u753b\u9762\u4e0a\u306b\u5b58\u5728\u3059\u308b\u304b\u3092\u5224\u5b9a
   * \u751f\u5b58\u3067\u304d\u308b\u6642\u9593\u5185\u3067\u3001\u753b\u9762\u306e\u56db\u89d2\u306e\u4e2d\u306b\u3044\u308b\u5834\u5408\u306e\u307ftrue\u3092\u8fd4\u3059
   */
  public boolean isInRect(int x, int y, int w, int h) {
    if (TIMELIMIT<count) return false;

    if (x <= this.x && this.x <= w)
      if (y <= this.y && this.y <= h)
        return true;
    return false;
  }
}


/*
 * \u9802\u70b9\u30af\u30e9\u30b9
 * java\u306e\u304c\u3042\u308b\u3051\u3069\u2026
 * \u5b9f\u306f\u91cd\u529b\u70b9\u306b\u3057\u304b\u4f7f\u3063\u3066\u306a\u3044
 * \u3044\u3064\u304b\u661f\u306e\u4e2d\u5fc3\u3082\u3053\u308c\u3067\u7ba1\u7406\u3059\u308b\u3088\u3046\u306b\u2026
 */
class Point {
  float x;
  float y;
  Point(float x, float y) {
    this.x = x;
    this.y = y;
  }
}

/*
 * \u5186\u306e\u30af\u30e9\u30b9
 * \u4e2d\u5fc3\u70b9\u3068\u534a\u5f84
 * \u5f8c\u308d\u306e\u661f\u306b\u3057\u304b\u4f7f\u3063\u3066\u306a\u3044
 */
class Circle extends Point{
  float r;
  Circle(float x,float y,float r){
    super(x,y);
    this.r = r;
  } 
}


/*
 * \u5de6\u5074\u306e\u30b9\u30b3\u30a2\u306e\u7dda\u3092\u7ba1\u7406\u3059\u308b\u30af\u30e9\u30b9
 */
class ScoreLine {
  // x\u5ea7\u6a19\u3068\u30b4\u30fc\u30eb\u30d0\u30fc\u306e\u79fb\u52d5\u901f\u5ea6
  int x, vy;
  
  // \u30b4\u30fc\u30eb\u30d0\u30fc\u306e\u4f4d\u7f6e\u3068\u9577\u3055
  int goalPoint, goalLength;
  
  // \u5f97\u70b9
  int score;

  /*
   * \u63cf\u753b\u4f4d\u7f6e\u3068\u3001\u30b4\u30fc\u30eb\u30d0\u30fc\u306e\u5834\u6240\u3068\u9577\u3055\u3092\u6307\u5b9a\u3059\u308b
   */
  ScoreLine(int x, int vy, int goalPoint, int goalLength) {
    this.x = x;
    this.vy = vy;
    this.goalPoint = goalPoint;
    this.goalLength = goalLength;

    score = 0;
  }

  /*
   * \u30b4\u30fc\u30eb\u30d0\u30fc\u3068\u7dda\u3092\u66f8\u304f
   */
  public void drawLine() {
    if (height < goalPoint + vy + goalLength)
      vy = -vy;
    if (goalPoint + vy < 0)
      vy = -vy;
    goalPoint += vy;

    strokeWeight(4);
    stroke(color(0, 0, 255));
    line(x, 0, x, height); 

    stroke(color(255, 255, 0));
    line(x, goalPoint, x, goalPoint+goalLength);
  }
  
  /*
   * \u5185\u5074\u306e\u8679\u8272\u306e\u5f97\u70b9\u3092\u66f8\u304f
   * HSB\u8272\u7a7a\u9593\u3067\u5897\u3084\u3057\u3066\u3044\u304f\u3060\u3051
   */
  public void drawScore() {
    noStroke();
    fill(0, 0, 0);
    rect(0, 0, x, height);  

    colorMode(HSB, height);
    strokeWeight(1);
    for (int i=0; i<score;i++) {
      stroke(i+1, height,height);
      line(0,height - i, x-2, height - i);
    }
    colorMode(RGB,255);
  }
  
  /*
   * \u30b9\u30b3\u30a2\u30e9\u30a4\u30f3\u3092\u63cf\u753b\u3059\u308b
   */
  public void drawScoreLine() {
    drawLine();
    drawScore();
  }

  /*
   * \u6307\u5b9a\u3057\u305f\u9802\u70b9\u304c\u30b4\u30fc\u30eb\u306b\u5165\u3063\u305f\u304b\u3069\u3046\u304b\u3002
   * \u5165\u3063\u3066\u3044\u305f\u3089\u30b9\u30b3\u30a2\u306br\u3092\u52a0\u7b97\u3057\u3066true\u3092\u8fd4\u3059
   */
  public boolean isInGoal(float x, float y,int r) {
    if (x <= this.x) {
      if (goalPoint <= y) {
        if (y <= goalPoint+goalLength) {
          score += r;
          return true;
        }
      }
    }
    return false;
  }
}


/*
 * \u65b0\u3057\u3044\u30d1\u30fc\u30c6\u30a3\u30af\u30eb\u3092\u4f5c\u6210\u3059\u308b
 */ 
public Particle makeNewPartcile() {
  Particle p = new Particle(startx, starty, -1*random(2, 10), random(2, 5), random(1, triangleNum), triangles);
  p.setColor(color(random(30, 255), random(30, 255), random(30, 255), random(90, 100)));
  return p;
}


// \u30d1\u30fc\u30c6\u30a3\u30af\u30eb\u306e\u6700\u5927\u6570\u3068\u305d\u306e\u914d\u5217
int pmax = 200;
Particle particles[];

// \u4e94\u8292\u661f\u306e\u5927\u304d\u3055\u3092\u6307\u5b9a\u3059\u308b
int triangleNum = 21;
TriangleDrawing triangles[];

// \u30a6\u30a3\u30f3\u30c9\u30a6\u306e\u5927\u304d\u3055\u3068\u304b
int seihou = 500;
int width = 800;
int height = 500;

// \u661f\u304c\u3069\u3053\u304b\u3089\u751f\u307e\u308c\u308b\u304b
int startx = width;
int starty = 0;

// \u8a2d\u5b9a\u3067\u304d\u308b\u91cd\u529b\u70b9\u306e\u500b\u6570
Point gPoint[];
int gSize = 6;
int gCount = 0;

ScoreLine score; 

// \u753b\u9762\u5f8c\u308d\u306e\u5b87\u5b99\u3063\u307d\u3055\u3092\u51fa\u3059\u305f\u3081\u306e\u661f
Circle backStar[];
int backStarNum = 200;


/*
 * \u521d\u671f\u5316
 */
public void setup() {
  size(width, height);

  triangles = new TriangleDrawing[triangleNum];
  for (int i=0; i<triangleNum; i++) {
    triangles[i] = new TriangleDrawing(i);
  }

  particles = new Particle[pmax];
  for (int i=0; i<pmax; i++) {
    particles[i] = makeNewPartcile();
    particles[i].setInit(width*1.5f, random(height*2), 0.0f, random(10));
  }

  gPoint = new Point[gSize];
  for (int i=0; i < gSize; i++)
    gPoint[i] = new Point(1000, 1000);
    
  backStar = new Circle[backStarNum];
  for(int i=0; i<backStarNum; i++)
    backStar[i] = new Circle(random(30,width), random(0,height), random(2));
  

  score = new ScoreLine(30, 5, 100, 50);
  frameRate(20);
}

/*
 * \u30de\u30a6\u30b9\u306e\u30af\u30ea\u30c3\u30af\u30a4\u30d9\u30f3\u30c8
 * \u30af\u30ea\u30c3\u30af\u3055\u308c\u305f\u3089\u547c\u3073\u51fa\u3055\u308c\u308b
 * \u30af\u30ea\u30c3\u30af\u3057\u305f\u4f4d\u7f6e\u306b\u91cd\u529b\u70b9\u3092\u751f\u6210\u3059\u308b
 */
public void mouseClicked() {
  gPoint[gCount] = new Point(mouseX, mouseY);
  gCount = (gCount+1) % gSize;
}

/*
 * \u63cf\u753b\u95a2\u6570
 * \u4e00\u5b9a\u6642\u9593\u4e8b\u306b\u5b9a\u671f\u7684\u306b\u547c\u3073\u51fa\u3055\u308c\u308b
 */
public void draw() {
  background(0);
  noStroke(); 

  fill(255,255,0);   
  for(int i=0; i<backStarNum; i++){
    ellipse(backStar[i].x,backStar[i].y,backStar[i].r,backStar[i].r);
  }
 
  fill(255, 0, 0);
  for (int i=0; i<gSize;i++) {
    ellipse(gPoint[i].x, gPoint[i].y, 10, 10);
  }

  for (int i=0; i<pmax; i++) {
    // \u304b\u304b\u308b\u91cd\u529b\u306e\u8a08\u7b97
    for (int j=0; j<gSize; j++)
      particles[i].setMoving(gPoint[j].x, gPoint[j].y);
    
    // \u79fb\u52d5\u3057\u3066\u63cf\u753b
    particles[i].move();
    particles[i].draw();

    // \u30b4\u30fc\u30eb\u3057\u305f\u308a\u3001\u6307\u5b9a\u3057\u305f\u30b2\u30fc\u30e0\u306e\u7bc4\u56f2\u5916\u306b\u306a\u3063\u305f\u3089\u6d88\u6ec5\u3057\u3066\u65b0\u3057\u3044\u306e\u3092\u51fa\u3059
    // \u8868\u793a\u9818\u57df\u5916\u3067\u3082\u3042\u308b\u7a0b\u5ea6\u306e\u5927\u304d\u3055\u307e\u3067\u306f\u7bc4\u56f2\u5185\u306b\u306a\u308b
    if (score.isInGoal(particles[i].x, particles[i].y, particles[i].r)) 
      particles[i] = makeNewPartcile();
    else if (!particles[i].isInRect(30, -height, width * 2, height * 2)) 
      particles[i] = makeNewPartcile();
  }
  
  // \u70b9\u6570\u63cf\u753b
  score.drawScoreLine();
}
  static public void main(String args[]) {
    PApplet.main(new String[] { "--bgcolor=#D4D0C8", "StarGame" });
  }
}
