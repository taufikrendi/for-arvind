import 'package:flutter/material.dart';
import 'package:cooperation_apps/constants/home.dart';
import 'package:cooperation_apps/constants/colors.dart';
import 'package:fl_chart/fl_chart.dart';

class HomePage extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => new _State();
}

class _State extends State<HomePage> {
  static const cutOffYValue = 0.0;
  static const yearTextStyle =
  TextStyle(fontSize: 10, color: Colors.black, fontWeight: FontWeight.bold);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        color: homeBgScreen,
        child: SafeArea(
          child: SingleChildScrollView(
            padding: EdgeInsets.all(5),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: <Widget>[
                //member card
                Container(
                    margin: EdgeInsets.symmetric(horizontal: 32, vertical: 10),
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.all(Radius.circular(10)),
                      color: memberCardBg,
                    ),
                    padding: EdgeInsets.all(16),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: <Widget>[
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: <Widget>[
                            Text(
                              "KSPPS",
                              style: TextStyle(
                                  fontStyle: FontStyle.italic,
                                  fontSize: 28,
                                  color: memberCardAllText,
                                  fontWeight: FontWeight.w900),
                            ),
                            Text(
                              "Modal Bersama Sejahtera",
                              style: TextStyle(
                                  fontStyle: FontStyle.italic,
                                  fontSize: 14,
                                  color: memberCardAllText,
                                  fontWeight: FontWeight.w900),
                            ),
                          ],
                        ),
                        SizedBox(
                          height: 32,
                        ),
                        Text(
                          "**** **** **** ****",
                          style: TextStyle(
                              fontSize: 20,
                              color: memberCardAllText,
                              fontWeight: FontWeight.w700,
                              letterSpacing: 2.0),
                        ),
                        SizedBox(
                          height: 32,
                        ),
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: <Widget>[
                            Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: <Widget>[
                                Text(
                                  "CARD HOLDER",
                                  style: TextStyle(
                                      fontSize: 12,
                                      color: memberCardAllText,
                                      fontWeight: FontWeight.w700,
                                      letterSpacing: 2.0),
                                ),
                                Text(
                                  "Bagus Setya Wardana",
                                  style: TextStyle(
                                      fontSize: 16,
                                      color: memberCardAllText,
                                      fontWeight: FontWeight.w700,
                                      letterSpacing: 2.0),
                                ),
                              ],
                            ),
                            Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: <Widget>[
                                Text(
                                  "EXPIRES",
                                  style: TextStyle(
                                      fontSize: 12,
                                      color: memberCardAllText,
                                      fontWeight: FontWeight.w700,
                                      letterSpacing: 2.0),
                                ),
                                Text(
                                  "-/-",
                                  style: TextStyle(
                                      fontSize: 16,
                                      color: memberCardAllText,
                                      fontWeight: FontWeight.w700,
                                      letterSpacing: 2.0),
                                ),
                              ],
                            ),
                          ],
                        )
                      ],
                    )
                ),
                // services
                Container(
                  padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                    height: MediaQuery.of(context).size.height * 0.225,
                    child: GridView.builder(
                      physics: NeverScrollableScrollPhysics(),
                      gridDelegate: SliverGridDelegateWithMaxCrossAxisExtent(
                          maxCrossAxisExtent: 125,
                          childAspectRatio: 3 / 3,
                      ),
                      itemCount: menus_slide.length,
                      itemBuilder: (BuildContext ctx, index) {
                        return Container(
                          alignment: Alignment.center,
                          child: GestureDetector(
                            onTap: (){
                              switch(menus_slide[index]['title']){
                                case 'Simpanan': {
                                  viewSavings(context);
                                }
                                break;
                                case 'Tagihan': {
                                  viewPayment(context);
                                }
                                break;
                                case 'Top Up': {
                                  viewTopUp(context);
                                }
                                break;
                                case 'Penarikan': {
                                  viewWithDraw(context);
                                }
                                break;
                              }
                            },
                            child: Column(
                              children: <Widget>[
                                Image(image:AssetImage(menus_slide[index]['image'])),
                                Text(
                                  menus_slide[index]['title'],
                                  style: TextStyle(color: slideMenuTextH.withOpacity(0.6), fontSize: 12.5),
                                ),
                              ],
                            ),
                          ),
                          decoration: BoxDecoration(
                              borderRadius: BorderRadius.circular(15)
                          ),
                        );
                      }
                    ),
                  ),
                // your performance
                Container(
                  alignment: Alignment.center,
                  padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                  height: MediaQuery.of(context).size.height * 0.250,
                  width: MediaQuery.of(context).size.width * 0.90,
                  child:  Column(
                    children: <Widget>[
                      Container(
                        alignment: Alignment.center,
                        child: Text(
                          'Rekapitulasi',
                          style: TextStyle(fontSize: 20),
                        ),
                      ),
                      Expanded(
                        child: ListView.builder(
                            physics: NeverScrollableScrollPhysics(),
                            itemCount: menus_list.length,
                            itemBuilder: (context, index) {
                              return Container(
                                  child: Row(
                                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                    children: <Widget>[
                                      Container(
                                        alignment: Alignment.centerLeft,
                                        child: Text(
                                          menus_list[index]['sub'],
                                          textAlign: TextAlign.left,
                                          style: TextStyle(
                                            fontSize: 17.5,
                                          ),
                                        ),
                                      ),
                                      Container(
                                        alignment: Alignment.centerRight,
                                        child: Text(
                                          menus_list[index]['title'],
                                          textAlign: TextAlign.end,
                                          style: TextStyle(
                                            fontSize: 17.5,
                                          ),
                                        ),
                                      )
                                    ],
                                  )
                              );
                            }
                        ),
                      ),
                    ],
                  ),
                  decoration: BoxDecoration(
                    color: Colors.redAccent[100],
                    border: Border.all(
                      color: Colors.red,
                    ),
                    borderRadius: BorderRadius.all(Radius.circular(20))
                  ),
                ),
                // news
                Container(
                  padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                  child: Column(
                    children: <Widget>[
                      Container(
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: <Widget>[
                            Container(
                              alignment: Alignment.centerLeft,
                              child: Text(
                                'Pertanyaan Populer',
                                style: TextStyle(fontSize: 20),
                              ),
                            ),
                            Container(
                              alignment: Alignment.centerRight,
                              child: Text(
                                'Lihat Semua',
                                style: TextStyle(fontSize: 20),
                              ),
                            ),
                          ],
                        ),
                      ),
                      Container(
                        padding: EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                        height: MediaQuery.of(context).size.height * 0.225,
                        // width: MediaQuery.of(context).size.width * 0.90,
                        child: ListView.builder(
                          scrollDirection: Axis.horizontal,
                          itemCount: news_slide.length,
                          shrinkWrap: true,
                          itemBuilder: (context, index) {
                            return Column(
                              crossAxisAlignment: CrossAxisAlignment.center,
                              children: <Widget>[
                                Image(
                                  image:AssetImage(news_slide[index]['image']),
                                  height: 150,
                                  width: 150,
                                ),
                                Text(
                                  news_slide[index]['title'],
                                )
                              ],
                            );
                          },
                        ),
                      ),
                    ],
                  ),
                ),
                // performance company
                Container(
                  height: MediaQuery.of(context).size.height * 0.300,
                  width: MediaQuery.of(context).size.width * 0.950,
                  child: Column(
                    children: <Widget>[
                      Text(
                        'Performa Koperasi',
                        style: TextStyle(
                          fontSize: 20
                        ),
                      ),
                      Expanded(
                          child: SizedBox(
                            width: 330,
                            height: 180,
                            child: LineChart(
                              LineChartData(
                                lineTouchData: LineTouchData(enabled: false),
                                lineBarsData: [
                                  LineChartBarData(
                                    spots: [
                                      FlSpot(0, 0),
                                      FlSpot(1, 1),
                                      FlSpot(2, 3),
                                      FlSpot(3, 3),
                                      FlSpot(4, 5),
                                      FlSpot(4, 4)
                                    ],
                                    isCurved: false,
                                    barWidth: 1,
                                    colors: [
                                      Colors.black,
                                    ],
                                    belowBarData: BarAreaData(
                                      show: true,
                                      colors: [Colors.lightGreen.withOpacity(0.4)],
                                      cutOffY: cutOffYValue,
                                      applyCutOffY: true,
                                    ),
                                    aboveBarData: BarAreaData(
                                      show: true,
                                      colors: [Colors.red.withOpacity(0.6)],
                                      cutOffY: cutOffYValue,
                                      applyCutOffY: true,
                                    ),
                                    dotData: FlDotData(
                                      show: false,
                                    ),
                                  ),
                                ],
                                minY: 0,
                                titlesData: FlTitlesData(
                                  bottomTitles: SideTitles(
                                      showTitles: true,
                                      reservedSize: 6,
                                      getTitles: (value) {
                                        switch (value.toInt()) {
                                          case 0:
                                            return '2015';
                                          case 1:
                                            return '2016';
                                          case 2:
                                            return '2017';
                                          case 3:
                                            return '2018';
                                          case 4:
                                            return '2019';
                                          default:
                                            return '';
                                        }
                                      }),
                                  leftTitles: SideTitles(
                                    showTitles: true,
                                    getTitles: (value) {
                                      return '\$ ${value + 20}';
                                    },
                                  ),
                                ),
                                axisTitleData: FlAxisTitleData(
                                    leftTitle: AxisTitle(showTitle: true, titleText: 'Value', margin: 10),
                                    bottomTitle: AxisTitle(
                                        showTitle: true,
                                        margin: 10,
                                        titleText: 'Year',
                                        textStyle: yearTextStyle,
                                        textAlign: TextAlign.right)),
                                gridData: FlGridData(
                                  show: true,
                                  checkToShowHorizontalLine: (double value) {
                                    return value == 1 || value == 2 || value == 3 || value == 4;
                                  },
                                ),
                              ),
                            ),
                          ),
                      ),
                    ],
                  ),
                ),
              ],
            )
          ),
        )
      )
    );
  }
}