from manim import *

class aplications(Scene):
    def construct(self):
        apt1 = Text("aplicación 1")
        apt1 = Text("aplicación 2")
        apt1 = Text("aplicación 3")
        apt1 = Text("aplicación 4")

class references(Scene):
    def construct(self):
        eq3 = MathTex(r"\vec{\nabla} \times \vec{E}&= \frac{\partial E_{z}}{\partial y}\hat{x}=E_{0}\cos(y-vt)\hat{x}")
        self.play(Create(eq3))
        self.wait(3)

class relation(Scene):
    def construct(self):
        
        eq1 = MathTex(r"\vec{E}=E_{0}\sin(y-vt)\hat{z}")
        eq2 = MathTex(r"\vec{B}=B_{0}\sin(y-vt)\hat{x}")
        eq3 = MathTex(r"\vec{\nabla} \times \vec{E}&= \frac{\partial E_{z}}{\partial y}\hat{x}=E_{0}\cos(y-vt)\hat{x}")
        eq4 = MathTex(r"\frac{\partial \vec{B}}{\partial t}&=-vB_{0}\cos(y-vt)\hat{x}")

        eq1.shift(UP*2 + LEFT*3.4)
        eq2.shift(UP*2 + RIGHT*3.9)
        self.play(Create(eq1), Create(eq2))
        eq3.shift(LEFT*3)
        eq4.shift(RIGHT*4)
        self.play(Create(eq3), Create(eq4))

        
        eq5 = MathTex(r"\vec{\nabla} \times \vec{E} &= -\frac{\partial \vec{B}}{\partial t}")
        eq6 = MathTex(r"E_{0}\cos(y-vt)&=vB_{0}\cos(y-vt) ")
        eq7 = MathTex(r"E_{0}&=vB_{0} =cB_{0}")
        eq7.set_color_by_gradient("#33ccff","#ff00ff")

        self.play(Uncreate(eq1), Uncreate(eq2))
        eq5.shift(DOWN*2)
        self.play(Create(eq5))
        eq6.shift(UP*2)
        self.play(Create(eq6))
        self.play(Uncreate(eq5))
        self.play(Uncreate(eq3), Uncreate(eq4))
        self.play(ReplacementTransform(eq6, eq7))
        
        
        eq8 = MathTex(r"|\vec{S}|&=\frac{1}{\mu_{0}}|\vec{E} \times \vec{B}|")
        eq9 = MathTex(r"\frac{1}{\mu_{0}}\left| |\vec{E}| |\vec{B}|\sin(90^{\circ})\right|")
        eq10 = MathTex(r"\frac{1}{\mu_{0}} \frac{E^{2}}{c} = \epsilon_{0}cE^{2}")
        eq11 = MathTex(r"\epsilon_{0}c\left[ \frac{kqa\sin \theta}{c^{2}R} \right]^{2}=\frac{\epsilon_{0}k^{2}q^{2}a^{2}\sin ^{2}\theta}{c^{3}R^{2}}")

        
        eq12 = MathTex(r"P=\int \mid \vec{S}\mid R^{2} \, d\Omega")
        eq13 = MathTex(r"P= \int_{0}^{2\pi}\int_{0}^{\pi}  \frac{\epsilon_{0}k^{2}q^{2}a^{2}\sin ^{2}\theta}{c^{3}R^{2}} R^{2} \,d\Omega ")
        eq14 = MathTex(r"P=\frac{\epsilon_{0}k^{2}q^{2}a^{2}\sin ^{2}\theta}{c^{3}} \int_{0}^{2\pi}\int_{0}^{\pi} \sin ^{3}\theta \,d \theta d\phi")
        
        eq15 = MathTex(r"P=\frac{q^{2}a^{2}}{6\pi \epsilon_{0}c^{3}}")
        eq15.set_color_by_gradient("#33ccff","#ff00ff")
        self.wait(3)
        

