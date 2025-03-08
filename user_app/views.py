

from django.http import JsonResponse
from .models import UserInfo
import json

# 创建用户信息

def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = UserInfo.objects.create(
                nick_name=data.get('nick_name'),
                name=data.get('name'),
                gender=data.get('gender'),
                birth_year=data.get('birth_year'),
                birth_month=data.get('birth_month'),
                birth_day=data.get('birth_day'),
                is_in_school=data.get('is_in_school'),
                is_in_school_authenticated=data.get('is_in_school_authenticated'),
                current_student_stage=data.get('current_student_stage'),
                college_enter_year=data.get('college_enter_year'),
                is_invited_to_school=data.get('is_invited_to_school'),
                school_invitor=data.get('school_invitor'),
                school_invitation_reason=data.get('school_invitation_reason'),
                location_province=data.get('location_province'),
                location_city=data.get('location_city'),
                academic_certificate=data.get('academic_certificate'),
                academic_certificate_type=data.get('academic_certificate_type'),
                mianji_goal=data.get('mianji_goal'),
                is_real_person_authenticated=data.get('is_real_person_authenticated'),
                avatar_image_url=data.get('avatar_image_url'),
                is_avatar_checked=data.get('is_avatar_checked'),
                is_safe_authenticated=data.get('is_safe_authenticated'),
                last_safe_authenticated_time=data.get('last_safe_authenticated_time'),
                last_pay_safe_authenticated_time=data.get('last_pay_safe_authenticated_time'),
                safe_json=data.get('safe_json'),
                is_married=data.get('is_married'),
                is_married_authenticated=data.get('is_married_authenticated'),
                last_married_authenticated_time=data.get('last_married_authenticated_time'),
                last_pay_married_authenticated_time=data.get('last_pay_married_authenticated_time'),
                height=data.get('height'),
                weight=data.get('weight'),
                college=data.get('college'),
                hukou_province=data.get('hukou_province'),
                hukou_city=data.get('hukou_city'),
                hometown_province=data.get('hometown_province'),
                hometown_city=data.get('hometown_city'),
                business=data.get('business'),
                job=data.get('job'),
                company=data.get('company'),
                salary_min=data.get('salary_min'),
                salary_max=data.get('salary_max'),
                house_purchased=data.get('house_purchased'),
                house_purchased_city=data.get('house_purchased_city'),
                car_purchased=data.get('car_purchased'),
                license_plate_city=data.get('license_plate_city'),
                wealth_level=data.get('wealth_level'),
                is_wealth_level_authenticated=data.get('is_wealth_level_authenticated'),
                extend_authentication=data.get('extend_authentication'),
                tags=data.get('tags'),
                tags_like=data.get('tags_like'),
                images_desc_list=data.get('images_desc_list'),
                characters=data.get('characters'),
                psychological_evaluations=data.get('psychological_evaluations'),
                valid_mian_ji_s=data.get('valid_mian_ji_s'),
                moments=data.get('moments')
            )
            return JsonResponse({'message': '用户信息创建成功', 'user_id': user.id}, status=201)
        except Exception as e:
            return JsonResponse({'message': f'创建用户信息失败: {str(e)}'}, status=400)
    return JsonResponse({'message': '请求方法不允许'}, status=405)

# 获取用户信息

def get_user(request, user_id):
    try:
        user = UserInfo.objects.get(id=user_id)
        user_data = {
            'id': user.id,
            'nick_name': user.nick_name,
            'name': user.name,
            'gender': user.gender,
            'birth_year': user.birth_year,
            'birth_month': user.birth_month,
            'birth_day': user.birth_day,
            'is_in_school': user.is_in_school,
            'is_in_school_authenticated': user.is_in_school_authenticated,
            'current_student_stage': user.current_student_stage,
            'college_enter_year': user.college_enter_year,
            'is_invited_to_school': user.is_invited_to_school,
            'school_invitor': user.school_invitor,
            'school_invitation_reason': user.school_invitation_reason,
            'location_province': user.location_province,
            'location_city': user.location_city,
            'academic_certificate': user.academic_certificate,
            'academic_certificate_type': user.academic_certificate_type,
            'mianji_goal': user.mianji_goal,
            'is_real_person_authenticated': user.is_real_person_authenticated,
            'avatar_image_url': user.avatar_image_url,
            'is_avatar_checked': user.is_avatar_checked,
            'is_safe_authenticated': user.is_safe_authenticated,
            'last_safe_authenticated_time': user.last_safe_authenticated_time,
            'last_pay_safe_authenticated_time': user.last_pay_safe_authenticated_time,
            'safe_json': user.safe_json,
            'is_married': user.is_married,
            'is_married_authenticated': user.is_married_authenticated,
            'last_married_authenticated_time': user.last_married_authenticated_time,
            'last_pay_married_authenticated_time': user.last_pay_married_authenticated_time,
            'height': user.height,
            'weight': user.weight,
            'college': user.college,
            'hukou_province': user.hukou_province,
            'hukou_city': user.hukou_city,
            'hometown_province': user.hometown_province,
            'hometown_city': user.hometown_city,
            'business': user.business,
            'job': user.job,
            'company': user.company,
            'salary_min': user.salary_min,
            'salary_max': user.salary_max,
            'house_purchased': user.house_purchased,
            'house_purchased_city': user.house_purchased_city,
            'car_purchased': user.car_purchased,
            'license_plate_city': user.license_plate_city,
            'wealth_level': user.wealth_level,
            'is_wealth_level_authenticated': user.is_wealth_level_authenticated,
            'extend_authentication': user.extend_authentication,
            'tags': user.tags,
            'tags_like': user.tags_like,
            'images_desc_list': user.images_desc_list,
            'characters': user.characters,
            'psychological_evaluations': user.psychological_evaluations,
            'valid_mian_ji_s': user.valid_mian_ji_s,
            'moments': user.moments
        }
        return JsonResponse(user_data, status=200)
    except UserInfo.DoesNotExist:
        return JsonResponse({'message': '用户信息不存在'}, status=404)

# 更新用户信息

def update_user(request, user_id):
    if request.method == 'PUT':
        try:
            user = UserInfo.objects.get(id=user_id)
            data = json.loads(request.body)
            for key, value in data.items():
                setattr(user, key, value)
            user.save()
            return JsonResponse({'message': '用户信息更新成功'}, status=200)
        except UserInfo.DoesNotExist:
            return JsonResponse({'message': '用户信息不存在'}, status=404)
        except Exception as e:
            return JsonResponse({'message': f'更新用户信息失败: {str(e)}'}, status=400)
    return JsonResponse({'message': '请求方法不允许'}, status=405)

