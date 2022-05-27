using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Net.Http;
using System.Net.Http.Headers;
using Newtonsoft.Json;

namespace WindowsFormsApp1
{
    //version 2.0.0 fixbug timeout
    public class NetworkHelper
    {
        private string host = "http://18.141.11.24";
        public List<Dictionary<string, string>> getData(string url)
        {
            List<Dictionary<string, string>> data = getMethod(url).Result;
            
            return data ?? null; 
        }
        private async Task<List<Dictionary<string, string>>> getMethod(string url)
        {
            try
            {
                HttpClient client = new HttpClient();
                client.BaseAddress = new Uri(host);
                client.DefaultRequestHeaders.Accept.Clear();
                client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
                HttpResponseMessage response = await client.GetAsync(url).ConfigureAwait(false);
                response.EnsureSuccessStatusCode();
                string responseBody = await response.Content.ReadAsStringAsync();
                // Above three lines can be replaced with new helper method below
                //var data = JsonConvert.DeserializeObject<List<Dictionary<string, string>>>(responseBody);
                //Console.WriteLine(responseBody);
                //return responseBody ?? null;
                var data = JsonConvert.DeserializeObject<List<Dictionary<string, string>>>(responseBody);
                return data;

            }
            catch (HttpRequestException e)
            {
                Console.WriteLine("\nException Caught!");
                Console.WriteLine("Message :{0} ", e.Message);
                return null ;
            }
        }

        public List<Dictionary<string, string>> postData(string url, object ob)
        {
            List<Dictionary<string, string>> data = postMethod(url, ob).Result;

            return data ?? null;
        }
        private async Task<List<Dictionary<string, string>>> postMethod(string url, object ob)
        {
            try
            {
                HttpClient client = new HttpClient();
                client.BaseAddress = new Uri(host);
                client.DefaultRequestHeaders.Accept.Clear();
                if(ob != null)
                {
                    var json = JsonConvert.SerializeObject(ob);
                    var dataJson = new StringContent(json, Encoding.UTF8, "application/json");

                    var response = await client.PostAsync(url, dataJson);
                    response.EnsureSuccessStatusCode();
                    string responseBody = await response.Content.ReadAsStringAsync().ConfigureAwait(false);

                    var data = JsonConvert.DeserializeObject<List<Dictionary<string, string>>>(responseBody);
                    return data;
                }
                else
                {
                    return null;
                }

            }
            catch(HttpRequestException e)
            {
                Console.WriteLine("\nException Caught!");
                Console.WriteLine("Message :{0} ", e.Message);
                return null;
            }
        }
    }
}
