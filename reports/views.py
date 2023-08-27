from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ReportSerializer, ReportSerializerReport
from .models import TreeReport
from trades.models import Trade
from contracts.models import Contract, ContractWithPartner
from trades.serializers import TradeSerializerReport
from contracts.serializers import ContractSerializerReport, ContractWithPartnerSerializerReport
from rest_framework import status
from rest_framework.authentication import TokenAuthentication


class TreeReportCreateAPIView(generics.CreateAPIView):
    queryset = TreeReport.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class DocsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        pk = self.request.GET.get('status')
        search = self.request.GET.get('search')
        trade = Trade.objects.all()
        contract = Contract.objects.all()
        report = TreeReport.objects.all()
        partner = ContractWithPartner.objects.all()
        if pk:
            trade = trade.filter(status=pk)
            contract = contract.filter(status=pk)
            report = report.filter(status=pk)
            partner = partner.filter(status=pk)
        if search:
            trade = trade.filter(contract_number__icontains=search)
            contract = contract.filter(name_company__icontains=search)
            report = report.filter(company_name__icontains=search)
            partner = partner.filter(partner_name__icontains=search)
        partner_ser = ContractWithPartnerSerializerReport(partner, many=True).data
        trade_ser = TradeSerializerReport(trade, many=True).data
        contract_ser = ContractSerializerReport(contract, many=True).data
        report_ser = ReportSerializerReport(report, many=True).data
        return Response({
            1: trade_ser,
            2: contract_ser,
            3: report_ser,
            4: partner_ser
        }, status=status.HTTP_200_OK)


class DocsUpdateAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        pk = self.request.data.get('id')
        statu = self.request.data.get('status')
        model = self.request.data.get('model')
        if int(model) == 1:
            trade = Trade.objects.filter(id=pk).first()
            trade.status = statu
            trade.save()
            return Response({'message': 'Successfully changed status'}, status=status.HTTP_200_OK)
        if int(model) == 3:
            report = TreeReport.objects.filter(id=pk).first()
            report.status = statu
            report.save()
            return Response({'message': 'Successfully changed status'}, status=status.HTTP_200_OK)
        if int(model) == 2:
            contract = Contract.objects.filter(id=pk).first()
            contract.status = statu
            contract.save()
            return Response({'message': 'Successfully changed status'}, status=status.HTTP_200_OK)
        if int(model) == 4:
            contract_with = ContractWithPartner.objects.filter(id=pk).first()
            contract_with.status = statu
            contract_with.save()
            return Response({'message': 'Successfully changed status'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
