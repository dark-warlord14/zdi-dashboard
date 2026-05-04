# ZDI-20-805: C-MORE HMI EA9 Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-805
- **ZDI-CAN:** ZDI-CAN-10182
- **Date:** 2020-07-07
- **CVE:** CVE-2020-10918
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** C-MORE
- **Affected Products:** HMI EA9
- **Credit:** Ta-Lun Yen & Chizuru Toyama of TXOne IoT/ICS Security Research Labs (Trend Micro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-805/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of C-MORE HMI EA9 touch screen panels. Authentication is not required to exploit this vulnerability. The specific flaw exists within the authentication mechanism. The issue is due to insufficient authentication on post-authentication requests. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from unauthenticated users.

## Additional Details

Fixed in version 6.60

## Disclosure Timeline

- 2020-02-10 - Vulnerability reported to vendor
- 2020-07-07 - Coordinated public release of advisory
- 2020-11-24 - Advisory Updated
