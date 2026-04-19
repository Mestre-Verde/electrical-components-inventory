#include <stdbool.h>  // inclui o bool
#include <stdio.h>

#define IMPUT_FILE_PATH "tmp/input.tmp"
#define OUTPUT_FILE_PATH "tmp/output.tmp"
#define HISTORY "data/history.txt"
enum Commands = {SETUP =0}


_Bool setup() {
  puts("Dentro de setup().") return 0;
}

int main(int argc, char const* argv[]) {
  if (argc < 2) {
    printf("Erro\n");
    return 1;
  }

  switch (expression) {
    case 0: setup(); break;

    default: break;
  }
  return 0;
}
