# 一.设计 RESTful API

## 1.协议
``` API与用户的通信协议，尽量使用HTTPS协议， ```

## 2.域名
+ 尽量将API部署在专用域名之下
``` https://api.example.com ```
+ 如果API比较简单，不会有进一步扩展，可以放在主域名下
``` https://example.com/api/ ```

## 3.版本
+ 将API版本号放入URL
``` https://api.example.com/v1/api ```
+ 另一种做法是讲版本号放入HTTP头信息中,不太方便和直观

## 4.路径
+ 路径又称"终点"（endpoint），表示API的具体网址。

## 5.HTTP动词
+ 对于资源的具体操作类型，常用的有

``` bash
GET（SELECT）：从服务器取出资源（一项或多项）。
POST（CREATE）：在服务器新建一个资源。
PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）。
PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）。
DELETE（DELETE）：从服务器删除资源。
HEAD：获取资源的元数据。
OPTIONS：获取信息，关于资源的哪些属性是客户端可以改变的。
```

+ 示例

``` bash
GET /zoos：列出所有动物园
POST /zoos：新建一个动物园
GET /zoos/ID：获取某个指定动物园的信息
PUT /zoos/ID：更新某个指定动物园的信息（提供该动物园的全部信息）
PATCH /zoos/ID：更新某个指定动物园的信息（提供该动物园的部分信息）
DELETE /zoos/ID：删除某个动物园
GET /zoos/ID/animals：列出某个指定动物园的所有动物
DELETE /zoos/ID/animals/ID：删除某个指定动物园的指定动物
```

## 6.过滤信息（Filtering）
+ 如果记录数量很多，服务器不可能都将它们返回给用户。API应该提供参数，过滤返回结果。

``` bash
?limit=10：指定返回记录的数量
?offset=10：指定返回记录的开始位置。
?page=2&per_page=100：指定第几页，以及每页的记录数。
?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序。
?animal_type_id=1：指定筛选条件
```

## 7.状态码 (Status Codes)
+ 服务器向用户返回的状态码和提示信息，常见的有

``` bash
200 OK - [GET]：服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）。
201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。
202 Accepted - [*]：表示一个请求已经进入后台排队（异步任务）
204 NO CONTENT - [DELETE]：用户删除数据成功。
400 INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。
401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。
403 Forbidden - [*] 表示用户得到授权（与401错误相对），但是访问是被禁止的。
404 NOT FOUND - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
406 Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。
410 Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。
422 Unprocesable entity - [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。
500 INTERNAL SERVER ERROR - [*]：服务器发生错误，用户将无法判断发出的请求是否成功。
```

## 8.错误处理 (Error handling)
+ 如果状态码是4xx，就应该向用户返回出错信息。一般来说，返回的信息中将error作为键名，出错信息作为键值即可。

``` bash
{
    error: "Invalid API key"
}
```

## 9.返回结果
+ 针对不同操作，服务器向用户返回的结果应该符合以下规范

## 10.Auth


# 二.HTTP API 设计指南
