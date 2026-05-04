# ZDI-20-808: C-MORE HMI EA9 Control Port Missing Authentication for Critical Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-808
- **ZDI-CAN:** ZDI-CAN-10493
- **Date:** 2020-07-07
- **CVE:** CVE-2020-10920
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** C-MORE
- **Affected Products:** HMI EA9
- **Credit:** Ta-Lun Yen & Chizuru Toyama of TXOne IoT/ICS Security Research Labs (Trend Micro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-808/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of C-More HMI EA9 touch screen panels. Authentication is not required to exploit this vulnerability. The specific flaw exists within the control service, which listens on TCP port 9999 by default. The issue results from the lack of authentication prior to allowing alterations to the system configuration. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Fixed in version 6.60

## Disclosure Timeline

- 2020-02-21 - Vulnerability reported to vendor
- 2020-07-07 - Coordinated public release of advisory
- 2020-07-08 - Advisory Updated
