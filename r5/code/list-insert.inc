/* On failure, *head is unchanged. */
int push_front(struct Node **head, int value) {
    struct Node *node = malloc(sizeof(struct Node));
    if (node == NULL) return 0;
    node->data = value;
    node->next = *head;
    *head = node;
    return 1;
}
