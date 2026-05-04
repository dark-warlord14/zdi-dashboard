# ZDI-15-294: Adobe Flash Sound Universal Cross Site Scripting Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-294
- **ZDI-CAN:** ZDI-CAN-2872
- **Date:** 2015-07-08
- **CVE:** CVE-2015-3125
- **CVSS:** 5.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Flash
- **Credit:** David Kraftsow (dontsave)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-294/
## Vulnerability Details

This vulnerability allows remote attackers to read arbitrary data on vulnerable Adobe Flash installations. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of Sound objects. A remote attacker can run arbitrary script in the context of any domain. An attacker can leverage this vulnerability to read browser cookies or saved passwords.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/flash-player/apsb15-16.html

## Disclosure Timeline

- 2015-04-28 - Vulnerability reported to vendor
- 2015-07-08 - Coordinated public release of advisory
