import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:expence/data/expense_data.dart';
import 'package:expence/bargraph/bar_graph.dart';

class ExpenseSummary extends StatelessWidget{
  final DateTime startOfWeek;
  const ExpenseSummary({
    super.key,
    required this.startOfWeek,
  });

  @override
  Widget build(BuildContext context){
    return Consumer<ExpenseData>(
      builder: (context, value, child) => const SizedBox(
        height: 200,
        child: MyBarGraph(
          maxY: 100,
          sunAmount: 20,
          monAmount: 50,
          tueAmount: 80,
          wenAmount: 10,
          thurAmount: 61,
          friAmount: 28,
          satAmount: 90,
        ),
      ),
    );
  }
}