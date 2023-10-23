using System;
using System.Text;

class Solution
{
    static void Main(string[] args)
    {
        string message1 = Console.ReadLine();
        string message2 = Console.ReadLine();
        string message3 = Console.ReadLine();

        byte[] m1 = Convert.FromHexString(message1);
        byte[] m2 = Convert.FromHexString(message2);
        byte[] m3 = Convert.FromHexString(message3);

        byte[] m0 = new byte[m1.Length];
        for (int i = 0; i < m0.Length; i++)
        {
            m0[i] = (byte)(m1[i] ^ m2[i] ^ m3[i]);
        }
        string answer = Encoding.ASCII.GetString(m0);
        Console.WriteLine(answer);
    } 
}
