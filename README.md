# Flechazo

Este es un juego desarrollado en Python utilizando la biblioteca Pygame. El objetivo del juego es controlar un corazón para esquivar a cupido que se mueven horizontalmente a través de la pantalla. 

## Funcionalidades

- *Pantalla de bienvenida*: Antes de comenzar el juego, se muestra una pantalla de bienvenida que indica al jugador que presione Enter para iniciar el juego.
- *Control del jugador*: El jugador puede mover el corazón rojo usando las flechas del teclado en las cuatro direcciones: arriba, abajo, izquierda y derecha.
- *Enemigos*: El enemigo es cupido que se mueve de derecha a izquierda a través de la pantalla.
- *Conteo de tiempo*: El juego cuenta cuántos segundos el jugador ha sobrevivido.
- *Colisiones y vidas*: El jugador tiene tres vidas y pierde una cada vez que colisiona con una flecha. El juego termina cuando se pierden todas las vidas.
- *Pantalla de pérdida*: Cuando el jugador pierde todas las vidas, se muestra una pantalla de pérdida indicando el tiempo sobrevivido y una instrucción para presionar Espacio para reiniciar.
- *Cerrar el juego*: El juego puede cerrarse en cualquier momento presionando la tecla Escape.

## Cómo jugar

1. *Pantalla de bienvenida*: 
   - Al iniciar el juego, verás una pantalla de bienvenida. 
   - Presiona Enter para comenzar el juego.
   - Presiona Escape para cerrar el juego.

2. *Durante el juego*: 
   - Usa las teclas de flecha (arriba, abajo, izquierda, derecha) para mover el corazón rojo y esquivar las flechas negras.
   - El objetivo es sobrevivir el mayor tiempo posible sin colisionar con cupido.

3. *Pantalla de pérdida*: 
   - Si colisionas con cupido y pierdes todas tus vidas, verás una pantalla de pérdida.
   - La pantalla de pérdida muestra el tiempo que lograste sobrevivir.
   - Presiona Espacio para reiniciar el juego y volver a la pantalla de bienvenida.
   - Presiona Escape para cerrar el juego.

## Requisitos

- Python 3.x
- Pygame
