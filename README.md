# Proyecto.1

(a) Descripcion del Activo

(b) Rendimientos Diarios

Despues de la descarga de Datos que se realizo antes, calculamos la Media: 0.000970, el Sesgo: -0.235001 y Exceso de curtosis: 5.454364.

La media representa el rendimiento promedio diario del activo. En este caso, se obtiene un valor positivo (0.000970), lo que indica que, en promedio, el activo presenta una ligera tendencia al alza.
El Sesgo es una medida de asimetría de la distribución, para una normal β = 0. Sin embargo nosotros calculamos β=-0.235001 por lo que sabemos β < 0 indica que la cola izquierda es más larga y más pesada que la derecha. Esto quiere decir que el activo tiene mayor probabilidad de grandes pérdidas y sufrir caídas abruptas con mayor frecuencia
Tenemos tambien que la curtosis es una medida de concentración en la mediana con respecto a las colas. Para una distribución normal κ = 3. Pero nuestra aplicacion calculo que tenemos un caso donde κ > 3 lo indica una distribución leptucurtica con menor concentración en la mediana, y colas pesadas, lo que implica una mayor probabilidad de eventos extremos.

Estos resultados sugieren que los rendimientos no siguen una distribución normal, especialmente debido a la presencia de colas pesadas. Cosa que podemos comprobar al observar nuestro Histograma de Rendimientos.

Y respecto a nuestra serie de Rendimientos Logaritmicos, podemos ver como las ganancias y perdidas rondan alrededor del cero, que es un comportamiento tipico que nos dice que los cambios diarios en los rendimientos son pequeños, aunque esto no quita que veamos tambien subidas y bajadas significativas, lo que implica la presencia de eventos extremos. En especial vemos unos pocos más picos negativos y estos son más pronunciados que los positivos, lo que corresponde con nuestro sesgo negativo. 

(c) Calculo de VaR y ES

Calculando el VaR y ES para la serie completa de datos a los siguientes intervalos de confianza: α = 0,95, 0,975, y 0,99 obtuvimos lo siguiente: 

VaR y ES bajo una aproximación paramétrica asumiendo una distribución normal
0,95 VaR: -0.0279 ES: -0.0352
0,975 VaR: -0.0334 ES: -0.0401 
0,99 VaR: -0.0399 ES: -0.0458

VaR y ES bajo una aproximación paramétrica asumiendo una distribución t-student
0,95 VaR: -0.0344 ES: -0.0498 
0,975 VaR: -0.0442 ES: -0.0609 
0,99 VaR: -0.0581 ES: -0.0772

VaR y ES bajo una aproximación historica
0,95 VaR: -0.0269 ES: -0.0405
0,975 VaR: -0.0355 ES: -0.0504
0,99 VaR: -0.0474 ES: -0.0655

VaR y ES bajo una aproximación Monte Carlo
0,95 VaR: -0.0281 ES: -0.0355
0,975 VaR: -0.0333 ES: -0.0408
0,99 VaR: -0.0395 ES: -0.0449

Donde lo primero que podemos destacar es que el Expected Shortfall es más negativo que su respectivo VaR ya que como sabemos es la pérdida promedio en los peores escenarios, es decir, en la cola de la distribución.

Para cada diferente aproximación tambien observamos que mientras más aumenta el intervalo de confianza, tambien lo hace el VaR y el ES lo que indica que se van considerando escenarios de perdida cada vez más extremos.

Respecto a la comparativa de aproximaciones, podemos ver que como la aproximación asumiendo una distribucion T-student es la que genera estimaciones con el mayor número de perdidas, y que las aproximaciones Monte Carlo y Normal tienen valores muy parecidos porque ambos se generean bajo el supuesto de normalidad.

(d) Ganancias y pérdidas con α = 0,95 y 0,99 con una rolling window de 252 retornos

En nuestra serie de tiempo podemos observas como obviamente tanto el VaR como el ES varian atravez del tiempo, vemos de una forma muy marcada, más si prestamos atención a la estimación parametrica con α = 0,99, que despues de picos negativos muy pronunciados las estimaciones de riesgo más negativas por la incertidumbre que se tiene, mientras que en periodos de mayor estabilidad, donde las ganancias y perdidas no se mueven mucho son menos pronunciadas en todas las aproximaciones, hasta podemos ver como casi se emparejan en algunos casos, aunque eso si, el ES siempre esta más abajo que su respectivo VaR. Mencionar por ultimo que aun asi hay puntos en los cuales los rendimientos reales caen por debajo del VaR estimado, lo que corresponde a violaciones, aunque la cantidad de estos puntos depende del intervalo de confianza que estemos tomando, pero esto es cosa de otro inciso.

(e) Calculo del numero de violaciones

Como vimos antes, tenemos puntos en los cuales los rendimientos reales caen por debajo del VaR estimado, osea las violaciones, en nuestra tabla podemos ver como para el VaR al 95% obtuvimos porcentajes de violaciones de 5.79% en la aproximación historica y 5.23% en la paramétrica, valores que son cercanos al 5% esperado, por lo que podemos decir hay una buena calibración en este nivel de confianza.
Sin embargo esto es distinto para el VaR al 99% ya que obtuvimos porcentajes de 1.48% para la aproximación historica y 1.99% para la paramétrica, que parece poco pero en relación al esperado 1% teorico ambos son mucho más grandes. Para el ES podemos ver como siempre es más pequeño el porcentaje ya que captura solo las perdidas más severas.

Podemos concluir que la aproximación historica tiene un mejor desempeño ya que los porcentajes que obtenemos se parecen más a los teoricos, especialmente en el caso de el VaR al 99% ya que si bien 1.48% es más grande de lo esperado, no lo es tanto en comparación con el 1.99% del enfoque parametrico.

(f) VaR volatilidad móvil

Por ultimo, vemos en la grafica como el VaR cambia atravez del tiempo en función a los rendimientos. En periodos de alta volatilidad el VaR se vuelve más negativo ya que hay un mayor nivel de riesgo, mientras que en periodos de estabilidad se reduce el riesgo se reduce por asi decirlo. Tambien vemos que otra vez obtuvimos para el VaR al 95% un porcentaje de violacion de 4.66%, similar al 5% teorico, cin embargo para el VaR al 99% este fue de 1.79% por lo que podemos decir que se subestima el riesgo en casos extremos.

Por lo que podemos decir que el uso de volatilidad móvil si mejora la capacidad del modelo para adaptarse a cambios en el mercado, aunque el supuesto de normalidad sigue siendo una limitación importante para capturar eventos extremos.
