Imports System
Imports System.Reflection

Module Program
    Sub Main()
        Dim Str1 As String
        Dim vowelA, vowelE, vowelI, vowelO, vowelU As Integer
        Dim Char1 As Char
        vowelA = 0
        vowelE = 0
        vowelI = 0
        vowelO = 0
        vowelU = 0
        Console.Write("Enter String: ")
        Str1 = Console.ReadLine
        Str1 = UCase(Str1)
        For i = 1 To Len(Str1)
            Char1 = Mid(Str1, i, 1)
            Select Case Char1
                Case "A"
                    vowelA += 1
                Case "E"
                    vowelE += 1
                Case "I"
                    vowelI += 1
                Case "O"
                    vowelO += 1
                Case "U"
                    vowelU += 1
            End Select
        Next
        Console.WriteLine("Number of 'A': " & vowelA)
        Console.WriteLine("Number of 'E': " & vowelE)
        Console.WriteLine("Number of 'I': " & vowelI)
        Console.WriteLine("Number of 'O': " & vowelO)
        Console.WriteLine("Number of 'U': " & vowelU)
        Console.ReadLine()
    End Sub
End Module
