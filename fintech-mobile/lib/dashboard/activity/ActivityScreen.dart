import 'package:flutter/material.dart';
import 'package:cooperation_apps/constants/activity.dart';
import 'package:cooperation_apps/constants/colors.dart';


class ActivityPage extends StatefulWidget {

  @override
  State<StatefulWidget> createState() => new _State();
}

class _State extends State<ActivityPage> {

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: MaterialApp(
        home: Scaffold(
          appBar: AppBar(
            backgroundColor: appBarBg,
            bottom: TabBar(
              onTap: (index) {
                // Tab index when user select it, it start from zero
              },
              indicatorColor: Colors.red,
              unselectedLabelColor: Colors.red,
                tabs: [
                  Tab(
                    // payment, shop
                    icon:new Image(image:AssetImage('images/logo.png')),
                  ),
                  // saving
                  Tab(
                    icon: new Image(image:AssetImage('images/logo.png')),
                ),
                  // bantu anggota
                  Tab(
                    icon: new Image(image:AssetImage('images/logo.png')),
                ),
              ],
            ),
            title: Center(
              child: Text(
                  'Semua Aktifitas',
                  style: TextStyle(color: appBarText),
              ),
            ),
          ),
          body: TabBarView(
            children: [
              //Transaction
              Container(
                child: SafeArea(
                    child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: <Widget>[
                          Container(
                            child: Expanded(
                              child: Column(
                                children: [
                                  ListView.builder(
                                      scrollDirection: Axis.vertical,
                                      shrinkWrap: true,
                                      itemCount: activity_list.length,
                                      itemBuilder: (context, index) => Card(
                                        margin: new EdgeInsets.symmetric(horizontal: 10.0, vertical: 6.0),
                                        child: ListTile(
                                          contentPadding: EdgeInsets.symmetric(horizontal: 20.0, vertical: 10.0),
                                          // leading: Image(image:AssetImage(activity_list[index]['image'])),
                                          title: Text(activity_list[index]['title']),
                                          subtitle: Text(activity_list[index]['sub']),
                                          trailing: Text(activity_list[index]['date']),
                                        ),
                                      )
                                  ),
                                ],
                              ),
                            ),
                          ),
                        ]
                    )
                ),
              ),
              //Saving
              Container(
                child: SafeArea(
                    child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: <Widget>[
                          Container(
                            child: Expanded(
                              child: Column(
                                children: [
                                  ListView.builder(
                                      scrollDirection: Axis.vertical,
                                      shrinkWrap: true,
                                      itemCount: activity_list.length,
                                      itemBuilder: (context, index) => Card(
                                        margin: new EdgeInsets.symmetric(horizontal: 10.0, vertical: 6.0),
                                        child: ListTile(
                                          contentPadding: EdgeInsets.symmetric(horizontal: 20.0, vertical: 10.0),
                                          title: Text(activity_list[index]['title']),
                                          subtitle: Text(activity_list[index]['sub']),
                                          trailing: Text(activity_list[index]['date']),
                                        ),
                                      )
                                  ),
                                ],
                              ),
                            ),
                          ),
                        ]
                    )
                ),
              ),
              //People
              Container(
                child: SafeArea(
                    child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: <Widget>[
                          Container(
                            child: Expanded(
                              child: Column(
                                children: [
                                  ListView.builder(
                                      scrollDirection: Axis.vertical,
                                      shrinkWrap: true,
                                      itemCount: activity_list.length,
                                      itemBuilder: (context, index) => Card(
                                        margin: new EdgeInsets.symmetric(horizontal: 10.0, vertical: 6.0),
                                        child: ListTile(
                                          contentPadding: EdgeInsets.symmetric(horizontal: 20.0, vertical: 10.0),
                                          title: Text(activity_list[index]['title']),
                                          subtitle: Text(activity_list[index]['sub']),
                                          trailing: Text(activity_list[index]['date']),
                                        ),
                                      )
                                  ),
                                ],
                              ),
                            ),
                          ),
                        ]
                    )
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}