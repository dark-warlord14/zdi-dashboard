# ZDI-15-132: Microsoft Word Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-132
- **ZDI-CAN:** ZDI-CAN-2686
- **Date:** 2015-04-15
- **CVE:** CVE-2015-1650
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** 3S Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-132/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of abstract number elements in numbering.xml. By adding unexpected nodes within an abstractNum node, the attacker can cause memory to be used after it is freed, leading to arbitrary code execution in the context of the Word process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms15-033.aspx

## Disclosure Timeline

- 2015-01-27 - Vulnerability reported to vendor
- 2015-04-15 - Coordinated public release of advisory
