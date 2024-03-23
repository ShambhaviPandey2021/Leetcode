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
    void reorderList(ListNode* head) {
        if (!head || !head->next || !head->next->next) return;
        ListNode *slow = head, *fast = head;
        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* second_half = reverseList(slow->next);
        slow->next = nullptr;
        mergeLists(head, second_half);
    }

private:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* current = head;
        while (current) {
            ListNode* next_node = current->next;
            current->next = prev;
            prev = current;
            current = next_node;
        }
        return prev;
    }
    void mergeLists(ListNode* l1, ListNode* l2) {
        while (l1 && l2) {
            ListNode* next_l1 = l1->next;
            ListNode* next_l2 = l2->next;
            l1->next = l2;
            l2->next = next_l1;
            l1 = next_l1;
            l2 = next_l2;
        }
    }
};
