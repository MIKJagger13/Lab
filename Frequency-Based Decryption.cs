using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution
{
    static void Main(string[] args)
    {
        string message = Console.ReadLine();
        int[] tabel = new int[26];
        Array.Fill(tabel, 0);
        foreach(byte c in message.ToUpper())
        {
            if(c < (byte)'A' || c > (byte)'Z')
                continue;
            else
                tabel[c - (byte)'A']++;
        }
        int e = 0;
        for(int i = 1; i < 26; i++)
            if(tabel[i] > tabel[e])
                e = i;
        int offset = e - 'E' + 'A';
        string answer = "";
        string add = message.ToUpper();
        Console.Error.WriteLine($"key: {offset} message: {add}");
        for(int i = 0; i < add.Length; i++)
        {
            if(add[i] < (byte)'A' || add[i] > (byte)'Z')
            {
                answer += message[i];
            }
            else
            {
                int t = (add[i] - 'A' - offset) % 26;
                if(t < 0)
                    t+=26;
                t -= add[i] - 'A';
                    answer += (char)(message[i] + t);   
            }
        }
        Console.WriteLine(answer);
    }
}
