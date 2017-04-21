/**
 * Created by mac on 17/1/10.
 */
//var httpUrl = 'http://www.jiangjie.com/api/v1/';
//var httpUrl = 'http://test.53hello.com/api/v1/';
//var httpUrl = 'http://127.0.0.1:8000/api/v1/';
var httpUrl = '/api/v1/';

var homes = angular.module('home', ['ngRoute']);
homes.controller('homeShow', ['$scope', '$location', function ($scope, $location) {
    $scope.url_ = {
        rowUrl: '/template/admin/info_table.html',
        floorUrl: '/template/admin/user_floor.html'
    };
    $scope.data = {
        listHtml: [
            {
                type: 0, name: '统计信息', url: '/template/admin/info_table.html', f_url: '/template/admin/user_floor.html',
                routeName: '#/info'
            },
            {
                type: 0, name: '用户', url: '/template/admin/user_table.html', f_url: '/template/admin/user_floor.html',
                routeName: '#/user'
            },
            {
                type: 0, name: '勋章', url: '/template/admin/medal_table.html', f_url: '/template/admin/medal_floor.html',
                routeName: '#/medal'
            },
            {
                type: 0,
                name: '任务统计',
                url: '/template/admin/task_record_table.html',
                routeName: '#/task_record'
            },
            //{
            //    type: 0,
            //    name: '讨论区',
            //    url: '/template/admin/discuss_table.html',
            //    f_url: '/template/admin/discuss_floor.html',
            //    routeName: '#/discuss'
            //},
            {
                type: 1, name: '角色',
                child: [
                    {
                        name: '角色信息', url: '/template/admin/role_table.html', f_url: '/template/admin/role_floor.html',
                        routeName: '#/role_info'
                    },
                    {
                        name: '角色标签',
                        url: '/template/admin/role_tag_table.html',
                        f_url: '/template/admin/role_tag_floor.html',
                        routeName: '#/role_tag'
                    }
                ]
            },
            {
                type: 1, name: '活动',
                child: [
                    {
                        name: '人物设定活动',
                        url: '/template/admin/feature_txt_event_table.html',
                        f_url: '/template/admin/feature_txt_event_floor.html',
                        routeName: '#/feature_txt_event'
                    },
                    {
                        name: '收藏室活动',
                        url: '/template/admin/feature_img_event_table.html',
                        f_url: '/template/admin/feature_img_event_floor.html',
                        routeName: '#/feature_img_event'
                    },
                    {
                        name: '脑洞活动',
                        url: '/template/admin/brain_event_table.html',
                        f_url: '/template/admin/feature_img_event_floor.html',
                        routeName: '#/feature_brain_event'
                    }
                ]
            },
            {
                type: 1, name: '话题',
                child: [
                    {
                        name: '话题列表',
                        url: '/template/admin/topic_table.html',
                        f_url: '/template/admin/topic_floor.html',
                        routeName: '#/topics'
                    },
                    {
                        name: '话题管理员申请者列表',
                        url: '/template/admin/topic_manager_table.html',
                        f_url: '/template/admin/topic_floor.html',
                        routeName: '#/topic_manager'
                    }
                ]
            },
            {
                type: 1, name: '首页',
                child: [
                    {
                        name: '精选',
                        url: '/template/admin/index_feature_table.html',
                        f_url: '/template/admin/index_feature_floor.html',
                        routeName: '#/index'

                    },
                    {
                        name: 'banner',
                        url: '/template/admin/banner_table.html',
                        f_url: '/template/admin/banner_floor.html',
                        routeName: '#/banner'
                    },
                    {
                        name: '角色池',
                        url: '/template/admin/role_pool_table.html',
                        f_url: '/template/admin/role_pool_floor.html',
                        routeName: '#/hot_role'
                    },
                    {
                        name: '作品池',
                        url: '/template/admin/post_pool_table.html',
                        f_url: '/template/admin/post_pool_floor.html',
                        routeName: '#/hot_product'

                    },
                    {
                        name: '快速入口',
                        url: '/template/admin/index_event_table.html',
                        f_url: '/template/admin/index_event_floor.html',
                        routeName: '#/fast_enter'

                    },
                    {
                        name: '活动', url: '/template/admin/event_table.html', f_url: '/template/admin/event_floor.html',
                        routeName: '#/event'
                    },
                    {
                        name: '公告',
                        url: '/template/admin/announce_table.html',
                        f_url: '/template/admin/announce_floor.html',
                        routeName: '#/announce'
                    },
                    {
                        name: 'bug活动记录',
                        url: '/template/admin/event_bug_table.html',
                        f_url: '/template/admin/announce_floor.html',
                        routeName: '#/bug_event'
                    }
                ]
            },
            {
                type: 1, name: '作品',
                child: [
                    {
                        name: '阵营作品', url: '/template/admin/table_camp_product.html',
                        f_url: '/template/admin/floor_camp_product.html', routeName: '#/camp_product'
                    },
                    {
                        name: '机构作品', url: '/template/admin/table_organize_product.html',
                        f_url: '/template/admin/floor_organize_product.html', routeName: '#/organ_product'
                    },
                    {
                        name: '角色作品', url: '/template/admin/table_role_product.html',
                        f_url: '/template/admin/floor_role_product.html', routeName: '#/role_product'
                    }
                ]
            },

            {
                type: 1, name: '章节',
                child: [
                    {
                        name: '阵营章节', url: '/template/admin/table_camp_chapter.html',
                        f_url: '/template/admin/floor_camp_chapter.html', routeName: '#/camp_chapter'
                    },
                    {
                        name: '机构章节', url: '/template/admin/table_organize_chapter.html',
                        f_url: '/template/admin/floor_organize_chapter.html', routeName: '#/organ_chapter'
                    }
                ]
            },

            {
                type: 1, name: '任务',
                child: [
                    {
                        name: '任务池', url: '/template/admin/table_task.html',
                        f_url: '/template/admin/floor_task.html', routeName: '#/task'
                    },
                    // f_url: '/template/admin/floor_task.html'},
                    {
                        name: '角色任务', url: '/template/admin/table_task_role.html',
                        f_url: '/template/admin/floor_task_role.html', routeName: '#/task_role'
                    },

                    {
                        name: '角色任务记录', url: '/template/admin/table_task_role_info.html',
                        f_url: '/template/admin/floor_task_role_info.html', routeName: '#/task_role_info'
                    }

                ]
            }


        ]
    }
    $scope.fun = {
        hrefF: function (str) {
            $scope.url_.rowUrl = 'template/' + str;
        },
        ajax_: function () {

        },
        tohref: function (str, fStr) {
            // $scope.$apply(function(){
            //     $scope.url_.floorUrl = fStr;
            // });
            window.location.href = str;
            //$scope.url_.floorUrl = fStr;
            //$scope.fun.resizaFloor();
            window.location.reload();
        },
        resizaFloor: function () {
            var allDtat = $scope.data.listHtml;
            var hrefName = $location.url();
            for (var i = 0; i < allDtat.length; i++) {
                if (allDtat[i].routeName == '#' + hrefName) {
                    $scope.url_.floorUrl = allDtat[i].f_url;
                    return false;
                }
                if (allDtat[i].child) {
                    var dattC = allDtat[i].child;
                    for (var j = 0; j < dattC.length; j++) {
                        if (dattC[j].routeName == '#' + hrefName) {
                            $scope.url_.floorUrl = dattC[j].f_url;
                            return false;
                        }
                    }
                }


            }
        }
    }
    $scope.fun.resizaFloor();

}]);

