Imports System

Module Module1
    Sub Main()
        Dim Str1 As String
        Dim notIndex As Integer
        Dim badIndex As Integer
        Dim result As String
        Console.WriteLine("Enter String: ")
        Str1 = Console.ReadLine()
        notIndex = Str1.IndexOf("not")
        badIndex = Str1.IndexOf("bad")
        If notIndex <> -1 AndAlso badIndex <> -1 AndAlso notIndex < badIndex Then
            result = Str1.Substring(0, notIndex) & "good" & Str1.Substring(badIndex + 3)
            Console.WriteLine("Resulting string: " & result)
        Else
            Console.WriteLine("No 'not' followed by 'bad' found or 'bad' precedes 'not'. No replacement needed.")
        End If
        Console.ReadLine()
    End Sub
End Module

