function Batch_Training
    P = [1 2 2 3; 2 1 3 1];
    T = [4 5 7 7];
    net = linearlayer(0,0.01);
    net = configure(net,P,T);
    net.IW{1,1} = [0 0];
    net.b{1} = 0;
    net.trainParam.epochs = 100;
    net.trainParam.showWindow = false;
    net.trainParam.showCommandLine = true;
    net.trainParam.show= 10;
    net = train(net,P,T);
