import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;


public class ProblemC {
	String filename = "C-large.in";
	public static void main(String[] args) {
		try {
			new ProblemC().start();
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
			
			long n = sc.nextLong();
			
			long x = 1;
			while(true){
				if (n < x * 2) break;
				x = x * 2;
			}
			
			if( (x*2) -1 < n) x = (x*2) -1;
			else x--;
			
			long y = n-x;
			String a = Long.toBinaryString(x);
			String b = Long.toBinaryString(y);

			int num = 0;
			for(int i=0; i<a.length(); i++)
				if (a.charAt(i) == '1') num++;
			
			for(int i=0; i<b.length(); i++)
				if (b.charAt(i) == '1') num++;

		 	String ans = "" + num;
			String output = "Case #" + (test+1) + ": " + ans;
			System.out.println(output);
			out.write(output + "\n");
		}
		out.close();
	}
}
