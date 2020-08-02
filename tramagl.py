import re

re_format = r"\d{1,4}"

STATIC_DATA = "00105Tiket 0000000009478 1000^0100COMPUMAR DEMO^0100 Pemex ES 5189^0000R.F.C. VIEE7001301U3^0000PERMISO CRE: PL/22638/EXP/ES/2019^0   SERVICIO SUGASTI XALAPA^0000 00106Tiket 0000000009478 1000^0000*************************************^0100  CONTADO ORIGINAL^0000*************************************^0000 00106Tiket 0000000009478 1000^0000     Cliente:  Publico en General^0000 Fecha Venta: 2020/07/30 19:33:32^0000 Fecha Impre: 2020/07/30 19:33:38^0000       Turno: 2020072201^0000 00106Tiket 0000000009478 1000^0101Transaccion^01013015^0000^0000       Venta: 9478^0000      Web Id: t00100000301502^0000        Isla: 1^0000       Bomba: 1^0000    Manguera: 1 00106Tiket 0000000009478 1000^0000    Forma Pago: ^0000^0000Producto  Cantidad Precio  Total ^0000-----------------------------------^0000Magna  0.815    81.40    14.80^0000 00106Tiket 0000000009478 1000^0000    Subtotal: 12.77^0000         IVA: 2.03^0000       Total: 14.80^0000^0000CATORCE PESOS CON 80/100 M.N. 00106Tiket 0000000009478 1000^0000-----------------------------------^BARQ0518902t0010000030150200014.8202007301933^0   ESTE TICKET ES FACTURABLE SOLO^0   EL DIA DE SU CONSUMO 00107Tiket 0000000009478 1000^0   FACTURACION EN LINEA:^0   gl-operacion.com.mx"

def get_format_and_sentences(data):
   
   split_data = lambda fullsentence: [fullsentence[0:4],fullsentence[4:]] if len(fullsentence)>4 else ['\n']

   splited_data = list(map(split_data,data.split('^')))

   return splited_data

if __name__ == '__main__':

	result = get_format_and_sentences(STATIC_DATA)
	print(f"Resultado \n\n\n")
	list(map(lambda sentence: print(sentence), result))
	

"""
TRAMA DE GL

"00105Tiket 0000000009478 1000^
0100COMPUMAR DEMO^
0100 Pemex ES 5189^
0000R.F.C. VIEE7001301U3^
0000PERMISO CRE: PL/22638/EXP/ES/2019^
0   SERVICIO SUGASTI XALAPA^
0000 00106Tiket 0000000009478 1000^
0000*************************************^
0100  CONTADO ORIGINAL^
0000*************************************^
0000 00106Tiket 0000000009478 1000^
0000     Cliente:  Publico en General^
0000 Fecha Venta: 2020/07/30 19:33:32^
0000 Fecha Impre: 2020/07/30 19:33:38^
0000       Turno: 2020072201^
0000 00106Tiket 0000000009478 1000^
0101Transaccion^
01013015^
0000^
0000       Venta: 9478^
0000      Web Id: t00100000301502^
0000        Isla: 1^
0000       Bomba: 1^
0000    Manguera: 1 00106Tiket 0000000009478 1000^
0000    Forma Pago: ^
0000^
0000Producto  Cantidad Precio  Total ^
0000-----------------------------------^
0000Magna  0.815    81.40    14.80^
0000 00106Tiket 0000000009478 1000^
0000    Subtotal: 12.77^
0000         IVA: 2.03^
0000       Total: 14.80^
0000^
0000CATORCE PESOS CON 80/100 M.N. 00106Tiket 0000000009478 1000^
0000-----------------------------------^
BARQ0518902t0010000030150200014.8202007301933^
0   ESTE TICKET ES FACTURABLE SOLO^
0   EL DIA DE SU CONSUMO 00107Tiket 0000000009478 1000^
0   FACTURACION EN LINEA:^
0   gl-operacion.com.mx"


TRAMA FILTRADA

['0010', '5Tiket 0000000009478 1000']
['0100', 'COMPUMAR DEMO']
['0100', ' Pemex ES 5189']
['0000', 'R.F.C. VIEE7001301U3']
['0000', 'PERMISO CRE: PL/22638/EXP/ES/2019']
['0   ', 'SERVICIO SUGASTI XALAPA']
['0000', ' 00106Tiket 0000000009478 1000']
['0000', '*************************************']
['0100', '  CONTADO ORIGINAL']
['0000', '*************************************']
['0000', ' 00106Tiket 0000000009478 1000']
['0000', '     Cliente:  Publico en General']
['0000', ' Fecha Venta: 2020/07/30 19:33:32']
['0000', ' Fecha Impre: 2020/07/30 19:33:38']
['0000', '       Turno: 2020072201']
['0000', ' 00106Tiket 0000000009478 1000']
['0101', 'Transaccion']
['0101', '3015']
['0000']
['0000', '       Venta: 9478']
['0000', '      Web Id: t00100000301502']
['0000', '        Isla: 1']
['0000', '       Bomba: 1']
['0000', '    Manguera: 1 00106Tiket 0000000009478 1000']
['0000', '    Forma Pago: ']
['0000']
['0000', 'Producto  Cantidad Precio  Total ']
['0000', '-----------------------------------']
['0000', 'Magna  0.815    81.40    14.80']
['0000', ' 00106Tiket 0000000009478 1000']
['0000', '    Subtotal: 12.77']
['0000', '         IVA: 2.03']
['0000', '       Total: 14.80']
['0000']
['0000', 'CATORCE PESOS CON 80/100 M.N. 00106Tiket 0000000009478 1000']
['0000', '-----------------------------------']
['BARQ', '0518902t0010000030150200014.8202007301933']
['0   ', 'ESTE TICKET ES FACTURABLE SOLO']
['0   ', 'EL DIA DE SU CONSUMO 00107Tiket 0000000009478 1000']
['0   ', 'FACTURACION EN LINEA:']
['0   ', 'gl-operacion.com.mx']

"""