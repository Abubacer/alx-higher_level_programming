#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - function that prints some basic info
 * about Python lists.
 * @p: The pyobject list to print.
 *
 * Return: void.
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size;
	int item, alloc;

	list_size = PySequence_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", list_size);
	printf("[*] Allocated = %d\n", alloc);

	for (item = 0 ; item < list_size ; item++)
	{
		PyObject *obj = PySequence_GetItem(p, item);

		printf("Element %d: %s\n", item, Py_TYPE(obj)->tp_name);
		Py_DECREF(obj);
	}
}
