import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;


public class ProblemB {
	public static void main(String[] args) {
		try {
			new ProblemB().start();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	class coffie implements Comparable<coffie>{
		long point;
		long day;
		long num;
		coffie(long p,long d,long n){
			this.point = p;
			this.day = d;
			this.num = n;
		}
		@Override
		public int compareTo(coffie arg0) {
			if(this.point < arg0.point)
				return 1;
			if(this.point == arg0.point)
				return 0;
			return -1;
		}
	}

	private void start() throws IOException {
		Scanner sc = new Scanner(new File("B-large.in"));
		FileWriter out = new FileWriter(new File("out.txt"));

		
		int testCase = sc.nextInt();
		
		for(int test=0; test<testCase; test++){
			int num = sc.nextInt();
			long day = sc.nextLong();
			
			ArrayList<coffie> coff = new ArrayList<coffie>();
			long[] stopDay = new long[num+1];
			for(int i=0; i<num; i++){
				long n =sc.nextLong();
				long d =sc.nextLong();
				long p =sc.nextLong();
				coff.add(new coffie(p,d,n));
				stopDay[i] = d;
			}
			stopDay[num] = 0;
			long maxPoint = getMax(day, coff, stopDay);
		
			String output = "Case #" + (test+1) + ": " + maxPoint;
			System.out.println(output);
			out.write(output + "\n");
		}
		out.close();
		
	}
	

	private long getMax(long day, ArrayList<coffie> coff, long[] stopDay) {
		long answer = 0;
		Collections.sort(coff);
		Arrays.sort(stopDay);
		int x = stopDay.length-1;
		
		while(0 < day){
			if(coff.size() == 0) return answer;
			
			boolean flag = false;
			for(int i=0; i<coff.size(); i++){
				coffie c = coff.get(i);
				
				if(day <= c.day){
					
					long drinkDay = day-c.num;
					if(drinkDay < stopDay[x]){
						drinkDay = stopDay[x];
						x--;
					}
					
					long drinkNum = (day-drinkDay);
					
					answer += drinkNum * c.point;
					c.num -= drinkNum;
					day -= drinkNum;

					if(c.num == 0)
						coff.remove(i);
					flag = true;
					break;
				}
			}
			if(!flag)day = stopDay[x--];
		}

		return answer;
	}
}
