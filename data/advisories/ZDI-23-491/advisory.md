# ZDI-23-491: Foxit PDF Reader exportXFAData Exposed Dangerous Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-491
- **ZDI-CAN:** ZDI-CAN-19697
- **Date:** 2023-05-01
- **CVE:** CVE-2023-27363
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PDF Reader
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-491/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PDF Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the exportXFAData method. The application exposes a JavaScript interface that allows writing arbitrary files. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxit.com/support/security-bulletins.html

## Disclosure Timeline

- 2023-01-20 - Vulnerability reported to vendor
- 2023-05-01 - Coordinated public release of advisory
