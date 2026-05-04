# ZDI-14-098: IBM Lotus Quickr ActiveX Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-098
- **ZDI-CAN:** ZDI-CAN-2028
- **Date:** 2014-04-17
- **CVE:** CVE-2013-6748
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** IBM
- **Affected Products:** Lotus Quickr
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-098/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM Lotus Quickr for Domino. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within an ActiveX control included in QP2.dll. The specific flaw is a stack buffer overflow in a vulnerable function in the control. By passing an overly long value into a property, and then triggering the function, an attacker may execute arbitrary code in the context of the current process.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www-01.ibm.com/support/docview.wss?uid=swg21662653

## Disclosure Timeline

- 2014-02-07 - Vulnerability reported to vendor
- 2014-04-17 - Coordinated public release of advisory
