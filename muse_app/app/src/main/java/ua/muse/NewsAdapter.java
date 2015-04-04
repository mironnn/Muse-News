package ua.muse;

import android.content.Context;
import android.support.v4.widget.SwipeRefreshLayout;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.Arrays;

/**
 * Created by yatagan on 4/4/15.
 */
public class NewsAdapter extends BaseAdapter {
    private ArrayList<Data> datas = new ArrayList<Data>();
    LayoutInflater inflater;

    NewsAdapter(Context context) {

        inflater = (LayoutInflater)context.getSystemService
                (Context.LAYOUT_INFLATER_SERVICE);

        update(null);


    }

    @Override
    public int getCount() {
        return datas.size();
    }

    @Override
    public Object getItem(int position) {
        return datas.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if( convertView == null ){
            //We must create a View:
            convertView = inflater.inflate(R.layout.sample_news_view, parent, false);
//            NewsView newsView = (NewsView) convertView.findViewById(R.id.newsView);
//            newsView.setExampleString(datas.get(position).getTitle());
            TextView textView = (TextView) convertView.findViewById(R.id.textView);
            textView.setText(datas.get(position).getTitle());
        }
        //Here we can do changes to the convertView, such as set a text on a TextView
        //or an image on an ImageView.
        return convertView;
    }

    public void setData(Data []newDatas) {
        datas.clear();
        if (newDatas != null)
            datas.addAll(Arrays.asList(newDatas));
    }

    public void update(SwipeRefreshLayout swipeContainer) {
        AsyncHttpGet get = new AsyncHttpGet(this, swipeContainer);
//        get.execute("http://192.168.20.205:8000/post/1/");
//        get.execute("http://192.168.20.205:8000/posts/");
        get.execute("http://192.168.20.183:8000/posts/");
    }
}
