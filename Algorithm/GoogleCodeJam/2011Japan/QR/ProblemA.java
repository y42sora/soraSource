import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;


public class ProblemA {
	String filename = "A-large.in";
	public static void main(String[] args) {
		try {
			new ProblemA().start();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	private void start() throws IOException {
		Scanner sc = new Scanner(new File(filename));
		FileWriter out = new FileWriter(new File(filename + "out.txt"));

		int tnum = sc.nextInt();
		
		for(int test = 0; test < tnum; test++){
			
			// 入力
			long m = sc.nextLong();
			int c = sc.nextInt();
			long w = sc.nextLong();
			
			Pair p[] = new Pair[c];
			for(int i=0; i<c; i++){
				long a = sc.nextLong();
				long b = sc.nextLong();
				p[i] = new Pair(a,b);
			}
			
			// 後ろから順に、指定された部分がどこに当たるかを求める
			c--;
			while(0 <= c){
				long a = p[c].a;
				long b = p[c].b;
				long l = p[c].l;
				
				if(b < w){
					//nothing
				}else if(0 < w-l){
					w = w-l;
				}else{
					w = b + (w-l);
				}

				c--;
			}
			
		 	String ans = "" + w;
			String output = "Case #" + (test+1) + ": " + ans;
			System.out.println(output);
			out.write(output + "\n");
		}
		out.close();		
	}
	
	class Pair{
		long a;
		long b;
		long l;
		Pair(long a,long b){
			this.a = a;
			this.b = a+b-1;
			this.l = b;
		}
	}
}