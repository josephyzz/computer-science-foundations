// This program demonstrates the concept of direct mapping
// by counting the frequency of characters in a given string.

# include <stdio.h>


int main()
{
  char word[] = "BANANA";
  int frequency[256] = {0};
 
  for (int i = 0; word[i] != '\0'; i++){
    // Increment the frequency count
    // for the ASCII value of the character
    frequency[(int) word[i]]++;
  };

  printf("frequency of 'A': %d\n", frequency['A']);

  return 0;
}
