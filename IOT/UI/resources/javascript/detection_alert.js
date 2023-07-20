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

    $.fn.detectionAlert = function( data ) {
        return this.each(function() {

            $el = $(this);
            $el.addClass('detectionAlert');

            $.each(data.lines, function(i,line){

                $('<div class="small-box box box-warning box-solid bg-yellow">' +
                    '<div class="inner">' +
                    '<p class="alert-time">'+line.time+'</p>' +
                    '<h4>'+line.content+'</h4>' +
                    '<p>detected</p>' +
                    '</div>' +
                    '<div class="icon">' +
                    '<i class="fa fa-play" data-videoid="video1" data-eventtime="'+line.videoTime+'" style="color: white;"></i>' +
                    '</div>' +
                    '</div>').appendTo($el);
            });
        });
    };

}( jQuery ));
