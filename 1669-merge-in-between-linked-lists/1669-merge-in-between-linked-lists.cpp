/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* current = list1;
        for (int i = 1; i < a; ++i)
            current = current->next;
        
        ListNode* end = current;
        for (int i = 0; i < b - a + 2; ++i)
            end = end->next;
        current->next = list2;
        while (list2->next != nullptr)
            list2 = list2->next;
        list2->next = end;
        
        return list1;
    }
};
