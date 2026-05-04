# ZDI-13-099: IBM SPSS SamplePower Vsflex8l.ocx ActiveX ComboList/ColComboList Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-099
- **ZDI-CAN:** ZDI-CAN-1544
- **Date:** 2013-05-29
- **CVE:** CVE-2012-5945
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** IBM
- **Affected Products:** SPSS
- **Credit:** Alexander Gavrun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-099/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM SPSS SamplePower. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Vsflex8l.ocx ActiveX control. This component performs insufficient bounds checking on user-supplied data passed into the 'ComboList' or 'ColComboList' properties which results in memory corruption. An attacker can leverage this situation to execute code under the context of the user running the browser.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www.ibm.com/support/docview.wss?uid=swg21635515

## Disclosure Timeline

- 2012-11-21 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory
