close all
clear
clc

% One Step Constrained Optimal Control Problem Plots
u_0_constraint=[0.01,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.70,0.75,0.80,0.85,0.90,0.95,1]
primalsolution1=[-49.434,-50.25,-51,-51.45,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6]
dualsolution1=[-72.006,-67.35,-61.8,-56.55,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6]

delta=[0.8,0.85,0.9,0.95,0.96,0.97,0.98,0.99]
primalsolution2=[-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,]
dualsolution2=[-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,-51.6,]

iterations=[200,225,250,150,100,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50]
size(iterations)

figure
plot(u_0_constraint,primalsolution1,'b','LineWidth',1.5)
hold on
plot(u_0_constraint,dualsolution1,'r','LineWidth',1.5)
legend('Optimal Primal Solution','Optimal Dual Solution')
title('Dual vs. Primal Solution as u_0 constraint changes')
xlabel('u_0')
ylabel('Solution')

figure
plot(u_0_constraint,iterations,'b','LineWidth',1.5)
title('u_0 constraint vs. Iterations')
xlabel('u_0')
ylabel('Iterations')
ylim([0,300])