class Wave(MovingCameraScene):
    def construct(self):
        # Crear y animar el sistema de coordenadas sin los números de la escala y con un color de cuadrícula personalizado
        axes = NumberPlane(
            x_range=[-7, 7],
            y_range=[-5, 5],
            background_line_style={"stroke_color": GREY_E, "stroke_width": 2},  # Change grid color here
            axis_config={
                "stroke_color": GREY_E,  # Color of the axes
                "stroke_width": 4,  # Width of the axes lines
                "include_numbers": False  # Do not include numbers on axes
            },
        )

        # Animar la creación del sistema de coordenadas
        self.play(Create(axes), run_time=3, lag_ratio=0.2)  # Control the time here
        
        Y = Arrow(start=ORIGIN, end=np.array([0, 4, 0]), buff=0, color=WHITE)
        X = Arrow(start=ORIGIN, end=np.array([-4, -2, 0]), buff=0, color=WHITE)
        Z = Arrow(start=ORIGIN, end=np.array([4.3, -1.5, 0]), buff=0, color=WHITE)
        
        self.play(Create(X), Create(Y), Create(Z))
        self.wait(3)


class Potencia_larmor(Scene):
    def construct(self):

        eq1 = MathTex(r"\vec{\nabla} \cdot (\vec{E} \times \vec{B}) = \vec{B} \cdot \vec{\nabla} \times \vec{E} - \vec{E} \cdot \vec{\nabla} \times \vec{B}")
        eq2 = MathTex(r"\frac{\vec{\nabla} \cdot (\vec{E} \times \vec{B})}{\mu_{0}} = \vec{B} \cdot \vec{\nabla} \times \frac{\vec{E}}{\mu_{0}} - \vec{E} \cdot \vec{\nabla} \times \frac{\vec{B}}{\mu_{0}}")
        amper = MathTex(r"\vec{\nabla} \times \vec{B} = \mu_{0} \vec{J} + \mu_{0} \epsilon_{0} \frac{\partial \vec{E}}{\partial t}")
        faraday = MathTex(r"\vec{\nabla} \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}")
        amper2 = MathTex(r"\vec{\nabla} \times \vec{B} = \mu_{0} \epsilon_{0} \frac{\partial \vec{E}}{\partial t}")
        UB = MathTex(r"\vec{B} \cdot \vec{\nabla} \times \frac{\vec{E}}{\mu_{0}} = -\vec{B} \cdot \frac{\vec{\partial B}}{\partial t} \frac{1}{\mu_{0}} = -\frac{1}{2} \frac{\partial}{\partial t}(\vec{B} \cdot \vec{B}) \frac{1}{\mu_{0}} = -\frac{\partial}{\partial t}\left( \frac{1}{2\mu_{0}} B^{2} \right) = \frac{\partial U_{B}}{\partial t}").scale(0.9)
        UE = MathTex(r"\vec{E} \cdot \vec{\nabla} \times \frac{\vec{B}}{\mu_{0}} = \vec{E} \cdot \epsilon_{0} \frac{\partial}{\partial t} (\vec{E} \cdot \vec{E}) = \frac{\partial}{\partial t}\left( \frac{\epsilon_{0}}{2} E^{2}\right) = \frac{\partial U_{E}}{\partial t}")
        UE_UB = MathTex(r"\vec{\nabla} \cdot \left( \frac{1}{\mu_{0}} \vec{E} \times \vec{B}\right) = -\frac{\partial}{\partial t}(U_{E}+U_{B})")
        eq3 = MathTex(r"\iiint_{V} \vec{\nabla} \cdot \left( \frac{1}{\mu_{0}} \vec{E} \times \vec{B} \right) dV = -\frac{\partial}{\partial t} \iiint_{V} (U_{E}+U_{B})dV")
        Gauss = MathTex(r"\iint_{\partial U} \vec{F} \cdot d\vec{S} = \iiint_{U} \vec{\nabla} \cdot \vec{F}dV")
        eq5 = MathTex(r"\iint_{S} \left( \frac{1}{\mu_{0}} \vec{E} \times \vec{B}\right) d\vec{S} = -\frac{\partial}{\partial t} \iiint_{V}(U_{B}+ U_{E})dV")
        poynting = MathTex(r"\vec{S} = \frac{\vec{E} \times \vec{B}}{\mu_{0}}")
        
        eq1.shift(UP*2)
        self.play(Write(eq1))
        self.wait(1)
        self.play(Write(eq2))
        self.wait(1)
    
        amper.set_color_by_gradient("#33ccff","#ff00ff")
        amper2.set_color_by_gradient("#33ccff","#ff00ff")
        faraday.set_color_by_gradient("#33ccff","#ff00ff")
        
        amper.shift(DOWN*1.5 + LEFT*3)
        amper2.shift(DOWN*1.5 + LEFT*3)
        faraday.shift(DOWN*1.5 + RIGHT*3.5)

        self.play(Write(amper))
        self.wait(1)
        self.play(Write(faraday))
        self.wait(1)
        self.play(ReplacementTransform(amper, amper2))
        
        self.wait(1)
        UB.shift(UP*2)
        self.play(ReplacementTransform(eq1,UB))
        self.wait(1)
        self.play(ReplacementTransform(eq2,UE))
        self.wait(1)
        self.play(Uncreate(amper2), Uncreate(faraday))
        self.wait(1)

        
        UE_UB.set_color_by_gradient("#33ccff","#ff00ff")
        UE_UB.shift(DOWN*1.5)
        self.play(Write(UE_UB))
        self.wait(1)
        self.play(Uncreate(UB), Uncreate(UE))
        self.play(UE_UB.animate.move_to(UP*1.5))
        eq3.shift(UP*1.5)
        self.wait(1)
        self.play(ReplacementTransform(UE_UB, eq3))
        self.wait(1)
        self.play(Write(Gauss))
        eq5.shift(UP*1.5)
        self.play(ReplacementTransform(eq3, eq5))
        self.play(Uncreate(Gauss))
        self.wait(1)
        self.play(eq5.animate.move_to(ORIGIN))
        self.wait(1)
        poynting.set_color_by_gradient("#33ccff","#ff00ff")
        self.wait(3)
        self.play(ReplacementTransform(eq5, poynting))
        self.wait(5)
        

