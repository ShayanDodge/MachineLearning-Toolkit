function Shallow_Newral_Networks
    load bodyfat_dataset.mat
    net = feedforwardnet(20);
    net = configure(net, bodyfatInputs, bodyfatTargets);
    net = init(net);
    [net,tr] = train(net,bodyfatInputs,bodyfatTargets);

    % plot the relationship between the outputs of the network and the targets.
    bodyfatOutputs = net(bodyfatInputs);
    trOut = bodyfatOutputs(tr.trainInd);
    vOut = bodyfatOutputs(tr.valInd);
    tsOut = bodyfatOutputs(tr.testInd);
    trTarg = bodyfatTargets(tr.trainInd);
    vTarg = bodyfatTargets(tr.valInd);
    tsTarg = bodyfatTargets(tr.testInd);
    plotregression(trTarg, trOut, 'Train', vTarg, vOut, 'Validation', tsTarg, tsOut, 'Testing')