# ZDI-22-1166: Delta Industrial Automation DIALink Hardcoded Cryptographic Key Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1166
- **ZDI-CAN:** ZDI-CAN-16889
- **Date:** 2022-08-24
- **CVE:** CVE-2022-2660
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** DIALink
- **Credit:** Y4er
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1166/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Delta Industrial Automation DIALink. Authentication is not required to exploit this vulnerability. The specific flaw exists within the authorization of requests to the server. The issue results from hardcoding crytographic keys within the product. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/uscert/ics/advisories/icsa-22-235-02

## Disclosure Timeline

- 2022-04-27 - Vulnerability reported to vendor
- 2022-08-24 - Coordinated public release of advisory
