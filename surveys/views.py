import json
from users.models import User

from django.views import View
from django.http  import JsonResponse

from surveys.models import SurveyInfo, Body, Symptom, SurveyInfo_Symptom
from products.models import Product, Food, Feature, Summary
from users.models import User

from users.utils import user_auth

class SurveyView(View):
    @user_auth
    def post(self, request):
        try:
            user = request.user
            data = json.loads(request.body)
            
            SurveyInfo.objects.create(
                user_id = user,
                gender  = data['gender'],
                age     = data['age'],
            )
            return JsonResponse({"message" : "SUSCCESS"}, status=200)
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

    @user_auth
    def get(self, request):
        bodies = Body.objects.all()

        result =[{
            "id"   : body.id,
            "name" : body.name
            }for body in bodies]
        return JsonResponse({"result" : result}, status=200)

class SymptomView(View):
    @user_auth
    def get(self, request):
        try:
            first_body  = request.GET.get('first-body')
            second_body = request.GET.get('second-body')

            first_symptoms = Symptom.objects.filter(body_id__name=first_body)

            if not first_symptoms:
                return JsonResponse({"message" : "WRONG_BODY"}, status=400)
            
            first_result = [{
                'id'      : symptom.id,
                'body'    : first_body,
                'symptom' : symptom.description
            } for symptom in first_symptoms]
            
            if second_body:
                second_symptoms = Symptom.objects.filter(body_id__name=second_body)
                
                if not second_symptoms:
                    return JsonResponse({"First_Body" : first_result}, status=200)

                second_result = [{
                    'id'      : symptom.id,
                    'body'    : second_body,
                    'symptom' : symptom.description
                } for symptom in second_symptoms]

                return JsonResponse({"First_Result" : first_result, "Second_Result" : second_result}, status=200)
    
            return JsonResponse({"First_Body" : first_result}, status=200)
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

    @user_auth
    def post(self, request):
        try:
            user = request.user
            data = json.loads(request.body)
            
            print(data['symptom_id'])
            symptoms = data['symptom_id']
            
            for symptom in symptoms:
                SurveyInfo_Symptom.objects.create(
                    surveyinfo_id = SurveyInfo.objects.filter(user_id=user).last().id,
                    symptom_id = symptom
                )
            return JsonResponse({"message" : "SUCCESS"}, status=200)
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)
            
class SurveyResultView(View):
    @user_auth
    def get(self, request):
        try:
            user = request.user
            survey_user = SurveyInfo.objects.filter(user_id=user).last().id
            products = Product.objects.filter(symptom__surveyinfo_symptom__surveyinfo_id=survey_user)

            if not products:
                return JsonResponse({"message" : "PRODUCT NOT FOUND"}, status=400)

            result = [{
                'product_name' : product.name,
                'summary'      : [summary.name for summary in Summary.objects.filter(product_id=product.id)],
                'image'        : product.image_set.first().image_url,
                'food'         : [{
                    'name'       : food.name,
                    'url'        : food.food_url,
                    'daily_dose' : food.daily_dose,
                    'feature'    : [{
                        'name' : feature.name
                    }for feature in food.feature_set.all()]
                } for food in product.food_set.all()]
            }for product in products]

            return JsonResponse({"Result" : result}, status=200)
        except KeyError:
            return JsonResponse({"message" : "KEY ERROR"}, status=400)
        except AttributeError:
            return JsonResponse({"message" : "DATA NOT FOUND"}, status=400)

class UserSurveyListView(View):
    @user_auth
    def get(self, request):
        user = request.user

        surveys = SurveyInfo.objects.filter(user_id=user)
        
        if not surveys:
            return JsonResponse({"Message" : "SURVEY IS EMPTY"}, status=200)

        result =[{
            "id"           : survey.id,
            "created_at"   : survey.created_at,
            "product_name" : [product.name for product in Product.objects.filter(symptom__surveyinfo__id=survey.id)]
        }for survey in surveys]

        return JsonResponse({"Result" : result}, status=200)

class UserSurveyResultView(View):
    @user_auth
    def get(self, request):
        try:
            user = request.user
            survey = request.GET.get('survey-id')
            survey_user = SurveyInfo.objects.get(user_id=user, id=survey).id
            products = Product.objects.filter(symptom__surveyinfo_symptom__surveyinfo_id=survey_user)

            if not products:
                return JsonResponse({"message" : "PRODUCT NOT FOUND"}, status=400)

            result = [{
                'product_name' : product.name,
                'summary'      : [summary.name for summary in Summary.objects.filter(product_id=product.id)],
                'image'        : product.image_set.first().image_url,
                'food'         : [{
                    'name'       : food.name,
                    'url'        : food.food_url,
                    'daily_dose' : food.daily_dose,
                    'feature'    : [{
                        'name' : feature.name
                    }for feature in food.feature_set.all()]
                } for food in product.food_set.all()]
            }for product in products]

            return JsonResponse({"Result" : result}, status=200)
        except KeyError:
            return JsonResponse({"message" : "KEY ERROR"}, status=400)
        except AttributeError:
            return JsonResponse({"message" : "DATA NOT FOUND"}, status=400)
        except SurveyInfo.DoesNotExist:
            return JsonResponse({"message" : "WORNG SURVEY"}, status=400)
