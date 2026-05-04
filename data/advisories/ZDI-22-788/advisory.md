# ZDI-22-788: Ivanti Avalanche SetSettings Exposed Dangerous Function Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-788
- **ZDI-CAN:** ZDI-CAN-15919
- **Date:** 2022-05-26
- **CVE:** CVE-2022-36983
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** Piotr Bazydlo (@chudypb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-788/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Ivanti Avalanche. Authentication is not required to exploit this vulnerability. The specific flaw exists within the SetSettings class. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://download.wavelink.com/Files/avalanche_v6.3.4_release_notes.txt

## Disclosure Timeline

- 2021-12-08 - Vulnerability reported to vendor
- 2022-05-26 - Coordinated public release of advisory
- 2022-07-27 - Advisory Updated
