from login_sunat import login_operaciones_linea
from navegar_seccion import entrar_consultar_facturas_boletas_y_notas

driver = login_operaciones_linea("10214673211", "RBOUSTOR", "erryncelm")
entrar_consultar_facturas_boletas_y_notas(driver)

