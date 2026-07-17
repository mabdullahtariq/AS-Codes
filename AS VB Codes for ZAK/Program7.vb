Imports System

Module Program
    Sub Main()
        Dim Str1 As String
        Dim Length As Integer
        Dim chr1 As String
        Dim chr2 As String
        Dim chr3 As String
        Console.Write("Enter String: ")
        Str1 = Console.ReadLine()
        Length = Len(Str1)
        If Length > 2 Then
            chr1 = Left(Str1, 2)
            chr2 = Right(Str1, 2)
            chr3 = chr1 & chr2
            Console.Write(chr3)
        ElseIf Length <= 2 Then
            Console.WriteLine(Str1)
        End If
    End Sub
End Module
