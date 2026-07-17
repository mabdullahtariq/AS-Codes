Imports System

Module Program
    Sub Main()
        Dim Str1 As String
        Dim Rep As Char
        Dim Rep2 As Char
        Dim Replaced As String
        Dim X As Char
        Console.Write("Enter Name: ")
        Str1 = Console.ReadLine
        Console.Write("Enter Character to Replace: ")
        Rep = Console.ReadLine
        Console.Write("Enter Character to Replace With: ")
        Rep2 = Console.ReadLine
        Replaced = ""
        For i = 1 To Len(Str1)
            X = Mid(Str1, i, 1)
            If X = Rep Then
                Replaced = Replaced & Rep2
            Else
                Replaced = Replaced & X
            End If
        Next
        Console.Write("String Replaced is: ")
        Console.WriteLine(Replaced)
        Console.ReadLine()
    End Sub
End Module