//function Trim(str)
//{
//    return str.replace(/(^\s*)|(\s*$)/g, "");
//}

//$(document).on('paste','.wysiwyg-editor',function(){
//    console.log('this is paste=====')
//    console.log(this)
//    var self = this;
//    var prev_len = $(self).text().length;
//    setTimeout(function() {
//        var now_len = $(self).text().length;
//        var paste_values = $(self).text().slice(prev_len, now_len - prev_len);
//        var old_values = $(self).text().slice(0, prev_len);
//        //var new_values = $.htmlClean(paste_values, { format: true,allowedTags:["a",] });//清除HTML格式 。
//        var new_values = Trim(paste_values);//清除HTML格式 。
//
//        $(self).text(old_values + new_values);
//    },0);
//});


homes.config(['$routeProvider', function ($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: '/template/admin/info_table.html'
        })
        .when('/user', {
            templateUrl: '/template/admin/user_table.html'
        })
        .when('/medal', {
            templateUrl: '/template/admin/medal_table.html'
        })
        //.when('/discuss', {
        //    templateUrl: '/template/admin/discuss_table.html'
        //})
        .when('/role_info', {
            templateUrl: '/template/admin/role_table.html'
        })
        .when('/role_tag', {
            templateUrl: '/template/admin/role_tag_table.html'
        })
        .when('/index', {
            templateUrl: '/template/admin/index_feature_table.html'
        })
        .when('/banner', {
            templateUrl: '/template/admin/banner_table.html'
        })
        .when('/hot_role', {
            templateUrl: '/template/admin/role_pool_table.html'
        })
        .when('/hot_product', {
            templateUrl: '/template/admin/post_pool_table.html'
        })
        .when('/fast_enter', {
            templateUrl: '/template/admin/index_event_table.html'
        })
        .when('/welcome_product', {
            templateUrl: '/template/admin/table3-4.html'
        })
        .when('/camp_product', {
            templateUrl: '/template/admin/table_camp_product.html'
        })
        .when('/organ_product', {
            templateUrl: '/template/admin/table_organize_product.html'
        })
        .when('/role_product', {
            templateUrl: '/template/admin/table_role_product.html'
        })
        .when('/task_record', {
            templateUrl: '/template/admin/task_record_table.html'
        })
        .when('/feature_txt_event', {
            templateUrl: '/template/admin/feature_txt_event_table.html'
        })
        .when('/feature_img_event', {
            templateUrl: '/template/admin/feature_img_event_table.html'
        })
        .when('/feature_brain_event', {
            templateUrl: '/template/admin/brain_event_table.html'
        })
        .when('/camp_chapter', {
            templateUrl: '/template/admin/table_camp_chapter.html'
        })
        .when('/organ_chapter', {
            templateUrl: '/template/admin/table_organize_chapter.html'
        })
        .when('/task', {
            templateUrl: '/template/admin/table_task.html'
        })

        .when('/task_role', {
            templateUrl: '/template/admin/table_task_role.html'
        })

        .when('/task_role_info', {
            templateUrl: '/template/admin/table_task_role_info.html'
        })
        .when('/event', {
            templateUrl: '/template/admin/event_table.html'
        })
        .when('/announce', {
            templateUrl: '/template/admin/announce_table.html'
        })
        .when('/bug_event', {
            templateUrl: '/template/admin/event_bug_table.html'
        })
        .when('/info', {
            templateUrl: '/template/admin/info_table.html'
        })
        .when('/topic_manager', {
            templateUrl: '/template/admin/topic_manager_table.html'
        })
        .when('/topics', {
            templateUrl: '/template/admin/topic_table.html'
        })
        .otherwise({
            redirectTo: '/'
        });
}])


