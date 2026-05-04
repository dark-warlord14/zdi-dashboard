# ZDI-11-073: Adobe Reader ICC Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-073
- **ZDI-CAN:** ZDI-CAN-973
- **Date:** 2011-02-08
- **CVE:** CVE-2011-0598
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Sebastian Apelt (www.siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-073/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the ICC parsing component of ACE.dll. It is possible to cause an integer overflow due to several multiplications of controlled byte values. This leads to the allocation of a small buffer which can subsequently be overflowed. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the user running Reader.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-03.html

## Disclosure Timeline

- 2010-11-15 - Vulnerability reported to vendor
- 2011-02-08 - Coordinated public release of advisory
