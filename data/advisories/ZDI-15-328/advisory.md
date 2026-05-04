# ZDI-15-328: Microsoft Office Excel table Tag Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-328
- **ZDI-CAN:** ZDI-CAN-2898
- **Date:** 2015-07-14
- **CVE:** CVE-2015-2375
- **CVSS:** 6.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:N/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** 3S Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-328/
## Vulnerability Details

This vulnerability allows remote attackers to read freed memory on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of the altText and altTextSummary properties of the table tag. Under some conditions, strings representing those values are used in one thread while they are being freed in another thread, leading to a race condition. An attacker can leverage this vulnerability to disclose information under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS15-070

## Disclosure Timeline

- 2015-04-21 - Vulnerability reported to vendor
- 2015-07-14 - Coordinated public release of advisory
