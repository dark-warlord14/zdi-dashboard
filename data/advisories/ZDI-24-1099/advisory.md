# ZDI-24-1099: Apache OFBiz resolveURI Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1099
- **ZDI-CAN:** ZDI-CAN-24775
- **Date:** 2024-08-06
- **CVE:** CVE-2024-38856
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apache
- **Affected Products:** OFBiz
- **Credit:** Nicholas Zubrisky (@NZubrisky) of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1099/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Apache OFBiz. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the resolveURI method. The issue results from improper URI validation. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: https://lists.apache.org/thread/olxxjk6b13sl3wh9cmp0k2dscvp24l7w

## Disclosure Timeline

- 2024-07-12 - Vulnerability reported to vendor
- 2024-08-06 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
