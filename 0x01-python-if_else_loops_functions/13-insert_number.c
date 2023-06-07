
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
	listint_t *current_node, *new_node;

	current_node = *head;
	new_node = malloc(sizeof(listint_t));

	if (new_node == 0)
		return (0);

	new_node->n = number;

	if (!current_node || current_node->n >= number)
	{
		new_node->next = current_node;
		*head = new_node;
		return (new_node);
	}

	while (current_node->next && current_node->next->n < number)
		current_node = current_node->next;

	new_node->next = current_node->next;
	current_node->next = new_node;

	return (new_node);
}
