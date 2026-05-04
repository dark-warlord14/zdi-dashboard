# ZDI-15-517: Microsoft Office Excel calculatedColumnFormula Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-517
- **ZDI-CAN:** ZDI-CAN-3014
- **Date:** 2015-10-13
- **CVE:** CVE-2015-2555
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office
- **Credit:** 3S Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-517/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of calculatedColumnFormula objects. A specially crafted calculatedColumnFormula object can cause Excel to load information from memory that has already been freed. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS15-110

## Disclosure Timeline

- 2015-07-09 - Vulnerability reported to vendor
- 2015-10-13 - Coordinated public release of advisory
