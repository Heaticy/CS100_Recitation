void free_list(struct Node *head) {
    while (head != NULL) {
        struct Node *next = head->next;
        free(head);
        head = next;
    }
}
/* caller: free_list(head); head = NULL; */