class Campo_irradiado(Scene):
    def construct(self):
        
        eq = MathTex(r"E_{\theta} = (v_{0}\tau - \frac{1}{2}a\tau^{2})\sin(\theta)")
        self.play(Write(eq))

        eq1 = MathTex(r"E_{\theta} \approx v_{0}\tau \sin(\theta)")
        eq1.set_color_by_gradient("#33ccff","#ff00ff")
        self.wait()

        self.play(ReplacementTransform(eq, eq1))
        self.play(eq1.animate.to_corner(UL))

        eq3 = MathTex(r"E_{r}=c\tau")
        eq3.set_color_by_gradient("#33ccff","#ff00ff")
        self.play(Write(eq3))
        self.play(eq3.animate.to_corner(UR))

        self.wait()
        eq4 = MathTex(r"\frac{E_{\theta}}{E_{r}}=\frac{v_{0}\tau \sin(\theta)}{c\tau}")
        self.play(Write(eq4))

        self.wait()
        #self.play(Uncreate(eq))
        eq5 = MathTex(r"E_{\theta} = \frac{v_{0}\tau \sin(\theta)}{c\tau} E_{r}")
        eq5.set_color_by_gradient("#33ccff","#ff00ff")
        self.play(ReplacementTransform(eq4, eq5))
        self.play(eq5.animate.shift(UP*3.2))
        
        self.wait()
        coulomb = Text("Campo eléctrico para una carga puntual").scale(0.5)
        coulomb.shift(UP*1.5)
        self.play(Write(coulomb))

        self.wait()
        eq6 = MathTex(r"E_{r}=\frac{1}{4\pi \epsilon_{0}} \frac{q}{r^{2}}")
        eq7 = MathTex(r"E_{r}=\frac{1}{4\pi \epsilon_{0}} \frac{1}{r} \frac{q}{r}")
        eq8 = MathTex(r"E_{r}=\frac{1}{4\pi \epsilon_{0}} \frac{1}{c\tau} \frac{q}{r}")
        
        self.play(Write(eq6))
        self.play(ReplacementTransform(eq6, eq7))
        self.wait()
        self.play(ReplacementTransform(eq7, eq8))
        self.wait()

        eq99 = MathTex(r"E_{\theta}= \frac{v_{0} \sin(\theta)}{c} \left(\frac{1}{c\tau} \frac{kq}{4\pi \epsilon_{0} r}\right)")
        eq99.shift(DOWN*2)
        self.play(Write(eq99))
        eq9 = MathTex(r"E_{\theta}= \frac{|a|\tau \sin(\theta)}{c} \left(\frac{1}{c\tau} \frac{kq}{4\pi \epsilon_{0} r}\right)")
        eq9.shift(DOWN*2)

        self.play(ReplacementTransform(eq99, eq9))
        self.wait()

        eq10 = MathTex(r"\vec{E}_{\theta}=\frac{qa\sin(\theta)}{4 \pi \epsilon_{0} c^{2} r} \hat{\theta}") 
        eq10.set_color_by_gradient("#33ccff","#ff00ff")
        eq10.shift(DOWN*2)
        self.play(ReplacementTransform(eq9, eq10))
        
        self.play(Uncreate(eq1), Uncreate(eq3), Uncreate(eq5), Uncreate(eq8), Uncreate(coulomb))
        self.play(eq10.animate.move_to(UP*2))    

        explanation_title = Text("Donde:").scale(0.8).to_corner(UL+DOWN*1)
        e_rad = MathTex(r" \mathbf{E}_{\theta} : \text{Campo eléctrico irradiado}").scale(0.6)
        q = MathTex(r" q : \text{Carga de la partícula}").scale(0.6)
        epsilon_0 = MathTex(r" \epsilon_0 : \text{Permitividad del vacío}").scale(0.6)
        a = MathTex(r" |\mathbf{a}| : \text{Magnitud de la aceleración de la carga}").scale(0.6)
        theta = MathTex(r" \theta : \text{Ángulo entre la dirección de la aceleración y la dirección de observación}").scale(0.6)
        c = MathTex(r" c : \text{Velocidad de la luz en el vacío}").scale(0.6)
        r = MathTex(r" r : \text{Distancia al punto de observación desde la partícula}").scale(0.6)
        hat_theta = MathTex(r" \hat{\theta} : \text{Vector unitario perpendicular a la dirección de observación en el plano de la aceleración}").scale(0.6)

        e_rad.next_to(explanation_title, DOWN*1, buff=0.3, aligned_edge=LEFT)
        q.next_to(e_rad, DOWN, buff=0.1, aligned_edge=LEFT)
        epsilon_0.next_to(q, DOWN, buff=0.1, aligned_edge=LEFT)
        a.next_to(epsilon_0, DOWN, buff=0.1, aligned_edge=LEFT)
        theta.next_to(a, DOWN, buff=0.1, aligned_edge=LEFT)
        c.next_to(theta, DOWN, buff=0.1, aligned_edge=LEFT)
        r.next_to(c, DOWN, buff=0.1, aligned_edge=LEFT)
        hat_theta.next_to(r, DOWN, buff=0.1, aligned_edge=LEFT)

        self.play(Write(explanation_title))
        self.wait(0.5)
        self.play(
            Write(e_rad),
            Write(q),
            Write(epsilon_0),
            Write(a),
            Write(theta),
            Write(c),
            Write(r),
            Write(hat_theta),
            run_time=1.5
        )

        
        #larmor = ImageMobject("larmor.png").scale(1)
        #self.add(larmor)

        self.wait(4)

        



