Sea una carga que se mueve con velocidad constante en el eje $\hat{x}$ con una velocidad inicial $\vec{v}_{0}$ la cual al pasar por el origen de nuestro sistema de referencia sufre una desaceleración en un tiempo pequeño $\tau$ y observamos que sucede con las líneas de campo eléctrico en un tiempo $T$ donde se cumple que $T\gg \tau$


En ese pequeño intervalo se genera una concha que separa el espacio que ahora denotaremos como Región I y II. Dado que la velocidad de la luz es un limite de velocidad universal la información no puede viajar mas rápido que ella. Dentro de la región I el campo eléctrico se ajusta a una velocidad $c$ pero fuera de ella el campo no ha recibido la información de la desaceleración. Y dado que las líneas de campo deben ser continuas, ósea no pueden haber cortes podemos descomponer la parte del campo en sus componentes polares $E(r, \theta)$

Ahora describamos la desaceleración que sufrió la carga:
$$
\vec{v}_{f}=\vec{v}_{0}+\vec{a}t \rightarrow \vec{0}=\vec{v}_{0}+\vec{a}\tau
$$
$$
\vec{a}=-\frac{v_{0}}{\tau}\hat{x} \tag{1}
$$
Ahora describamos el campo eléctrico radial el cual esta dado por la ley de Coulomb
$$
q
$$
Según el diagrama debe haber una proporción entre la componente radial y tangencial 
$$
\frac{E_{\theta}}{E_{r}}=\frac{v_{0}T\sin \theta}{c\tau}=\frac{\frac{v_{0}}{\tau}T\sin \theta}{c}=\frac{|a|T\sin \theta}{c}
$$
$$
\begin{align}
E_{\theta}&=\left( \frac{|a|T\sin \theta}{c} \right)E_{r}=\left( \frac{|a|T\sin \theta}{c} \right)\left[ \frac{1}{cT}\left( \frac{kq}{R} \right) \right] \\
E_{\theta}&=\frac{qk|a|\sin \theta}{c^{2}R} \tag{2}
\end{align}
$$
Donde denotaremos $(2)$ como la formula de Larmor. Ahora recordando la densidad de energía volumétrica asociado a un campo electromagnético: 
_____
# Demostración del vector de Poynting.
Haciendo uso de la propiedad:$$\vec{\nabla}*(\vec{E} \times \vec{B})=\vec{B}*\vec{\nabla} \times \vec{E}-\vec{E}*\vec{\nabla} \times \vec{B}$$ Multiplicando por la permeabilidad magnética en el vació $\mu_{0}$ se obtiene $(1)$ $$\frac{\vec{\nabla}*(\vec{E} \times \vec{B})}{\mu_{0}}=\vec{B}*\vec{\nabla} \times \frac{\vec{E}}{\mu_{0}}-\vec{E}*\vec{\nabla} \times \frac{\vec{B}}{\mu_{0}} \tag{1}$$
Considerando ahora la **Ley de Ampere-Maxwell** y la **Ley de Faraday** 

$$\begin{align}
\vec{\nabla } \times \vec{B}&=\mu_{0} \vec{J}+\mu_{0} \epsilon_{0}  \frac{\partial\vec{E}}{\partial t} \tag{2}\\
\vec{\nabla} \times \vec{E}&= - \frac{\partial \vec{B}}{\partial t} \tag{3}
\end{align} 
$$
Recordando la condición de trabajo en la cual se estudian las leyes de Maxwell 

> Zonas del espacio vacío suficientemente alejadas de las fuentes de los campos, ósea, se cumple que la densidad de corriente $\vec{J}=\vec{0}$ y la densidad de carga $\rho=0$

Por lo que las expresión $(2)$ queda de la forma:

$$\vec{\nabla}\times \vec{B} =\mu_{0} \epsilon_{0}  \frac{\partial\vec{E}}{\partial t}$$
y la ley de Faraday mantiene su forma, remplazando en la primera parte de la expresión $(1)$ se obtiene: $$\vec{B}* \vec{\nabla} \times \frac{\vec{E}}{\mu_{0}}=- \vec{B} *\frac{\vec{\partial B}}{\partial t} \frac{1}{\mu_{0}}=-\frac{1}{2} \frac{\partial}{\partial t}(\vec{B}* \vec{B}) \frac{1}{\mu_{0}}= -\frac{\partial}{\partial t}\left( \frac{1}{2\mu_{0}} B^{2} \right)=\frac{\partial U_{B}}{\partial t}$$Donde $U_{B}$ es la densidad volumétrica de energía magnética debida a un campo magnético $\vec{B}$. 

Tomando ahora el segundo argumento de $(1)$ se obtiene lo siguiente:

$$\vec{E}*\vec{\nabla} \times \frac{\vec{B}}{\mu_{0}}=\vec{E}* \epsilon_{0} \frac{\partial}{\partial t} (\vec{E}* \vec{E})=\frac{\partial}{\partial t}\left( \frac{\epsilon_{0}}{2} E^{2}\right)=\frac{\partial U_{E}}{\partial t} \tag{4}$$
Donde $U_{E}$ es la densidad volumétrica de energía eléctrica debida a un campo eléctrico. Retomando $(1)$ se obtiene que:

