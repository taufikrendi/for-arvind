import 'package:flutter/material.dart';
import 'package:cooperation_apps/constants/colors.dart';


class LoginPage extends StatefulWidget {

  @override
  State<StatefulWidget> createState() => new _State();
}

class _State extends State<LoginPage> {
  TextEditingController nameController = TextEditingController();
  TextEditingController passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Padding(
            padding: EdgeInsets.all(10),
            child: ListView(
              children: <Widget>[
                Container(
                    alignment: Alignment.center,
                    padding: EdgeInsets.all(10),
                    child: new Image(image:AssetImage('images/logo.png'))
                ),
                //text field
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextField(
                    controller: nameController,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Email',
                    ),
                  ),
                ),
                Container(
                  padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
                  child: TextField(
                    obscureText: true,
                    controller: passwordController,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Sandi',
                    ),
                  ),
                ),
                //forgot password button
                Container(
                    padding: EdgeInsets.fromLTRB(10, 0, 10, 10),
                    child: Row(
                      children: <Widget>[
                        TextButton(
                          child: Text(
                            'Lupa Password',
                            style: TextStyle(color: linkTextB),
                          ),
                          onPressed: () {
                            Navigator.pushNamed(context, '/forgot-password/');
                          },
                        )
                      ],
                      mainAxisAlignment: MainAxisAlignment.center,
                    )),
                //login button
                Container(
                    height: 50,
                    padding: EdgeInsets.fromLTRB(10, 0, 10, 10),
                    child: ElevatedButton(
                      style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(buttonGeneric)),
                      child: Text('Login'),
                      onPressed: () {
                        Navigator.pushNamed(context, '/home/');
                      },
                    )),
                //register button
                Container(
                    padding: EdgeInsets.fromLTRB(10, 0, 10, 10),
                    child: Row(
                      children: <Widget>[
                        Text('Bukan Anggota? '),
                        TextButton(
                          child: Text(
                            'Daftar',
                            style: TextStyle(fontSize: 20,color: linkTextB),
                          ),
                          onPressed: () {
                            Navigator.pushNamed(context, '/registrations/');
                          },
                        )
                      ],
                      mainAxisAlignment: MainAxisAlignment.center,
                    )),
              ],
            )));
  }
}