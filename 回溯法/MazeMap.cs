using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

/*
回溯法(深搜)迷宫问题求解
*/

namespace BackTracking1
{
    public class MazeMap
    {
        public int Length { get; }
        public int Width { get; }
        private char[,] Mazepmap;
        private Coord EntranceCood;
        private Coord ExitCood;
        private bool[][][] MazeDire;
        private bool IsProcessed = false;
        private char[,] res;
        private bool IsRes = false;


        public MazeMap(int w = 5, int l = 5)
        {
            Length = l;
            Width = w;
            Mazepmap = new char[l, w];
            MazeDire = new bool[l][][];
            for (int i = 0; i < l; i++)
            {
                MazeDire[i] = new bool[w][];
                for (int j = 0; j < w; j++)
                {
                    MazeDire[i][j] = new bool[5] { false, false, false, false, false };
                }
            }

        }
        public void Clear()
        {
            IsRes = false;
            Array.Clear(Mazepmap, 0, Mazepmap.Length);
            Mazepmap = new char[Length, Width];
            if( res != null && res.Length != 0) Array.Clear(res, 0, res.Length);
            //Array.Clear(MazeDire, 0, Mazepmap.Length);
            MazeDire = new bool[Length][][];
            IsProcessed = false;
            EntranceCood = default;
            ExitCood = default;
            for (int i = 0; i < Length; i++)
            {
                MazeDire[i] = new bool[Width][];
                for (int j = 0; j < Width; j++)
                {
                    MazeDire[i][j] = new bool[5] { false, false, false, false, false };
                }
            }
            GC.Collect();
        }

        public void SetMaze(Coord mazeEntrance, Coord mazeExit, int[,] maze = null)
        {
            IsRes = false;
            for (int i = 0; i < Length; i++)
            {
                MazeDire[i] = new bool[Width][];
                for (int j = 0; j < Width; j++)
                {
                    MazeDire[i][j] = new bool[5] { false, false, false, false, false };
                }
            }
            GC.Collect();
            if (maze == null)
            {
                Console.WriteLine($"输入迷宫 {Width} * {Length}:");
                for (int i = 0; i < Length; i++)
                    for (int j = 0; j < Width; j++)
                    {
                        char k;
                        k = (char)Console.Read();
                        if (k == '1') Mazepmap[i, j] = '■';
                        else Mazepmap[i, j] = '□';
                    }
                Console.WriteLine("输入迷宫入口坐标x:");
                int x = Console.Read();
                Console.WriteLine("输入迷宫入口坐标y:");
                int y = Console.Read();
                EntranceCood = new Coord(x, y);
                Console.WriteLine("输入迷宫出口坐标x:");
                int l = Console.Read();
                Console.WriteLine("输入迷宫出口坐标y:");
                int m = Console.Read();
                ExitCood = new Coord(l, m);
            }
            else
            {
                for (int i = 0; i < Length; i++)
                    for (int j = 0; j < Width; j++)
                    {
                        if (maze[i, j] == 1) Mazepmap[i, j] = '■';
                        else Mazepmap[i, j] = '□';
                    }
                EntranceCood = mazeEntrance;
                ExitCood = mazeExit;
            }
            for (int i = 0; i < Length; i++)
                for (int j = 0; j < Width; j++)
                {


                    if (i - 1 >= 0 && Mazepmap[i - 1, j] == '□')
                    {
                        MazeDire[i][j][(int)Direct.Up] = true;
                        //Console.WriteLine($"点 ({i},{j}) 上方可以走");
                    }

                    if (i + 1 < Length && Mazepmap[i + 1, j] == '□')
                    {
                        MazeDire[i][j][(int)Direct.Down] = true;
                        //Console.WriteLine($"点 ({i},{j}) 下方可以走");
                    }


                    if (j + 1 < Width && Mazepmap[i, j + 1] == '□')
                    {
                        MazeDire[i][j][(int)Direct.Right] = true;
                        //Console.WriteLine($"点 ({i},{j}) 右侧可以走");
                    }



                    if (j - 1 >= 0 && Mazepmap[i, j - 1] == '□')
                    {
                        MazeDire[i][j][(int)Direct.Left] = true;
                        //Console.WriteLine($"点 ({i},{j}) 左侧可以走");
                    }


                }
            IsProcessed = true;
        }
        private bool IsBeen(int x, int y)
        {
            return MazeDire[x][y][(int)Direct.Been];
        }

        private bool IsNear(Coord lhs, Coord rhs)
        {
            if ((Math.Abs(lhs.x - rhs.x) <= 1 && lhs.y == rhs.y) || (Math.Abs(lhs.y - rhs.y) <= 1 && lhs.x == rhs.x)) return true;
            else return false;

        }
        public void ShowMaze()
        {
            Console.WriteLine("迷宫图: ");
            for (int i = 0; i < Length; i++)
                for (int j = 0; j < Width; j++)
                {
                    Console.Write(Mazepmap[i, j]);
                    if (j == Length - 1) Console.Write('\n');
                }
        }

