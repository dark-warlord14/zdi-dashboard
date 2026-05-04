# ZDI-22-1456: LibreOffice Exposed Dangerous Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1456
- **ZDI-CAN:** ZDI-CAN-17859
- **Date:** 2022-10-21
- **CVE:** CVE-2022-3140
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** LibreOffice
- **Affected Products:** LibreOffice
- **Credit:** TheSecurityDev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1456/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of LibreOffice. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of document files. The issue results from an exposed dangerous function. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

LibreOffice has issued an update to correct this vulnerability. More details can be found at: https://www.libreoffice.org/about-us/security/advisories/CVE-2022-3140

## Disclosure Timeline

- 2022-08-24 - Vulnerability reported to vendor
- 2022-10-21 - Coordinated public release of advisory
