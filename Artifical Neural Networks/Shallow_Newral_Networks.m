function Shallow_Newral_Networks
    load bodyfat_dataset.mat
    net = feedforwardnet(20);
    net = configure(net, bodyfatInputs, bodyfatTargets);
    net = init(net);
    [net,tr] = train(net,bodyfatInputs,bodyfatTargets);
    net.trainParam