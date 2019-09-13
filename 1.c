#include <stdio.h>
#include <stdlib.h>

// Question:
// Easy
// Given an array of integers, return indices of the two numbers such that they add up to a specific target.

// You may assume that each input would have exactly one solution,
// and you may not use the same element twice.

// Example :

// Given nums = [ 2, 7, 11, 15 ],
// target = 9,

// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [ 0, 1 ].

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *twoSum(int *nums, int numsSize, int target, int *returnSize)
{
    int *indices = malloc(2 * sizeof(int));
    *returnSize = 2;
    for (int i = 0; i < numsSize; i++)
    {
        for (int j = 0; j < numsSize; j++)
        {
            if (nums[i] + nums[j] == target && i != j)
            {
                indices[0] = i;
                indices[1] = j;
                return indices;
            }
        }
    }
    return indices;
}