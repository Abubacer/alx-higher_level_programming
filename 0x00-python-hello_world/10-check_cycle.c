#include "lists.h"

/**
 * check_cycle - a function that checks whether the singly linked list
 * has a cycle in it.
 * @list: the singly linked list to check.
 * Return: 1 if a cycle is detected and 0 otherwise.
 *
 * Description: this function moves two pointers at different speeds the slow
 * pointer moves one step at a time while the fast moves two steps at a time
 * through the sequence of values until they both point to equal values.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow_ptr, *fast_ptr;

	slow_ptr = list;
	fast_ptr = list;

	if (list == 0)
		return (0);

	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;

		if (slow_ptr == fast_ptr)
			return (1);
	}

	return (0);
}
