#include <stdio.h>

// Question:
// Easy
// Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

// The binary search tree is guaranteed to have unique values.

struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void dfs(struct TreeNode *root, int L, int R, int *sum)
{
    if (root == NULL)
    {
        return;
    }

    dfs(root->left, L, R, sum);
    if (root->val >= L && root->val <= R)
    {
        *sum += root->val;
    }
    dfs(root->right, L, R, sum);
}

int rangeSumBST(struct TreeNode *root, int L, int R)
{
    int sum;
    int *p_sum = &sum;

    dfs(root, L, R, p_sum);

    return sum;
}
