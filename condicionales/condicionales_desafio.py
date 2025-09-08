tarifa_base = 7000
precio_por_unidad_consumo = 200
bonificacion = 0
recargo = 0
descuento_especial = 0

# Input
consumo = int(input("Ingrese la cantidad de metros cubicos consumidos: "))
tipo_cliente = input("Ingrese la tipo de cliente: ")


# Calculos 
costo_consumo = consumo * precio_por_unidad_consumo

if tipo_cliente == "Residencial":
    if consumo < 30:
        bonificacion = costo_consumo * 0.10
    if consumo > 80:
        recargo = costo_consumo * 0.15
    
    if costo_consumo < 35000:
        descuento_especial = (costo_consumo + tarifa_base) * 0.05 # No especifica que sea sobre el costo de consumo unicamente

if tipo_cliente == "Comercial":
    if consumo > 150:
        bonificacion = costo_consumo * 0.08
    elif consumo > 300:
        bonificacion = costo_consumo * 0.12
        
    if consumo < 50:
        recargo = (costo_consumo + tarifa_base) * 0.05 # No especifica que el recargo sea sobre el costo del consumo

if tipo_cliente == "Industrial":
    if consumo > 500 and consumo < 1000:
        bonificacion = costo_consumo * 0.20
    elif consumo > 1000:
        bonificacion = costo_consumo * 0.30
    
    if consumo < 200:
        recargo = (costo_consumo + tarifa_base) * 0.10 # Lo mismo, no especifica que sea sobre el costo del consumo

total_sin_iva = costo_consumo - bonificacion - descuento_especial + recargo
total_iva = total_sin_iva * 0.21
total_con_iva = total_sin_iva + total_iva

# Output

print(f"Costo de consumo: {costo_consumo}")
print(f"Bonificaciones: {bonificacion}(bonificacion),  {descuento_especial}(descuento especial)")
print(f"Recargos: {recargo}")
print(f"Subtotal: {total_sin_iva}")
print(f"Iva aplicado (21%): {total_iva}")
print(f"Total a pagar: {total_con_iva}")





