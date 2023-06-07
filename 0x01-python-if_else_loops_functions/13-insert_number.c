
#include "lists.h"

/**
 * insert_node - a function in C that inserts a number
 * into a sorted singly linked list.
 * @head: a pointer to the head of the singly linked list
 * @number: the number to be insterted into the list
 *
 * Return: the new node or NULL if the function fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *currnt_node, *new_node;

	currnt_node = *head;
	new_node = malloc(sizeof(listint_t));

	if (new_node == 0)
		return (0);

	new_node->n = number;

	if (currnt_node == 0 || currnt_node->n >= number)
	{
		new_node->next = currnt_node;
		*head = new_node;
		return (new_node);
	}

	while (currnt_node->next && currnt_node->next->n < number)
		currnt_node = currnt_node->next;

	new_node->next = currnt_node->next;
	currnt_node->next = new_node;

	return (new_node);
}
