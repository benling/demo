if($(window).width() > 991) {
	var total = window.innerHeight;
	document.getElementById("title").style.height = total * 0.1 + "px";
	document.getElementById("main").style.height = total * 0.9 + "px";
	title = document.getElementById("title");
	main = document.getElementById("main");

	box02 = document.getElementById("box02");
	box03 = document.getElementById("box03");
	box04 = document.getElementById("box04");
	title_h = title.offsetHeight;
	main_h = main.offsetHeight;

	box02_h = box02.offsetHeight;
	box03_h = box03.offsetHeight;
	box04_h = box04.offsetHeight;
	document.getElementById("box01").style.height = main_h * 0.65 + "px";
	document.getElementById("box8-box").style.height = main_h * 0.3 + "px";
	box02.style.height = main_h * 0.62 + "px";
	document.getElementById("box9-box").style.height = main_h * 0.3 + "px";
	box03.style.height = main_h * 0.475 + "px";
	box04.style.height = main_h * 0.475 + "px";
	box01 = document.getElementById("box01");
	box01_h = box01.offsetHeight;
	document.getElementById("total-mn1").style.height = box01_h * 0.02 + "px";
	document.getElementById("total-mn2").style.height = box01_h * 0.02 + "px";
	//document.getElementById("live-box").style.height = box01_h * 0.05 + "px";
	//document.getElementById("ym-menu").style.height = box03_h * 0.1 + "px";
};
//alert('test');
var app = angular.module('myApp', []);
app.controller('customersCtrl', function($scope, $http) {
	$http({
		method: 'get',
		url: 'static/da.json'
	}).then(function(res) {
		$scope.listHead = res.data.listHead; //数据列表-头
		$scope.listContent = res.data.listContent; //数据列表

		$scope.productListHead = res.data.productListHead; //列表
		$scope.productListContent = res.data.productListContent;
							
		var worldMapContainer2 = document.getElementById('box2');
		var box01 = document.getElementById("box01");
		var box01_h = box01.offsetHeight;
		var box01_w = box01.offsetWidth;
		//用于使chart自适应高度和宽度,通过窗体高宽计算容器高宽
		var resizeWorldMapContainer2 = function() {
			worldMapContainer2.style.width = box01_w * 0.96 + 'px';
			worldMapContainer2.style.height = box01_h * 0.38 + 'px';
		};
		//设置容器高宽
		resizeWorldMapContainer2();

		//------------------一周订单图表---------------------------------
		var myChart = echarts.init(worldMapContainer2);
		var option = {
			color: ['#38b3f1'],
			tooltip: {
				trigger: 'axis',
				axisPointer: { // 坐标轴指示器，坐标轴触发有效
					type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
				}
			},
			textStyle: {
				color: '#ccc'
			},
			legend: {
				data: ['成交量'],
			},
			grid: {
				top: '10%',
				left: '3%',
				right: '3%',
				bottom: '6%',
				containLabel: true
			},
			xAxis: [{
				type: 'category',
				data: res.data.titleList,
				axisTick: {
					alignWithLabel: true
				}
			}],
			yAxis: [{
				type: 'value'
			}],
			series: [{
				name: '订单数量',
				type: 'bar',
				barWidth: '60%',
				data: res.data.dataList
			}]
		};
		myChart.setOption(option);

		//用于使chart自适应高度和宽度
		window.onresize = function() {
			//重置容器高宽
			resizeWorldMapContainer2();
			myChart.resize();
		};
		
		//-------------------------一周成交额-----------------------------
		var worldMapContainer4 = document.getElementById('box4');
		//用于使chart自适应高度和宽度,通过窗体高宽计算容器高宽
		var resizeWorldMapContainer4 = function() {
			worldMapContainer4.style.width = box01_w * 0.96 + 'px';
			worldMapContainer4.style.height = box01_h * 0.48 + 'px';
		};
		//设置容器高宽
		resizeWorldMapContainer4();
		//一周成交额
		var myChart = echarts.init(worldMapContainer4);
		// 指定图表的配置项和数据

		var option = {
			color: ['#4fe2c5'],
			tooltip: {
				trigger: 'axis',
				formatter: "{a} <br/>{b} : {c} (元)"
			},
			textStyle: {
				color: '#ccc'
			},
			legend: {
				data: ['成交额'],
			},
			xAxis: [{
				type: 'category',
				data: res.data.titleList,
				axisTick: {
					alignWithLabel: true
				}
			}],
			yAxis: [{
				type: 'value'
			}],
			calculable: true,
			series: [{
				color: ['#00fa9a'],
				name: '成交额',
				type: 'bar',
				radius: '72%',
				center: ['50%', '45%'],
				data: res.data.dataTradeList
			}]
		};

		// 使用刚指定的配置项和数据显示图表。
		myChart.setOption(option);

		//用于使chart自适应高度和宽度
		window.onresize = function() {
			//重置容器高宽
			resizeWorldMapContainer4();
			myChart.resize();
		};


		//-------------------------	月成交额-------------------------------
		var worldMapContainer8 = document.getElementById('box8');
		box8_box = document.getElementById("box8-box");
		box8_box_h = box8_box.offsetHeight;
		box8_box_w = box8_box.offsetWidth;
		//用于使chart自适应高度和宽度,通过窗体高宽计算容器高宽
		var resizeWorldMapContainer8 = function() {
			worldMapContainer8.style.width = box8_box_w * 0.98 + 'px';
			worldMapContainer8.style.height = box8_box_h * 0.98 + 'px';
		};
		//设置容器高宽
		resizeWorldMapContainer8();

		// 月成交额
		var myChart = echarts.init(worldMapContainer8);
		// 指定图表的配置项和数据
		var option = {
			// title : {
			// 	text: '月度成交额',
			// 	subtext: '实时统计'
			// },
			color: ['#38b3f1'],
			tooltip: {
				trigger: 'axis',
				formatter: "{a} <br/>{b} : {c}元"
			},
			textStyle: {
				color: '#ccc'
			},
			legend: {
				data: ['成交额'],
				textStyle: {
					color: '#ccc'
				}
			},
			calculable: true,
			xAxis : [
				{
					type : 'category',
					boundaryGap : false,
					data : res.data.titleMonths
				}
			],
			yAxis : [
				{
					type : 'value'
				}
			],
			series: [{
				name: '成交额',
				type: 'line',
				// left: '10%',
				// top: '5%',
				// bottom: '17%',
				// width: '80%',
				smooth:true,
				itemStyle: {normal: {areaStyle: {type: 'default'}}},
				data:res.data.dataMonths
			}]
		};

		// 使用刚指定的配置项和数据显示图表。
		myChart.setOption(option);

		//用于使chart自适应高度和宽度
		window.onresize = function() {
			//重置容器高宽
			resizeWorldMapContainer8();
			myChart.resize();
		};

		//------------------------------一周会员增长数据--------------------------
		//一周会员增长数据
		var worldMapContainer = document.getElementById('box3');
		box03 = document.getElementById("box03");
		box03_h = box03.offsetHeight;
		box03_w = box04.offsetWidth;
		//用于使chart自适应高度和宽度,通过窗体高宽计算容器高宽
		var resizeWorldMapContainer = function() {
			worldMapContainer.style.width = box03_w * 1 + 'px';
			worldMapContainer.style.height = box03_h * 0.75 + 'px';
		};
		//设置容器高宽
		resizeWorldMapContainer();
		// 一周会员增长数据
		var myChart = echarts.init(worldMapContainer);

		// 指定图表的配置项和数据
		var option = {
			//color: ['#4fe2c5'],
			title : {
				x: 'center',
				text: '一周会员增长数据',
				textStyle: {
					color: '#ccc'
				}
			},
			tooltip : {
				trigger: 'axis'
			},
			textStyle: {
				color: '#ccc'
			},
			legend: {
				x:'left',
				padding: 30,
				textStyle: {
					color: '#ccc'
				},
				data:['会员数']
			},
			calculable : true,
			xAxis : [
				{
					type : 'category',
					data : res.data.titleList
				}
			],
			yAxis : [
				{
					type : 'value'
				}
			],
			series : [
				{
					name:'会员数',
					color: ['#19e873'],
					type:'bar',
					radius: '72%',
					center: ['50%', '45%'],
					data:res.data.dataweekList,
					markPoint : {
						data : [
							{type : 'max', name: '最大值'},
							{type : 'min', name: '最小值'}
						]
					},
					markLine : {
						data : [
							{type : 'average', name: '平均值'}
						]
					}
				}
			 
			]
		};
		
		// 使用刚指定的配置项和数据显示图表。
		myChart.setOption(option);

		//用于使chart自适应高度和宽度
		window.onresize = function() {
			//重置容器高宽
			resizeWorldMapContainer();
			myChart.resize();
		};
		
		//--------------------月份会员增长数据----------------------------------
		//              月份会员增长数据
		var worldMapContainer5 = document.getElementById('box5');
		box04 = document.getElementById("box04");
		box04_h = box04.offsetHeight;
		box04_w = box04.offsetWidth;
		//用于使chart自适应高度和宽度,通过窗体高宽计算容器高宽
		var resizeWorldMapContainer5 = function() {
			worldMapContainer5.style.width = box04_w * 0.96 + 'px';
			worldMapContainer5.style.height = box04_h * 0.50 + 'px';
		};
		//设置容器高宽
		resizeWorldMapContainer5();
		// 基于准备好的dom，初始化echarts实例
		var myChart = echarts.init(worldMapContainer5);

		// 指定图表的配置项和数据
		var option = {
			tooltip : {
				trigger: 'axis'
			},
			textStyle: {
				color: '#ccc'
			},
			legend: {
				textStyle: {
					color: '#ccc'
				},
				data:['会员数']
			},
			calculable : true,
			xAxis : [
				{
					type : 'category',
					boundaryGap : false,
					data : res.data.titleMonths
				}
			],
			yAxis : [
				{
					type : 'value'
				}
			],
			series : [
				{
					name:'会员数',
					color:'#6b8e23',
					type:'line',
					stack: '总量',
					symbol: 'none',
					smooth:true,
					itemStyle: {
						normal: {
							areaStyle: {
								// 区域图，纵向渐变填充
								color : '#ff7d4e'
							}
						}
					},
					data:res.data.dataMonthMem
				}
			]
		};


		// 使用刚指定的配置项和数据显示图表。
		myChart.setOption(option);

		//用于使chart自适应高度和宽度
		window.onresize = function() {
			//重置容器高宽
			resizeWorldMapContainer5();
			myChart.resize();
		};

		//-------------------即时业务数据--------------------------------
		//              地图即时业务数据分布
		var worldMapContainer1 = document.getElementById('box1');
		box02 = document.getElementById("box02");
		box02_h = box02.offsetHeight;
		box02_w = box02.offsetWidth;
		//用于使chart自适应高度和宽度,通过窗体高宽计算容器高宽
		var resizeWorldMapContainer1 = function() {
			worldMapContainer1.style.width = box02_w * 0.9 + 'px';
			worldMapContainer1.style.height = box02_h * 0.82 + 'px';
		};
		//设置容器高宽
		resizeWorldMapContainer1();
		// 基于准备好的dom，初始化echarts实例
		var myChart = echarts.init(worldMapContainer1);
		// 指定图表的配置项和数据
		function randomData() {
			return Math.round(Math.random() * 3000);
		}
		var option = {
			tooltip: {
				trigger: 'item'
			},
			legend: {
				orient: 'vertical',
				x: 'left',
				y: 'bottom',
				data: [
					'订单量',
					'成交额',
					'当日订单'
				],
				textStyle: {
					color: '#ccc'
				}
			},
			visualMap: {
				min: 0,
				max: 2500,
				left: 'right',
				top: 'bottom',
				text: ['高', '低'], // 文本，默认为数值文本
				calculable: true,
				//color: ['#26cfe4', '#f2b600', '#ec5845'],
				textStyle: {
					color: '#fff'
				}
			},
			series: [{
					name: '订单量',
					type: 'map',
					aspectScale: 0.75,
					zoom: 1.2,
					mapType: 'china',
					roam: false,
					label: {
						normal: {
							show: false
						},
						emphasis: {
							show: false
						}
					},
					data: function() {
						var serie = [];
						for(var i = 0; i < res.data.titleList7.length; i++) {
							var item = {
								name: res.data.titleList7[i],
								value: randomData()
							};
							serie.push(item);
						}
						return serie;
					}()

				},
				{
					name: '成交额',
					type: 'map',
					mapType: 'china',
					label: {
						normal: {
							show: true
						},
						emphasis: {
							show: true
						}
					},
					data: function() {
						var serie = [];
						for(var i = 0; i < res.data.titleList8.length; i++) {
							var item = {
								name: res.data.titleList8[i],
								value: randomData()
							};
							serie.push(item);
						}
						return serie;
					}()

				},
				{
					name: '当日订单',
					type: 'map',
					mapType: 'china',
					label: {
						normal: {
							show: true
						},
						emphasis: {
							show: true
						}
					},
					data: function() {
						var serie = [];
						for(var i = 0; i < res.data.titleList9.length; i++) {
							var item = {
								name: res.data.titleList9[i],
								value: randomData()
							};
							serie.push(item);
						}
						return serie;
					}()

				}
			]
		};

		// 使用刚指定的配置项和数据显示图表。
		myChart.setOption(option);

		//用于使chart自适应高度和宽度
		window.onresize = function() {
			//重置容器高宽
			resizeWorldMapContainer1();
			myChart.resize();
		};
	});
});