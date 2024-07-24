also:: question/javascript
  - Variable
    collapsed:: true
    - var #[[vs]] let #[[vs]] const
      collapsed:: true
      - 作用域 var > let
        - 暂时性死区 let、const 所声明的变量绑定局部区域，不受外部影响
      - const 声明之后必须马上赋值，否则会报错
      - 变量提升
      - 重复声明
        - var 支持, 后两种不支持
      - via:
        - [第177题：var、let、const 有什么区别 · Issue #477 · Advanced-Frontend/Daily-Interview-Question](https://github.com/Advanced-Frontend/Daily-Interview-Question/issues/477)
  - Loop
    collapsed:: true
    - Case 1: 持续滚动
      collapsed:: true
      - **NOT** Loop!!! But [setInterval() - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/setInterval);
        - 因为 `loop` 的方式会持续抢占 CPU, 不会把 CPU 还给 `window` 窗体去响应滑动的操作;
        - via: [javascript - while(true) vs setInterval(function(),0) - Stack Overflow](https://stackoverflow.com/questions/14840527/whiletrue-vs-setintervalfunction-0)
        - And Demo Code Following
          - ```javascript
            /* Not Works Code*/
            function sleep(milliseconds) {
                const date = Date.now();
                let currentDate = null;
                do {
                  currentDate = Date.now();
                } while (currentDate - date < milliseconds);
            }
            scrollDownTillEnd = () => {
                for(let i = 0; i < 10000; i++) {
                    window.scrollBy(0, 1000);
                };
            };
            scrollDownTillEnd();
            /* Works Code*/
            let i = 0;
            var times = prompt("Input how many times to scroll?");
            if (times == ""){
                times = 1000;
            }
            function scrollDownTillEnd(countryDropdownList) {
                let scrollingInterval = setInterval( function () {
                    window.scrollTo(0, document.body.scrollHeight
                        || document.documentElement.scrollHeight);
                    if (i >= times)
                        clearInterval(scrollingInterval);
                    console.log(i++ + "Times.");
                }, 200);
            }
            scrollDownTillEnd();
            ```
          - via:
            - [javascript - Scroll Automatically to the Bottom of the Page - Stack Overflow](https://stackoverflow.com/questions/11715646/scroll-automatically-to-the-bottom-of-the-page)
            - [javascript - Why cant I scroll browser window in a loop in console? - Stack Overflow](https://stackoverflow.com/questions/56173022/why-cant-i-scroll-browser-window-in-a-loop-in-console)
            - [dom events - Stop setInterval call in JavaScript - Stack Overflow](https://stackoverflow.com/questions/109086/stop-setinterval-call-in-javascript)
            - [javascript - How to terminate script execution when debugging in Google Chrome? - Stack Overflow](https://stackoverflow.com/questions/13134723/how-to-terminate-script-execution-when-debugging-in-google-chrome)
-