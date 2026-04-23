import math

prezzi = [100.0, 102.0, 101.5, 104.0, 103.2, 106.5]

log_returns = []

log_return_day2 = math.log(prezzi[1] / prezzi[0])
log_return_day3 = math.log(prezzi[2] / prezzi[1])
log_return_day4 = math.log(prezzi[3] / prezzi[2])
log_return_day5 = math.log(prezzi[4] / prezzi[3])
log_return_day6 = math.log(prezzi[5] / prezzi[4])

log_returns.append(log_return_day2)
log_returns.append(log_return_day3)
log_returns.append(log_return_day4)
log_returns.append(log_return_day5)
log_returns.append(log_return_day6)

print(f"rendimenti logaritmici: {log_returns}")

print(f"numero totale rendimenti: {len(log_returns)}")
print(f"rendimento minimo: {min(log_returns):.4f}")
print(f"rendimento massimo: {max(log_returns):.4f}")
print(f"somma dei rendimenti logaritmici: {sum(log_returns):.4f}")


copia_lista = log_returns.copy()

copia_lista.append(0.999)

print(f"copia della lista dei log return: {copia_lista}")
print(f"lista originale: {log_returns}")
