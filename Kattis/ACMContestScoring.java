import java.util.HashMap;
import java.util.Scanner;

public class ACMContestScoring {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        HashMap<String, Integer> subs = new HashMap<>();
        String in = s.nextLine();
        int penalty = 0;
        int corrects = 0;
        while(in.length()>2){
            String[] fields = in.split(" ");
            if(fields[2].equals("right")){
                corrects++;
                penalty += Integer.parseInt(fields[0]);
                if(subs.containsKey(fields[1]))
                    penalty += 20*subs.get(fields[1]);
            }
            else{
                if(subs.containsKey(fields[1]))
                    subs.replace(fields[1], subs.get(fields[1])+1);
                else
                    subs.put(fields[1], 1);
            }
            in = s.nextLine();
        }
        System.out.println(corrects + " " + penalty);
    }
}
