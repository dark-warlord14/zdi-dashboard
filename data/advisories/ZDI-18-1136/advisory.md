# ZDI-18-1136: Microsoft Edge Hazardous URI Insufficient UI Warning Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1136
- **ZDI-CAN:** ZDI-CAN-6489
- **Date:** 2018-10-10
- **CVE:** CVE-2018-8495
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** @qab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1136/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious web page and perform a UI action. There are multiple issues with the way the product handles URIs within certain schemes. The product does not warn the user that a dangerous navigation is about to take place. An attacker can manipulate the user interface so that the user's action is interpreted as permission to proceed with opening a dangerous file. Because special characters in the URI are not sanitized, this could lead to the execution of arbitrary commands. An attacker can leverage this vulnerability to execute code in the context of the current user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8495

## Disclosure Timeline

- 2018-07-03 - Vulnerability reported to vendor
- 2018-10-10 - Coordinated public release of advisory
- 2018-10-10 - Advisory Updated
