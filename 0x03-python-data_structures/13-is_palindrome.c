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
 * Description: the function split the list in the middle into two
 * lists, reverses the second list and finally compare the splitted
 * two list and return whether the list is a palindrome or not.
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr, *fast_ptr, *list_one, *list_two;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	slow_ptr = *head;
	fast_ptr = *head;

	while (slow_ptr)
	{
		slow_ptr = slow_ptr->next;
		if (slow_ptr == NULL)
		{
			list_two = fast_ptr->next;
			break;
		}
		if (slow_ptr->next == NULL)
		{
			list_two = fast_ptr->next->next;
			break;
		}
		fast_ptr = fast_ptr->next;
	}

	fast_ptr->next = NULL;
	list_two = reverse_list(list_two);
	list_one = *head;

	while (list_one != NULL && list_two != NULL)
	{
		if (list_one->n == list_two->n)
		{
			list_one = list_one->next;
			list_two = list_two->next;
		}
		else
			return (0);
	}
	return (1);
}
