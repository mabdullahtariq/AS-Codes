Imports System
Imports System.Threading

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
            If Load = "A" Or Load = "B" Or Load = "C" Or Load = "D" Or Load = "E" Or Load = "F" Or Load = "G" Or Load = "H" Or Load = "I" Or Load = "J" Or Load = "K" Or Load = "L" Or Load = "M" Or Load = "N" Or Load = "O" Or Load = "P" Or Load = "Q" Or Load = "R" Or Load = "S" Or Load = "T" Or Load = "U" Or Load = "V" Or Load = "W" Or Load = "X" Or Load = "Y" Or Load = "Z" Then
                Count2 = Count2 + 1
            End If
        Next count1
        If Count2 = 26 Then
                    Console.WriteLine("Yes! The input String has all the alphabets")
                Else Console.WriteLine("No! The input String does Not have all the alphabets")

        End If
        Console.ReadLine()
    End Sub
End Module
