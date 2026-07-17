Imports System

Module Program
    Sub Main()
        Dim Str1 As String
        Dim count1 As Integer
        Dim Load As String
        Dim Count2 As Integer
        Dim A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z As Boolean
        Load = ""
        Count2 = 0
        A = False
        B = False
        C = False
        D = False
        E = False
        F = False
        G = False
        H = False
        I = False
        J = False
        K = False
        L = False
        M = False
        N = False
        O = False
        P = False
        Q = False
        R = False
        S = False
        T = False
        U = False
        V = False
        W = False
        X = False
        Y = False
        Z = False
        Console.Write("Enter String: ")
        Str1 = Console.ReadLine
        Str1 = UCase(Str1)
        For count1 = 1 To Len(Str1)
            Load = Mid(Str1, count1, 1)
            Select Case Load
                Case "A"
                    A = True
                Case "B"
                    B = True
                Case "C"
                    C = True
                Case "D"
                    D = True
                Case "E"
                    E = True
                Case "F"
                    F = True
                Case "G"
                    G = True
                Case "H"
                    H = True
                Case "I"
                    I = True
                Case "J"
                    J = True
                Case "K"
                    K = True
                Case "L"
                    L = True
                Case "M"
                    M = True
                Case "N"
                    N = True
                Case "O"
                    O = True
                Case "P"
                    P = True
                Case "Q"
                    Q = True
                Case "R"
                    R = True
                Case "S"
                    S = True
                Case "T"
                    T = True
                Case "U"
                    U = True
                Case "V"
                    V = True
                Case "W"
                    W = True
                Case "X"
                    X = True
                Case "Y"
                    Y = True
                Case "Z"
                    Z = True
            End Select
        Next count1
        If A And B And C And D And E And F And G And H And I And J And K And L And M And N And O And P And Q And R And S And T And U And V And W And X And Y And Z Then
            Console.WriteLine("Yes! The input String has all the alphabets")
        Else
            Console.WriteLine("No! The input String does not have all the alphabets")
        End If
        Console.ReadLine()
    End Sub
End Module
