using System;
using System.Collections.Generic;
namespace HelloProject {
	
	class Program {
		static void Main(string[] args) {
		    string s = "1\r\n1 2\r\n1 2 3\r\n1 2 3 4\r\n1 2 3 4 5\r\n";
			int width = 10;
			int cnt = 0;
			int len = s.Length;
			string ans = "";
			string tmp = "";
			for(int i=0; i+1<len; i++){
			  if(s[i] == '\r' && s[i+1] == '\n'){
				  int space = width - cnt;
				  for(int j=0; j<space; j++) ans += ' ';
				  ans += tmp;
				  tmp = "";
				  ans += '\r';
				  ans += '\n';
				  cnt = 0;
				  i += 2;
			  }
			  cnt++;
			  tmp += s[i];
			}
			Console.WriteLine(ans);
		}
	}
}
