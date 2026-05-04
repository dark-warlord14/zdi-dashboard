# ZDI-15-546: Microsoft Office Excel Binary Worksheet Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-546
- **ZDI-CAN:** ZDI-CAN-3270
- **Date:** 2015-11-10
- **CVE:** CVE-2015-6094
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-546/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of binary Excel files (.xlsb). By providing a malformed file, an attacker can cause a pointer to be re-used after it has been freed. An attacker could leverage this to execute arbitrary code under the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-116

## Disclosure Timeline

- 2015-09-08 - Vulnerability reported to vendor
- 2015-11-10 - Coordinated public release of advisory
