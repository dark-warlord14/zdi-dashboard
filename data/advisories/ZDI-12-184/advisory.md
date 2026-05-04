# ZDI-12-184: Microsoft Excel Feature11/Feature12 Record Trusted Counter Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-184
- **ZDI-CAN:** ZDI-CAN-1373
- **Date:** 2012-11-15
- **CVE:** CVE-2012-2543
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-184/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Excel's parsing of Feature11/Feature12 records. The process trusts a supplied counter value without validating its size and proceeds to use it within a copy operation to the stack. An attacker can abuse this to execute arbitrary code under the context of the user running Excel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms12-076

## Disclosure Timeline

- 2012-07-24 - Vulnerability reported to vendor
- 2012-11-15 - Coordinated public release of advisory
