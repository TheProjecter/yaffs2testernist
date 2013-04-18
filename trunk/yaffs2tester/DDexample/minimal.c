#include <stdio.h>
#include <assert.h>

int foo(int x) {
  return x - 10;
}

int main () {
  int i, j, k;
  int *p = &i;
  int *q = &j;
  i = 10;
  j = 17;
  k = 3;
  printf ("This is line 1.\n");
  printf ("Calling foo: %d\n", foo(i));

  assert (j == i);

  //q = 0; // This is the problem.

  printf ("p = %d\n", *p);
  printf ("q = %d\n", *q);
}
