# ZDI-07-080: Multiple Vendor Web Console Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-080
- **ZDI-CAN:** ZDI-CAN-173
- **Date:** 2010-01-27
- **CVE:** N/A
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** 3Com TippingPoint, Juniper
- **Affected Products:** TippingPoint IPS, ScreenOS
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-080/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of TippingPoint IPS and Juniper ScreenOS. Authentication is required to exploit this vulnerability. The specific flaw exists in the web-based administrative console of the affected devices. Unprivileged users with read only permissions are not presented with restricted functionality such as the ability to modify users, device configuration or reboot the device. However, no check is made on the back end to prevent unprivileged users from accessing these resources. By manually generating requests to administrative components, privilege restrictions are easily bypassed.

## Additional Details

This issue has been addressed in TippingPoint IPS version 2.5.1.6826 released on April 2nd 2007. Customers can obtain the update through the SMS device or by visiting http://tmc.tippingpoint.com This issue has been addressed in ScreenOS versions 6.0 and 5.4R4, released in April of 2007.

## Disclosure Timeline

- 2007-03-16 - Vulnerability reported to vendor
- 2010-01-27 - Coordinated public release of advisory
