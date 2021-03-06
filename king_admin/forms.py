# author：wylkjj
# date：2020/2/7
# -*- coding:utf-8 -*-
from django.utils.translation import ugettext as _
from django.forms import forms, ModelForm
from django.forms import ValidationError
from crm import models


class CustomerModelForm(ModelForm):
    class Meta:
        model = models.Customer
        fields = "__all__"


def creatr_model_form(request, admin_class):
    """动态生成 MODEL FORM"""
    def __new__(cls, *args, **kwargs):  # new方法是在构造函数__init__之前执行(cls相当于self)
        # base_fields是一个字典,关于前端样式的
        for field_name, field_obj in cls.base_fields.items():
            field_obj.widget.attrs['class'] = 'form-control'
            if not hasattr(admin_class, "is_add_form"):  # 代表这是添加Form，不需要disabled
                if field_name in admin_class.readonly_fields:
                    field_obj.widget.attrs['disabled'] = 'disabled'
            if hasattr(admin_class, "clean_%s" % field_name):
                field_clean_func = getattr(admin_class, "clean_%s" % field_name)
                setattr(cls, "clean_%s" % field_name, field_clean_func)
                # print("---", field_clean_func)
        return ModelForm.__new__(cls)  # 相当于继承

    def default_clean(self):
        """给所有的form默认加一个clean验证 """
        # print("---running default clean",admin_class)
        # print("---running readonly_fields", admin_class.readonly_fields)
        # print("---obj instance", self.instance)
        error_list = []
        if self.instance.id:  # 这是个修改的表单
            for field in admin_class.readonly_fields:
                field_val = getattr(self.instance, field)  # 获取数据库的值
                print(field_val)
                field_val_from_frontend = self.cleaned_data.get(field)
                # print("clean data:",self.cleaned_data)
                # print("haha:",self.cleaned_data.get(field))
                if field_val != field_val_from_frontend:
                    error_list.append(ValidationError(
                        _('Field %(field)s is readonly,data should be %(val)s'),
                        code='invalid',
                        params={'field': field, 'val': field_val},)
                    )  # 抛出异常
        if admin_class.readonly_table:
            raise ValidationError(
                _('Table is readonly,cannot be modified or added'),
                code='invalid')
        if error_list:
            raise ValidationError(error_list)
        # admin_class.default_form_validation(admin_class) #钩子

    class Meta:
        model = admin_class.model
        fields = "__all__"
        exclude = admin_class.modelform_exclude_fields
    attrs = {"Meta": Meta}
    _model_form_class = type("DynamicModelForm", (ModelForm,), attrs)  # 创建类的特殊的方法
    setattr(_model_form_class, "__new__", __new__)  # 创建一个新的属性
    setattr(_model_form_class, 'clean', default_clean)
    return _model_form_class












