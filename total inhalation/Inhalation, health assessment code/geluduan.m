clear;
T=232;%һ���ڹ���������
I0=1;%������������
C0=10*1e-9;%�ο���Ũ����ֵ��λ��kg/m3)
IH=4745;%�����ƽ����������
sj=[1268 1590 1211 1674];%���г��з�ʽ����ʱ��
lu=[241.9 233 418.15 276.15;
    177 226.25 167.5 203.5;
    144.55 200 72.05 265.4];%����·��ÿǧ������ʱ�䣨�룩
day=[10.06950176 9.696188416 9.541157062 7.470842523 7.465459489 7.543244318;
    17.73080267	17.07345681 16.80047108	13.15497407	13.1454954 13.2824622;
    23.8587108 22.97418092 22.60684912 17.701439 17.68868442 17.87298805;
    55.23960833	53.19167353	52.34119736	40.98379687	40.95426644	41.38098105];%������Ⱥ�����г��з�ʽ��ÿ��������
lu1=[0.001792895 0.001726426 0.001698822 0.001330199 0.00132924 0.00134309;
     0.002515143 0.002421898 0.002383174 0.001866055 0.00186471 0.001884139;
     0.003293828 0.003171714 0.003121002 0.002443783 0.002442022 0.002467466;
     0.009272912 0.008929131 0.008786364 0.006879831 0.006874874 0.006946505];%·��1��������Ⱥ�����г��з�ʽ�µ�λ����������
lu2=[0.001463514 0.001409256 0.001386724 0.001085822 0.001085039 0.001096345;
     0.002508136 0.00241515	0.002376535	0.001860856	0.001859515	0.00187889;
     0.001389612 0.001338094 0.001316699 0.001030992 0.001030249 0.001040983;
     0.006218099 0.005987571 0.005891836 0.00461338	0.004610056	0.004658089];%·��2��������Ⱥ�����г��з�ʽ�µ�λ����������
lu3=[0.001099041 0.001058295 0.001041374 0.000815409 0.000814821 0.000823311;
     0.002285389 0.002200661 0.002165475 0.001695593 0.001694371 0.001712026;
     0.006417372 0.006179457 0.006080654 0.004761226 0.004757796 0.004807369;
     0.009252938 0.008909897 0.008767438 0.006865011 0.006860064 0.006931541];%·��3��������Ⱥ�����г��з�ʽ�µ�λ����������
beta=[0.13 0.27 2.1 0.13 0.27 2.1;
      0.0070 0.027 0.50 0.0070 0.027 0.50;
      0.96 1.2 4.6 0.96 1.2 4.6];%������Ⱥ�ֱ�������Ѫ�ܡ��ΰ���ȫ�������ı���ϵ��
EF=[16 24 100 16 24 100;
    0.40 1.4 17 0.40 1.4 17;
    120 110 200 120 110 200];%������Ⱥ�ֱ�������Ѫ�ܡ��ΰ���ȫ��������������ʮ���ˣ�
P=[237320 137772 89304 207949 128193 85299].*1e-5;%���ֱ�¶��Ⱥ����
AA=[];
BB=[];
for n=1:1:4
D0=2*C0*IH.*T/365/24/60/60.*lu(3,n);%�ο�������ֵ
I=I0.*exp(beta.*((2*T.*lu3(n,:).*(1e-6)-(D0)).*1e5));%������������ȡֵ
dI=I.*(1-exp(-1*beta.*((2*T.*lu3(n,:)*(1e-6)-(D0)).*1e5)));%�����������ձ仯
R=P.*dI;%���������ն˱仯
D1=2*T.*lu3(n,:).*(1e-6);%���ɱ�׼�ĵ�λ
DALY=P.*D1.*EF.*1e5;
AA=[AA;R];
BB=[BB;DALY];
end