import java.util.HashMap;
import java.util.Scanner;

public class MakingAnagrams {

    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        HashMap<Character, Integer> h = new HashMap<>();
        String s1 = s.nextLine();
        for(char temp : s1.toCharArray()){
            if(h.containsKey(temp))
                h.put(temp, h.get(temp)+1);
            else
                h.put(temp, 1);
        }
        String s2 = s.nextLine();
        for(char temp: s2.toCharArray()){
            if(h.containsKey(temp))
                h.put(temp, h.get(temp)-1);
            else
                h.put(temp, -1);
        }
        int sum = 0;
        for(int temp : h.values())
            sum += Math.abs(temp);
        System.out.println(""+sum);
    }
}
