import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# 1. Definir o símbolo t e a função de posição s(t)
t = sp.symbols('t')
s = t**3 - 6*t**2 + 9*t  # Exemplo de função s(t)

# 2. Calcular a velocidade v(t) = s'(t) e aceleração a(t) = v'(t)
v = sp.diff(s, t)
a = sp.diff(v, t)

print("Função posição s(t):", s)
print("Função velocidade v(t):", v)
print("Função aceleração a(t):", a)

# 3. Converter para funções numéricas para plotagem
s_func = sp.lambdify(t, s, modules=['numpy'])
v_func = sp.lambdify(t, v, modules=['numpy'])
a_func = sp.lambdify(t, a, modules=['numpy'])

# 4. Intervalo de tempo
t_vals = np.linspace(0, 10, 400)
s_vals = s_func(t_vals)
v_vals = v_func(t_vals)
a_vals = a_func(t_vals)

# 5. Plotar os gráficos
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t_vals, s_vals, 'b', label='s(t) - Posição')
plt.title('Função Posição s(t)')
plt.ylabel('s(t)')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t_vals, v_vals, 'g', label='v(t) - Velocidade')
plt.title('Função Velocidade v(t)')
plt.ylabel('v(t)')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t_vals, a_vals, 'r', label='a(t) - Aceleração')
plt.title('Função Aceleração a(t)')
plt.xlabel('Tempo (t)')
plt.ylabel('a(t)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
