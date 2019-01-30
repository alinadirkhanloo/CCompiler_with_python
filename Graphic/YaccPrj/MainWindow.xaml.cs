using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Windows;
using BespokeFusion;

namespace YaccPrj
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();

            textBox.Text = File.ReadAllText(@"C:\Users\M-H-KARAMI\Desktop\Yacc\example\fff.txt");
        }

        private void button_Click(object sender, RoutedEventArgs e)
        {
            run_cmd();
        }

        private void run_cmd()
        {

            const string fileName = @"C:\Users\M-H-KARAMI\Desktop\Yacc\assign31.py";

            var p = new Process
            {
                StartInfo = new ProcessStartInfo(
                    @"C:\Users\M-H-KARAMI\AppData\Local\Programs\Python\Python36-32\python.exe", fileName)
                {
                    RedirectStandardOutput = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                }
            };
            p.Start();

            var output = p.StandardOutput.ReadToEnd();

            p.WaitForExit();

            Console.WriteLine(output);

            var result = output.Split('\n').ToList();

            var myResult = new List<string>();

            foreach (var o in result)
            {
                if (o.Contains("error : "))
                    myResult.Add(o);
            }          

            listBox.ItemsSource = myResult;

            Console.ReadLine();
        }

        private void Button_Save_Click(object sender, RoutedEventArgs e)
        {
            File.WriteAllText(@"C:\Users\M-H-KARAMI\Desktop\Yacc\example\fff.txt", textBox.Text);
        }

        private void Button_About_Click(object sender, RoutedEventArgs e)
        {
            MaterialMessageBox.Show("Sir J0l@n \nSir K@r@m \nG0d 0f Bug", "About");
        }
    }
}
