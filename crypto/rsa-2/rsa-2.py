#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes

n1 = 19923456590552251975162382016814931637382722375359317208772451871483356576714885405606097241378501075931369906670869061248093649172881861192415328175663097814656963736628313898192077466201058425384752569296996738377762539233037404643814812839894268154220478743035005438051770194437690753198077282440197305242179520050148380897574370600817779326137623367669108915782523407192924244211054831306140325178040945340487553314593944938986145125036773442922867233469484732742374036099352126374556352618891702660032199891902387345141014680832744060658322845566908945809269331920931166181902583367526789454630626729460870647169
n2 = 23652833904119539867170294668574519424764451584703709844692900487740199502027597219325105779509757750797225761350201692963410434498426449300686946983803002021489077408094793455555430544612634765894489927184427882039278621190257263451767512691221747983840404059919424585305403183478687231730821351928952948387786999318351680488492230221474263072462047902669589861650172415714744833823410983928596263345045594725340746629428670770352781564040112067286818358284699547765286831757865286706603307438315831970396001029588630072110064604209495792029805266048287992268106514474824700175027996395298427269399103991524141700041
e = 65537

# the implication of this problem is:
# if attacker obtains two encrypted pakets of the same message + both public keys
# he's able to calculate the original message

output1 = 12278158833241263370930062575716063681369848347727064768204390204885977167155563107836235942564513581018883676391917665334488509487635763195414312755247755559283361478811654947231669548127225321505105317874090315582061803722028612975077098003568434906106093020331293685958165558492584653482909982179268457461221025389032327820153659778683664398635809458333308054319655218157736372560382953044278483830802166140103213298143821881919871650670212387075255311439623542943026425162579056803986284728196080669728957335306762638754288658714631692764552185005977623203375854644592722116295994159176669836231102886274729455944
output2 = 1645484211925706235753160467637145624607024171371070269825755869629486838608358671594135950253179901855929042252740352047743668609090881198368203243015383913513781779802395311162180037901008190452776729394330297494755594288397671967813865758456157708255345142916357226715102023967293904114355813089939347372711617781478585959041679996146144934469424163366832086647386791835215463619003840176753195911569504306025854379155032908892329865698767852631936987265963921740468298590651494468682602926148528983485109224215796115101492369792148592511142694853699409670394319657540567814094766913015721788272195922239051184956

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

#print("common factor of n1, n2: {}".format(egcd(n1, n2)[0]))
p1 = egcd(n1, n2)[0]
q2 = n2/p1
phi_n2 = (p1 - 1) * (q2 - 1)
print(egcd(e, phi_n2))
gcd1, a2, b2 = egcd(e, phi_n2)

#d = mmi(e, eulerphi_n)
# modular multiplicative inverse 
#c = pow(output1, d1, n1)
#flag = long_to_bytes(c).decode()
#print(flag)
#print("common factor of out1, out2: {}".format(egcd(output1, output2)[0]))