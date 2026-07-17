Imports System
Imports System.ComponentModel.DataAnnotations

Module Program
    Sub Main()
        Dim Str1 As String
        Dim Str2 As String
        Dim Length As Integer
        Dim Last As String
        Console.WriteLine("Enter String: ")
        Str1 = Console.ReadLine()
        Length = Len(Str1)
        Last = Right(Str1, 3)
        If Length >= 3 Then
            If Last = "ing" Then
                Str2 = Str1 & "ly"
            Else
                Str2 = Str1 & "ing"
            End If
        ElseIf Length = 2 Then
            Str2 = Str1 & "ing"
        ElseIf Length = 1 Then
            Str2 = Str1
        End If
        Console.WriteLine("Resulting string: " & Str2)
        Console.ReadLine()
    End Sub
End Module
