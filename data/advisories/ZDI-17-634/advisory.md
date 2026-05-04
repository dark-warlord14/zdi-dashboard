# ZDI-17-634: Adobe Flash URL Redirect Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-634
- **ZDI-CAN:** ZDI-CAN-4762
- **Date:** 2017-08-08
- **CVE:** CVE-2017-3085
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** Björn Ruytenberg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-634/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of external resources. The issue lies in the failure to properly apply sandbox rules when following a URL redirect. An attacker can leverage this vulnerability to steal credentials under the context of the current user.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb17-23.html

## Disclosure Timeline

- 2017-05-04 - Vulnerability reported to vendor
- 2017-08-08 - Coordinated public release of advisory
