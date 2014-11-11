#include <stdio.h>

main()
{
	float distancia;
	float velocidade;
	float resultado;

	printf("Calcule o Tempo percorrido por um veiculo.\n");
	printf("Informe a distancia percorrida: \n");
	scanf("%f", &distancia);
	printf("Informe a velocidade media: \n");
	scanf("%f", &velocidade);
	
	resultado = distancia/velocidade;

	printf("O valor do tempo gasto é: %.2f\n", resultado);

}