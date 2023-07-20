/*
 * Authors: Mihaela Mihai <mihaela.mihai@rinftech.com>
 *          Stefan Andritoiu <stefan.andritoiu@gmail.com>
 * Copyright (c) 2018 Intel Corporation.
 *
 * Permission is hereby granted, free of charge, to any person obtaining
 * a copy of this software and associated documentation files (the
 * "Software"), to deal in the Software without restriction, including
 * without limitation the rights to use, copy, modify, merge, publish,
 * distribute, sublicense, and/or sell copies of the Software, and to
 * permit persons to whom the Software is furnished to do so, subject to
 * the following conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
 * LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 * OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 * WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */

(function( $ ) {

    $.fn.timeline = function( data ) {
        return this.each(function() {

            $el = $(this);
            $el.addClass('timeline');


            // calc ratio for event positions
            var ratio = 100/(data.stop_time - data.start_time)

            $.each(data.lines, function(i,line){
                var lineTmpl = $('<div class="line"><div class="events"></div><h4 class="total">'+line.total+'</h4></div>').addClass("line "+ line.css).appendTo($el);

                $.each(line.events, function(index,event){
                    var position = ((event.time - data.start_time)*ratio).toFixed(2);

                    var eventTmpl = $('<div class="event"><div class="circle" data-videoid="'+i+'" data-eventtime="'+event.time+'"><div class="circle-inner"></div></div></div>').appendTo($('.events', lineTmpl)).css('left',position+'%');
                });
            });

            var timeTmpl = $('<div class="time">').appendTo($el);
            var periodTmpl = $('<div class="period"><div class="label last">'+(new Date(data.stop_time).toLocaleString())+'</div><div class="label first">'+(new Date(data.start_time).toLocaleString())+'</div></div>').css({left:"0%", width:"100%"}).appendTo(timeTmpl);

        });
    };

}( jQuery ));
