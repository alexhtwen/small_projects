using System;
class ReverseString
{
    static void Main(string[] args)
    {
        string rawStr, reverseStr;
        rawStr = "abcde";

        char[] arr = rawStr.ToCharArray();  // 先將字串轉為char array。
        Array.Reverse(arr);                 // 將char array中的元素位置逆轉。
        reverseStr = new string(arr);         // 逆轉完的char array轉回字串，即成逆字串。

        Console.WriteLine("rawStr: " + rawStr);
        Console.WriteLine("reverseStr: " + reverseStr);
    }
}