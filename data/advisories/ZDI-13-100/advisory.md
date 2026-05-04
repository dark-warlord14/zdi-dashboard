# ZDI-13-100: IBM SPSS SamplePower C1sizer.ocx ActiveX TabCaption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-100
- **ZDI-CAN:** ZDI-CAN-1545
- **Date:** 2013-05-29
- **CVE:** CVE-2012-5946
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** IBM
- **Affected Products:** SPSS
- **Credit:** Alexander Gavrun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-100/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of IBM SPSS SamplePower. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the C1sizer.ocx ActiveX Control. This component performs insufficient bounds checking on user-supplied data on the TabCaption property which results in memory corruption. An attacker can leverage this situation to execute code under the context of the user running the browser.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: http://www.ibm.com/support/docview.wss?uid=swg21635476

## Disclosure Timeline

- 2012-11-21 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory
