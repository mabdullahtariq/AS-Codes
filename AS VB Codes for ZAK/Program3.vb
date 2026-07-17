Imports System

Module Program
    Sub Main()
        Dim count As Integer
        Dim Str1 As String
        Dim word As Char
        Console.Write("Enter String: ")
        Str1 = Console.ReadLine
        Do
            word = Left(Str1, 1)
            For i = 1 To Len(Str1)
                If Mid(Str1, i, 1) = word Then
                    count += 1
                End If
            Next i
            Console.WriteLine("The Word " & word & " came up " & count & " time")
            count = 0
            Str1 = Str1.Replace(word, "")
            If Len(Str1) = 0 Then Exit Do
        Loop
    End Sub
End Module
