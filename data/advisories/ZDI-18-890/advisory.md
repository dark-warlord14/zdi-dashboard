# ZDI-18-890: ABB Panel Builder bebhoffadseth AmsNetId Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-890
- **ZDI-CAN:** ZDI-CAN-6086
- **Date:** 2018-08-10
- **CVE:** N/A
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ABB
- **Affected Products:** Panel Builder 800
- **Credit:** Michael Flanders of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-890/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ABB Panel Builder 800. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the TargetAmsNetId and AmsNetId parameters of the ABB bebhoffadseth OPC Driver. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of an administrator.

## Disclosure Timeline

- 2018-04-12 - Vulnerability reported to vendor
- 2018-08-10 - Coordinated public release of advisory
- 2018-08-10 - Advisory Updated
