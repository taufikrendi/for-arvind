import 'package:flutter/material.dart';
import 'package:cooperation_apps/constants/profile.dart';
import 'package:cooperation_apps/constants/colors.dart';

class ProfilePage extends StatefulWidget {

  @override
  State<StatefulWidget> createState() => new _MessagePageState();
}

class _MessagePageState extends State<ProfilePage> {

  @override
  Widget build(BuildContext context) {
    double width = MediaQuery.of(context).size.width;
    double height = MediaQuery.of(context).size.height;
    return Scaffold(
        body: Container(
          child: SafeArea(
              child: SingleChildScrollView(
                padding: EdgeInsets.all(5),
                child:  Column(
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: <Widget>[
                      Container(
                            child: Padding(
                                padding: const EdgeInsets.fromLTRB(50.0, 10.0, 50.0, 12.5),
                            child: Stack(
                              alignment: const Alignment(0.9, 0.9),
                              children: <Widget>[
                                CircleAvatar(
                                  backgroundImage: NetworkImage("https://st3.depositphotos.com/1036149/19032/i/1600/depositphotos_190328682-stock-photo-fun-horse-cycling-illustration.jpg"),
                                  radius: 50.0,
                                ),
                              ],
                            ),
                          ),
                      ),
                      Padding(
                        padding: const EdgeInsets.fromLTRB(8.0, 8.0, 8.0, 4.0),
                        child: Text("Bagus Setya Wardana",
                            style: TextStyle(
                                color: Colors.black,
                                fontSize: 26.0,
                                fontWeight: FontWeight.bold)),
                      ),
                      Padding(
                        padding: const EdgeInsets.fromLTRB(8.0, 0.0, 8.0, 8.0),
                        child: Text(
                          "Bukan Anggota",
                          style: TextStyle(
                              color: Colors.grey,
                              fontSize: 15.0,
                              fontWeight: FontWeight.bold),
                        ),
                      ),
                      Container(
                        child: Column(
                          children: [
                            ListView.builder(
                                physics: NeverScrollableScrollPhysics(),
                                scrollDirection: Axis.vertical,
                                shrinkWrap: true,
                                itemCount: profile_list.length,
                                itemBuilder: (context, index) {
                                  return GestureDetector(
                                      onTap: () => Navigator.pushNamed(context, profile_list[index]['link']),
                                      child: Card(
                                        child: ListTile(
                                          title: Text(profile_list[index]['title']),
                                          trailing: Icon(Icons.arrow_forward_ios_outlined),
                                        ),
                                      )
                                  );
                                }
                            ),
                          ],
                        ),
                      ),
                      Container(
                          alignment: Alignment.bottomRight,
                          padding: EdgeInsets.all(10),
                          child: Text('Version: 1.0',
                            style: TextStyle(color: versionText),
                          )
                      ),
                    ]
                ),
              ),
          ),
        )
    );
  }
}