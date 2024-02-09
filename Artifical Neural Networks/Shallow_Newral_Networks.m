function Shallow_Newral_Networks
    load bodyfat_dataset.mat
    net = feedforeard;
    net = configure(net, bodyfatInputs, bodyfatTargets)