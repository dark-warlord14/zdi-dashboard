# ZDI-13-092: IBM SPSS Chart2D olch2x32.ocx ActiveX Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-092
- **ZDI-CAN:** ZDI-CAN-1576
- **Date:** 2013-05-29
- **CVE:** CVE-2013-0593
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** IBM
- **Affected Products:** SPSS
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-092/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM SPSS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the olch2x32.ocx ActiveX control. This object uses the Load() method to load a 2D chart into the browser. When parsing an OC2 file, the code trusts a value at a certain offset. An attacker can alter this value to control the arithmetic done on this value which can result in a user controlled pointer. An attacker can leverage this vulnerability to execute code under the context of the process.

## Additional Details

http://www-01.ibm.com/support/docview.wss?uid=swg21635503

## Disclosure Timeline

- 2013-03-22 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory
