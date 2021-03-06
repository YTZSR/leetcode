/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        int ans = 0;
        if(root == null){
            return 0;
        }
        if(root.left.left == null && root.left.right == null){
            return root.left.val;
        }

        return sumOfLeftLeaves(root.right) + sumOfLeftLeaves(root.left);
        

    }
}//Unfinished