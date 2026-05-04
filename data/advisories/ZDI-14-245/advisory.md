# ZDI-14-245: Advantech WebAccess bwocxrun ActiveX Control Installation Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-245
- **ZDI-CAN:** ZDI-CAN-2061
- **Date:** 2014-07-18
- **CVE:** CVE-2014-2368
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Advantech
- **Affected Products:** Advantech WebAccess
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-245/
## Vulnerability Details

This vulnerability allows remote attackers to install certain ActiveX controls without user interaction on vulnerable installations of Advantech WebAccess. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists with the bwocxrun ActiveX control, which allows for navigation from the network to the local file system. When combined with system settings and other components included as part of the installation, this allows for the activation of ActiveX controls resident on the local file system (even if not installed) without user interaction. An attacker can use this to install vulnerable controls on the target system.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: http://ics-cert.us-cert.gov/advisories/ICSA-14-198-02

## Disclosure Timeline

- 2014-04-23 - Vulnerability reported to vendor
- 2014-07-18 - Coordinated public release of advisory
