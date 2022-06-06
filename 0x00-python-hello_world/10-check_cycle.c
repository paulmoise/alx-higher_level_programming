#include "lists.h"
/**
 * check_cycle - function that checks if a single linked list has a cycle
 * @list: pointer on the head of the list
 *
 * Return: 0 if there is no cycle, 1 if there is cyle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL || list->next == NULL)
		return (0);
	fast = list;
	slow = list;
	while (slow->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
