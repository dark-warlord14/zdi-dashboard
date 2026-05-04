# ZDI-20-806: C-MORE HMI EA9 Weak Cryptography for Passwords Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-806
- **ZDI-CAN:** ZDI-CAN-10185
- **Date:** 2020-07-07
- **CVE:** CVE-2020-10919
- **CVSS:** 5.9
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** C-MORE
- **Affected Products:** HMI EA9
- **Credit:** Ta-Lun Yen & Chizuru Toyama of TXOne IoT/ICS Security Research Labs (Trend Micro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-806/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of C-MORE HMI EA9 touch screen panels. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of passwords. When transmitting passwords, the process encrypts them in a recoverable format. An attacker can leverage this vulnerability to disclose credentials, leading to further compromise.

## Additional Details

Fixed in version 6.60

## Disclosure Timeline

- 2020-02-10 - Vulnerability reported to vendor
- 2020-07-07 - Coordinated public release of advisory
- 2020-10-08 - Advisory Updated