homes.controller('creationBox', ['$scope', '$location', '$http', function ($scope, $location, $http) {
    $scope.fun = {
        imgUpload: function () {
            var tag_a = ' ';
            $('#imgtagShow li').each(function (index) {
                // tag_a += '#' + $(this).find('span').html();
                tag_a += ' ' + $(this).find('span').html();
            });
            var data_ = {
                "role": $('#add_role').val(),
                "title": $scope.fd.imgName,      //绘画标题
                "introduce": $scope.fd.imgD,   //简介
                "tag_text": tag_a, //标签
                "upload_image_list": $scope.data.img,
                "cover_img": {
                    "raw_url": $('#imgHeadShow').attr('src'), //等待裁切图片的url
                    "parameter": $('#imgHeadShowBox').attr('infoimg')      //裁切参数
                },
                "is_origin": $scope.fd.imgSm,  //是否原创，默认为原创
            }
            $.ajax({
                url: httpUrl + 'roles/' + $('#add_role').val() + '/draws/',
                type: "POST",
                data: JSON.stringify(data_),
                contentType: "application/json; charset=utf-8",
                success: function (response) {
                    // 刷新页面
                    // window.location.reload()
                    // http://test.53hello.com/role/#/atlas/162/76
                    //
                    // var redict = "/role/#/atlas/"  + response.role.id + "/" + response.id
                    // window.open(redict);

                    window.location.reload()

                },
                error: function (err) {

                    alert(err.responseText)
                    console.log('err')
                    console.log(err.responseText)
                    $('.tothreeStep').html(err.responseText)
                }
            });

        },
        bookUpTo: function () {
            var type_ = $('#creatA').attr('typeIdF');
            var role_id = new Array;
            var role_ht = $('.wysiwyg-editor').find('a');
            var tag_a = ' ';
            $('#txttagShow li').each(function (index) {
                tag_a += ' ' + $(this).find('span').html();
            });
            for (var i = 0; i < role_ht.length; i++) {
                role_id.push($(role_ht).eq(i).attr('href').slice(16))
            }

            if (type_ == 0) {
                var data_ = {
                    // "role": $.cookie('role_id'),
                    "role": $('#add_role').val(),
                    "title": $scope.fd.txtName,
                    "introduce": $('#txtDecS').val(),
                    "related_role": role_id,//相关角色id列表
                    "cover_img": {          //如果自定义封面
                        "raw_url": $('#creatA').attr('src'), //等待裁切图片的url
                        "parameter": $('#creatABox').attr('infoimg')      //裁切参数
                    },
                    "content": $('.wysiwyg-editor').html(),//文章内容
                    "tag_text": tag_a,//标签
                    "status": "1",  //默认为发布，可以不传
                    "is_origin": $scope.fd.imgCheck, //是否原创，默认为原创
                }
            } else {
                var data_ = {
                    "role": $('#add_role').val(),
                    "title": $scope.fd.txtName,
                    "introduce": $('#txtDecS').val(),
                    "related_role": role_id,//相关角色id列表
                    "default_cover": $('#creatA').attr('typeId'),  //如果用户选择了官方封面，cover_img和default_cover不能同时上传
                    "content": $('.wysiwyg-editor').html(),//文章内容
                    "tag_text": tag_a,//标签
                    "status": "1",  //默认为发布，可以不传
                    "is_origin": $scope.fd.imgCheck, //是否原创，默认为原创
                }
            }

            $.ajax({
                url: httpUrl + 'roles/' + $('#add_role').val() + '/articles/',
                type: "POST",
                data: JSON.stringify(data_),
                contentType: "application/json; charset=utf-8",
                success: function (response) {
                    $('textarea').val('');
                    // 刷新页面

                    // var redict = "/role/#/essay/"  + response.role.id + "/" + response.id
                    // window.open(redict);

                    window.location.reload()

                },
                error: function (err) {
                    alert(err.responseText)

                }
            });
        },
        createBook: function () {
            var type_ = $('#creatB').attr('typeIdF');
            if (type_ == 0) {
                var data_ = {
                    "role": $('#add_role').val(),
                    "title": $scope.fd.floorN,
                    "introduce": $scope.fd.floorD,
                    "cover_img": {          //如果自定义封面
                        "raw_url": $('#creatB').attr('src'), //等待裁切图片的url
                        "parameter": $('#creatBShowBox').attr('infoimg')      //裁切参数
                    },
                    "status": 1
                }
            } else {
                var data_ = {
                    "role": $('#add_role').val(),
                    "title": $scope.fd.floorN,
                    "introduce": $scope.fd.floorD,
                    "default_cover": $('#creatB').attr('typeId'),  //如果用户选择了官方封面，cover_img和default_cover不能同时上传
                    "status": 1
                }
            }
            if ($('.addBooksCover h2').html() != '新增书籍') {
                var url_n = 'draw_sets';
            } else {
                var url_n = 'article_sets';
            }
            $.ajax({
                url: httpUrl + 'roles/' + $('#add_role').val() + '/' + url_n + '/',
                type: "POST",
                data: JSON.stringify(data_),
                contentType: "application/json; charset=utf-8",
                success: function (response) {
                    $('.closeBtn').click();
                    $scope.fun.listData();
                },
                error: function (err) {
                    alert(err.responseText)
                }
            });
        },
        createBookFloor: function () {
            var type_ = $('#creatB').attr('typeIdF');
            if (type_ == 0) {
                var data_ = {
                    // "role": $.cookie('role_id'),
                    "role": $('#add_role').val(),
                    "title": $scope.fd.floorN,
                    "introduce": $scope.fd.floorD,
                    "cover_img": {          //如果自定义封面
                        "raw_url": $('#creatB').attr('src'), //等待裁切图片的url
                        "parameter": $('#creatBShowBox').attr('infoimg')      //裁切参数
                    },
                    "status": 1
                }
            } else {
                var data_ = {
                    "role": $('#add_role').val(),
                    "title": $scope.fd.floorN,
                    "introduce": $scope.fd.floorD,
                    "default_cover": $('#creatB').attr('typeId'),  //如果用户选择了官方封面，cover_img和default_cover不能同时上传
                    "status": 1
                }
            }
            // if ($('.addBooksCover h2').html() != '新增书籍') {
            var url_n = 'article_sets';
            // } else {
            //     var url_n = 'article_sets';
            // }
            $.ajax({
                url: httpUrl + 'roles/' + $('#add_role').val() + '/' + url_n + '/',
                type: "POST",
                data: JSON.stringify(data_),
                contentType: "application/json; charset=utf-8",
                success: function (response) {
                    // 刷新页面
                    window.location.reload()
                },
                error: function (err) {
                    alert(err.responseText)
                }
            });
        },

        createDrawFloor: function () {
            var type_ = $('#creatB').attr('typeIdF');
            if (type_ == 0) {
                var data_ = {
                    // "role": $.cookie('role_id'),
                    "role": $('#add_role').val(),
                    "title": $scope.fd.floorN,
                    "introduce": $scope.fd.floorD,
                    "cover_img": {          //如果自定义封面
                        "raw_url": $('#creatB').attr('src'), //等待裁切图片的url
                        "parameter": $('#creatBShowBox').attr('infoimg')      //裁切参数
                    },
                    "status": 1
                }
            } else {
                var data_ = {
                    "role": $('#add_role').val(),
                    "title": $scope.fd.floorN,
                    "introduce": $scope.fd.floorD,
                    "default_cover": $('#creatB').attr('typeId'),  //如果用户选择了官方封面，cover_img和default_cover不能同时上传
                    "status": 1
                }
            }
            // if ($('.addBooksCover h2').html() != '新增书籍') {
            var url_n = 'draw_sets';
            // } else {
            //     var url_n = 'article_sets';
            // }
            $.ajax({
                url: httpUrl + 'roles/' + $('#add_role').val() + '/' + url_n + '/',
                type: "POST",
                data: JSON.stringify(data_),
                contentType: "application/json; charset=utf-8",
                success: function (response) {
                    // 刷新页面
                    window.location.reload()
                },
                error: function (err) {
                    alert(err.responseText)
                }
            });
        },

        closeBtn: function () {
            $('.closeBtn').click();
        },
        listData: function () {

            $http({
                url: httpUrl + 'roles/' + $('#add_role').val() + '/draw_sets/',
                method: 'get'
            }).success(function (response) {
                var da_ = response;
                var str_ = '<option value="no" label="无">无</option>';
                for (var i = 0; i < da_.length; i++) {
                    str_ += '<option value="' + da_[i].title + '"  optionId="' + da_[i].id + '" label="">' + da_[i].title + '</option>';
                }
                $('#imgSelected').html(' ');
                $('#imgSelected').html(str_);
                str_ = ' ';
            }).error(function (data, status, headers, config) {
            });

            $http({
                url: httpUrl + 'roles/' + $('#add_role').val() + '/article_sets/',
                method: 'get'
            }).success(function (response) {
                var da_ = response;
                var str_ = '<option value="no" label="无">无</option>';
                for (var i = 0; i < da_.length; i++) {
                    str_ += '<option value="' + da_[i].title + '"  optionId="' + da_[i].id + '" label="">' + da_[i].title + '</option>';
                }
                $('#txtSelected').html(' ');
                $('#txtSelected').html(str_);
                str_ = ' ';
            }).error(function (data, status, headers, config) {
            });
        }
    };
    $scope.flag = {
        show: $location.path() == '/article' ? true : false
    }
    $scope.fd = {
        imgN: '',
        txtN: '',
        imgName: '',
        imgDec: '',
        imgSm: true,
        txtDec: '',
        txtList: '无',
        txtSm: true,//原创声明
        imgList: '无',
        imgCheck: true,
        imgD: '该作品没有提供任何简介内容，这给万界图书馆的整编工作造成了不小的困扰',
        floorD: '该作品没有提供任何简介内容，这给万界图书馆的整编工作造成了不小的困扰',
        floorN: ''
    }
    $scope.data = {
        img: [],
        imgDec: '上传图片',
        drawsL: [],
        txtL: [],
        faceL: [],
        roleList: []
    }
    $scope.$watch('fd.txtN', function (newValue, oldValue) {
        $scope.fd.txtN = $scope.fd.txtN.slice(0, 30);
    });
    $scope.$watch('fd.imgN', function (newValue, oldValue) {
        $scope.fd.imgN = $scope.fd.imgN.slice(0, 30);
    });
    $scope.$watch('fd.imgD', function (newValue, oldValue) {
        $scope.fd.imgD = $scope.fd.imgD.slice(0, 100);
    });
    $scope.$on('$locationChangeStart', function (next, current) {
        $scope.flag.show = $location.path() == '/article' ? true : false;
    });


    $scope.fun.listData();
    $http({
        url: httpUrl + 'default_covers/',
        method: 'get'
    }).success(function (response) {
        $scope.data.faceL = response;
        $('.floorBox .bookCover .acquiescent').eq(0).click();
    }).error(function (data, status, headers, config) {
    });
    $(document).on('click', '.creationArticle .bookCover .acquiescent', function () {
        var src_ = $(this).find('img').attr('src');
        var src_Id = $(this).find('img').attr('srcId');
        $('#creatA').attr('typeId', src_Id);
        $('#creatA').attr('typeIdF', 1);
        $('.creationArticle .bookCover .acquiescent').removeClass('redB');
        $(this).addClass('redB');
    });
//      img-book creat
    $(document).on('click', '.floorBox .bookCover .acquiescent', function () {
        var src_ = $(this).find('img').attr('src');
        var src_Id = $(this).find('img').attr('srcId');
        $('#creatB').attr('typeId', src_Id);
        $('#creatB').attr('typeIdF', 1);
        $('.floorBox .bookCover .acquiescent').removeClass('redB');
        $(this).addClass('redB');
    });
    $('body').on('change', '#coverArticle', function () {
        $.ajax({
            url: httpUrl + 'social_network/multi_upload/',
            type: "POST",
            data: new FormData($('#coverArticleFF')[0]),
            processData: false,
            contentType: false,
            success: function (response) {
                console.log('aaaaa=creatABox')
                console.log(response)
                var src_ = response.url[0];
                $('.cropDraw3').slideDown('slow', function () {
                    coverFn('#cover_3', 0, src_);
                    console.log('src_===' + src_)
                    $('#creatA').attr('typeId', 0);
                    $('#creatA').attr('typeIdF', 0);
                    $('.creationArticle .bookCover .acquiescent').removeClass('redB');
                    var imageCover = new Image();
                    imageCover.src = src_;
                    imageCover.onload = function () {
                        var w = this.width;
                        var h = this.height;
                        setTimeout(function () {
                            cropFn('#creatA', '#creatABox', w, h, 180);
                        }, 0);
                        $('.clippingBox3').removeClass('hidden');
                    }
                });
            },
            error: function (err) {
            }
        });
    });
    $('body').on('change', '#coverArticleF', function () {
        $.ajax({
            url: httpUrl + 'social_network/multi_upload/',
            type: "POST",
            data: new FormData($('#coverArticleForm')[0]),
            processData: false,
            contentType: false,
            success: function (response) {
                var src_ = response.url[0];
                $('.cropDraw2').slideDown('slow', function () {
                    coverFn('#cover_2', 0, src_);
                    $('#creatB').attr('typeId', 0);
                    $('#creatB').attr('typeIdF', 0);
                    $('.floorBox .bookCover .acquiescent').removeClass('redB');
                    var imageCover = new Image();
                    imageCover.src = src_;
                    imageCover.onload = function () {
                        var w = this.width;
                        var h = this.height;
                        setTimeout(function () {
                            cropFn('#creatB', '#creatBShowBox', w, h, 180);
                        }, 0);
                        $('.clippingBox1').removeClass('hidden');
                    }
                });
            },
            error: function (err) {
            }
        });
    });

    $(document).on('click', '.useForCover', function () {
        var src_ = $(this).parent().find('img').attr('src');
        $('.cropDraw1').slideDown('slow', function () {
            coverFn('#cover_1', 0, src_);
            var imageCover = new Image();
            imageCover.src = src_;
            imageCover.onload = function () {
                var w = this.width;
                var h = this.height;
                setTimeout(function () {
                    cropFn('#imgHeadShow', '#imgHeadShowBox', w, h, 180);
                }, 0);
                $('.clippingBox1').removeClass('hidden');
            }
        });
    });


    $('body').on('change', '#upsInput', function () {
        $.ajax({
            url: httpUrl + 'social_network/multi_upload/',
            type: "POST",
            data: new FormData($('#locationForm')[0]),
            processData: false,
            contentType: false,
            success: function (response) {
                $scope.$apply(function () {
//                        $scope.data.img = response.url;
                    for (var i = 0; i < response.url.length; i++) {
                        $scope.data.img.push(response.url[i]);
                    }
                    if ($scope.data.img.length >= 1) {
                        $scope.data.imgDec = '继续上传';
                    } else {
                        $scope.data.imgDec = '上传图片';
                    }

                    console.log('this is a $scope.data.img!!!')
                    console.log($scope.data.img);
                });
            },
            error: function (err) {

            }
        });
    });


    $('.tagInfo1 .tagWrite').keydown(function (e) {
        if (e.keyCode == 32 || e.keyCode == 13) {
            var str = $.trim($(this).val());
            var arr = str.split(' ');
            var str1 = ' ';
            for (var i in arr) {
                str1 += '<li>';
                str1 += '<span>' + arr[i].substring(0, 4) + '</span>';
                str1 += '<i class="fa fa-close" aria-hidden="true"></i>';
                str1 += '</li>';
            }
            if ($('.tagShow').eq(0).children().length < 5) {
                $('.tagShow').eq(0).append(str1);
                str1 = ' ';
                $(this).val('');
            } else {
                str1 = ' ';
                $(this).val('');
            }

        }
    });
    $('.tagInfo2 .tagWrite').keydown(function (e) {
        if (e.keyCode == 32 || e.keyCode == 13) {
            var str = $.trim($(this).val());
            var arr = str.split(' ');
            var str1 = ' ';
            for (var i in arr) {
                str1 += '<li>';
                str1 += '<span>' + arr[i].substring(0, 4) + '</span>';
                str1 += '<i class="fa fa-close" aria-hidden="true"></i>';
                str1 += '</li>';
            }
            if ($('.tagShow').eq(1).children().length < 5) {
                $('.tagShow').eq(1).append(str1);
                str1 = ' ';
                $(this).val('');
            } else {
                str1 = ' ';
                $(this).val('');
            }

        }
    });
    $(document).on('click', '.uesdTag1 li', function () {
        var usedStr = $(this).find('span').html();
        var str1 = '';
        str1 += '<li>';
        str1 += '<span>' + usedStr.substring(0, 4) + '</span>';
        str1 += '<i class="fa fa-close" aria-hidden="true"></i>';
        str1 += '</li>';
        if ($('.tagShow').eq(0).children().length < 5) {
            $('.tagShow').eq(0).append(str1);
            str1 = ' ';
        } else {
            str1 = ' ';
        }
    });
    $(document).on('click', '.uesdTag2 li', function () {
        var usedStr = $(this).find('span').html();
        var str1 = '';
        str1 += '<li>';
        str1 += '<span>' + usedStr.substring(0, 4) + '</span>';
        str1 += '<i class="fa fa-close" aria-hidden="true"></i>';
        str1 += '</li>';
        if ($('.tagShow').eq(1).children().length < 5) {
            $('.tagShow').eq(1).append(str1);
            str1 = ' ';
        } else {
            str1 = ' ';
        }
    });
    $(document).on('click', '.tagShow .fa-close', function () {
        $(this).parent().remove();
    });

    $(document).on('click', '.useForDel', function () {
        $(this).parents('.acquiescent').remove();
        $scope.data.img = [];
        $('.bookImgCover .acquiescent img').each(function () {
            $scope.data.img.push($(this).attr('src'));
        });
        if ($scope.data.img.length >= 1) {
            $scope.$apply(function () {
                $scope.data.imgDec = '继续上传';
            })
        } else {
            $scope.$apply(function () {
                $scope.data.imgDec = '上传图片';
            })
        }
    });
    $(document).on('keydown', '#userLink', function (e) {
        if (e.keyCode == 32 || e.keyCode == 13) {
            var str = $.trim($(this).val());
            findRole(str);
        }
    });
}]);
