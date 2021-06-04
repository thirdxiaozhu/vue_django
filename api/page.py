from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination

class MyLimitOffsetPagination(PageNumberPagination):
    #每页显示多少个
    page_size = 3
    #默认每页显示3个，但可以通过掺入pager1/?currentPage=2&pageSize=4,改变默认每页显示的个数
    page_size_query_param = "pagesize"
    #最大页数
    max_page_size = 100
    #获取页码
    page_query_param = "currentpage"