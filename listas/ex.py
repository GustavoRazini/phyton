def caucular_multa(dias_atraso):
	if dias_atraso <= 0:
		return 0
	elif 1 <= dias_atraso <= 5:
		return 0.50 * dias_atraso