class FieldLines(MovingCameraScene):
    def construct(self):
        # Step 1: Create and animate the coordinate system without arrow tips and custom grid color
        axes = NumberPlane(
            x_range=[-7, 7],
            y_range=[-5, 5],
            background_line_style={"stroke_color": GREY_E, "stroke_width": 2}  # Change grid color here
        )
        axes.add_coordinates()
        self.play(Create(axes), run_time=3, lag_ratio=0.2)  # Control the time here
        self.wait(1)
        
        # Step 2: Create and animate the negative charge at the origin
        charge = Dot(point=LEFT*5, color=RED_D, stroke_width=0).scale(2)  # Change color to BLUE
        charge_label = Tex("-", color=WHITE, stroke_width=0)
        charge_label.add_updater(lambda m: m.move_to(charge).shift(DOWN*0.01))  # Update position
        charge_label.scale(1.5)
        self.play(FadeIn(charge), Write(charge_label))  # Remove run_time here
        self.wait(2)
        
        # Step 3: Draw and animate the field lines
        field_lines = VGroup()
        num_lines = 10
        for i in range(num_lines):
            angle = i * TAU / num_lines
            line = Line(
                start=LEFT*5, 
                end=LEFT*5 + 10* np.array([np.cos(angle), np.sin(angle), 0]),  # Adjust line length here
                color=WHITE
            )
            field_lines.add(line)
        
        self.play(*[Create(line) for line in field_lines], run_time=3)  # Control the time here
        self.wait(1)
        
        # Step 4: Move the charge and the field lines to the origin without scaling
        self.play(
            charge.animate.shift(ORIGIN - charge.get_center()).set_rate_func(there_and_back),
            *[line.animate.shift(ORIGIN - line.get_start()) for line in field_lines],
            run_time=5  # Ajusta el tiempo total de la animación
        )

        self.play(*[line.animate.set_color(GRAY_D) for line in field_lines])
            
        # Step 5: Create circles for zoom effect
        circle = Circle(radius=3, color=WHITE)
        circle2 = Circle(radius=4, color=WHITE)
        tittle = MathTex(r"R_{1}=cT").scale(0.7)
        tittle2 = MathTex(r"R_{2}=c(T-\tau)").scale(0.7)
        tittle.shift([-1.5, -1.9, 0])
        tittle2.shift([-5, -2, 0])
        self.play(Write(tittle))
        self.play(Create(circle))
        self.play(Write(tittle2))
        self.play(Create(circle2))

        self.wait(1)
        self.play(circle.animate.set_color(GRAY_D), circle2.animate.set_color(GRAY_D))

        # Step 6: Save the current state of the camera frame
        camera1 = self.camera.frame.save_state()

        # Step 7: Apply a zoom transformation to a specific point
        self.play(
            self.camera.frame.animate.set(width=8).move_to([3.5, 1.8, 10]),
            run_time=2
        )
        angle = 0.6283
        line = Line(ORIGIN, 3*RIGHT).rotate(angle, about_point=ORIGIN)
        self.play(Create(line))
        
        start_point = 4 * RIGHT
        end_point = 10 * RIGHT
        dotted_line = DashedLine(start_point, end_point, color=WHITE).rotate(angle, about_point=ORIGIN)
        
        final_start_point =  np.array([2.077, 0, 0])
        final_end_point =  np.array([8.47, 4.621, 0])
        
        # Mover la línea a las coordenadas finales

        self.play(Create(dotted_line))
        self.play(dotted_line.animate.put_start_and_end_on(final_start_point, final_end_point))
        self.play(dotted_line.animate.set_color(GRAY_D))

        # Agregar la línea a la escena


        self.wait(1)

        star_point = [3.775, 1.225, 0]
        end_point  = [6, 2.83, 0]

        p1_start   = [2.43, 1.75, 0]
        p1_end     = [3.775, 1.225, 0]

        Efield1 = Line(p1_start, p1_end)
        Efield1.set_color(WHITE)

        Efield2 = Arrow(star_point, end_point).scale(1.22)
        Efield2.set_color(WHITE)

        label1 = MathTex(r"\Vec{E}")
        label1.shift([6, 1.8, 0])
        self.play(Create(Efield1), Create(Efield2), Write(label1))

        Er_1S = [2.43, 1.75, 0] 
        Er_1E = [3.24, 2.34 , 0]

        Et_1S = [2.43, 1.75, 0]
        Et_1E = [3.16, 0.78,  0]

        Erfield = Arrow(Er_1S, Er_1E).scale(2)
        Erfield.set_color(PURE_RED)

        Etfield = Arrow(Et_1S, Et_1E).scale(1.7)
        Etfield.set_color(PURE_RED)
        label_r  = MathTex(r"\vec{E}_{r}")
        label_r.shift([2.5, 2.5, 0])
        label_t  = MathTex(r"\vec{E}_{\theta}")
        label_t.shift([2.2, 1.1, 0])
        
        self.play(Create(Erfield))
        self.play(Write(label_r))
        

        self.wait()

        self.play(Create(Etfield))
        self.play(Write(label_t))
        
        self.wait()
        origen_line = ORIGIN    
        end_line = np.array([10, 0, 0])
        line1 = Line(origen_line, end_line)
        self.play(Create(line1))
        angle = Angle(line1, line, radius=0.5, other_angle=False)
        angle_label = MathTex(r"\theta")
        angle_label.shift([0.8, 0.3, 0])
        self.play(Create(angle), Write(angle_label))

        self.wait()
        
        charge1 = Dot(point=ORIGIN, color=RED_D, stroke_width=0).scale(2)  # Change color to BLUE
        #charge1.set_opacity(2)
        charge_label1 = Tex("-", color=WHITE, stroke_width=0)
        self.play(Create(charge1), run_time=0.01)
        self.play(ApplyMethod(charge1.shift, 2.07*RIGHT))
        self.wait()
        self.play(Etfield.animate.put_start_and_end_on(np.array([1.3, 0.94, 0]), np.array([2.07, 0, 0])))
        self.wait(2)
        
        self.play(Restore(camera1), run_time=2)
        self.wait()



if __name__ == "__main__":
    scene = Math()
    scene.render()
