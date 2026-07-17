Imports System

Module Program
    Sub Main()
        Dim donutCount As Integer
        Dim Str1 As String
        Dim Str2 As Integer
        Console.Write("Enter the number of donuts: ")
        donutCount = Console.ReadLine()
        If donutCount >= 10 Then
            Str1 = "Number of donuts: many"
            Console.Write(Str1)
        Else
            Str2 = donutCount
            Console.Write("Number of donuts: ")
            Console.WriteLine(donutCount)
        End If
    End Sub
End Module


