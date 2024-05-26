Para asegurarte de que GitHub renderice correctamente el texto, debes seguir algunas reglas de Markdown y LaTeX. Aquí tienes el documento corregido:

```markdown
# Matemática

Sea una carga que se mueve con velocidad constante en el eje $\hat{x}$ con una velocidad inicial $\vec{v}_{0}$, la cual al pasar por el origen de nuestro sistema de referencia sufre una desaceleración en un tiempo pequeño $\tau$, y observamos qué sucede con las líneas de campo eléctrico en un tiempo $T$, donde se cumple que $T \gg \tau$.

En ese pequeño intervalo se genera una concha que separa el espacio que ahora denotaremos como Región I y II. Dado que la velocidad de la luz es un límite de velocidad universal, la información no puede viajar más rápido que ella. Dentro de la región I, el campo eléctrico se ajusta a una velocidad $c$, pero fuera de ella el campo no ha recibido la información de la desaceleración. Y dado que las líneas de campo deben ser continuas, es decir, no pueden haber cortes, podemos descomponer la parte del campo en sus componentes polares $E(r, \theta)$.

Ahora describamos la desaceleración que sufrió la carga:

$$
\vec{v}_{f} = \vec{v}_{0} + \vec{a}t \rightarrow \vec{0} = \vec{v}_{0} + \vec{a}\tau
$$

$$
\vec{a} = -\frac{v_{0}}{\tau}\hat{x} \tag{1}
$$

Ahora describamos el campo eléctrico radial, el cual está dado por la ley de Coulomb:

$$
q
$$

Según el diagrama, debe haber una proporción entre la componente radial y tangencial:

$$
\frac{E_{\theta}}{E_{r}} = \frac{v_{0}T\sin \theta}{c\tau} = \frac{\frac{v_{0}}{\tau}T\sin \theta}{c} = \frac{|a|T\sin \theta}{c}
$$

$$
\begin{align}
E_{\theta} &= \left( \frac{|a|T\sin \theta}{c} \right)E_{r} = \left( \frac{|a|T\sin \theta}{c} \right)\left[ \frac{1}{cT}\left( \frac{kq}{R} \right) \right] \\
E_{\theta} &= \frac{qk|a|\sin \theta}{c^{2}R} \tag{2}
\end{align}
$$

Donde denotaremos $(2)$ como la fórmula de Larmor. Ahora, recordando la densidad de energía volumétrica asociada a un campo electromagnético: 

_____

# Demostración del vector de Poynting

Haciendo uso de la propiedad:

$$
\vec{\nabla} \cdot (\vec{E} \times \vec{B}) = \vec{B} \cdot \vec{\nabla} \times \vec{E} - \vec{E} \cdot \vec{\nabla} \times \vec{B}
$$

Multiplicando por la permeabilidad magnética en el vacío $\mu_{0}$, se obtiene:

$$
\frac{\vec{\nabla} \cdot (\vec{E} \times \vec{B})}{\mu_{0}} = \vec{B} \cdot \vec{\nabla} \times \frac{\vec{E}}{\mu_{0}} - \vec{E} \cdot \vec{\nabla} \times \frac{\vec{B}}{\mu_{0}} \tag{1}
$$

Considerando ahora la **Ley de Ampère-Maxwell** y la **Ley de Faraday**:

$$
\begin{align}
\vec{\nabla} \times \vec{B} &= \mu_{0} \vec{J} + \mu_{0} \epsilon_{0} \frac{\partial \vec{E}}{\partial t} \tag{2} \\
\vec{\nabla} \times \vec{E} &= - \frac{\partial \vec{B}}{\partial t} \tag{3}
\end{align}
$$

Recordando la condición de trabajo en la cual se estudian las leyes de Maxwell:

> Zonas del espacio vacío suficientemente alejadas de las fuentes de los campos, es decir, se cumple que la densidad de corriente $\vec{J} = \vec{0}$ y la densidad de carga $\rho = 0$

Por lo que la expresión $(2)$ queda de la forma:

$$
\vec{\nabla} \times \vec{B} = \mu_{0} \epsilon_{0} \frac{\partial \vec{E}}{\partial t}
$$

Y la ley de Faraday mantiene su forma. Reemplazando en la primera parte de la expresión $(1)$ se obtiene:

$$
\vec{B} \cdot \vec{\nabla} \times \frac{\vec{E}}{\mu_{0}} = - \vec{B} \cdot \frac{\partial \vec{B}}{\partial t} \frac{1}{\mu_{0}} = -\frac{1}{2} \frac{\partial}{\partial t} (\vec{B} \cdot \vec{B}) \frac{1}{\mu_{0}} = -\frac{\partial}{\partial t} \left( \frac{1}{2\mu_{0}} B^{2} \right) = \frac{\partial U_{B}}{\partial t}
$$

Donde $U_{B}$ es la densidad volumétrica de energía magnética debida a un campo magnético $\vec{B}$.

Tomando ahora el segundo argumento de $(1)$ se obtiene lo siguiente:

$$
\vec{E} \cdot \vec{\nabla} \times \frac{\vec{B}}{\mu_{0}} = \vec{E} \cdot \epsilon_{0} \frac{\partial}{\partial t} (\vec{E} \cdot \vec{E}) = \frac{\partial}{\partial t} \left( \frac{\epsilon_{0}}{2} E^{2} \right) = \frac{\partial U_{E}}{\partial t} \tag{4}
$$

Donde $U_{E}$ es la densidad volumétrica de energía eléctrica debida a un campo eléctrico. Retomando $(1)$ se obtiene que:

$$
\vec{\nabla} \cdot \left( \frac{1}{\mu_{0}} \vec{E} \times \vec{B} \right) = -\frac{\partial}{\partial t} (U_{E} + U_{B}) \tag{5}
$$

Integrando $(4)$ sobre un volumen $V$ encerrado en una superficie $S$:

$$
\iiint_{V} \vec{\nabla} \cdot \left( \frac{1}{\mu_{0}} \vec{E} \times \vec{B} \right) dV = -\frac{\partial}{\partial t} \iiint_{V} (U_{E} + U_{B}) dv
$$

Aplicando el teorema integral de Gauss, o mal llamado teorema de la divergencia:

$$
\iint_{\partial U} \vec{F} \cdot d\vec{S} = \iiint_{U} \vec{\nabla} \cdot \vec{F} dV
$$

Donde $d\vec{S}$ representa un diferencial de flujo en la superficie $S$ que encierra el volumen $V$, obteniendo así que:

$$
\iint_{S} \left( \frac{1}{\mu_{0}} \vec{E} \times \vec{B} \right) d\vec{S} = - \frac{\partial}{\partial t} \iiint_{V} (U_{B} + U_{E}) dV
$$

Donde la parte de la derecha representa la energía interna en el volumen $V$ o interna en la superficie $S$, y la variación que acompaña al término implica la variación de la energía interna en el volumen $V$ o la superficie $S$. Por otra parte, el término de la izquierda $\frac{1}{\mu_{0}} \vec{E} \times \vec{B}$ representa variación de la energía, sea entrante o saliente, esto lo dictará el símbolo. Definimos así el conocido **vector de Poynting**:

$$
\vec{S} = \frac{\vec{E} \times \vec{B}}{\mu_{0}} \tag{6}
$$

Usando la notación de intensidad magnética en el vacío $\vec{H} = \frac{\vec{B}}{\mu_{0}}$:

$$
\vec{S} = \vec{E} \times \vec{H}
$$

> Pudiendo así interpretar el vector de Poynting como la energía que porta la onda electromagnética y que atraviesa la superficie $S$.

Extendiendo $(6)$ para cualquier medio material cuya permeabilidad magnética $\mu$ sea conocida, dada la expresión:

$$
\vec{H} = \frac{\vec{
