%% MATLAB Implementation of a Perceptron Network
% The problem involves a system with four inputs and one output. 
% The desired output is "one" if the input pattern contains an odd number 
% of 1s, and "zero" otherwise.
function feedforwardnet_test
    %% Enter the input and the target vectors
    inp = [0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1;0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1;...
    0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1; 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1];
    out= [0 1 1 0 1 0 0 1 1 0 0 1 0 1 1 0];
    %% Creating a network
    network = feedforwardnet(6);
    % network.trainParam.epochs = 500;
    % network.trainParam.lr = 0.05;
    % network.layers{1}.transferFcn = 'logsig';
    % network.layers{end}.transferFcn = 'logsig';
    network1 = configure(network,inp,out);
    view(network1)
    %% Training the network 
    network1=adapt(network1,inp,out);
    %% Simulate network and plot the result
    y=sim(network1,inp);
    plot(inp,out,inp,y,"o")
    title("After Training");
    axis([-5 5 -2.0 2.0]);