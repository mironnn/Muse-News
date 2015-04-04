package ua.muse;

import com.google.gson.Gson;

/**
 * Created by yatagan on 4/4/15.
 */
public class News {
    int id;
    String title;
    String body;
    String time;

    @Override
    public String toString() {
        return new Gson().toJson(this);
    }

    String getTitle() { return title; }
}
