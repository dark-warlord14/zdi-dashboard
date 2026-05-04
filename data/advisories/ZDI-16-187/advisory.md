# ZDI-16-187: Microsoft Internet Explorer Input Range Control Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-187
- **ZDI-CAN:** ZDI-CAN-3499
- **Date:** 2016-03-08
- **CVE:** CVE-2016-0114
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Simon Zuckerbraun - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-187/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how Internet Explorer processes HTML input elements having a type of "range". By manipulating a document's elements an attacker can force a structure in memory to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-023

## Disclosure Timeline

- 2016-01-07 - Vulnerability reported to vendor
- 2016-03-08 - Coordinated public release of advisory
