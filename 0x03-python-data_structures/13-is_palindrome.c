#include "lists.h"
/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: pointer on struct
 * Return: 0 if it is not palindrome, 1 it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *prev, *tmp, *right, *left;

	if (head == NULL)
		return (1);

	fast = *head;
	slow = *head;

	/* find the middle (slow) */
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	/* reverse the second half of the list */
	prev = NULL;
	while (slow != NULL)
	{
		tmp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = tmp;
	}

	/** check palindrome */
	left = *head;
	right = prev;

	while (right != NULL)
	{
		if (left->n != right->n)
			return (0);
		left = left->next;
		right = right->next;
	}
	return (1);
}
