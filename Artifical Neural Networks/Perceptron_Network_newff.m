%% MATLAB Implementation of a Perceptron Network
% The problem involves a system with four inputs and one output. 
% The desired output is "one" if the input pattern contains an odd number 
% of 1s, and "zero" otherwise.
clc
close all
clear
%% Enter the input and the target vectors
inp = [0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1;0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1;...
0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1; 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1];
out= [0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0];
%% Creating a network
network=newff([0 1;0 1; 0 1; 0 1],[6 1],{"logsig","logsig"});
network.trainParam.epochs = 500;
network.trainParam.lr = 0.05;
view(network)
network=init(network);
%% Training the network 
network=train(network,inp,out);
%% Simulate network and plot the result
y=sim(network,inp);
plot(inp,out,inp,y,"o")
title("After Training");
axis([-5 5 -2.0 2.0]);