$$\vec{\nabla}*\left( \frac{1}{\mu_{0}} \vec{E} \times \vec{B}\right)=-\frac{\partial}{\partial t}(U_{E}+U_{B}) \tag{5}$$
Integrando $(4)$ de un volumen $V$  encerrado en una superficie $S$ 

$$\iiint_{V} \vec{\nabla}*\left( \frac{1}{\mu_{0}} \vec{E} \times \vec{B} \right)dV=-\frac{\partial}{\partial t} \iiint_{V} (U_{E}+U_{B})dv$$
Aplicando el teorema integral de Gauss, o mal llamado teorema de la divergencia$$\iint _{\partial U} \vec{F} \cdot d \vec{S}=\iiint_{U}\vec{\nabla}\cdot \vec{F}dV$$
Donde $d\vec{S}$ representa un diferencial de flujo en la superficie $S$ que encierra el volumen $V$ obteniendo así que:

$$\iint_{S}\left( \frac{1}{\mu_{0}} \vec{E} \times \vec{B}\right) d\vec{S}=- \frac{\partial}{\partial t} \iiint_{V}(U_{B}+ U_{E})dV$$
Donde la parte de la derecha representa la energía interna en el volumen $V$ o interna en la superficie $S$ y la variación que acompaña al termino implica la variación de la energía interna en el volumen $V$ o la superficie $S$. Por otra parte el termino de la izquierda $\frac{1}{\mu_{0}} \vec{E} \times \vec{B}$ representa variación de la energía, sea entrante o saliente, esto lo dictara el símbolo, definimos así el conocido **vector de Poynting** $$\vec{S}=\frac{\vec{E} \times \vec{B}}{\mu_{0}} \tag{6}$$
Usando la notación de intensidad magnética en el vacío $\vec{H}=\frac{\vec{B}}{\mu_{0}}$:
$$\vec{S}=\vec{E} \times \vec{H}$$
> Pudiendo así interpretar el vector de Poynting como la energía que porta la onda electromagnética y que atraviesa la superficie S

Extendiendo $(6)$ para cualquier medio material cuya permeabilidad magnética $\mu$ sea conocida dada la expresión:$$\vec{H}=\frac{\vec{B}}{\mu}$$
_____
![[campo.png]]
$$
\begin{align}
\vec{E}=E_{0}\sin(y-vt)\hat{z} \\
\vec{B}=B_{0}\sin(y-vt)\hat{x}
\end{align}
$$
$$
\begin{align}
\vec{\nabla} \times \vec{E}&= \frac{\partial E_{z}}{\partial y}\hat{x}=E_{0}\cos(y-vt)\hat{x} \\
\frac{\partial \vec{B}}{\partial t}&=-vB_{0}\cos(y-vt)\hat{x}  
\end{align}
$$
De la **Ley de Faraday** se cumple:
$$
\begin{align}
\vec{\nabla} \times \vec{E} &= -\frac{\partial \vec{B}}{\partial t} \\
E_{0}\cos(y-vt)&=vB_{0}\cos(y-vt) \\
E_{0}&=vB_{0} =cB_{0}
\end{align}
$$

Volviendo a nuestra relación del vector de Poynting asociado al campo irradiado por una carga se cumple:

$$
\begin{align}
|\vec{S}|&=\frac{1}{\mu_{0}}|\vec{E} \times \vec{B}| \\
&= \frac{1}{\mu_{0}}\left| |\vec{E}| |\vec{B}|\sin(90^{\circ})\right| \\
&=\frac{1}{\mu_{0}} \frac{E^{2}}{c} = \epsilon_{0}cE^{2} \\
&=\epsilon_{0}c\left[ \frac{kqa\sin \theta}{c^{2}R} \right]^{2}=\frac{\epsilon_{0}k^{2}q^{2}a^{2}\sin ^{2}\theta}{c^{3}R^{2}}
\end{align}
$$

Obteniendo ahora la potencia irradiada de forma isotrópica en una ángulo solido
$$
\begin{align}
P&=\int \mid \vec{S}\mid R^{2} \, d\Omega  \\
P&= \int_{0}^{2\pi}\int_{0}^{\pi}  \frac{\epsilon_{0}k^{2}q^{2}a^{2}\sin ^{2}\theta}{c^{3}R^{2}} R^{2} \,d\Omega \\
P&=\frac{\epsilon_{0}k^{2}q^{2}a^{2}\sin ^{2}\theta}{c^{3}} \int_{0}^{2\pi}\int_{0}^{\pi} \sin ^{3}\theta \,d \theta d\phi
\end{align}
$$
$$
P=\frac{q^{2}a^{2}}{6\pi \epsilon_{0}c^{3}}
$$



# Referencias 

- [[Eisberg_resnick-quantum_physics.pdf]]
- [Thomson's Derivation of the Larmor Formula](http://www.mysearch.org.uk/website1/html/475.Radiation.html) 
- ELECTRICITY AND MAGNETISM, EDWARD M. PURCELL, Harvard University, Massachusetts
