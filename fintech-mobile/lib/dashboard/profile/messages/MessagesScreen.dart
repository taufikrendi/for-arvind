import 'package:flutter/material.dart';
import 'package:cooperation_apps/constants/messages.dart';
import 'package:cooperation_apps/constants/colors.dart';


class MessagePage extends StatefulWidget {

  @override
  State<StatefulWidget> createState() => new _MessagePageState();
}

class _MessagePageState extends State<MessagePage> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          backgroundColor: appBarBg,
          title: Center(
            child: new  Text(
              'Semua Notifikasi',
              style: TextStyle(color: appBarText),
            ),
          ),
        automaticallyImplyLeading: false,
      ),
      body: Container(
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
                              itemCount: messages_list.length,
                              itemBuilder: (context, index){
                                return Column(
                                  children: <Widget>[
                                    ListTile(
                                      title: Text(messages_list[index]['title']),
                                      subtitle: Text(messages_list[index]['sub']),
                                      trailing: Text(messages_list[index]['date']),
                                    ),
                                    Divider(),
                                  ],
                                );
                              }
                          ),
                        ],
                      ),
                    ),
                  ),
                ]
            )
        ),
      )
    );
  }
}