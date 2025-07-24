subroutine rk4g_solver(n, h, y0, y_out)
    implicit none
    integer, intent(in) :: n
    real*8, intent(in) :: h
    real*8, intent(in) :: y0(3)
    real*8, intent(out) :: y_out(3, n+1)

    real*8 :: A, B, C, D
    real*8 :: K1(3), K2(3), K3(3), K4(3)
    real*8 :: y(3)
    integer :: i

    A = (sqrt(2.d0) - 1.d0)/2.d0
    B = (2.d0 - sqrt(2.d0))/2.d0
    C = -sqrt(2.d0)/2.d0
    D = (2.d0 + sqrt(2.d0))/2.d0

    y = y0
    y_out(:, 1) = y0

    do i = 1, n
        call f(y, K1)
        call f(y + 0.5d0*h*K1, K2)
        call f(y + h*(A*K1 + B*K2), K3)
        call f(y + h*(C*K2 + D*K3), K4)

        y = y + (h/6.d0)*(K1 + K4) + (h/3.d0)*(B*K2 + D*K3)
        y_out(:, i+1) = y
    end do
end subroutine rk4g_solver

subroutine f(y, dy)
    implicit none
    real*8, intent(in) :: y(3)
    real*8, intent(out) :: dy(3)
    real*8 :: k1, k2

    k1 = 1.d0
    k2 = 0.5d0

    dy(1) = -k1 * y(1)
    dy(2) = k1 * y(1) - k2 * y(2)
    dy(3) = k1 * y(1) + k2 * y(2)
end subroutine f