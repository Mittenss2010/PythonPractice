 public bool ErrorCalibration(int x, int y)
        {
            ///���ƫ�����쳣���
            if (x > 256 && x < -256)
            {
                //X�����쳣
            }

            if (y > 256 && y < -256)
            {
                //y�����쳣
            }

            //ƫ����XY�ַ���ƴ��
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


            //�ַ���ƴ��
            string orignalData = "01 10 00 32 00 02 04" + offsetX + offsetY;
            string checkData = Get_CRC16_C(StringToByte(orignalData));
            string dataToSend = orignalData + checkData;
            SendData(dataToSend);
            Thread.Sleep(100);


            //To Do 
            return true;
        }


���Ϳ�ʼУ׼
01 04 00 32 00 02 D0 04 
��ʼУ׼�ظ�
Length: 9, Data: 01 04 04 00 00 00 00 FB 84

����У׼����
�ȴ�У׼�ظ�

����У׼���
01 05 00 03 FF 00 7C 3A 
У׼��ϻظ�
01 05 00 03 FF 00 7C 3A 