import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:cooperation_apps/constants/messages.dart';
import 'package:cooperation_apps/constants/colors.dart';


class AddAccountBankPage extends StatefulWidget {

  @override
  State<StatefulWidget> createState() => new _AddAccountBankPageState();
}

class _AddAccountBankPageState extends State<AddAccountBankPage> {
  List<String> cityList = [
    'Ajman',
    'Al Ain',
    'Dubai',
    'Fujairah',
    'Ras Al Khaimah',
    'Sharjah',
    'Umm Al Quwain'
  ];

  TextEditingController bankAccountNumber = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Container(
          child: SafeArea(
              child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: <Widget>[
                    Container(
                        alignment: Alignment.center,
                        padding: EdgeInsets.all(10),
                        child: Center(
                          child: Text('Tambahkan Akun Bank Anda'),
                        )
                    ),
                    Container(
                      padding: EdgeInsets.all(10),
                      child: DropdownButtonFormField(
                        decoration: InputDecoration(
                            border: OutlineInputBorder(
                              borderRadius: const BorderRadius.all(
                                const Radius.circular(30.0),
                              ),
                            ),
                            filled: true,
                            hintStyle: TextStyle(color: Colors.grey[800]),
                            hintText: "Nama Bank",
                            fillColor: Colors.blue[200]),

                        items: cityList
                            .map((cityTitle) => DropdownMenuItem(
                            value: cityTitle, child: Text("$cityTitle")))
                            .toList(), onChanged: (String? value) {  },
                      ),
                    ),
                    Container(
                      padding: EdgeInsets.all(10),
                      child: TextFormField(
                        controller: bankAccountNumber,
                        keyboardType: TextInputType.number,
                        decoration: InputDecoration(
                          border: OutlineInputBorder(),
                          labelText: 'No. Rekening',
                          helperText: 'Masukkan No Rekening',
                        ),
                      ),
                    ),
                    Container(
                      padding: EdgeInsets.all(10),
                      child: TextFormField(
                        controller: bankAccountNumber,
                        keyboardType: TextInputType.number,
                        decoration: InputDecoration(
                          border: OutlineInputBorder(),
                          labelText: 'Nama Lengkap',
                          helperText: 'Masukkan Nama Lengkap Sesuai dengan Nama di Rekening',
                        ),
                      ),
                    ),
                    Container(
                        height: 50,
                        padding: EdgeInsets.fromLTRB(10, 0, 10, 10),
                        child: TextButton(
                          style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(buttonGeneric)),
                          child: Text('Simpan'),
                          onPressed: () {
                            Navigator.pushNamed(context, '/home/');
                          },
                        )
                    ),
                  ]
              )
          ),
        )
    );
  }
}