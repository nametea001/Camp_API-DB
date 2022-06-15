using System.Threading;

public Form1()
        {
            InitializeComponent();
            Thread trd = new Thread(new ThreadStart(this.getValue));
            trd.IsBackground = true;
            trd.Start();
        }

        private void getValue()
        {

            string url = "/hw/get_by_id?ID=1";
            string temp = "";
            while (true)
            {
                var data = con.getData(url);
                if (data != null)
                {
                    string value = data[0]["value"].ToString();
                    temp = value;
                    label1.Invoke((MethodInvoker)(() => label1.Text = value));
                    textBox1.Invoke((MethodInvoker)(() => textBox1.Text = value));
                }
                else
                {
                    label1.Invoke((MethodInvoker)(() => label1.Text = temp));
                }

                
                Thread.Sleep(500);
            }
        } 