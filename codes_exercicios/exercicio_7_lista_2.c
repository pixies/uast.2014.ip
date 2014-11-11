#include <stdio.h>

main()
{

	float area_total; //area total a ser pintada
//	float litros_lata = 18; //Quantos litros tem em uma lata
	float preco_lata = 80; // preco por lata
	float preco_total; //preco total a ser gasto com tinta
	float qt_latas; //quantidade de latas
	float area_lata = 54; //area por lata
	int redondo;

	printf("Forneça o tamanho total da area a ser pintada em m2");
	scanf("%f", &area_total);

	qt_latas = (area_total / area_lata);

	preco_total = qt_latas * preco_lata; 

	redondo = (((qt_latas+0.999)/3)*3);

	printf("%f, %f, %d", preco_total, qt_latas, redondo);
	printf("\n");


}