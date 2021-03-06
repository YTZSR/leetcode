import java.util.Queue;
import java.util.LinkedList;
class Solution {
    public int maxDistance(int[][] grid) {
        if(checkMap(grid)){
            return -1;
        }

        int [][] temp = new int[grid.length][grid[0].length];
        for(int i = 0;i < grid.length; i++){
            for(int j = 0; j < grid[i].length;j++){
                temp[i][j] = -1;
            }
        }
        int max = 0;
        Queue<Integer> queue = new LinkedList<Integer>();
        for(int i = 0;i < temp.length; i++){
            for(int j = 0; j < temp[i].length;j++){
                if(grid[i][j] == 1){
                    temp[i][j] = 0;
                    queue.add(i);
                    queue.add(j);
                    
                }
            }
        }
        while(!queue.isEmpty()){
            int i = queue.poll();
            int j = queue.poll();
            // System.out.println(i + " " + j + " " + temp[i][j]);
            if(temp[i][j] > max){
                max += 1;
            }
            
            if(i > 0 && temp[i-1][j] == -1){
                temp[i-1][j] = temp[i][j] + 1;
                queue.add(i -1);
                queue.add(j);
            }
            if(i < temp.length - 1 && temp[i+1][j] == -1){
                temp[i+1][j] = temp[i][j] + 1;
                queue.add(i + 1);
                queue.add(j);
            }
            if(j > 0 && temp[i][j - 1] == -1){
                temp[i][j-1] = temp[i][j] + 1;
                queue.add(i);
                queue.add(j-1);
            }
            if(j < temp.length - 1 && temp[i][j+1] == -1){
                temp[i][j+1] = temp[i][j] + 1;
                queue.add(i);
                queue.add(j + 1);
            }
        }
        return max;
        
    }

    public boolean checkMap(int[][] grid){
        int count = 0;
        for(int i = 0;i < grid.length; i++){
            for(int j = 0; j < grid[i].length;j++){
                count += grid[i][j];
            }
        }
        if(count == 0 || count == Math.pow(grid.length, 2)){
            return true;
        }
        return false;
    }
}