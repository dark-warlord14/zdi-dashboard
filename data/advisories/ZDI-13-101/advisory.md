# ZDI-13-101: IBM SPSS SamplePower Vsflex7l.ocx ActiveX ComboList Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-101
- **ZDI-CAN:** ZDI-CAN-1546
- **Date:** 2013-05-29
- **CVE:** CVE-2012-5947
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** IBM
- **Affected Products:** SPSS
- **Credit:** Alexander Gavrun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-101/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM SPSS SamplePower. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Vsflex7l.ocx ActiveX Control. This component performs insufficient bounds checking on user-supplied data passed into the ComboList or ColComboList methods which results in memory corruption. This vulnerability can be leveraged by an attacker to execute code under the context of the user.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www.ibm.com/support/docview.wss?uid=swg21635511

## Disclosure Timeline

- 2012-11-21 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory
