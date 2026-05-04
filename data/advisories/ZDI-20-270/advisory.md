# ZDI-20-270: IBM Spectrum Protect Plus username Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-270
- **ZDI-CAN:** ZDI-CAN-9750
- **Date:** 2020-03-05
- **CVE:** CVE-2020-4213
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** IBM
- **Affected Products:** Spectrum Protect Plus
- **Credit:** Jeremy Brown
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-270/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of IBM Spectrum Protect Plus. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Administrative Console Framework service. When parsing the username parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of an administrator.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://www.ibm.com/support/pages/node/3178863

## Disclosure Timeline

- 2019-12-11 - Vulnerability reported to vendor
- 2020-03-05 - Coordinated public release of advisory
