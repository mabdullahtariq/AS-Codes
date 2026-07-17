Imports System
Imports System.ComponentModel.DataAnnotations

Module Program
        Sub Main()
            Dim Str1 As String
            Dim i As Integer
            Dim Length As Integer
            Dim Chr1 As Char
        Dim Chr2 As String
        Console.WriteLine("Input String: ")
        Str1 = Console.ReadLine()
        Length = Len(Str1)
        If Length >= 1 Then
            Chr1 = Mid(Str1, 1, 1)
            Chr2 = Chr1
            For i = 2 To Length
                If Mid(Str1, i, 1) = Chr1 Then
                    Chr2 &= "*"
                Else
                    Chr2 &= Mid(Str1, i, 1)
                End If
            Next
            Console.WriteLine("Modified string: " & Chr2)
        Else
            Console.WriteLine("Please enter a string of Length 1 or more")
            End If
        Console.ReadLine()
    End Sub
    End Module
