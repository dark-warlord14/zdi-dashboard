# ZDI-16-223: HID VertX/Edge discoveryd Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-223
- **ZDI-CAN:** ZDI-CAN-3177
- **Date:** 2016-03-28
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** HID
- **Affected Products:** VertX/Edge
- **Credit:** Ricky "HeadlessZeke" Lawshae - Trend Micro DVLabs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-223/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HID Edge. Authentication is not required to exploit this vulnerability. The specific flaw exists within the discoveryd service. The issue lies in the failure to sanitize user data before executing a system call. An attacker could leverage this vulnerability to execute code with root privileges.

## Additional Details

These controllers are sold through a "closed" channel of development partners, so the documentation, as well as the firmware fix, is available to those partners through our password protected developers site ( http://www.hidglobal.com/developer-center/opin-api ) The partners were notified via newsletter, as well as an email to registered users of the developers site.

## Disclosure Timeline

- 2016-02-25 - Vulnerability reported to vendor
- 2016-03-28 - Coordinated public release of advisory
