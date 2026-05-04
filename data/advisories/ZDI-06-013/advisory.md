# ZDI-06-013: TippingPoint SMS Server Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-013
- **ZDI-CAN:** ZDI-CAN-017
- **Date:** 2006-05-09
- **CVE:** CVE-2006-0993
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** 3Com TippingPoint
- **Affected Products:** TippingPoint SMS
- **Credit:** Micheal Cottingham
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-013/
## Vulnerability Details

This vulnerability may allow attackers to access sensitive information from vulnerable TippingPoint SMS servers. The specific flaw exists within the web management interface. Due to insufficient protections on specific directories, an attacker with access to the web interface may be able to view benign data such as the user manual. In the event that the device was being used for backup purposes, it may be possible for an attacker to identify additional information such as configuration settings.

## Additional Details

This issue has been addressed in TippingPoint SMS Server release version 2.2.1.4478. Customers can obtain the update through the SMS device or by visiting http://tmc.tippingpoint.com

## Disclosure Timeline

- 2006-01-19 - Vulnerability reported to vendor
- 2006-05-09 - Coordinated public release of advisory
