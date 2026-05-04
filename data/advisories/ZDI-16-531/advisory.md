# ZDI-16-531: VMware Horizon View loggerBean Directory Traversal Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-531
- **ZDI-CAN:** ZDI-CAN-3714
- **Date:** 2016-10-11
- **CVE:** CVE-2016-7087
- **CVSS:** 5.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:N
- **Affected Vendors:** VMware
- **Affected Products:** Horizon View
- **Credit:** Mike Arnold (Bruk0ut)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-531/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of VMware Horizon View. Authentication is not required to exploit this vulnerability. The specific flaw exists within the loggerBean service. The loadConfig method does not properly sanitize the path supplied. An attacker can leverage this vulnerability to disclose arbitrary files from the system.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: http://www.vmware.com/security/advisories/VMSA-2016-0015.html

## Disclosure Timeline

- 2016-04-29 - Vulnerability reported to vendor
- 2016-10-11 - Coordinated public release of advisory
