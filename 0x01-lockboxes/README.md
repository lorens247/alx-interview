# 0x01-lockboxes

# 0x01. Lockboxes

## Overview

In the realm of programming and algorithmic challenges, tackling problems related to "Lockboxes" is a common exercise. Lockboxes are essentially containers holding keys, often nested within each other. The typical challenge involves determining whether all the boxes can be unlocked through a recursive exploration of the keys.

## Problem Description

You are given an array `boxes` where each index `i` contains a list of keys represented by integers. The key `k` at `boxes[i]` can unlock the box at index `k`. Initially, all the boxes are locked. Your task is to determine if it's possible to unlock all the boxes.

Write a function:

```typescript
function canUnlockAll(boxes: number[][]): boolean;
```

**Input:**
- `boxes`: An array of length `n` (1 ≤ n ≤ 1000) representing the `n` lockboxes. Each box is represented by an index from 0 to n-1.

**Output:**
- Return `true` if all boxes can be unlocked; otherwise, return `false`.

## Example

```typescript
const boxes1 = [[1], [2], [3], []];
canUnlockAll(boxes1);
// Output: true
// Explanation: Box 0 has key 1, unlocking box 1. Box 1 has key 2, unlocking box 2. Box 2 has key 3, unlocking box 3. All boxes can be unlocked.

const boxes2 = [[1, 2], [3], [4], [], []];
canUnlockAll(boxes2);
// Output: false
// Explanation: Box 0 has key 1, unlocking box 1. Box 1 has keys 2 and 3. Box 2 has key 4. Box 3 is empty. Box 4 has no keys. There is no way to unlock box 4.
```

## Constraints

- The input array ensures there are at most 1000 boxes and at most 1000 keys.

## Notes

- The keys are positive integers.
- A key with value `k` can unlock the box at index `k`.
- The initial state is that all boxes are locked.