        public void ShowResult()
        {
            if (!IsRes) return;
            Console.WriteLine("迷宫图解: ");
            for (int i = 0; i < Length; i++)
                for (int j = 0; j < Width; j++)
                {

                    Console.Write(res[i, j]);
                    if (j == Length - 1) Console.Write('\n');
                }
        }

        public Coord GetEntrance()
        {
            return EntranceCood;
        }

        public Coord GetExit()
        {
            return ExitCood;
        }

        public void Go()
        {
            if (!IsProcessed)
            {
                Console.WriteLine("迷宫未初始化!!!");
                return;
            }
            Stack<Coord> Way = new Stack<Coord>();
            List<Coord> Path = new List<Coord>();
            Way.Push(EntranceCood);
            if (MazeDire[EntranceCood.x][EntranceCood.y][(int)Direct.Left]) Way.Push(new Coord(EntranceCood.x, EntranceCood.y - 1));
            if (MazeDire[EntranceCood.x][EntranceCood.y][(int)Direct.Up]) Way.Push(new Coord(EntranceCood.x - 1, EntranceCood.y));
            if (MazeDire[EntranceCood.x][EntranceCood.y][(int)Direct.Right]) Way.Push(new Coord(EntranceCood.x, EntranceCood.y + 1));
            if (MazeDire[EntranceCood.x][EntranceCood.y][(int)Direct.Down]) Way.Push(new Coord(EntranceCood.x + 1, EntranceCood.y));
            //Console.WriteLine($"数量 {Way.Count}");
            if (Way.Count == 1)
            {
                Console.WriteLine("迷宫不通...");
                Console.WriteLine("结束");
                return;
            }
            MazeDire[EntranceCood.x][EntranceCood.y][(int)Direct.Been] = true;
            Path.Add(EntranceCood);
            //Console.WriteLine($"{EntranceCood.ToString()}");
            while (Way.Count != 0)
            {
                Coord tmp = Way.Pop();

                if (tmp == ExitCood)
                {
                    MazeDire[tmp.x][tmp.y][(int)Direct.Been] = true;

                    Path.Add(tmp);
                    Console.WriteLine("迷宫已经走完...");
                    Console.WriteLine("路线 ");
                    Path.ForEach(x => { Console.WriteLine($" --> {x}"); });
                    res = (char[,])Mazepmap.Clone();
                    Path.ForEach(p => { res[p.x, p.y] = '△'; });
                    IsRes = true;
                    return;
                }
                if (IsBeen(tmp.x, tmp.y)) continue;
                MazeDire[tmp.x][tmp.y][(int)Direct.Been] = true;
                int tnum = Way.Count;
                if (MazeDire[tmp.x][tmp.y][(int)Direct.Left] && !IsBeen(tmp.x, tmp.y - 1)) Way.Push(new Coord(tmp.x, tmp.y - 1));
                if (MazeDire[tmp.x][tmp.y][(int)Direct.Up] && !IsBeen(tmp.x - 1, tmp.y)) Way.Push(new Coord(tmp.x - 1, tmp.y));
                if (MazeDire[tmp.x][tmp.y][(int)Direct.Right] && !IsBeen(tmp.x, tmp.y + 1)) Way.Push(new Coord(tmp.x, tmp.y + 1));
                if (MazeDire[tmp.x][tmp.y][(int)Direct.Down] && !IsBeen(tmp.x + 1, tmp.y)) Way.Push(new Coord(tmp.x + 1, tmp.y));
                if (tnum == Way.Count)
                {
                    //if (Way.Peek() == Path[Path.Count - 1]) Path.RemoveAt(Path.Count - 1);
                    while (!IsNear(Path[Path.Count - 1], Way.Peek()))
                    {
                        Path.RemoveAt(Path.Count - 1);
                    }
                    continue;
                }

                //Console.WriteLine($"{tmp.ToString()}");

                Path.Add(tmp);

            }
            Console.WriteLine("迷宫没有走完...");
            Console.WriteLine("出错了，截止: ");
            Path.ForEach(x => { Console.WriteLine($" --> {x}"); });
            return;
        }

    }
    public struct Coord
    {
        public Coord(int x1 = 0, int y1 = 0)
        {
            x = x1;
            y = y1;
        }
        public int x;
        public int y;
        public override string ToString()
        {
            return $"({x}, {y})";
        }

        public static bool operator ==(Coord lhs, Coord rhs)
        {
            if (lhs.x == rhs.x && lhs.y == rhs.y) return true;
            else return false;
        }
        public static bool operator !=(Coord lhs, Coord rhs)
        {
            if (lhs.x != rhs.x || lhs.y != rhs.y) return true;
            else return false;
        }

        public override bool Equals(object obj)
        {
            Coord ob = (Coord)obj;
            if (this.x == ob.x && this.y == ob.y) return true;
            else return false;
        }

        public override int GetHashCode()
        {
            return x ^ y;
        }
    }



    enum Direct
    {
        Left,
        Up,
        Right,
        Down,
        Been
    };

}