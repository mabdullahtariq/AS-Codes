Imports System
Imports System.Transactions

Module Program
    Sub Main()
        Dim Str1 As String
        Dim Rep As Char
        Dim Rep2 As Char
        Console.Write("Enter a String: ")
        Str1 = Console.ReadLine
        Console.Write("Enter character that you want to replace: ")
        Rep = Console.ReadLine
        Console.Write("Enter character that you want to replace with: ")
        Rep2 = Console.ReadLine
        For i = 1 To Len(Str1)
            If Mid(Str1, i, 1) = Rep Then
                Mid(Str1, i, 1) = Rep2
            End If
        Next
        Console.Write("The changed string is: ")
        Console.WriteLine(Str1)
    End Sub
End Module
