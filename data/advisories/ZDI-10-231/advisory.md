# ZDI-10-231: Juniper Secure Access Series meeting_testjava.cgi XSS Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-231
- **ZDI-CAN:** ZDI-CAN-886
- **Date:** 2010-11-07
- **CVE:** N/A
- **CVSS:** 6.4
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:N
- **Affected Vendors:** Juniper
- **Affected Products:** Secure Access Series
- **Credit:** Davy Douhine
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-231/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Juniper SA Series devices. Authentication is not required to exploit this vulnerability. The specific flaw exists within the meeting_testjava.cgi page which is used to test JVM compatibility. When handling the DSID HTTP header the code allows an attacker to inject arbitrary javascript into the page. This can be abused by an attacker to perform a cross-site scripting attack on the device.

## Additional Details

The fix to this issue is now available for download on the vendor's website. The issue has been resolved in IVE OS 6.5r7 (Build 16789) and 7.0r3 (Build 16899). A product security notice, PSN-2010-11-983, has been released by the vendor. Customers can sign up for proactive alerts of IVE OS software releases by visiting the Juniper Networks Support Center and selecting "Subscribe to Email Alerts" under Technical Bulletins.

## Disclosure Timeline

- 2010-10-15 - Vulnerability reported to vendor
- 2010-11-07 - Coordinated public release of advisory
