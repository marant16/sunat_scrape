from helium import *

def entrar_consultar_facturas_boletas_y_notas(driver):
    click("Empresas")
    click("Comprobantes de pago")
    click("Factura Electrónica")
    click("Consultar Factura, Boletas y Notas")
    click(S('//*[@id="nivel4_11_9_5_1_1"]'))
