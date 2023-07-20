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

var videosInPage = [];
/*used in order to determine the length of timelime*/
var durations = [];
/* +- for video seek and counters display*/
var deviation = 100;

var timelineData = {
    start_time: 0,
    stop_time: 0,
    lines: {
    }
};

$(document).ready(function () {

    $(".video-holder").find('video').each(
        function() {
            if (typeof this == 'object' && $(this).attr('id') !== undefined) {
                videosInPage[$(this).attr('id')]=this
            }
        });

    $("#video1").on(
        "canplay",
        function(event) {
            generateTimelines();
            generateAlerts();
        });
});

function generateTimelines() {

    //reset timelinedata before reading it again
    timelineData = {
        start_time: 0,
        stop_time: 0,
        lines: {
        }
    };

    for (i  in videosInPage) {
        if (videosInPage[i].duration !== undefined) {
            if (jQuery.inArray(videosInPage[i].duration, durations) == -1) {
                durations.push(videosInPage[i].duration);
            }

            var videoname = $(videosInPage[i]).attr('data-videoname');
            var videoid = $(videosInPage[i]).attr('data-videoid');

            if (timelineData.lines[videoid] == undefined) {
                timelineData.lines[videoid] = {
                    title: videoname,
                    css: videoid,
                    events: [],
                    total: 0
                }
            }
        }
    }

    timelineData.stop_time = Math.max.apply(Math,durations)*1000;

    $.getJSON('resources/video_data/data.json')
        .done(function(data) {
            var json = data;

            for (var i in json) {
                if (timelineData.lines[i] !== undefined && jQuery.inArray(i, Object.keys(videosInPage)) !== -1) {

                    for (var idx in json[i]) {
                        timelineData.lines[i].events.push({
                            id: (timelineData.lines[i].events.length+1),
                            time: idx*1000,
                            counter: json[i][idx]
                        });
                    }

                    timelineData.lines[i].total = json['totals'][i];
                }
            }

            $('.tl').html('');
            $('.tl').timeline(timelineData);


            //size of panels with timeline and alerts must be identical
            var heightLeft = $(".panel-left").map(function() {
                return $(this).height();
            }).get();
            $(".panel-right").height(heightLeft);

            //alerts are size to match panel heights

            $('.scrollbar-light').slimScroll({
                height: heightLeft
            });
        })
        .fail(function(data){
            console.log("Data for video could not be loaded!");
        });
}
function generateAlerts() {

    //reset timelinedata before reading it again
    alertsData = {
        "videoId": "",
        lines: []
    };

    $.getJSON('resources/video_data/events.json')
        .done(function(data) {
            var json = data;

            for (var i in json) {
                alertsData.videoId = i;
                if (jQuery.inArray(i, Object.keys(videosInPage)) !== -1) {
                    for (var idx in json[i]) {
                        alertsData.lines.push({
                            time: json[i][idx]['time'],
                            videoTime: parseFloat(json[i][idx]['videoTime'],3)*1000,
                            content: json[i][idx]['content']
                        });
                    }
                }
            }

            $('#detection-alert').html('');
            $('#detection-alert').detectionAlert(alertsData);

            $("i.fa-play").click(onClickTimelineBullet);
        })
        .fail(function(data){
            console.log("Events for video could not be loaded!");
        });
}

function onClickTimelineBullet() {

    var videoId = $(this).attr('data-videoid');
    var time = (parseFloat(($(this).attr('data-eventtime'))/1000) > 0)?parseFloat(($(this).attr('data-eventtime'))/1000):0;

    $('#'+videoId)[0].pause();
    $('#'+videoId)[0].currentTime = time;
    $('#'+videoId)[0].play();
}
