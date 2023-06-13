#include <Python.h>

/**
 * print_python_list_info - function that prints some basic info
 * about Python lists.
 * @p: The pyobject list to print.
 *
 * Return: void.
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t py_size = PySequence_Size(p);
	Py_ssize_t py_size = item;

	printf("[*] Size of the Python List = %zd\n", py_size);

	for (item = 0 ; item < py_size ; item++)
	{
		PyObject *obj = PySequence_GetItem(p, i);

		printf("Element %zd: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
