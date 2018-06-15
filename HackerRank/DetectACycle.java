import java.util.HashSet;

public class DetectACycle {
    boolean hasCycle(Node head) {
        HashSet<Node> nodeSet = new HashSet<>();
        while(head != null){
            if(nodeSet.contains(head)){
                return true;
            }
            nodeSet.add(head);
            head = head.next;
        }
        return false;
    }

    private class Node {
        int data;
        Node next;
    }
}
