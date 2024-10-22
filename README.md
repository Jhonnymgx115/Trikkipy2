# Juego Triki - En Python

## 📝 Descripción
Triki es una implementación en Python del clásico juego Tres en Línea (Tic-Tac-Toe) utilizando la biblioteca Tkinter para la interfaz gráfica. El juego está desarrollado siguiendo los principios de la Programación Orientada a Objetos (POO) y ofrece dos modos de juego: contra otro jugador o contra la computadora.

## 🚀 Características
- Interfaz gráfica intuitiva
- Dos modos de juego:
  - Jugador vs Jugador
  - Jugador vs Computadora
- Sistema de puntuación
- Temporizador de juego
- Detección automática de victoria y empate

## 💻 Requisitos
- Python 3.x
- Tkinter (incluido en la instalación estándar de Python)

## 🎮 Cómo Jugar
1. Ejecuta el script Python:
```bash
python triki_game.py
```
2. Selecciona el modo de juego:
   - "2 Players" para jugar contra otro jugador
   - "Against Computer" para jugar contra la computadora
3. El jugador X siempre comienza
4. Haz clic en cualquier celda vacía para realizar tu movimiento
5. En modo computadora, la máquina jugará automáticamente después de tu turno

## 🏗️ Estructura del Código
El juego está construido utilizando principios de POO:

### Encapsulamiento
- La clase `TrikiGame` encapsula toda la lógica y datos del juego
- Atributos privados:
  - `buttons`: Matriz de botones del tablero
  - `score_x`, `score_o`: Puntuaciones
  - `player_turn`: Turno actual
  - `game_over`: Estado del juego
  - `mode`: Modo de juego actual

### Abstracción
Métodos principales:
- `check_win()`: Verifica condiciones de victoria
- `computer_move()`: Lógica de la computadora
- `update_score()`: Gestión de puntuación
- `click()`: Manejo de interacciones del usuario

### Constructores
El método `__init__`:
- Inicializa el estado del juego
- Configura la interfaz gráfica
- Establece valores predeterminados
- Crea componentes visuales

### Atributos de Clase
Gestión de estado a través de:
- `self.player_turn`: Control de turnos
- `self.game_over`: Estado de finalización
- `self.buttons`: Estado del tablero
- `self.mode`: Modo de juego actual

## 🎯 Funcionalidades Principales

### Control de Juego
```python
def click(self, row, column):
    # Maneja las jugadas de los usuarios
    # Verifica validez del movimiento
    # Actualiza el estado del juego
```

### Lógica de Victoria
```python
def check_win(self):
    # Verifica filas, columnas y diagonales
    # Retorna True si hay un ganador
```

### Movimientos de la Computadora
```python
def computer_move(self):
    # Selecciona una celda vacía aleatoriamente
    # Realiza el movimiento
    # Verifica victoria o empate
```

## 📊 Gestión de Estado
- Sistema de puntuación persistente durante la sesión
- Temporizador de juego activo
- Detección automática de fin de juego
- Cambio dinámico entre modos de juego

## 🔄 Ciclo de Juego
1. Inicialización del tablero
2. Selección de modo
3. Turnos alternados entre jugadores
4. Verificación de victoria/empate
5. Actualización de puntuación
6. Opción de reinicio

## 🤝 Contribuciones
Las contribuciones son bienvenidas. Para contribuir:
1. Haz fork del repositorio
2. Crea una rama para tu feature
3. Realiza tus cambios
4. Envía un pull request

## 📄 Licencia
Este proyecto está bajo la Licencia MIT.
