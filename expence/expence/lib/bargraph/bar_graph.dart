import 'package:fl_chart/fl_chart.dart';
import 'package:flutter/material.dart';

class MyBarGraph extends StatelessWidget{
  final double? maxY;
  final double sunAmount;
  final double monAmount;
  final double tueAmount;
  final double wenAmount;
  final double thurAmount;
  final double friAmount;
  final double satAmount;

  const MyBarGraph({
    super.key,
    required this.sunAmount,
    required this.monAmount,
    required this.tueAmount,
    required this.wenAmount,
    required this.thurAmount,
    required this.friAmount,
    required this.satAmount,
  });

  @override
  Widget build(BuildContext context) {
    
    //intialize the bar data
    BarData myBarData = BarData(
      sunAmount: sunAmount,
      monAmount: monAmount,
      tueAmount: tueAmount,
      wenAmount: wenAmount,
      thurAmount: thurAmount,
      friAmount: friAmount,
      satAmount: satAmount,
    );
    myBarData.initializeBarData();

    return BarChart(BarChartData(
      maxY: maxY,
      maxX: 0,
      barGroups: myBarData.barData
        .map(
          (data) => barChartGroupData(
            x:data.x,
            barRods: [
              BarChartRodData(toY: data.y)
            ],
          ),
        )
        .toList(),
    ));
  }
}