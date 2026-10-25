#include <stdio.h>
#include <stdlib.h>
struct Node {
    int data;
    struct Node *next;
};
/* On failure, *head is unchanged. */
int push_front(struct Node **head, int value) {
    struct Node *node = malloc(sizeof *node);
    if (node == NULL) return 0;
    node->data = value;
    node->next = *head;
    *head = node;
    return 1;
}
void free_list(struct Node *head) {
    while (head != NULL) {
        struct Node *next = head->next;
        free(head);
        head = next;
    }
}
/* caller: free_list(head); head = NULL; */

int main(void) {
    struct Node *head = NULL;
    if (!push_front(&head, 10) || !push_front(&head, 20)) {
        free_list(head);
        return EXIT_FAILURE;
    }
    printf("%d %d\n", head->data, head->next->data);
    free_list(head);
    head = NULL;
    return 0;
}
