# Guia de Código de Conduta

Este guia define **padrões de estilo e documentação** para facilitar a leitura, manutenção e colaboração no projeto.



## 1. Nome de Variáveis

- Utilize **CamelCase** para nomes de variáveis:
```c
  int nomeDaVariavel = 10;
  float valorTotal = 25.5;
  char primeiraLetra = 'A';
```

* Evite:

  * Nomes muito curtos ou genéricos: `x`, `t`
  * Espaços, acentos ou caracteres especiais

* É permitido:
    - "i" para index;
    - "tmp" para temporário;


## 2. Estrutura de Documentação

Para funções, utilize o seguinte padrão de documentação em C:

```c
/**
 * @brief Breve descrição da função
 * @details Descrição detalhada do que a função faz
 * @param parametro1 Descrição do parâmetro 1
 * @param parametro2 Descrição do parâmetro 2
 * @return Descrição do valor retornado
 * @author Teu Nome
 */
```

### Exemplo Prático

```c
/**
 * @brief Calcula a soma de dois números
 * @details Recebe dois inteiros e retorna a soma
 * @param a Primeiro número
 * @param b Segundo número
 * @return A soma de a e b
 * @author Carlos Gomes
 */
int soma(int a, int b) {
    return a + b;
}
```

---

## 3. Boas Práticas Gerais


* Comente funções e linhas complexos do código
  
* Nomes de funções claros: `calculaMedia()`, `imprimeMenu()`
* Separe código em módulos/pastas por funcionalidade (ex: `menus/`, `utils/`, `math/`)

# Notas de comunidade
 - Proibido leftis woke;
 - Proibidos terroristas islamicos e seus apoiadores;