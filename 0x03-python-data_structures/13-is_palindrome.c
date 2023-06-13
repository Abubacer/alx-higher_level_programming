#include "lists.h"

/**
* reverse_list - a function that reverses a singly-linked.
* @head: The starting node of the linked list to reverse.
*
* Return: The head of the reversed linked list.
*/

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev_node, *current_node, *next_node;

	prev_node = 0;
	current_node = head;
	next_node = 0;

	while (current_node != NULL)
	{
		next_node = current_node->next;
		current_node->next = prev_node;
		prev_node = current_node;
		current_node = next_node;
	}

	return (prev_node);
}

/**
 * is_palindrome - a function that that checks if a singly linked list
 * is a palindrome.
 * @head: A double pointer to head of linked list.
 * Return: 1 if the linked list is a palindrome or 0 if it is not.
 *
 * Description: The function finds the middle of the linked list using
 * a slow and fast pointers technique, reverses the second half and
 * finally compare the corresponding nodes in two halves of the list
 * and return whether the list is a palindrome or not.
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr, *fast_ptr, *list_one, *list_two;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	slow_ptr = *head;
	fast_ptr = *head;
	list_two = 0;

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}

	if (fast_ptr != NULL)
		slow_ptr = slow_ptr->next;

	list_one = *head;
	list_two = reverse_list(slow_ptr);

	while (list_two != NULL)
	{
		if (list_one->n != list_two->n)
			return (0);

		list_one = list_one->next;
		list_two = list_two->next;
	}

	return (1);
}
