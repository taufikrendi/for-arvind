import 'package:flutter/material.dart';
import 'package:cooperation_apps/constants/colors.dart';
import 'package:flutter/services.dart';


class ProfileVerificationPage extends StatefulWidget {

  @override
  State<StatefulWidget> createState() => new _State();
}

class _State extends State<ProfileVerificationPage> {
  TextEditingController nameController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Container(
          child: SingleChildScrollView(
            child: Column(
              children: <Widget>[
                //title
                Container(
                  padding: EdgeInsets.all(16),
                  child: Center(
                    child: Text(
                      'Isi Data Diri',
                      style: TextStyle(
                          color: appBarText,
                          fontSize: 30
                      ),
                    ),
                  ),
                ),
                //name
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextFormField(
                    controller: nameController,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Nama Lengkap',
                    ),
                    inputFormatters: [
                      LengthLimitingTextInputFormatter(50),
                    ],
                  ),
                ),
                //nik
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextFormField(
                    controller: nameController,
                    keyboardType: TextInputType.number,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'NIK',
                    ),
                    inputFormatters: [
                      LengthLimitingTextInputFormatter(16),
                    ],
                  ),
                ),
                //npwp
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextFormField(
                    controller: nameController,
                    keyboardType: TextInputType.number,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'NPWP',
                    ),
                    inputFormatters: [
                      LengthLimitingTextInputFormatter(16),
                    ],
                  ),
                ),
                //sex
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextFormField(
                    controller: nameController,
                    keyboardType: TextInputType.number,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Jenis Kelamin',
                    ),
                    inputFormatters: [
                      LengthLimitingTextInputFormatter(16),
                    ],
                  ),
                ),
                //pob
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextFormField(
                    controller: nameController,
                    keyboardType: TextInputType.number,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Tempat Lahir',
                    ),
                    inputFormatters: [
                      LengthLimitingTextInputFormatter(16),
                    ],
                  ),
                ),
                //dob
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextFormField(
                    controller: nameController,
                    keyboardType: TextInputType.number,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Tanggal Lahir',
                    ),
                    inputFormatters: [
                      LengthLimitingTextInputFormatter(16),
                    ],
                  ),
                ),
                //Prov
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextFormField(
                    controller: nameController,
                    keyboardType: TextInputType.number,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Provinsi',
                    ),
                    inputFormatters: [
                      LengthLimitingTextInputFormatter(16),
                    ],
                  ),
                ),
                //dis
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextFormField(
                    controller: nameController,
                    keyboardType: TextInputType.number,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Kecamatan',
                    ),
                    inputFormatters: [
                      LengthLimitingTextInputFormatter(16),
                    ],
                  ),
                ),
                //sub dis
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextFormField(
                    controller: nameController,
                    keyboardType: TextInputType.number,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Kelurahan',
                    ),
                    inputFormatters: [
                      LengthLimitingTextInputFormatter(16),
                    ],
                  ),
                ),
                //postal code
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextFormField(
                    controller: nameController,
                    keyboardType: TextInputType.number,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Kode Pos',
                    ),
                    inputFormatters: [
                      LengthLimitingTextInputFormatter(5),
                    ],
                  ),
                ),
                //address
                Container(
                  padding: EdgeInsets.all(10),
                  child: TextFormField(
                    controller: nameController,
                    keyboardType: TextInputType.number,
                    decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Alamat',
                    ),
                    inputFormatters: [
                      LengthLimitingTextInputFormatter(16),
                    ],
                  ),
                ),
                //button save
                Container(
                    height: 50,
                    padding: EdgeInsets.fromLTRB(10, 0, 10, 10),
                    child: ElevatedButton(
                      style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(buttonGeneric)),
                      child: Text('Simpan'),
                      onPressed: () {
                      },
                    )
                ),
              ],
            ),
          ),
        )
    );
  }
}