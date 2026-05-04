# ZDI-13-269: Valve Steam User Chat Message Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-269
- **ZDI-CAN:** ZDI-CAN-1975
- **Date:** 2013-11-24
- **CVE:** N/A
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:P/A:P
- **Affected Vendors:** Valve
- **Affected Products:** Steam
- **Credit:** Arnaud Dovi ad@heapoverflow.com http://goo.gl/Fgry8j
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-269/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Valve Steam. No action is necessary on the part of the vulnerable Steam user other than signing on to the Steam service. The specific flaw exists within the handling of user to user messages in the Steam client. An attacker can exploit this vulnerability by sending a malformed message to another Steam user via the Steam service. This can result in arbitrary code execution in the context of the Steam client.

## Additional Details

Valve has issued an update to correct this vulnerability. More details can be found at: http://store.steampowered.com/news/11750/

## Disclosure Timeline

- 2013-09-16 - Vulnerability reported to vendor
- 2013-11-24 - Coordinated public release of advisory
