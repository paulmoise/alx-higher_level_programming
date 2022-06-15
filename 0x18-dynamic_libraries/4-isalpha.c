#include "main.h"
/**
 * _isalpha - check if character is letter case insensitive
 * @c : character to be checked
 * Return: 1 if true or 0 if not
 */
int _isalpha(int c)
{
	if ((c >= 'a' && c <= 'z') || (c <= 'Z' && c >= 'A'))
		return (1);
	return (0);
}
