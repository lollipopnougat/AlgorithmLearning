using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/* 
回溯法(深搜)迷宫主类
*/

namespace BackTracking1
{
    class Program
    {
        [STAThread]
        static void Main()
        {
            try
            {
                OpenFileDialog ofd = new OpenFileDialog()
                {
                    DefaultExt = "csv",
                    Filter = "CSV文件|*.csv",
                    CheckFileExists = true,
                    Title = "选择CSV文件",
                    RestoreDirectory = true
                };
                int[,] fmaze;
                string gFileName;
                if (ofd.ShowDialog() == DialogResult.OK)
                {
                    gFileName = ofd.FileName;
                    if (gFileName.IndexOf(":") < 0) return;
                }
                else
                {
                    Console.WriteLine("未选择文件，退出");
                    Console.ReadKey();
                    return;
                }

                string[] strRows = System.IO.File.ReadAllLines(gFileName, Encoding.UTF8);
                int nn = 0;
                int l = strRows.Length;
                Console.WriteLine($"长度: {l}");
                Console.WriteLine($"宽度: {strRows[0].Split(',').Length}");
                int w = strRows[0].Split(',').Length;
                fmaze = new int[l, w];
                List<Coord> EE = new List<Coord>();
                int EENum = 0;
                foreach (string k in strRows)
                {

                    for (int j = 0; j < w; j++)
                    {


                        fmaze[nn, j] = Convert.ToInt32(k.Split(',')[j]);
                        if ((nn == 0 || j == 0 || nn == l - 1 || j == w - 1) && fmaze[nn, j] == 0)
                        {
                            EENum++;
                            EE.Add(new Coord(nn, j));
                        }
                    }
                    nn++;
                    //Console.WriteLine($"{k}");
                }

                /*
                for (int i = 0; i < l; i++)
                {
                    string[] tmp = strRows[i].Split(',');
                    for(int j = 0; j < w; j++)
                    {
                        if ((i == 0 || j == 0 || i == l - 1 || j == w - 1) && strRows[i][j] == 0)
                        {
                            EENum++;
                            EE.Add(new Coord(i, j));
                        }
                        fmaze[i, j] = Convert.ToInt32(strRows[i][j]);

                    }
                }
                for (int i = 0; i < l; i++)
                    for (int j = 0; j < w; j++)
                    {
                        Console.Write(fmaze[i, j]);
                        if (j == l - 1) Console.Write('\n');
                    }*/
                if (EENum != 2)
                {
                    Console.WriteLine("迷宫格式不对! 确保入口出口各一个!");
                    Console.ReadKey();
                    return;
                }
                Coord Entrance = EE[0];
                Coord Exit = EE[1];
                MazeMap mazeMap = new MazeMap(l, w);
                mazeMap.SetMaze(Entrance, Exit, fmaze);
                mazeMap.ShowMaze();
                Console.WriteLine("入口坐标 " + mazeMap.GetEntrance().ToString());
                Console.WriteLine("出口坐标 " + mazeMap.GetExit().ToString());
                mazeMap.Go();
                mazeMap.ShowResult();
                mazeMap.Clear();
                Console.ReadKey();
            }
            catch (Exception e)
            {
                System.Diagnostics.Process.Start($"https://www.google.com/search?q={e.Message}");
            }
        }
    }



}
