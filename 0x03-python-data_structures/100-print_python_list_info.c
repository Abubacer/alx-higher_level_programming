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

	list_size = PySequence_Size(p);
	Py_ssize_t item;

	printf("[*] Size of the Python List = %zd\n", list_size);

	for (item = 0 ; item < list_size ; item++)
	{
		PyObject *obj = PySequence_GetItem(p, item);

		printf("Element %zd: %s\n", item, Py_TYPE(obj)->tp_name);
		Py_DECREF(obj);
	}
}
