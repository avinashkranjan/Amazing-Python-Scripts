#!/usr/bin/env python3
"""
 Copyright (c) 2018 Intel Corporation.

 Permission is hereby granted, free of charge, to any person obtaining
 a copy of this software and associated documentation files (the
 "Software"), to deal in the Software without restriction, including
 without limitation the rights to use, copy, modify, merge, publish,
 distribute, sublicense, and/or sell copies of the Software, and to
 permit persons to whom the Software is furnished to do so, subject to
 the following conditions:

 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
 LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import os
import sys
import logging as log
from openvino.inference_engine import IENetwork, IECore


class Network:
    """
    Load and configure inference plugins for the specified target devices 
    and performs synchronous and asynchronous modes for the specified infer requests.
    """

    def __init__(self):
        self.net = None
        self.plugin = None
        self.input_blob = None
        self.out_blob = None
        self.net_plugin = None
        self.infer_request_handle = None

    def load_model(self, model, device, input_size, output_size, num_requests, cpu_extension=None, plugin=None):
        """
         Loads a network and an image to the Inference Engine plugin.
        :param model: .xml file of pre trained model
        :param cpu_extension: extension for the CPU device
        :param device: Target device
        :param input_size: Number of input layers
        :param output_size: Number of output layers
        :param num_requests: Index of Infer request value. Limited to device capabilities.
        :param plugin: Plugin for specified device
        :return:  Shape of input layer
        """

        model_xml = model
        model_bin = os.path.splitext(model_xml)[0] + ".bin"
        # Plugin initialization for specified device
        # and load extensions library if specified
        if not plugin:
            log.info("Initializing plugin for {} device...".format(device))
            self.plugin = IECore()
        else:
            self.plugin = plugin

        if cpu_extension and 'CPU' in device:
            self.plugin.add_extension(cpu_extension, "CPU")

        # Read IR
        log.info("Reading IR...")
        self.net = self.plugin.read_network(model=model_xml, weights=model_bin)
        log.info("Loading IR to the plugin...")

        if "CPU" in device:
            supported_layers = self.plugin.query_network(self.net, "CPU")
            not_supported_layers = \
                [l for l in self.net.layers.keys() if l not in supported_layers]
            if len(not_supported_layers) != 0:
                log.error("Following layers are not supported by "
                          "the plugin for specified device {}:\n {}".
                          format(device,
                                 ', '.join(not_supported_layers)))
                log.error("Please try to specify cpu extensions library path"
                          " in command line parameters using -l "
                          "or --cpu_extension command line argument")
                sys.exit(1)

        if num_requests == 0:
            # Loads network read from IR to the plugin
            self.net_plugin = self.plugin.load_network(
                network=self.net, device_name=device)
        else:
            self.net_plugin = self.plugin.load_network(
                network=self.net, num_requests=num_requests, device_name=device)
            # log.error("num_requests != 0")

        self.input_blob = next(iter(self.net.inputs))
        self.out_blob = next(iter(self.net.outputs))
        assert len(self.net.inputs.keys()) == input_size, \
            "Supports only {} input topologies".format(len(self.net.inputs))
        assert len(self.net.outputs) == output_size, \
            "Supports only {} output topologies".format(len(self.net.outputs))

        return self.plugin, self.get_input_shape()

    def get_input_shape(self):
        """
        Gives the shape of the input layer of the network.
        :return: None
        """
        return self.net.inputs[self.input_blob].shape

    def performance_counter(self, request_id):
        """
        Queries performance measures per layer to get feedback of what is the
        most time consuming layer.
        :param request_id: Index of Infer request value. Limited to device capabilities
        :return: Performance of the layer  
        """
        perf_count = self.net_plugin.requests[request_id].get_perf_counts()
        return perf_count

    def exec_net(self, request_id, frame):
        """
        Starts asynchronous inference for specified request.
        :param request_id: Index of Infer request value. Limited to device capabilities.
        :param frame: Input image
        :return: Instance of Executable Network class
        """

        self.infer_request_handle = self.net_plugin.start_async(
            request_id=request_id, inputs={self.input_blob: frame})
        return self.net_plugin

    def wait(self, request_id):
        """
        Waits for the result to become available.
        :param request_id: Index of Infer request value. Limited to device capabilities.
        :return: Timeout value
        """
        wait_process = self.net_plugin.requests[request_id].wait(-1)
        return wait_process

    def get_output(self, request_id, output=None):
        """
        Gives a list of results for the output layer of the network.
        :param request_id: Index of Infer request value. Limited to device capabilities.
        :param output: Name of the output layer
        :return: Results for the specified request
        """
        if output:
            res = self.infer_request_handle.outputs[output]
        else:
            res = self.net_plugin.requests[request_id].outputs[self.out_blob]
        return res

    def clean(self):
        """
        Deletes all the instances
        :return: None
        """
        del self.net_plugin
        del self.plugin
        del self.net
