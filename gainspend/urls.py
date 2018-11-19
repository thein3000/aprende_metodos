from django.urls import path

from . import views

urlpatterns = [
    # ------------------------------ MOVEMENT -----------------------------------
    path('',views.main_dashboard, name='main_dashboard'),
    path('register_method_completion/',views.register_method_completion, name='register_method_completion'),
    path('successful_excercise/',views.successful_excercise, name='successful_excercise'),
    path('preface_interpolacion_lineal/',views.preface_interpolacion_lineal, name='preface_interpolacion_lineal'),
    path('preface_interpolacion_lineal/excercise',views.excercise_interpolacion_lineal, name='excercise_interpolacion_lineal'),
    path('preface_newton_hacia_adelante/',views.preface_newton_hacia_adelante, name='preface_newton_hacia_adelante'),
    path('preface_newton_hacia_adelante/excercise',views.excercise_newton_hacia_adelante, name='excercise_newton_hacia_adelante'),
    path('preface_newton_hacia_atras/',views.preface_newton_hacia_atras, name='preface_newton_hacia_atras'),
    path('preface_newton_hacia_atras/excercise',views.excercise_newton_hacia_atras, name='excercise_newton_hacia_atras'),
    # path('preface_newton_con_diferencias_divididas/',views.preface_newton_con_diferencias_divididas, name='preface_newton_con_diferencias_divididas'),
    # path('preface_newton_con_diferencias_divididas/excercise',views.excercise_newton_con_diferencias_divididas, name='excercise_newton_con_diferencias_divididas'),
    path('preface_lagrange/',views.preface_lagrange, name='preface_lagrange'),
    path('preface_lagrange/excercise',views.excercise_lagrange, name='excercise_lagrange'),
    path('preface_punto_fijo/',views.preface_punto_fijo, name='preface_punto_fijo'),
    path('preface_punto_fijo/excercise',views.excercise_punto_fijo, name='excercise_punto_fijo'),
    # path('preface_grafico/',views.preface_grafico, name='preface_grafico'),
    # path('preface_grafico/excercise',views.excercise_grafico, name='excercise_grafico'),
    # path('preface_bisectriz/',views.preface_bisectriz, name='preface_bisectriz'),
    # path('preface_bisectriz/excercise',views.excercise_bisectriz, name='excercise_bisectriz'),
    path('preface_newton_raphson/',views.preface_newton_raphson, name='preface_newton_raphson'),
    path('preface_newton_raphson/excercise',views.excercise_newton_raphson, name='excercise_newton_raphson'),
    path('preface_falsa_posicion/',views.preface_falsa_posicion, name='preface_falsa_posicion'),
    path('preface_falsa_posicion/excercise',views.excercise_falsa_posicion, name='excercise_falsa_posicion'),
    path('preface_secante/',views.preface_secante, name='preface_secante'),
    path('preface_secante/excercise',views.excercise_secante, name='excercise_secante'),
    path('preface_montante/',views.preface_montante, name='preface_montante'),
    path('preface_montante/excercise',views.excercise_montante, name='excercise_montante'),
    path('preface_gauss_jordan/',views.preface_gauss_jordan, name='preface_gauss_jordan'),
    path('preface_gauss_jordan/excercise',views.excercise_gauss_jordan, name='excercise_gauss_jordan'),
    path('preface_eliminacion_gaussiana/',views.preface_eliminacion_gaussiana, name='preface_eliminacion_gaussiana'),
    path('preface_eliminacion_gaussiana/excercise',views.excercise_eliminacion_gaussiana, name='excercise_eliminacion_gaussiana'),
    # path('preface_gauss_seidel/',views.preface_gauss_seidel, name='preface_gauss_seidel'),
    # path('preface_gauss_seidel/excercise',views.excercise_gauss_seidel, name='excercise_gauss_seidel'),
    # path('preface_jacobi/',views.preface_jacobi, name='preface_jacobi'),
    # path('preface_jacobi/excercise',views.excercise_jacobi, name='excercise_jacobi'),
    path('preface_linea_recta/',views.preface_linea_recta, name='preface_linea_recta'),
    path('preface_linea_recta/excercise',views.excercise_linea_recta, name='excercise_linea_recta'),
    path('preface_cuadratica/',views.preface_cuadratica, name='preface_cuadratica'),
    path('preface_cuadratica/excercise',views.excercise_cuadratica, name='excercise_cuadratica'),
    path('preface_cubica/',views.preface_cubica, name='preface_cubica'),
    path('preface_cubica/excercise',views.excercise_cubica, name='excercise_cubica'),
    # path('preface_lineal_con_funcion/',views.preface_lineal_con_funcion, name='preface_lineal_con_funcion'),
    # path('preface_lineal_con_funcion/excercise',views.excercise_lineal_con_funcion, name='excercise_lineal_con_funcion'),
    # path('preface_cuadratica_con_funcion/',views.preface_cuadratica_con_funcion, name='preface_cuadratica_con_funcion'),
    # path('preface_cuadratica_con_funcion/excercise',views.excercise_cuadratica_con_funcion, name='excercise_cuadratica_con_funcion'),
    path('preface_newton_cotes_cerradas/',views.preface_newton_cotes_cerradas, name='preface_newton_cotes_cerradas'),
    path('preface_newton_cotes_cerradas/excercise',views.excercise_newton_cotes_cerradas, name='excercise_newton_cotes_cerradas'),
    path('preface_newton_cotes_abiertas/',views.preface_newton_cotes_abiertas, name='preface_newton_cotes_abiertas'),
    path('preface_newton_cotes_abiertas/excercise',views.excercise_newton_cotes_abiertas, name='excercise_newton_cotes_abiertas'),
    path('preface_regla_un_tercio_de_simpson/',views.preface_regla_un_tercio_de_simpson, name='preface_regla_un_tercio_de_simpson'),
    path('preface_regla_un_tercio_de_simpson/excercise',views.excercise_regla_un_tercio_de_simpson, name='excercise_regla_un_tercio_de_simpson'),
    path('preface_regla_tres_octavos_de_simpson/',views.preface_regla_tres_octavos_de_simpson, name='preface_regla_tres_octavos_de_simpson'),
    path('preface_regla_tres_octavos_de_simpson/excercise',views.excercise_regla_tres_octavos_de_simpson, name='excercise_regla_tres_octavos_de_simpson'),
    path('preface_euler_hacia_adelante/',views.preface_euler_hacia_adelante, name='preface_euler_hacia_adelante'),
    path('preface_euler_hacia_adelante/excercise',views.excercise_euler_hacia_adelante, name='excercise_euler_hacia_adelante'),
    # path('preface_euler_hacia_atras/',views.preface_euler_hacia_atras, name='preface_euler_hacia_atras'),
    # path('preface_euler_hacia_atras/excercise',views.excercise_euler_hacia_atras, name='excercise_euler_hacia_atras'),
    path('preface_euler_modificado/',views.preface_euler_modificado, name='preface_euler_modificado'),
    path('preface_euler_modificado/excercise',views.excercise_euler_modificado, name='excercise_euler_modificado'),
    path('preface_runge_kutta_segundo_orden/',views.preface_runge_kutta_segundo_orden, name='preface_runge_kutta_segundo_orden'),
    path('preface_runge_kutta_segundo_orden/excercise',views.excercise_runge_kutta_segundo_orden, name='excercise_runge_kutta_segundo_orden'),
    path('preface_runge_kutta_tercer_orden/',views.preface_runge_kutta_tercer_orden, name='preface_runge_kutta_tercer_orden'),
    path('preface_runge_kutta_tercer_orden/excercise',views.excercise_runge_kutta_tercer_orden, name='excercise_runge_kutta_tercer_orden'),
    path('preface_runge_kutta_cuarto_orden_por_un_tercio_de_simpson/',views.preface_runge_kutta_cuarto_orden_por_un_tercio_de_simpson, name='preface_runge_kutta_cuarto_orden_por_un_tercio_de_simpson'),
    path('preface_runge_kutta_cuarto_orden_por_un_tercio_de_simpson/excercise',views.excercise_runge_kutta_cuarto_orden_por_un_tercio_de_simpson, name='excercise_runge_kutta_cuarto_orden_por_un_tercio_de_simpson'),
    path('preface_runge_kutta_cuarto_orden_por_tres_octavos_de_simpson/',views.preface_runge_kutta_cuarto_orden_por_tres_octavos_de_simpson, name='preface_runge_kutta_cuarto_orden_por_tres_octavos_de_simpson'),
    path('preface_runge_kutta_cuarto_orden_por_tres_octavos_de_simpson/excercise',views.excercise_runge_kutta_cuarto_orden_por_tres_octavos_de_simpson, name='excercise_runge_kutta_cuarto_orden_por_tres_octavos_de_simpson'),
    # path('preface_runge_kutta_de_orden_superior/',views.preface_runge_kutta_de_orden_superior, name='preface_runge_kutta_de_orden_superior'),
    # path('preface_runge_kutta_de_orden_superior/excercise',views.excercise_runge_kutta_de_orden_superior, name='excercise_runge_kutta_de_orden_superior'),
]
