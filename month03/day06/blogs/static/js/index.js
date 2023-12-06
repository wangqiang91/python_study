//轮播图
$(function(){
    var slidehtml = '';
    var base_url = '../static/images/';
    $.each(faderData,function(i,data)
    {
      slidehtml += `<li class="slide">
      <img src="${base_url + data.img_url}" alt="">
      <span>${data.img_info}</span>
      </li>`;
    });
    $('.fader>li:last').before(slidehtml);
    var i = 0;
    $('.fader>li').eq(i).addClass('active'); // 为第一个li添加active
    
    function next(){
      $('.slide').eq(i).removeClass('active');  //当前图片移除active
      i++;
      if (i == $('.slide').length)
          i = 0;            //i的值越界时，重置i的值；
      $('.slide').eq(i).addClass('active');
    }
    // 每隔2s将当前class active移到下一个li上；
    var timer = setInterval(next,2000);
    // 鼠标移入时停止计时，鼠标移出时自动切换
    $('.fader').mouseover(function(){
      clearInterval(timer)
    }).mouseout(function(){
      timer = setInterval(next,2000);
    })

    //用户点击.prev时，切换到上一张图片（找到当前显示的li，移除active，找到上一个li，添加active）
    $('.prev').click(function(){
      $('.slide').eq(i).removeClass('active');
      i--;
      if (i == -1) i = $('.slide').length-1;
      $('.slide').eq(i).addClass('active');
    })
    $('.next').click(next);
})

//加载列表数据
$(function(){
  // 定义加载数据的方法；（遍历blogData的每一个blog对象，生成一个div，添加到页面中；）
  function AddBlogs(data){
    var bloghtml = '';
  $.each(data,function(i,blog){
    bloghtml += ` <div class="blogs">
    <h3>${blog.blogtitle}</h3>
    <div>
      <img src="../static/images/${blog.blogpic}" alt="">
    </div>
    <p>${blog.blogtext}</p>
    <ul>
      <li>${blog.bloginfo.author}</li>
      <li class="lmname">${blog.bloginfo.lmname}</li>
      <li class="timer">${blog.bloginfo.timer}</li>
      <li class="view">${blog.bloginfo.view}</li>
      <li class="like">${blog.bloginfo.like}</li>
    </ul>
  </div>`;
  }); //end each
  $('.blogsbox').append(bloghtml);
  }

  //先加载前4条
  var data = blogData.slice(0,4);
  AddBlogs(data);

  $(document).scroll(function(){
    //获取页面所有元素的高度
    var dh = $(document).height();
    //当前窗口的可视范围高度
    var wh = $(window).height();
    //滑动条的高度
    var st = $(document).scrollTop();
    //当前窗口可视高度 + 滚动条高度 = 所有元素的高度
    console.log(dh,wh,st);
    if (dh - wh - st <= 300){
      var size = $('.blogs').length;
      var data = blogData.slice(size,size+4);
      AddBlogs(data)
    }
  });
  
})