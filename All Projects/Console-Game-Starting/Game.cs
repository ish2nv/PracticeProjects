using System;

namespace ConsoleGame
{
    class Game : SuperGame
    {
        public new static void UpdatePosition(string keypressed, out int changeinx, out int changeiny)
        {
            changeinx = 0;
            changeiny = 0;
            switch (keypressed)
            {
                case "W":
                    changeiny = changeiny - 1;
                    break;
                case "S":
                    changeiny = changeiny + 1;
                    break;
                case "A":
                    changeinx = changeinx - 1;
                    break;
                case "D":
                    changeinx = changeinx + 1;
                    break;
                default:
                    changeinx = changeinx + 0;
                    changeiny = changeiny + 0;
                    break;
            }
        }
        public new static string UpdateCursor(string keypressed)
        {
            string unicodeString = char.ConvertFromUtf32(0x1F601);

            switch (keypressed)
            {
                case "W":
                    unicodeString = char.ConvertFromUtf32(0x1F601);
                    break;
                case "S":
                    unicodeString = char.ConvertFromUtf32(0x1F601);
                    break;
                case "A":
                    unicodeString = char.ConvertFromUtf32(0x1F601);
                    break;
                case "D":
                    unicodeString = char.ConvertFromUtf32(0x1F601);
                    break;

            }
            return unicodeString;
        }

        public new static int KeepInBounds(int coordinate, int maxval)
        {

            if (coordinate >= maxval)
            {
                return maxval - 1;
            }
            else if (coordinate < 0)
            {
                return 0;
            }
            else
            {
                return coordinate;
            }

        }

        public new static bool DidScore(int xval, int yval, int xfruit, int yfruit)
        {
            if (xval == xfruit && yval == yfruit)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}