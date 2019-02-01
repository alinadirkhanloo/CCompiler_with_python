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

            textBox.Text = File.ReadAllText(@"F:\Project\Python\CCompiler_with_python\example\input.txt");
        }

        private void button_Click(object sender, RoutedEventArgs e)
        {
            run_cmd();
        }

        private void run_cmd()
        {

            const string fileName = @"F:\Project\Python\CCompiler_with_python\pp(2).py";

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

            var results = output.Split('\n').ToList();

            var myResult = new List<string>();
            var myErrorResult = new List<string>();
            var mySymbolNybbleResult = new List<string>();

            foreach (var o in results)
            {
                if (o.Contains("error: "))
                    myErrorResult.Add(o.Replace("error: ", ""));

                if (o.Contains("message: "))
                    myResult.Add(o.Replace("message: ",""));

                if (o.Contains("["))
                    mySymbolNybbleResult.Add(o);
            }          

            result.ItemsSource = myResult;
            error.ItemsSource = myErrorResult;
            symbol.ItemsSource = mySymbolNybbleResult;

            Console.ReadLine();
        }

        private void Button_Save_Click(object sender, RoutedEventArgs e)
        {
            File.WriteAllText(@"F:\Project\Python\CCompiler_with_python\example\input.txt", textBox.Text);
        }

        private void Button_About_Click(object sender, RoutedEventArgs e)
        {
            MaterialMessageBox.Show("Sir J0l@n \nSir K@r@m \nG0d 0f Bug", "About");
        }
    }
}
