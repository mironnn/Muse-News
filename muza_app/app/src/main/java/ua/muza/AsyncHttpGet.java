package ua.muza;

import android.os.AsyncTask;
import android.util.Log;

import com.google.gson.Gson;

import org.apache.commons.io.IOUtils;

import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;


public class AsyncHttpGet extends AsyncTask<String, Void, String> {

    private Exception exception;
    MainActivity mainActivity;

    AsyncHttpGet(MainActivity act) {
        mainActivity = act;
    }

    protected String doInBackground(String... urls) {
        String result = "";
        URL url;
        try {
            url = new URL(urls[0]);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setReadTimeout(10000 /* milliseconds */);
            conn.setConnectTimeout(15000 /* milliseconds */);
            conn.setRequestMethod("GET");

            conn.setDoInput(true);
            // Starts the query
            conn.connect();
            InputStream stream = conn.getInputStream();
            result = IOUtils.toString(stream, "UTF-8");

        } catch (Exception e) {
            e.printStackTrace();
            exception = e;
        }

        return result;
    }

    protected void onPostExecute(String content) {
        if (exception != null)
            Log.d("muzad", exception.toString());


        Gson gson = new Gson();
        Data data = gson.fromJson(content, Data.class);
        Log.d("muzad", content);
        Log.d("muzad", data.toString());

        mainActivity.setText(data.toString());
    }
}