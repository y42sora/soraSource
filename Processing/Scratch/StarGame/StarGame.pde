// 重力の大きさ　適当
float gravity = 0.098;

// 星が永遠に生き続けるのを回避
static final int TIMELIMIT = 10000;

// 最高速度 低すぎると重力を振り切れない
static final int MAXSPEED = 20;

/*
 * 複数三角形を表示するクラス
 * 星は三角形の集まりで描画できる
 */
class TriangleDrawing {
  /*
   * 五芒星は10個の点からなる
   */
  float px[] = new float[10];
  float py[] = new float[10];

  /*
   * 星の大きさを指定して五芒星を書く
   */
  TriangleDrawing(int r) {
    setT( r);
  }
  
  /*
   * 五芒星は形は決まっているので、長さをどう変化させるかだけ
   */
  void setT(int r) {
    float rad = 36.0;

    for (int i=0; i<10; i++) {
      if (i % 2 == 0) {
        px[i] = sin(radians(rad*i))  *r;
        py[i] = cos(radians(rad*i))  *r;
      }
      else {
        px[i] = sin(radians(rad*i))  *r/3.0;
        py[i] = cos(radians(rad*i))  *r/3.0;
      }
    }
  }

  /*
   * 指定された座標(x,y)にradだけ回転させてcol色で描画する
   * 五芒星は中心点と鋭角の点と鈍角の点で作られる10個の3角形で描画できる
   */
  void drawStar(float x, float y, float rad, color col) {
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
 * 一個一個のパーティクル管理する
 */
class Particle {
  float x, y;
  float vx, vy;

  color col;
  
  // 生存時間
  int count;

  int r;  
  
  // 初期回転角と回転速度
  float rad, radSpeed;
  TriangleDrawing triangles[];

  /*
   * パーティクルの現在位置と移動ベクトル、星の大きさとおよび星のデータをとる
   * 星の形はみんな同じなので大きさ事に形を計算した配列を使い、それを使い回す
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
   * 再度初期化する
   */
  void setInit(float x, float y, float vx, float vy) {
    this.x = x;
    this.y = y;
    this.vx = vx;
    this.vy = vy;
  }

  void setColor(color newcol) {
    col = newcol;
  }

  void draw() {
    rad = (rad+radSpeed) % 360.0;
    // このパーティクルの大きさの星を描画する
    triangles[r].drawStar(x, y, radians(rad), col);
  }

  /*
   * 指定された重力点の重力を考慮して、次の移動ベクトルを計算する
   * 重力点が一つとは限らないので、実際に移動するのは別の所
   */
  void setMoving(float gx, float gy) {
    float dx = x - gx;
    float dy = y - gy;
    float l = sqrt(dx * dx + dy * dy);
    if (l > 0.0001) {
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
   * 移動させる
   */
  void move() {
    count++;
    vy += gravity;
    x += vx;
    y += vy;
  }

  /*
   * 画面上に存在するかを判定
   * 生存できる時間内で、画面の四角の中にいる場合のみtrueを返す
   */
  boolean isInRect(int x, int y, int w, int h) {
    if (TIMELIMIT<count) return false;

    if (x <= this.x && this.x <= w)
      if (y <= this.y && this.y <= h)
        return true;
    return false;
  }
}


/*
 * 頂点クラス
 * javaのがあるけど…
 * 実は重力点にしか使ってない
 * いつか星の中心もこれで管理するように…
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
 * 円のクラス
 * 中心点と半径
 * 後ろの星にしか使ってない
 */
class Circle extends Point{
  float r;
  Circle(float x,float y,float r){
    super(x,y);
    this.r = r;
  } 
}


/*
 * 左側のスコアの線を管理するクラス
 */
class ScoreLine {
  // x座標とゴールバーの移動速度
  int x, vy;
  
  // ゴールバーの位置と長さ
  int goalPoint, goalLength;
  
  // 得点
  int score;

  /*
   * 描画位置と、ゴールバーの場所と長さを指定する
   */
  ScoreLine(int x, int vy, int goalPoint, int goalLength) {
    this.x = x;
    this.vy = vy;
    this.goalPoint = goalPoint;
    this.goalLength = goalLength;

    score = 0;
  }

  /*
   * ゴールバーと線を書く
   */
  void drawLine() {
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
   * 内側の虹色の得点を書く
   * HSB色空間で増やしていくだけ
   */
  void drawScore() {
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
   * スコアラインを描画する
   */
  void drawScoreLine() {
    drawLine();
    drawScore();
  }

  /*
   * 指定した頂点がゴールに入ったかどうか。
   * 入っていたらスコアにrを加算してtrueを返す
   */
  boolean isInGoal(float x, float y,int r) {
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
 * 新しいパーティクルを作成する
 */ 
Particle makeNewPartcile() {
  Particle p = new Particle(startx, starty, -1*random(2, 10), random(2, 5), random(1, triangleNum), triangles);
  p.setColor(color(random(30, 255), random(30, 255), random(30, 255), random(90, 100)));
  return p;
}


// パーティクルの最大数とその配列
int pmax = 200;
Particle particles[];

// 五芒星の大きさを指定する
int triangleNum = 21;
TriangleDrawing triangles[];

// ウィンドウの大きさとか
int seihou = 500;
int width = 800;
int height = 500;

// 星がどこから生まれるか
int startx = width;
int starty = 0;

// 設定できる重力点の個数
Point gPoint[];
int gSize = 6;
int gCount = 0;

ScoreLine score; 

// 画面後ろの宇宙っぽさを出すための星
Circle backStar[];
int backStarNum = 200;


/*
 * 初期化
 */
void setup() {
  size(width, height);

  triangles = new TriangleDrawing[triangleNum];
  for (int i=0; i<triangleNum; i++) {
    triangles[i] = new TriangleDrawing(i);
  }

  particles = new Particle[pmax];
  for (int i=0; i<pmax; i++) {
    particles[i] = makeNewPartcile();
    particles[i].setInit(width*1.5, random(height*2), 0.0, random(10));
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
 * マウスのクリックイベント
 * クリックされたら呼び出される
 * クリックした位置に重力点を生成する
 */
void mouseClicked() {
  gPoint[gCount] = new Point(mouseX, mouseY);
  gCount = (gCount+1) % gSize;
}

/*
 * 描画関数
 * 一定時間事に定期的に呼び出される
 */
void draw() {
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
    // かかる重力の計算
    for (int j=0; j<gSize; j++)
      particles[i].setMoving(gPoint[j].x, gPoint[j].y);
    
    // 移動して描画
    particles[i].move();
    particles[i].draw();

    // ゴールしたり、指定したゲームの範囲外になったら消滅して新しいのを出す
    // 表示領域外でもある程度の大きさまでは範囲内になる
    if (score.isInGoal(particles[i].x, particles[i].y, particles[i].r)) 
      particles[i] = makeNewPartcile();
    else if (!particles[i].isInRect(30, -height, width * 2, height * 2)) 
      particles[i] = makeNewPartcile();
  }
  
  // 点数描画
  score.drawScoreLine();
}
