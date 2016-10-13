from django.shortcuts import render
from django.db.models import Q, Sum
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from usaspending_api.awards.models import FinancialAccountsByAwardsTransactionObligations, Award
from usaspending_api.awards.serializers import FinancialAccountsByAwardsTransactionObligationsSerializer, AwardSerializer


class AwardList(APIView):

    """
    List all awards (financials)
    """
    def get(self, request, uri=None, piid=None, fain=None, format=None):
        awards = None
        if uri:
            awards = FinancialAccountsByAwardsTransactionObligations.objects.filter(financial_accounts_by_awards__uri=uri)
        elif piid:
            awards = FinancialAccountsByAwardsTransactionObligations.objects.filter(financial_accounts_by_awards__piid=piid)
        elif fain:
            awards = FinancialAccountsByAwardsTransactionObligations.objects.filter(financial_accounts_by_awards__fain=fain)
        else:
            awards = FinancialAccountsByAwardsTransactionObligations.objects.all()

        serializer = FinancialAccountsByAwardsTransactionObligationsSerializer(awards, many=True)
        response_object = {
            "count": awards.count(),
            "results": serializer.data
        }
        return Response(response_object)


class AwardListSummary(APIView):

    """
    List all awards (summary level)
    """
    def get(self, request, uri=None, piid=None, fain=None, format=None):
        # Because these are all GET requests and mutually exclusive, we chain an
        # if statement here. We could use some nifty Q object nonsense but for
        # clarity we skip that here. For POST filters we will want to set that up
        awards = None
        if uri:
            awards = Award.objects.filter(uri=uri)
        elif piid:
            awards = Award.objects.filter(piid=piid)
        elif fain:
            awards = Award.objects.filter(fain=fain)
        else:
            awards = Award.objects.all()

        agency = request.GET.get('agency')
        fy = request.GET.get('fy')
        query = Q()

        if agency:
            query = Q(awarding_agency__fpds_code=agency)
            query |= Q(funding_agency__fpds_code=agency)
        if fy:
            query &= Q(date_signed__year=fy)

        awards = awards.filter(query)

        serializer = AwardSerializer(awards, many=True)
        response_object = {
            "count": awards.count(),
            "total_obligation_sum": awards.aggregate(Sum('total_obligation'))["total_obligation__sum"],
            "results": serializer.data
        }
        return Response(response_object)