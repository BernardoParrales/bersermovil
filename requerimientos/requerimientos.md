## Bersermovil

Bersermovil es una nueva operadora de telecomunicaciones el cual requiere de un sistema que provea el servicio de atención al cliente mediante llamadas al *555#. Cuando se realiza una llamada se abrira un menu donde saldran multiples opciones que el usuario podrá elegir.

## El sistema debe tener lo siguiente

- Muestra un menú principal donde se enviara la opción requerida.
- Se debe tener una base de números de telefonos definidos, los cuales deben tener un estado de activo o inactivo. 
    
    - Inactivo: El menu que se abre es para activar el numero, en este caso se pedira la información del usuario: nombres, apellidos, número de cedula.
    - Activo: En este estado se abrira el menu principal.

- La información debe almacenarse en una base de datos.
- Debe validar los datos de entrada.

## Clases

**Numeros:**
 
- id_numero 
- id_persona
- id_saldo
- numero_telefono
- estado

**Personas**

- id_persona
- nombre
- apellido
- cedula

**Paquetes**

- id_paquete
- descripcion
- id_saldo

**Bancos**

- id_banco
- nombre_banco

**CuentaBancaria**

- id_cuenta_bancaria
- id_banco
- id_persona
- tipo: (ahorro, corriente)
- tarjeta_debito
- clave

## Menú principal
1. Menu inicial

![alt text](image.png)

1.1. Paquetes

![alt text](image-1.png)

1.2. Recargas

![alt text](image-2.png)

1.2.1. Activación de tarjeta

![alt text](image-3.png)

1.2.2. Recarga de saldo en dolares

![alt text](image-4.png)

1.2.2.1. Elegir banco

![alt text](image-5.png)

![alt text](image-6.png)

- numero de cedula
- clave
- ultimos digitos de la tarjeta de debito

1.3. Consulta de saldo

![alt text](image-7.png)

1.3.1. 

![alt text](image-9.png)

![alt text](image-10.png)

1.3.2. 

![alt text](image-11.png)

1.3.2.1.

![alt text](image-12.png)

nos envia al 1.3.2.

![alt text](image-8.png)

1.3.2.2.

![alt text](image-13.png)

1.3.2.2.1.

![alt text](image-14.png)

1.3.2.2.1.1.

![alt text](image-15.png)

1.3.2.2.2.

![alt text](image-16.png)

1.4.

![alt text](image-17.png)

1.5.

![alt text](image-18.png)

1.5.1.

![alt text](image-19.png)

1.5.1.1.

![alt text](image-20.png)

1.5.2.

![alt text](image-21.png)

1.6.

![alt text](image-22.png)

