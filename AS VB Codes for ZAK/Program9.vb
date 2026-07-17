Imports System

Module Program
    Sub Main()
        Dim a As String
        Dim b As String
        Dim swapA As String
        Dim swapB As String
        Dim result As String
        Console.Write("Enter the first string (length 2 or more): ")
        a = Console.ReadLine()
        Console.Write("Enter the second string (length 2 or more): ")
        b = Console.ReadLine()
        If Len(a) >= 2 And Len(b) >= 2 Then
            swapA = b.Chars(0) & b.Chars(1) & a.Substring(2)
            swapB = a.Chars(0) & a.Chars(1) & b.Substring(2)
            result = swapA & " " & swapB
            Console.WriteLine("Resulting string: " & result)
        Else
            Console.WriteLine("Both strings must be of length 2 or more.")
        End If
        Console.ReadLine()
    End Sub
End Module
