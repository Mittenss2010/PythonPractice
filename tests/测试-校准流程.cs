 public bool ErrorCalibration(int x, int y)
        {
            ///入口偏移量异常检测
            if (x > 256 && x < -256)
            {
                //X参数异常
            }

            if (y > 256 && y < -256)
            {
                //y参数异常
            }

            //偏移量XY字符串拼接
            string offsetX = "";
            string offsetY = "";
            if ( x>= 0 && x<256 )
            {
                offsetX = " 00 " + Convert.ToString(x, 16);
            }
            if( x<0 && x>-256 )
            {
                int temp = 256 + x;
                offsetX = " FF " + Convert.ToString(temp, 16);
            }

            if (y >= 0 && y < 256)
            {
                offsetY = " 00 " + Convert.ToString(y, 16);
            }
            if (y < 0 && y > -256)
            {
                int temp = 256 + y;
                offsetY = " FF " + Convert.ToString(temp, 16);
            }


            //字符串拼接
            string orignalData = "01 10 00 32 00 02 04" + offsetX + offsetY;
            string checkData = Get_CRC16_C(StringToByte(orignalData));
            string dataToSend = orignalData + checkData;
            SendData(dataToSend);
            Thread.Sleep(100);


            //To Do 
            return true;
        }


发送开始校准
01 04 00 32 00 02 D0 04 
开始校准回复
Length: 9, Data: 01 04 04 00 00 00 00 FB 84

调用校准函数
等待校准回复

发送校准完毕
01 05 00 03 FF 00 7C 3A 
校准完毕回复
01 05 00 03 FF 00 7C 3A 